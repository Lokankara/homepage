# Transactions

SAP Commerce Cloud allows you to use the transaction system of the underlying database through a simple-to-use API. You do not have to resort to looking up a transaction object from a JNDI tree. Simply employ begin, commit, and rollback statements in your code. A transaction is a series of statements on a database that belong together in a certain context. Transactions are executed either in full or not at all, which keeps the database in a consistent state at any time. When using the SAP Commerce Cloud API, every transaction needs explicit begin, commit, and rollback statements called from within the Java code. You can also use the declarative approach by using Spring Transactions. See the chapter below for more information.

## Quick Start Note

If you do not want to use the SAP Commerce Cloud API but use Spring Transactions instead, scroll down to the Spring chapter. But although you do not need to fully understand the SAP Commerce Cloud Transactional API it would be a good idea to go through all chapters to get an in-depth view.

Every thread in SAP Commerce Cloud has a Transaction object, which offers transaction functionality. To get this Transaction object, use the static current() method, such as:
Transaction tx = Transaction.current();
Getting the Transaction object does not trigger a transaction begin. You need to explicitly trigger transactions via the begin(),
commit(), and rollback() methods.

The most basic implementation of a transaction in SAP Commerce Cloud looks as follows:
tx.begin(); boolean success = false; try { // do business logic doSomeBusinessLogic(); success = true; } finally { if( success ) tx.commit(); else tx.rollback(); }
However, it is recommended to avoid using explicit transaction operations whenever possible and use TransactionBody interface instead. By using TransactionBody one avoids all sort of problems that might arise when one uses given snippet (for example, forgetting to switch success ag to true or wrongly initializing it to true.)

## Note

Always use nally blocks. Using the nally operator here for rollback is an important aspect. During transaction execution, there may be issues which do not result in an Exception, but in an Error. Errors are not intercepted by a typically used catch(Exception) statement. If such an error arose during a transaction, the Transaction.current().commit(); statement would not be executed. The (incomplete) transaction would remain open, which blocks resources and impacts performance. The nally statement, however, will be executed if Errors arise, and can roll back the transaction. Then the database is in a consistent state again, and the connection to the database closes.

Be aware that since there is only one single Transaction object for every single thread, using several instances of the Transaction object does not result in different actual Transaction objects. For example, in the following code snippet, tx1 and tx2 are the same instance of the Transaction object. Do not use the following method:
Transaction tx1 = Transaction.current(); Transaction tx2 = Transaction.current(); //RETURNS THE SAME OBJECT AS TX1 tx1.begin(); tx2.begin(); //CALLS BEGIN ON AN ALREADY RUNNING TX
As there is only one Transaction object per thread, the two following code snippets are effectively the same:

Transaction tx = Transaction.current(); tx.begin(); ... tx.commit(); Transaction.current().begin();
..

Transaction.current().commit();
Whether you use the rst or the second style of code does not matter. Although both conventions produce the same results, introducing local variable to refer to current transaction usually leads to better coding style, because this makes transactional statements more explicit and "local" - the scope of the variable determines the scope of possible transactional operations. This is important when transactional code becomes more complicated.

## Using The Sap Commerce Cloud Transaction Api Nested Transactions

A side effect of the fact that there is only one Transaction object per thread is that it does not matter whether a submethod call opens a transaction of its own (that is, a nested transaction). The nested transaction does not start an individual transaction, but is executed in the context of the transaction of the calling method. Even if the underlying database system does not actually support nested transactions, SAP Commerce Cloud still accepts nested transactions.

void doSomethingBig() { ..begin(); doSomethingInTX(); ..commit(); //commit executed because not nested } void doSomethingInTX() { ...begin(); //begins a nested TX //will NOT throw error because tx is already running do() ... commit(); //commit ignored because inside nested TX }

## Using Transactionbody

SAP Commerce Cloud also offers an encapsulation for the Transaction object begin(), commit(), and rollback() methods. By instantiating a TransactionBody object and overriding the TransactionBody execute() method, you can encapsulate the entire transaction process, as in the following code snippet:
Transaction.current().execute( new TransactionBody() { public Object execute() { doSomething(); return something; } } );

Being wrapped in the execute() method of the TransactionBody object, the doSomething() method is executed in a transaction.

## Delayed Store

To optimize transaction speed and reduce database load, SAP Commerce Cloud offers a delayed-store mechanism. By default, SAP Commerce Cloud executes every statement as soon as it comes up. If "Delayed-store" is activated all database modication statements done by a transaction are kept in memory until the transaction is actually ushed and then executed at once. This allows optimizing (and possibly reducing) the set of database modication statements. The disadvantage is that since all of the database modication statements are executed at once, no data changes take place until the transaction is actually ushed. This may, for example, cause FlexibleSearch statements to return obsolete values because the database still returns old and stale content. To ush transaction in delayed-store mode, call the Transaction object ushDelayedStore() method, such as:
tx.flushDelayedStore();
There are two ways of setting whether or not to use delayed-store. First, there is the transaction.delayedstore property in the project.properties le that sets the global default value for delayed-store transactions. In addition, you can explicitly enable or disable delayed-store transactions via the Transaction object enableDelayedStore(Boolean) method. The value of the delayed-store transactions(Boolean) method is valid until the transaction is committed (or rolled back, depending on the outcome), and is reset to the global default afterwards.

For both the property and the enableDelayedStore(Boolean) method, true enables delayed-store transactions, while false disables delayed-store transactions.

Transaction.current().begin(); Transaction.current().enableDelayedStore(false); ...

## Intra Transaction Cache

It is possible to cache data manually for each transaction. Use the Transaction.set/getContextEntry(Object, Object) for storing data only for one transaction. Note that this data is reset to null whenever commit() or rollback() is called.

Transaction.current().setContextEntry("mykey","myvalue");

## Transactions And Junit Tests

If executing JUnit-Tests, it might be useful to roll back all changes at the end of the test to retain a fresh system and remove all data that was created during the test. For more information on how to write JUnit-Tests with SAP Commerce Cloud, see Testing with JUnit.

public class MyTest extends HybrisJUnit4TransactionalTest { @Test public void hereIsATest() { createProduct(); checkIfThereIsOneProductInTheSystem(); } }
There is no need to remove the product because all data is removed automatically at the end of each test.

## Using Transactions Via Spring

The HybrisTransactionManager implements the Spring PlatformTransactionManager registered at the core application context delegating all transaction calls to the SAP Commerce Cloud transaction framework. With that you are able to use the Spring Transaction Framework by means of using the @Transaction annotation, AOP-style transaction declaration (using tx schema) or by using the TransactionTemplate. The transaction template mechanism can be used by:
1. Inject or get the congured transaction manager 2. Instantiate a new template 3. Call the template execute method by dening a new body
// 1. PlatformTransactionManager manager=(PlatformTransactionManager) Registry.getApplicationContext().ge // 2. TransactionTemplate template = new TransactionTemplate(manager); // 3. template.execute(new TransactionCallbackWithoutResult() { @Override protected void doInTransactionWithoutResult(final TransactionStatus status) { // do something transactional } });
The AOP-style declaration can be made similar to the following xml snippet at your application-context.xml. Assuming that you have a FooService and you want to declare all getter as read-only transactional methods and all others as read and write ones, then declare it like that:
<bean id="fooService" class="x.y.service.DefaultFooService"/> <tx:advice id="txAdvice" transaction-manager="txManager"> <tx:attributes> <tx:method name="get*" read-only="true"/> <tx:method name="*"/> </tx:attributes>
</tx:advice>
<aop:config> <aop:pointcut id="fooServiceOperation" expression="execution(* x.y.service.FooService.*(..))"/> <aop:advisor advice-ref="txAdvice" pointcut-ref="fooServiceOperation"/> </aop:config>
You have to dene the tx and aop scheme at XML header.

## Frequently Asked Questions (Faq)

Does SAP Commerce Cloud use the UserTransaction Interface? No. Can we participate in global transactions of multiple systems? No.

## Resilience Against Connection Errors

The following property determines how many times transactions retry to connect with the database. If the connection isn't created after the number of attempts specied by this property, the retry mechanism is stopped.

This is   For more    the SAP Help  6 transaction.connection.retryOnBind.count=1

## Transactionconnectionbrokenexception Exception

When the transaction.execute method is called during a database outage, the TransactionConnectionBrokenException is thrown and any previous business logic exceptions are chained to it. If you don't want the system to throw exceptions during database outages, use the following property:
transaction.execute.throws.exception.for.broken.connection=false