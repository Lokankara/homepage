# Data Validation Framework

SAP Commerce Cloud provides a data validation framework based on the JSR 303 bean validation specication. This allows you to dene data validation constraints in an easy and intuitive way.

This is   For more    the SAP Help  24 Key features of the Data Validation framework include the following:

It is based upon the Hibernate Validator that is the reference implementation of the JSR 303 Bean Validation.

It includes the ValidationService that loads the validation engine with constraints, and invokes its logic.

It has a ValidationInterceptor that hooks the ValidationService into SAP Commerce Cloud Model life cycles.

Validation constraints can be created and manipulated in the SAP Commerce Cloud Administration Cockpit, and loaded into the validation engine at runtime, and are persisted in the persistence layer.

The logic is triggered both implicitly by the ValidationInterceptor and explicitly by direct calls to the ValidationService.

Validation violations are caught and displayed in an intuitive fashion in cockpits. There are multiple levels of violation severity: Info, Warning, and Error.

## Introduction

The purpose of the Data Validation is:
To offer a framework for dening data validation constraints in easy and intuitive way.

To validate data before it is saved.
To notify about any validation violations should they occur.

The validation logic may be triggered:
Implicitly by the ValidationInterceptor that hooks into calls to a Model's save method.

Explicitly by manually calling validate method of the ValidationService and passing in a SAP Commerce Cloud Model or POJO to be validated.
When some validation violations are found, they are presented to the caller for a resolution. The validation framework does not extend to performing client-side validation, rather the validation is performed on the server side only. There are three main areas to consider when describing the Data Validation:
The ValidationService: Validation constraint types are dened and data is validated.

The Administration Cockpit: A front end for managing instantiated validation constraints types. Cockpit integration: Providing users with validation feedback in cockpits.

![25_image_0.png](25_image_0.png)

## Validation Architecture

See the architecture of the data validation framework. The main features include:
Validation is performed by the DefaultValidationService that implements ValidationService.

This service uses a JSR 303-compliant Validation engine: Hibernate Validator that performs the validation.

The validation engine expects:
ValidationConstraint denitions and instances that are loaded into the validation engine. Constraint groups for validating multiple constraints in one invocation. constraint instances in the form of annotated java classes, or encoded in an XML le.

The service can be used both explicitly and implicitly.

In both cases, Models or POJOs are passed to the service to be validated and a possibly empty set of HybrisConstraintViolations is returned.

The service is called implicitly via the ValidationInterceptor that intercepts calls made by ModelService.save().
The service can be called directly via a normal java call to the service's methods.

ValidationService contains two groups of methods:
Validation methods used to validate items, properties, or values. Control methods used to alter a behavior of the validation engine.

See the illustration of the Data Validation architecture.

![26_image_0.png](26_image_0.png)

## Validation Constraints

Validation constraints are regular SAP Commerce Cloud Types and are stored in a database like all other Types. As a consequence they may be created in the Administration Cockpit. When the validation framework starts or is reloaded with the reloadValidationEngine method, the following steps are automatically performed:
1. All constraint types are retrieved from the database.

2. They are transformed from SAP Commerce Cloud Models to an XML representation expected by the validation engine. 3. They are loaded into the validation engine.

We can modify the SAP Commerce Cloud constraints, and again call reloadValidationEngine method to reload the validation engine. It allows us to change the validation constraints at runtime. The validation engine loads also any constraints that are annotated directly in Java code, for example:
public class User { @NotNull private String first_name; }

## Constraint Denition

The Data Validation framework provides implementation of all constraint types dened in the JSR 303 specication. This includes:
PatternConstraint: To validate values using regular expressions.

PastConstraint and FutureConstraint: To validate values in comparison with the current date.

MinConstraint and MaxConstraint: To validate integer values in comparison with a set value.

DecimalMinConstraint and DecimalMaxConstraint: To validate values in comparison with a set decimal value.

SizeConstraint: To validate sizes of strings and collections.

AssertTrueConstraint and AssertFalseConstraint: To ensure that a value is true or false.

IsNullConstraint and IsNotNullConstraint: To ensure that a value is null or not null.

NotEmpty and NotBlank: To ensure that a value is not empty or blank.

XorNotNull Annotation: to ensure that of two given values, one and only one value is set.

