# Registering Threads

## Registering Threads: Tutorial 1

Learn how to register threads you created yourself as non-suspendable using RegistrableThread, and provide some information about them.

## Context

By default, every thread, registered or not, is treated as suspendable. However, we recommend using RegistrableThread every time you create threads within SAP Commerce Cloud instead of Thread(…) because RegistrableThread enables you to easily and explicitly register your thread. As a result you gain full control over all operations. RegistrableThread also enables you to easily change the default behaviour and register threads as non-suspendable. It also enables you to provide specic information related to a given thread.

## Procedure

1. Create a runnable to do some "important stuff" for you.

Runnable runnable = new Runnable…
2. Create a new thread.

RegistrableThread thread = new RegistrableThread(runnable);
3. Make the thread non-suspendable, and provide information about it.

thread.withInitialInfo(OperationInfo.builder(). //
withCategory(Category.SYSTEM). // withStatusInfo("Doing very important stuff"). // asNotSuspendableOperation().build());
4. Start the thread.

thread.start();

## Results

The internal mechanism of RegistrableThread takes care of registering and deregistering the thread. The thread is correctly registered as a non-suspendable operation.

## Registering Threads: Tutorial 2

Learn how to register external threads as non-suspendable using OperationInfo, and provide information about it.

Whenever you don't have control over a thread creation process, for example in case of http threads coming from a web server, and therefore cannot use RegistrableThread, register such a thread manually:
RegistrableThread.registerThread(OperationInfo.builder().withCategory(Category.SYSTEM).asNotSuspend // do some business logic here RegistrableThread.unregisterThread();

## Registering Threads: Tutorial 3

Learn how to use the ProcessWithOperationInfo interface to register threads as suspendable when required when you use PoolableThread.

## Context

In case you use a PoolableThread, it is by default registered as a non-suspendable operation for the time of execution of its associated Runnable instance. When changing its state to idle, a PoolableThread is always registered as suspendable so that the system can be suspended when all PoolableThreads are idle.

If you want to change this behavior, you could use the ProcessWithOperationInfo interface to set a thread as suspendable whenever required, and to provide some information. Follow the steps to learn how to do it.

## Procedure

1. Implement runnable with some work to be done in the run() method, and ProcessWithOperationInfo to provide the correct information about the thread.

class MyRunnable implements Runnable, ProcessWithOperationInfo {
@Override public OperationInfo getOperationInfo() {
return OperationInfo.builder(). //
withStatusInfo("Doing very important stuff"). // build();
} @Override public void run() { // do some work here }
2. Instantiate your runnable and execute it with PoolableThread from the thread pool.

MyRunnable runnable = new MyRunnable(); final PoolableThread thread = Registry.getCurrentTenantNoFallback() .getThreadPool().borrowThread(); thread.execute(runnable);
For the time of execution, the status of the thread is changed. As PoolableThread is suspendable in the idle state, this will not change during execution.