Dynamic Annotation: similar to PatternConstraint but evaluates BeanShell code at runtime.

To see how these constraints are represented in SAP Commerce Cloud, and how to create constraint types, see the section below.

This is   For more    the SAP Help  27

## Creating Constraints Using Annotation

Constraints can be created by adding JSR303 Annotations to any POJO you may have written.

SamplePOJO.java class SamplePOJO
{ @NotNull private String value1;
 @Size(min = 3, max = 10)
private String value2; public void setValue1(final String value){ this.value1 = value; } public String getValue1(){ return value1; } public void setValue2(final String value){ this.value2 = value; } public String getValue2(){ return value2; }
}
@NotNull annotation for SamplePOJO.value1 has the same effect as creating IsNotNullConstraint in the SAP
Commerce Cloud Administration Cockpit. The similar situation is with the @Size annotation that corresponds to SizeConstraint. Annotations may be also used for Models, but it makes no sense, because Models are generated automatically and then annotations are removed. It is possible to create constraints for the same value both using annotations and the Administration Cockpit, for example, IsNotNullConstraint for value2. However, constraints created by using annotations are not displayed in the SAP Commerce Cloud Administration Cockpit. Nevertheless, they are used in the Data Validation process.

Let us consider the following example. There is a POJO with @Max(value = 3) annotation and a MaxConstraint with value set to 4 for the same POJO. The instance of this POJO gets the value set to 5. The data validation reports two violations:
Max violation: Value is 5 but must be 3. Max violation: Value is 5 but must be 4.

## Constraint Type System

The AbstractConstraint is the base type for all constraints and it contains methods and elds common for all constraint types. The AbstractConstraint contains an active attribute that can be used to exclude constraints from the validation process without a need to delete them and a needReload attribute, which displays whether the current constraint has already been loaded or not. Constraints may have different severity levels:
Error Warning Info

## 

They can be used to distinguish between various levels of constraint violations that may occur during the validation process.

They also have an inuence on the validation process. For example, a user is notied about some errors and warnings during the validation and is able to save an item only when errors are corrected.

![28_image_0.png](28_image_0.png) Figure: Hierarchy of constraint types in the Data Model Validation Every constraint type has a default error message that can be localized in the resources/ <extension_name>
/ValidationMessages.properties le in your extension.

It is common for all instances of a given constraint type. Besides, the default error message, every instance of the constraint type has also the message property. You may change its value to localize the message of the instance.

Constraints in the Data Model Validation are divided into two main groups:
Attribute related constraints.

## Type-Related Constraints.

This division reects differences between various constraint types and allows to maintain order in the code.

The AttributeConstraint is a base type for all attribute-related constraints. It extends the AbstractConstraint denition with the qualifier eld and a reference to the AttributeDescriptor. The AttributeConstraint contains information about a constrained attribute. It is used when you want to validate only one eld in a type.

There is also a possibility to validate POJO objects. In this case, the AttributeDescriptor and the ComposedType in a constraint instance are not used and the target attribute is set to a POJO class.

The TypeConstraint is a base type for all type-related constraints. It extends the AbstractConstraint and has a reference to the ComposedType. The TypeConstraint contains information about a constrained type. It is used when you want to validate more than one eld in a type. For example, the XorNotNullContraint, which extends the TypeConstraint, checks whether one of two elds: code or name is not null.

The DynamicConstraint allows to use the BeanShell script language to dene a constraint for a type or an attribute. The main advantage of the DynamicConstraint is an ability to change validation code without a need of recompilation. For This is   For more    the SAP Help  29

## Constraint Groups

Find out more about constraints groups. JSR303 Validators have the notion of constraint groups. Unless otherwise specied, all constraints belong to the default constraint group, which the validator uses by default when performing data validation. However, you're able to create, modify, and delete new constraint groups, and assign constraints to them. You may then perform data validation using a specic constraint group. This allows you to group validation rules to be run in different contexts. Constraint groups contain one or more constraints. The default constraint group can't be modied, renamed, or removed. It contains all constraints that aren't assigned to any other constraint group, and is used by default for data validation. However, you can call the validate method and pass in not only the Model or POJO, but also another constraint group. To activate one or more groups, call the validationService.setActiveConstraintGroups(list of groups). Constraint groups can be dened using the SAP Commerce Cloud Administration Cockpit. For more information, see Creating and Modifying Validation Constraints.

## Validation Errors

When validation errors occur during the implicit validation, a ModelSavingException is thrown, to conform with the current ModelService behavior.

However, the ModelSavingException contains a special ValidationViolationException as a cause of error, which can then be extracted and acted upon by the client. The ValidationViolationException gives information about constraint violations that occur during the validation process. It contains a message describing problems and a list of HybrisConstraintViolation objects, which gives a detailed information about violations.

When validation errors occur during the explicit validation, only a list of HybrisConstraintViolation is returned by the ValidationService.

The HybrisConstraintViolation is a wrapper class around ConstraintViolation object from the JSR 303 specication. It contains convenient methods that can be used to get information about validation violations. For more details, please refer to the API documentation.

## Validationservice

The ValidationService allows you to use the validation engine through a set of validation and control methods.

Validation methods are used to validate items, properties, or values. Control methods arevused to alter a behavior of the validation engine.

## Control Methods

setActiveConstraintGroups method allows choosing which constraint group is used for the implicit validation process. The save method from the ModelService requires only an item as a parameter. When you wish to change a default behavior and implicitly validate all saved items using specic constraint group, call the setActiveGroups method from the ValidationService with a desired group as the parameter. These settings persist for the current session only. An example:
Collection<ConstraintGroupModel> groups; // add desired constraint groups to groups object validationService.setActiveConstraintGroups(groups);
reloadValidationEngine method informs the validation engine that constraints have changed and reload is needed. Reloading the engine is necessary only when some constraints are added, removed, or edited. It is triggered in the Administration Cockpit. You can also call this explicitly when performing an explicit validation:
validationService.reloadValidationEngine();

## Validation Methods

validate method allows you to explicitly validate a Model or POJO.

validateProperty method validates only one property from a Model or a POJO.

validateValue method checks if a given value is valid for the specied property from a Model or POJO. This value, not the property value set in a Model, is checked for validity. To validate an existing Model property, use the validateProperty method.
All validation methods allow you to validate a Model or POJO class. A collection of constraint groups can be passed as an additional parameter. When groups are omitted, all active constraints from the default group are considered during the validation process.

All methods from this group return a collection of HybrisConstraintViolation objects. When the returned list is empty, the validation succeeded.

## Implicit Validation With The Validation Interceptor

The ValidationInterceptor is used to hook into the Model saving process where a model is rst validated before it can be saved.

The ValidationInterceptor is called just before the Model is saved to the database. Next, it passes the Model to the ValidationService, where appropriate validation rules are applied. If the Model is valid, it is saved to the database, otherwise the ValidationViolationException is thrown. All Models are implicitly validated before saving to the database. By default all saved items are validated using the defaultGroup constraint group. It means that all active constraints that do not belong to any group are in the default group and are used for the validation. When you wish to change a default behavior and implicitly validate all saved items using a specic constraint group, call the setActiveGroups method with a desired group as the parameter. If you wish to validate a constraint from another group in addition to constraints that are not assigned to any group, call the setActiveGroups method with both groups (default group and the additional group)
as parameters. These settings hold for the current session only.

![31_image_0.png](31_image_0.png)

## Explicit Validation With Direct Calls

The main usage of the ValidationService is for intercepting and validating models that are being saved. However, it is also possible to call the ValidationService directly.

All validation methods allow one to validate a Model or POJO class. Following POJOs are used for a demonstration:
SamplePOJO.java class SamplePOJO {
private String value1; private String value2; public void setValue1(final String value){ this.value1 = value; } public String getValue1(){ return value1; } public void setValue2(final String value){ this.value2 = value; } public String getValue2(){ return value2; }
}

# Examples Of Validation Methods

See examples of validation methods.

Validating a Model with the default constraint group:
ProductModel model = new ProductModel(); Set<HybrisConstraintViolation> constraintViolations = validationService.validate(model);
Validating a POJO with the default constraint group:
SamplePOJO pojo = new SamplePOJO(); Set<HybrisConstraintViolation> constraintViolations = validationService.validate(pojo);
Validating a Model with custom constraint groups:
ProductModel model = new ProductModel(); Collection<ConstraintGroupModel> groups; // add desired constraints groups to groups object and // pass it to the ValidationService Set<HybrisConstraintViolation> constraintViolations = validationService.validate(model, groups);
Validating a POJO with custom constraint groups:
SamplePOJO pojo = new SamplePOJO(); Collection<ConstraintGroupModel> groups; // add desired constraints groups to groups object and pass it to // the ValidationService Set<HybrisConstraintViolation> constraintViolations = validationService.validate(pojo, groups);
Validating one property from a Model with a default constraint group:
ProductModel model = new ProductModel();
String propertyName = "code";
Set<HybrisConstraintViolation> constraintViolations = validationService.validateProperty(model, propertyName);
Validating one property from a POJO with a default constraint group:
SamplePOJO pojo = new SamplePOJO(); String propertyName = "value1"; Set<HybrisConstraintViolation> constraintViolations = validationService.validateProperty(pojo, propertyName);
Validating one property from a Model with custom constraint groups:
ProductModel model = new ProductModel(); String propertyName = "code"; final Collection<ConstraintGroupModel> groups; // add desired constraints groups to groups object and // pass it to the ValidationService Set<HybrisConstraintViolation> constraintViolations = validationService.validateProperty(model, propertyName, groups);
Validating one property from a POJO with custom constraint groups:
SamplePOJO pojo = new SamplePOJO(); String propertyName = "value1"; final Collection<ConstraintGroupModel> groups; // add desired constraints groups to groups object and // pass it to the ValidationService Set<HybrisConstraintViolation> constraintViolations = validationService.validateProperty(pojo, propertyName, groups);
Validating one value from a Model with a default constraint group:
ProductModel model = new ProductModel(); String propertyName = "code"; String value = "1234"; Set<HybrisConstraintViolation> constraintViolations = validationService.validateValue(model, propertyName, value);
Validating one value from a POJO with a default constraint group:
SamplePOJO pojo = new SamplePOJO(); String propertyName = "value1"; String value = "1234"; Set<HybrisConstraintViolation> constraintViolations = validationService.validateValue(pojo, propertyName, value);
Validating one value from a Model with a custom constraint groups:
ProductModel model = new ProductModel(); String propertyName = "code"; String value = "1234"; final Collection<ConstraintGroupModel> groups; // add desired constraints groups to groups object and // pass it to the ValidationService Set<HybrisConstraintViolation> constraintViolations = validationService.validateValue(model, propertyName, value, groups);
Validating one value from a POJO with custom constraint groups:
SamplePOJO pojo = new SamplePOJO(); String propertyName = "value1";
String value = "1234";
final Collection<ConstraintGroupModel> groups; // add desired constraints groups to groups object and // pass it to the ValidationService Set<HybrisConstraintViolation> constraintViolations = validationService.validateValue(pojo, propertyName, value, groups);

## Validating Data For Multiple Languages

The Platform enables you to validate data in multiple languages before saving it. You can follow the guidelines to create constraints of any available type.

The following example assumes that you create an IsNotNull constraint for the name attribute of the Title type, for the Spanish and English languages. In order to save a new title, ll in the name eld for both English and Spanish.

## Creating A Constraint

You can easily create a new validation constraint and apply it to multiple languages using the Backoffice Administration Cockpit.

Procedure 1. Log in to Backoffice.

2. Go to System Validation Constraints . 3. Click the small arrow next to the + icon to open the options menu. 4. Click the arrow next to Attribute Constraint, and choose IsNotNull constraint. 5. In the window that appears, provide an identier for your constraint in the ID eld.

6. Click the ... icon next to the Enclosing Type eld, and search for and select the type with identier Title.

7. Click the ... icon next to the Attribute descriptor to validate eld, and select name.

8. Click the ... icon next to the Validation languages eld, and click the check marks next to English and Spanish in the window that appears to select them.

9. Optional: Click next to add additional attributes for your constraint.

10. Click Done to save your constraint.

## Creating An Item

After you have created your constraint, create an item.

## Procedure

1. Go to User Titles .

2. Click the + icon to add a new item. 3. Complete the Token eld. 4. Click Done.

## Results

If you try to save your item and you haven't provided both English and Spanish names for it, you get an error telling you that these names are required. This message means that validation works and the constraint has been imposed on the title.

## Customizing

Although the validation framework provides all constraints from the JSR 303 specication, sometimes other constraint types may be needed. This chapter presents how to create a custom constraint type.

## Creating Constraint Types

See the examples of how to create constraint types, including parameterized constraints.

## Note Simple Constraint Types

This section describes how to create simple constraint types. If you are interested in creating the DynamicConstraint, refer to the Creating Dynamic Constraints topic.

New constraint types can be dened in the <extension_name>-items.xml le in your extension. You may decide which basic classes the new constraint types should extend:
AttributeConstraint: If you wish to add constraints to a specied attribute.

TypeConstraint: If you wish to add constraints to a type (a group of attributes).
Custom constraint type creation consists of the following steps:
1. Dene a constraint type in the <extension_name> -items.xml le in your extension.

2. Create an annotation class that links the constraint type with a constraint validator. 3. Create the constraint validator class with a custom validation logic.

4. Add a constraint violation message template to the resources/ <extension_name>
/ValidationMessages.properties le.

## Note Package Name

In the examples from the next section, replace <YourPackage> with a package name that you use in your extension.

## Example Of Simple Constraint

Learn how to create a simple NotEmptyConstraint, which not only checks if a string is null, but also whether a validated string is not empty.

## Constraint Type Denition

First it is necessary to create the constraint type denition in the <extension_name> -items.xml le. The denition consists of:
code property: The constraint name extends property: A base type name jaloclass property: The name of the Jalo item class (gets generated at rst build).

annotation attribute with defaultValue property set to the name of the annotation class. Annotation is a link between the constraint type and a constraint validator that is used to validate data. To get more information about how to create an annotation, see the Annotation section. The constraint validator contains code that is executed when a constrained eld or type is being validated.
items.xml
<itemtype code="NotEmptyConstraint" autocreate="true" generate="true" extends="AttributeConstraint" jaloclass="<YourPackage>.NotEmptyConstraint">
<description>Custom constraint which checks for empty strings (Apache commons implementation)</description> <attributes>
<attribute qualifier="annotation" type="java.lang.Class" redeclare="true">
<modifiers write="false" initial="true" optional="false"/> <defaultvalue>
<YourPackage>.NotEmpty.class
</defaultvalue>
This is   For more    the SAP Help  36
</attribute>
</attributes>
</itemtype>

## Annotation

The next step is to create an annotation class to link the created constraint type with the constraint validator. The annotation class presented below may be used as a template for creating annotations. An annotation type is dened using the
@interface keyword. All attributes of an annotation type are declared in a method-like manner. The JSR 303 specication demands, that any constraint annotation denes:

The message attribute: Returns the default key for creating error messages if the constraint is violated.

The groups attribute: Allows the specication of validation groups, to which this constraint belongs. The default value is an empty array of type Class<?>.

The payload attribute: Can be used to assign custom payload objects to a constraint. This attribute is not used by the API itself.
Moreover, there are some rules that should be obeyed:

The value of @Target annotation should be set to FIELD when creating the AttributeConstraint.

The value of @Target annotation should be set to TYPE when creating the TypeConstraint.

The default value of message() method should be set to key from the resources/ <extension_name>
/ValidationMessages.properties le of your extension.
NotEmpty.java
@Target({ FIELD }) @Retention(RUNTIME) @Constraint(validatedBy = NotEmptyValidator.class) @Documented public @interface NotEmpty { String message() default "{<YourPackage>.NotEmpty.message}"; Class<?>[] groups() default {}; Class<? extends Payload>[] payload() default {}; }

## Constraint Validator

The constraint validator contains the validation logic. Its isValid method inherited from the ConstraintValidator interface from the JSR 303 specication is invoked whenever a Model containing constrained value is validated. Constraint validator denition consists of the annotation class, in our case NotEmpty, and a class of attribute being validated, in that case String. The same class is used in isValid method.

NotEmptyValidator.java public class NotEmptyValidator implements ConstraintValidator<NotEmpty, String> { @Override public void initialize(final NotEmpty constraintAnnotation) {
// empty
 }

 @Override public boolean isValid(final String value, final ConstraintValidatorContext context) {
return !StringUtils.isEmpty(value);
 } }

## Error Message

Insert an error message to the resources/ <extension_name> /ValidationMessages.properties le of your extension. It is displayed by default for every instance of a constraint type. There is also a possibility to override this message, but it should be done for each instance separately. The common practice is to use a fully qualied class name with .message suffix as a default value.

ValidationMessages.properties
<YourPackage>.NotEmpty.message='{type}.{field}' can not be empty.

## Example Of Parametrized Constraint

Learn how to add a parametrized StringLengthConstraint that checks if a given string length is in specied range.

The procedure is the same as for creating simple constraints but this time the new constraint type brings own attributes. Furthermore, a conguration for managing these attributes should be added for the Administration Cockpit additionally.

## Constraint Type Denition

Parametrized constraint denition extends the denition of a simple constraint type from the previous example with additional attributes: min and max.

items.xml
<itemtype code="StringLengthConstraint" autocreate="true" generate="true" extends="AttributeConstraint" jaloclass="<YourPackage>.StringLengthConstraint"> <description>Custom constraint which checks if string's length is in specified range.</description> <attributes> <attribute type="java.lang.Integer" qualifier="min"> <description>Underflow value</description> <modifiers read="true" write="true" search="true" optional="false" initial="true" />
 <persistence type="property" /> </attribute> <attribute type="java.lang.Integer" qualifier="max"> <description>Overflow value</description> <modifiers read="true" write="true" search="true" optional="false" initial="true" />
 <persistence type="property" /> </attribute> <attribute qualifier="annotation" type="java.lang.Class" redeclare="true"> <modifiers write="false" initial="true" optional="false"/> <defaultvalue> <YourAnnotationsPackage>.StringLength.class </defaultvalue> </attribute> </attributes> </itemtype>

## Annotation

Annotation denition from the previous example is extended with methods for additional parameters. These additional parameters are then used by the ConstraintValidator described below. Note that in annotation denition only primitive types like String, Class, annotations, enumerations, or 1-dimensional arrays are allowed. You can also congure here default values.

StringLength.java
@Target({ FIELD }) @Retention(RUNTIME) @Constraint(validatedBy = StringLengthValidator.class) @Documented public @interface StringLength { String message() default "{<YourPackage>.StringLength.message}"; Class<?>[] groups() default {}; Class<? extends Payload>[] payload() default {}; int min() default 0; int max() default Integer.MAX_VALUE; }

## Constraint Validator

Constraint validator denition from the section Example of Simple Constraint is extended with:
Additional parameters

initialize method to gather parameters from the constraintAnnotation Optional validateParameters method
StringLengthValidator.java public class StringLengthValidator implements ConstraintValidator<StringLength,String> { private int min; private int max; @Override public void initialize(final StringLength constraintAnnotation) { min = constraintAnnotation.min(); max = constraintAnnotation.max(); validateParameters(); } @Override public boolean isValid(final String value, final ConstraintValidatorContext constraintValidatorContext) { if (value == null) // According to the JSR 303 null values are valid {
 return true;
 } final int length = value.length(); return length >= min && length <= max; } private void validateParameters() { if (min < 0)
This is   For more    the SAP Help  39
 {
 throw new IllegalArgumentException("The min parameter cannot be negative.");
 } if (max < 0) {
 throw new IllegalArgumentException("The max parameter cannot be negative.");
 } if (max < min) {
 throw new IllegalArgumentException("The length cannot be negative.");
 } } }

## Error Message

In error messages, you can address constraint parameters using their names.

ValidationMessages.properties
<YourPackage>.StringLength.message='{type}.{field}' length must be between {min} and {max}.

## Conguration In The Administration Cockpit

An additional XML le is needed for Administration Cockpit to properly display new constraint types. The conguration le should be located in the /resources/admincockpit/config directory:
Editor_StringLengthConstraint_Admin.xml
<editor>
<group qualifier="AttributeConstraint" visible="true" initially-opened="true">
<label lang="de">Obligatorische Daten</label> <label lang="en">Mandatory data</label> <property qualifier="AbstractConstraint.id" /> <property qualifier="AttributeConstraint.descriptor" /> <property qualifier="AbstractConstraint.active" />
<property qualifier="AbstractConstraint.severity" />
<property qualifier="StringLengthConstraint.min" /> <property qualifier="StringLengthConstraint.max" /> <property qualifier="AbstractConstraint.defaultMessage" /> <property qualifier="AbstractConstraint.message" />
</group> <group qualifier="admin" visible="true" initially-opened="false">
<label lang="de">Andere Daten</label> <label lang="en">Other data</label> <property qualifier="AbstractConstraint.type" /> <property qualifier="AbstractConstraint.target" editor="class" /> <property qualifier="AttributeConstraint.qualifier" /> <property qualifier="AbstractConstraint.constraintGroups" >
<parameter>
<name>allowCreate</name> <value>true</value>
</parameter> <parameter>
<name>defaultEmptyLabelKey</name> <value>ea.constrain_group_default_label</value>
</parameter>
</property> <property qualifier="AbstractConstraint.annotation" editor="class"/> <property qualifier="Item.pk" /> <property qualifier="Item.creationTime" /> <property qualifier="Item.modifiedtime" />
</group>
</editor>

## Creating Constraint Groups

Constraint groups may be created using Java code.

Each constraint group should have a unique ID. Thus, each instance of the ConstraintGroup should use a unique interface as a marker. The interface is automatically generated during runtime basing on the unique group ID. However, it is possible to provide the interface name that should be used. It can be an existing interface class or a nonexisting class, because it can be generated. There exists a default constraint group, which can't be modied, removed, or assigned to constraints. Each constraint that is not assigned to any other group belongs to the default group.

To get constraints that are in the default group, use validationService.getDefaultconstraintGroup() method, as in the example.

AssertTrueConstraintModel constraint = modelService.create(AssertTrueConstraintModel.class) constraint.setId("trueconstraint"); //set attribute descriptor but no group here! modelService.save(constraint); constraint.getConstraintGroups(); //returns an empty set validationService.getDefaultconstraintGroup().getConstraints(); //return a collection with the Asse constraint.setConstraintGroups(SelfDefinedGroup); validationService.getDefaultconstraintGroup().getConstraints(); //now it returns an empty collectio The following code snippet presents how to create constraint groups in Java code.

Set<AbstractConstraintModel> constraints; // add desired constraints to set; ConstraintGroupModel group1 = new ConstraintGroupModel(); group1.setId("group1"); group1.setConstraints(constraints); modelService.save(group1); ConstraintGroupModel group2 = new ConstraintGroupModel(); group2.setId("group2"); group2.setInterfaceName("non.existing.Interface"); // it is important to use // different interface marker for each group group2.setConstraints(constraints); modelService.save(group2);
For details see the Constraint Groups section above.

## Creating Dynamic Constraints

The main advantage of the DynamicConstraint is that validation business logic can be written in Java dynamically without a need for recompilation. This is possible thanks to the BeanShell interpreter that can execute Java source code at runtime. To create a DynamicConstraint, you may use the SAP Commerce Cloud Administration Cockpit.

For more information, see Administration Cockpit Tutorial - Chapter (2): section Dynamic Constraints.

The script body for the DynamicConstraint attached to the Product checks if the Code is equal to the attribute Name for the current context language:
return getCode().equals(getName());
An instance, which gets validated is implicitly in context. It means that in our example getName() and getCode() methods are executed directly on the validated Product instance. A result of dynamic constraint validation depends on values of This is   For more    the SAP Help  41 attributes of instance being validated.

Hints for writing BeanShell snippet:
1. General regulation to write DynamicConstraint script, is that the expression must return object, which somehow can be evaluated as a boolean true or false value (logic or textual).

2. Implicitly script is performed when the validation object is passed as the this object in Java meaning. All methods from the constrained Model can be invoked as get(Property), is(Property).

3. You can also access implicit context object ctx, which is an instance of the org.springframework.context.ApplicationContext. It gives the possibility to access Spring-based beans, services.
4. Be aware of runtime exceptions, for example NullPointerException when invoking method of the null object.

Another example of BeanShell expression uses the ServiceLayer's I18Nservice. It compares the isocode of LanguageModel with the Locale's language of the current session:
java.util.Locale loc = ctx.getBean(de.hybris.platform.servicelayer.i18n.I18NService.class).getCurrentLocale(); return !loc.getLanguage().equals(getIsocode());
The code snippet below shows how to create DynamicConstraint using Java:
DynamicConstraintModel constraint = new DynamicConstraintModel(); constraint.setActive(true); constraint.setLanguage(ValidatorLanguage.BEANSHELL); constraint.setExpression("return false;");