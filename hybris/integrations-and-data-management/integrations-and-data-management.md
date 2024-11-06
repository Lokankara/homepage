# Integrations And Data Management

Integrate SAP Commerce Cloud with a range of other products and services, and synchronize data between them. Find information here about the integration options and tools available with the core SAP Commerce Cloud release. For ready-to-use solutions when integrating SAP Commerce Cloud with other SAP back end systems and services, see the options available in the separately released SAP Commerce Cloud, integration extension pack.

 Note Some integrations are released as separate product packs, and may not be available for all versions of SAP Commerce Cloud. For a complete list of current, separately released integrations and compatible SAP Commerce Cloud versions, see Integration Packs.

![1_image_0.png](1_image_0.png)

Introduction to SAP Commerce Cloud Integrations SAP Commerce Cloud offers various solutions to integrate with other SAP applications and services. The integration tools enable you to quickly get started with setting up one of the Intelligent Selling Services applications, or transferring master data to and from an SAP back end system using the Integration APIs to connect to SAP Business Technology Platform. For quickly importing and exporting data to and from your system, you can use ImpEx. SAP Commerce Cloud also includes the ready to use Intelligent Selling Services integrations for connecting to customer data-driven applications such as Merchandising and Segmentation. In addition to these ready to use integration solutions, SAP Commerce Cloud includes foundational tools for master data integration, such as the Integration API module and Data Hub. With these, you can connect to SAP back end systems for master data management of customer data, product and pricing, order and fulllment, or invoicing, for example. Ready-to-use solutions for many of these types of integrations are provided in the optional SAP Commerce Cloud, integration extension pack. The following diagram shows a conceptual overview of the SAP Commerce Cloud integration landscape. Explore the topics in this section or in the related links for more information about each solution.

![2_image_0.png](2_image_0.png)

Related Information SAP Commerce Cloud, Integration Extension Pack

## Integration Api Module

SAP Commerce Cloud's Integration API Module exposes a set of interfaces used for data integration with SAP Commerce Cloud. Use the Integration API module to connect services to send data to, or receive data from, SAP Commerce Cloud. The Integration API module simplies data integration with SAP Commerce Cloud using Integration Objects. These objects are used in the payload that is sent or received from SAP Commerce Cloud to dene data types. Inbound and outbound integration objects are described in this guide.

 Tip If you're looking for standard RESTful APIs to access SAP Commerce functionality for your storefront or other external application, then see Omni Commerce Connect.

![2_image_1.png](2_image_1.png)

This is   For more    the SAP Help  3

## Integration Api Features

Integration API features include Integration Objects, enhancements to the OData protocol for use with Integration API services, and Backoffice tools for modeling Integration Objects and monitoring Integration API requests.

About Integration Objects A new Integration Object creates an integration. A new integration creates API service endpoints that accept one or more objects, and dene the object's payload. Integration Object Modeling You can use Integration Objects to model items dened in the SAP Commerce Cloud platform Type System. OData Services OData is a protocol for building and using RESTful APIs that the Integration API uses and extends. Outbound Features Congure outbound services for publication and localization of Integration Objects, Items, and item attributes. Integration Object Modeling via Backoffice Use Modeling to create Integration Objects and Plain Old Java Object (POJO) Integration Objects. Integration Object Authentication In Backoffice, you can authenticate an Integration Object with OAuth or Basic authentication. Integration Object Authorization In the Backoffice Integration UI Tool, you can view type-level permissions and set up access rights for users working with Integration Objects. Integration API Request Monitoring View the results of inbound and outbound Integration API requests using the Integration UI Tool in Backoffice, and manage the data retention period for such requests. Integration API Security Secure Integration API endpoints using OAuth or Basic authentication, authorization, and SSL features. User groups and user roles provide security for dened groups and users. See the following topics for details. Integration API Meta APIs This topic provides an overview of the Meta APIs available for Integration API scenarios. Exporting Conguration Types This feature is useful when needing to move congurations from one environment to another without having to recreate them.

## About Integration Objects

A new Integration Object creates an integration. A new integration creates API service endpoints that accept one or more objects, and dene the object's payload. Each Integration Object is specic to its own use case, or purpose. For example, an SAP ERP order object might use all available elds, but an SAP Marketing order object might use only the elds related to Marketing needs. When you install the Integration API extensions, several services are available out-of-the-box, as described in this section. Meta API
You can view the provided Integration Objects and associated integration object items using the IntegrationServices endpoint. The following request returns all of the Integration Objects in the Integration API.

GET https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects To retrieve metadata, add the $metadata query option to the request URL. For example:
GET https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects?$metadata Integration Objects - Inbound You can generate OData v2 services by creating Integration Objects. Each service is generated through the Backoffice Integration UI Tool perspective or via ImpEx at runtime. The Integration Object denitions offer a business-world view of the types dened in the platform, which are better suited to real-world integration scenarios. For example, there are many parts composing products, orders, and customers that the Integration Objects encapsulate into a cohesive unit of work. Use the POST service to create and update Integration Objects. The POST service supports deep persistence and batch data loads. You can load up to 200 Integration Objects synchronously through the OData batch feature.

Use the GET service to look up an individual Integration Object by its integrationKey. There is also a convenient unique attribute for the types in the type system that do not dene a key.

Use DELETE to delete an Integeration Object using an integrationKey.

![4_image_0.png](4_image_0.png)

![4_image_1.png](4_image_1.png)

![4_image_2.png](4_image_2.png)

![4_image_3.png](4_image_3.png)

## Integration Object Modeling Creating A Simple Integration Object

Integration Objects - Outbound You can dynamically dene the payload of an Integration Object published to an external target. Developers leverage this ability to create skeletal business processes and interceptors (building blocks). If you are less technical, you can dynamically modify the building blocks at runtime using Backoffice.

Integration Objects are sent to HTTP or OData v2 endpoints. The payload of the request is dynamically dened through Backoffice or ImpEx.

The destination is dened at runtime through the apiregistryservice. Both OAuth2 and Basic Credentials are supported.

The default client is provided, but it can be extended to support other use cases.

Further, you can use outbound sync to publish new and modied Integration Objects to external systems. See Related Links for more information.

Related Information Outbound Sync You can create Integration Objects in the following ways:
Importing an Integration Object model via ImpEx. See Creating a Simple Integration Object. Posting an Integration Object model via the Meta API. See Modeling using the Meta API. Via the Backoffice. See Integration Object Modeling via Backoffice.

When creating an Integration Object, the following restrictions apply:
Integration Object root items must be complex item types. Items must not be created for primitive types. Attributes of platform atomic types are not supported except the atomic type for standard Java classes. Only primitive localized attributes are supported. Complex localized types cannot be handled. Only pimitive type map attributes are supported. Maps of complex types cannot be modeled. Although creating an Integration Object without a single item type is possible, it renders the Integration Object useless.

Context Create a Product Integration Object in the system for use in subsequent Integration API requests.

 Note You cannot associate two unique attributes to the same composed type in the type system and have the ag unique=true. The Attribute denitions must point to different IntegrationObjectItems in the returnIntegrationObjectItem. The mapping in this procedure ensures proper building of integration keys and allows attributes of the same type to have a different structure.

For example, the following ImpEx shows how the jobMedia and workMedia attributes return Integration Objects of type GetIntegrationTestGroup3:JobMedia and GetIntegrationTestGroup3:WorkMedia, which are of type ImpExMedia.

INSERT_UPDATE IntegrationObject; code[unique = true]; ; GetIntegrationTestGroup3 INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code) ; GetIntegrationTestGroup3 ; JobImpExMedia ; ImpExMedia ; GetIntegrationTestGroup3 ; WorkImpExMedia ; ImpExMedia ; GetIntegrationTestGroup3 ; ImpExImportCronJob ; ImpExImportCronJob INSERT_UPDATE IntegrationObjectItemAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = true]; attr ; GetIntegrationTestGroup3:ImpExImportCronJob ; code ; ImpExImportCronJob:code ; ; GetIntegrationTestGroup3:ImpExImportCronJob ; jobMedia ; ImpExImportCronJob:jobMedia ; GetIntegrationTestGroup3:JobImpExMedia ; true ; GetIntegrationTestGroup3:ImpExImportCronJob ; workMedia ; ImpExImportCronJob:workMedia ; GetIntegrationTestGroup3:WorkImpExMedia ; true ; GetIntegrationTestGroup3:JobImpExMedia ; code ; ImpExMedia:code ; ; GetIntegrationTestGroup3:WorkImpExMedia ; code ; ImpExMedia:code ; ; GetIntegrationTestGroup3:WorkImpExMedia ; name ; ImpExMedia:name ;
This is   For more    the SAP Help  5 You can use Integration Objects to model items dened in the SAP Commerce Cloud platform Type System. Creating an Integration Object extends the SAP Commerce Cloud type system and exposes an OData endpoint that you can call to get data about that Integration Object.

Procedure 1. In a web browser, navigate to the SAP Commerce Cloud Administration Console (Administration Console) at https://localhost:9002/ and log in.

2. Click Console ImpEx Import .

3. Paste the following script into the Import Content eld.

INSERT_UPDATE IntegrationObject; code[unique = true]; ; MyProduct INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique=true] ; code[unique = true] ; type(code) ; MyProduct ; Product ; Product ; MyProduct ; Catalog ; Catalog ; MyProduct ; CatalogVersion ; CatalogVersion ; MyProduct ; Unit ; Unit INSERT_UPDATE IntegrationObjectItemAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = true] ; MyProduct:Product ; code ; Product:code ; ; MyProduct:Product ; catalogVersion ; Product:catalogVersion ; MyProduct:CatalogVersion ; MyProduct:Product ; name ; Product:name ; ; MyProduct:Product ; unit ; Product:unit ; MyProduct:Unit ; MyProduct:Unit ; code ; Unit:code ; ; MyProduct:Catalog ; id ; Catalog:id ; ; MyProduct:CatalogVersion ; catalog ; CatalogVersion:catalog ; MyProduct:Catalog ; MyProduct:CatalogVersion ; version ; CatalogVersion:version 4. Click Import content. The script creates the Product Integration object.

## Modeling Best Practices

This topic outlines best practices for creating Integration Objects. When creating an Integration Object:
Select a root item. Include all attributes, which are unique in the type system for that item type. Include any optional primitive, enum, or map attributes for the item type. If the Integration Object is intended for inbound requests, include all non-optional attributes in the item. If the root item type has a unique attribute that references another item, include the referenced item type and only its key attributes in the Integration Object. If other non-key reference attributes must be included, then add the referenced item type and only its key attributes to the Integration Object. This Integration Object should not manage other referenced types as there should be other Integration Objects for managing the references. For example, Catalog is referenced from CatalogVersion's key attribute "catalog". Catalog and its key attribute "id" are included so that references to a Catalog in CatalogVersion are updated, but do not include any other Catalog attributes because it's beyond the scope of the example CatalogVersion Integration Object.

Be very careful when adding autoCreate=true to an Integration Object attribute because it means that the Integration Object manages more than one entity. Exceptions can be made, but you should weigh the pros and cons.

An important fact to always keep in mind when creating Integration Objects: The size of an Integration Object = the size of the database transaction. Growth of the database transaction increases chances of a deadlock. For example, a very simple Integration Object that contains only an Order item can't cause a deadlock because even if two concurrent requests are updating the Order record in the database, and each request is a transaction (FYI), the request that commits the changes rst wins, and the second request results in StaleDataException. Of course, the exact behavior depends on the isolation level congured for the transaction and locking strategies (row, page, table), so it may succeed too, but it's not important as there will be no deadlock.

If the Integration Object contains two items, for example, Order and OrderEntry. Although this relationship feels safe because it's a partOf relationship and OrderEntries can be bound to only one particular Order, a deadlock is possible. Imagine two concurrent requests updating the same order:
 Sample Code
{ "code": "order1", "entries": [ { "seqNumber": 1, ... }, { "seqNumber": 2, ... } ] }
and Sample Code
{ "code": "order1", "entries": [ { "seqNumber": 2, ... }, { "seqNumber": 1, ... }

If the two requests are being processed concurrently:
 Sample Code Request/Transaction 1 Request/Transaction 2 places lock on the entry 1 places lock on entry 2 waits to get a lock on entry 2 waits to get a lock on entry 1 That is a deadlock. If the Integration Object contains references to CatalogVersions, Catalog, Product, Unit, Currency, Customer, etc. types, each of those references can be locked on to, which increases the chances for a deadlock.

## Modeling Using The Meta Api

With the Meta API, you can create and view Integration Objects.

The IntegrationService API exposes all congured Integration Objects through the Integration API. The integrationservice denes the IntegrationService Integration Object for managing Integration Objects.

 Note For SAP Commerce Cloud version 2011 and higher, to expose an Integration Object as an API it must be associated with an InboundChannelConguration (ICC). When upgrading to version 2011 and higher, an ICC is automatically created with Basic authentication for an Integration Object that doesn't have a corresponding ICC. Once created, to set the authentication to OAuth, update the authentication type in the ICC. For more information, see Authentication and Exposing an Integration Object using the Meta API. For new Integration Objects, creating an Integration Object as part of an ICC is the most convenient approach.

When you dene a new Integration Object, the Integration API module exposes it through the following URL.

 https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects Because IntegrationService is also an Integration Object, you can request $metadata and a service document. The $metadata query option retrieves all metadata for an Integration Object.

For example:
GET https://localhost:9002/odata2webservices/IntegrationService/$metadata Note You can dene an Integration Object with either IntegrationObjectItems or IntegrationObjectClasses but an Integration Object can't include both at the same time.

All Integration Object Items are exposed through:
https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjectItems All Integration Object Item attributes are exposed through:
https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjectItemAttributes All Integration Object Classes are exposed through:
https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjectClasses All Integration Object Class attributes are exposed through:
https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjectClassAttributes IntegrationService Meta API Examples The following examples show how to make POST and GET requests to the IntegrationService API.

POST to the IntegrationService API Example This POST request example shows how to create an Integration Object named ExampleProduct through the IntegrationService Meta API. The example uses a simplied payload for circular reference attributes. For more information, see Circular Reference Attributes. Request URL
POST https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects Request Body
{ "code": "ExampleProduct", "integrationType": { "code": "INBOUND" }, "items": [ { "code": "Catalog", "type": { "code": "Catalog" }, "integrationObject": { "code": "ExampleProduct" }, "attributes": [ { "attributeName": "id", "attributeDescriptor": { "qualifier": "id", "enclosingType": { "code": "Catalog" } } }, { "attributeName": "name", "attributeDescriptor": { "qualifier": "name", "enclosingType": { "code": "Catalog" } } } ] }, { "code": "CatalogVersion", "type": { "code": "CatalogVersion" }, "integrationObject": { "code": "ExampleProduct" }, "attributes": [ { "attributeName": "version", "attributeDescriptor": { "qualifier": "version", "enclosingType": { "code": "CatalogVersion" } } }, { "attributeName": "catalog", "attributeDescriptor": { "qualifier": "catalog", "enclosingType": { "code": "CatalogVersion" } }, "returnIntegrationObjectItem": { "code": "Catalog", "integrationObject": { "code": "ExampleProduct" } }, "unique": true
 }
 ] }, { "code": "Unit", "type": { "code": "Unit" }, "integrationObject": { "code": "ExampleProduct" }, "attributes": [ { "attributeName": "code", "attributeDescriptor": { "qualifier": "code", "enclosingType": { "code": "Unit" } } }, { "attributeName": "unitType", "attributeDescriptor": { "qualifier": "unitType", "enclosingType": { "code": "Unit" } } } ] }, { "code": "Product", "type": { "code": "Product" }, "integrationObject": { "code": "ExampleProduct" }, "root": true, "attributes": [ { "attributeName": "code",
This is   For more    the SAP Help  8
 "attributeDescriptor": {
 "qualifier": "code", "enclosingType": { "code": "Product" } } }, { "attributeName": "catalogVersion", "attributeDescriptor": { "qualifier": "catalogVersion", "enclosingType": { "code": "Product" }
 },
 "returnIntegrationObjectItem": { "code": "CatalogVersion", "integrationObject": { "code": "ExampleProduct"} } }, { "attributeName": "name", "attributeDescriptor": { "qualifier": "name", "enclosingType": { "code": "Product" } } }, { "attributeName": "description", "attributeDescriptor": { "qualifier": "description", "enclosingType": { "code": "Product" } } }, { "attributeName": "unit", "attributeDescriptor": { "qualifier": "unit", "enclosingType": { "code": "Product" } }, "returnIntegrationObjectItem": { "code": "Unit", "integrationObject": { "code": "ExampleProduct"} } }, { "attributeName": "order", "attributeDescriptor": { "qualifier": "order", "enclosingType": { "code": "Product" } } } ] } ] }
POST to the IntegrationService Meta API to Create a POJO Integration Object Note You can't use POJO Integration Objects in REST endpoints to either post data to, or retrieve data from, the platform database. Only $metadata requests are supported for Integration Objects modeled with IntegrationObjectClass for GET, POST, PATCH, and DELETE requests.

This POST request example shows how to create a POJO Integration Object named Product through the IntegrationService Meta API. Request URL
 Sample Code POST https://localhost:9002/odata2webservices/IntegrationService/InboundChannelConfigurations Response Body Sample Code
{ "integrationObject": { "code": "POJO", "classes": [ { "root": false, "code": "Unit", "type": "de.hybris.platform.core.model.product.UnitModel", "attributes": [ { "attributeName": "code", "unique": true, "readMethod": "getCode" This is   For more    the SAP Help  9

 }
 ] }, { "root": true, "code": "Product", "type": "de.hybris.platform.core.model.product.ProductModel", "attributes": [ { "attributeName": "code", "unique": true, "readMethod": "getCode" }, {
 "attributeName": "unit",
 "returnIntegrationObjectClass": { "code": "Unit" } } ] } ] }, "authenticationType": { "code": "BASIC" } }
GET from the IntegrationService API
This GET request example shows how to view the ExampleProduct Integration Object posted in the previous example, using the IntegrationService Meta API.

Request URL
GET https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects?$filter=code eq 'ExampleProduct' Response Body
{ "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects('ExampleProduct')", "uri": "https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects('ExampleProduct')", "type": "HybrisCommerceOData.IntegrationObject" }, "code": "ExampleProduct", "integrationKey": "ExampleProduct", "integrationType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects('ExampleProduct')/integrationType" } }, "items": { "__deferred": {
 "uri": "https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects('ExampleProduct')/items"
 } } } ] } }
Modeling POJO Integration Objects for Outbound Events Create a Plain Old Java Object (POJO) as an Integration Object via ImpEx to use in outbound scenarios.

Context Note This page may contain information about features that were only introduced in an update release. Ensure you are always on the latest release to be able to make use of all xes, security updates, and features. For a complete list of what was introduced in each update release, see What's New.

Integration API supports modeling POJOs as Integration Objects for their use in outbound scenarios. POJO Integration Objects must include a root Integration Object Class. Any class found in the classpath can be modeled as an Integration Object, but only POJO Integration Objects allow you to model outbound business events. Any class type that extends the AbstractEvent type, except for item specic events (ItemUpdatedEvent, ItemCreatedEvent, ItemDeletedEvent), is considered a business event.

 Note Before you start, consider the following limitiations of a POJO Integration Object:
Modeling classes and items are separate: both cannot be done at the same time within the same Integration Object. Only one root Integration Object Class per POJO Integration Object is allowed.

Procedure 1. In a web browser, navigate to the SAP Commerce Cloud Administration Console (Administration Console) and log in.

2. Select Console ImpEx Import . 3. Paste the following sample script into the Import Content eld:
INSERT_UPDATE IntegrationObject; code[unique = true] ; SampleEventIO
INSERT_UPDATE IntegrationObjectClass; integrationObject(code)[unique = true]; code[unique = true]; type 
 ; SampleEventIO ; DeletedAddressEvent; de.hybris.platform.commerceservices.event.Del ; SampleEventIO ; BaseStore ; de.hybris.platform.store.BaseStoreModel ; SampleEventIO ; Customer ; de.hybris.platform.core.model.user.CustomerMo $type = integrationObjectClass(integrationObject(code), code) $attributeType = returnIntegrationObjectClass(integrationObject(code), code) INSERT_UPDATE IntegrationObjectClassAttribute; $type[unique = true] ; attributeName[unique = true]; readMethod ; $attributeType ; SampleEventIO:DeletedAddressEvent; id ; getTimestamp; ; SampleEventIO:DeletedAddressEvent; store ; getBaseStore; SampleEventIO:Base ; SampleEventIO:DeletedAddressEvent; customer ; ; SampleEventIO:Cust ; SampleEventIO:BaseStore ; id ; getUid ; ; SampleEventIO:BaseStore ; name ; ; ; SampleEventIO:Customer ; uid ; ; ; SampleEventIO:Customer ; name ; ; 
 Note The places where readMethod is empty are created automatically using the name of the attribute. In the above example, the name attribute has a method created called getName.

When you dene a POJO Integration Object, you can't dene integration keys and other key attribute descriptors, and the EDMX for that Integration Object does not describe any key attributes for the Integration Object.

4. Select Import Content. The script creates the Customer POJO Integration Object.

 Note If you want to restrict the ability to update the root class of a POJO Integration Object, set toggle.root.update.restriction.enabled to true. The default value is false.

## Advanced Integration Object Modeling

Some modeling tasks require conguration via ImpEx or Meta API instead of Backoffice. Advanced Integration Object modeling tasks include:
Linking an owner attribute between Customer and Address Creating a relationship between Order and Customer Modeling an Owner Attribute for Customer and Address Use either ImpEx or the Meta API to model the owner attribute to link the Customer and Address Integration Objects.

Context Because Backoffice does not support modeling of the owner attribute via the Integration UI Tool, use either ImpEx or the Meta API instead.

Modeling via ImpEx Procedure In the Administration Console, import the following ImpEx that includes the owner attribute:
INSERT_UPDATE IntegrationObject; code[unique = true]; integrationType(code) ; OutboundCustomer; INBOUND INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code); root[default = false]; itemTypeMatch(co ; OutboundCustomer ; Address ; Address ; ; ; ; OutboundCustomer ; Customer ; Customer ; true ; ; INSERT_UPDATE IntegrationObjectItemAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = true]; attr ; OutboundCustomer:Address ; publicKey ; Address:publicKey ; ; true ; ; OutboundCustomer:Address ; owner ; Address:owner ; OutboundCustomer:Customer ; ; ; OutboundCustomer:Customer ; uid ; Customer:uid ; ; true ; ; OutboundCustomer:Customer ; addresses ; Customer:addresses ; OutboundCustomer:Address ; ; 
Modeling via Meta API
Procedure Send POST request https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects with the following body:
 Sample Code
{ "code": "OutboundCustomer", "items": [ {
 "code": "Address",
 "type": { "code": "Address" }, "root": false }, { "code": "Customer", "type": { "code": "Customer" }, "root": true, "attributes": [ { "attributeName": "uid", "attributeDescriptor": { "qualifier": "uid", "enclosingType": { "code": "Customer" } }, "unique": true }, { "attributeName": "addresses", "attributeDescriptor": { "qualifier": "addresses", "enclosingType": { "code": "Customer" } }, "returnIntegrationObjectItem": { "code": "Address" }, "unique": false, "autoCreate": false } ] }, { "code": "Address", "attributes": [ { "attributeName": "publicKey", "attributeDescriptor": { "qualifier": "publicKey", "enclosingType": { "code": "Address" } }, "unique": true }, { "attributeName": "owner", "attributeDescriptor": { "qualifier": "owner", "enclosingType": { "code": "Address" } }, "returnIntegrationObjectItem": { "code": "Customer" }, "unique": false, "autoCreate": false } ] } ] }

 Note Address is dened twice because there is a circular reference between Customer and Address. The rst time you create the Address IntegrationObjectItem is to create the Customer referencing the Address. The second time is to update the Address IntegrationObjectItem so that it points the owner attribute to the Customer.

## Creating A Relationship Between Order And Customer

Congure an attribute for a specied user type, such as the Customer Integration Object's customerID attribute.

Context The Order Integration Object is associated with the User Integration Object, but Customer is a subtype of User. Therefore, to use a Customer attribute such as customerID, create that relationship using either ImpEx or the Meta API.

The following scenarios use an example Integration Object called MKTOutboundOrderTest. The steps assume that the Integration Object is already created and available in Backoffice.

## Modeling Via Impex Procedure

1. Navigate to Backoffice and log in.

2. Select the Integration UI Tool perspective and select Integration Object Modeling if it is not already selected. 3. Select the Integration Object from the dropdown list and select the Metadata Viewer button. 4. In the ImpEx View, select Copy to Clipboard and paste the contents into a text le.

5. In the text le, replace the User type with Customer and User:uid with Customer: customerID, as shown.

INSERT_UPDATE IntegrationObject; code[unique = true]; integrationType(code) ; MKTOutboundOrderTest; INBOUND INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique=true]; code[unique = true]; type(code) ; MKTOutboundOrderTest ; Order ; Order ; MKTOutboundOrderTest ; Customer ; Customer INSERT_UPDATE IntegrationObjectItemAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = true] ; MKTOutboundOrderTest:Order ; user ; Order:user ; MKTOutboundOrderTest:Customer ; ; ; MKTOutboundOrderTest:Order ; code ; Order:code ; ; true ; ; MKTOutboundOrderTest:Customer ; name ; Customer:name ; ; ; ; MKTOutboundOrderTest:Customer ; customerID ; Customer:customerID ; ; true ;
6. Copy the updated ImpEx. 7. Navigate to and log in to the Administration Console. 8. Select Console ImpEx Import . 9. In the Import content area, paste the updated ImpEx. Select Import content.

Modeling via Meta API
Procedure Send POST request https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects with the following body:
 Sample Code
{ "code": "MKTOutboundOrderTest", "items": [ { "code": "Customer", "type": { "code": "Customer" }, "root": false, "attributes": [ { "attributeName": "customerID", "attributeDescriptor": { "qualifier": "customerID", "enclosingType": { "code": "Customer" } }, "unique": true }, { "attributeName": "name", "attributeDescriptor": {
This is   For more    the SAP Help  13

![13_image_0.png](13_image_0.png)

 } } } ] }, { "code": "Order",
 "type": {
 "code": "Order" }, "root": true, "attributes": [ { "attributeName": "code", "attributeDescriptor": { "qualifier": "code", "enclosingType": { "code": "Order" } }, "unique": true }, { "attributeName": "user", "attributeDescriptor": { "qualifier": "user", "enclosingType": { "code": "Order" } }, "returnIntegrationObjectItem": { "code": "Customer" } } ] } ] ![13_image_3.png](13_image_3.png)

## Integration Object Modeling Features

![13_Image_1.Png](13_Image_1.Png)

![13_Image_2.Png](13_Image_2.Png)

Several features extend and simplify the back-end persistence logic. Enhancements to the OData EDMX schema include several custom features, including annotations and support for classication attributes. Annotations that belong to the custom namespace HybrisCommerceOData, such as IsUnique, Alias, and IsAutoCreate are identied with the prex s:. For example, the schema can show annotations on Entity properties such as s:IsUnique="true". See the following topics for further details about specied custom annotations.

The Integration Object modeling features do not affect the OData schema specication.

IsUnique Use the isUnique feature to identify an attribute of an Integration Object as unique in the Backoffice, using ImpEx, or when loading an Integration Object using the API. For any item in the Type system that does not have a unique key, applying isUnique to one or more attributes of that item creates a unique key for identication.

Deep Persistence Deep persistence refers to the ability to simultaneously persist two related items in SAP Commerce Cloud. This topic describes the available deep persistence methods and modications to the EDMX schema in support of deep persistence.

Root Items for Integration Objects Specify a root item for every Integration Object to ensure full outbound sync and Backoffice Integration Object modeling functionality. Classication Attributes This topic describes how the Integration API supports classication attributes for Product and its subtypes, and how they are congured. Map Attributes The Integration API supports primitive, or AtomicType, map attributes for schema generation. The Integration API's EDMX schema represents map values as collections. Because OData does not support map types, the Integration API uses, for example, a String2StringMapType entity that represents a key-value pair.

Runtime Attributes Runtime attributes allow you to extend the capabilities of Integration Objects. Virtual Attributes Virtual attributes allow you to extend the capabilities of the Integration API. Conguring Item Type Match for Integration Objects and Items You can congure the search behavior for all request methods in the Integration API.

## Isunique

Use the isUnique feature to identify an attribute of an Integration Object as unique in the Backoffice, using ImpEx, or when loading an Integration Object using the API. For any item in the Type system that does not have a unique key, applying isUnique to one or more attributes of that item creates a unique key for identication.

This is   For more    the SAP Help  14 isUnique indicates that an XML eld in the generated EDMX schema is required and must be unique to generate the integrationKey later. An example of an item in the Type system that does not have a unique key is StockLevel. When creating a StockLevel Integration Object, enable isUnique for one or more of its attributes to create a unique key for identication.

When using the Integration API, you can then use the key value to query the data.

The annotation is only present in the mentioned elements when IsUnique is true. If either of the following cases is true, IsUnique is set to true.

The Unique column value is set to true, dening an integrationObjectItemAttribute as unique.

The corresponding attribute in the Type system is dened as unique.

This table shows how IsUnique is determined using the two rules.

| Type System IsUnique   | integrationObjectItemAttribute IsUnique   | Generated EDMX Schema            |
|------------------------|-------------------------------------------|----------------------------------|
| null/false             | null/false                                | None                             |
| anything               | true                                      | isUnique="true" Nullable="false" |
| true                   | anything                                  | isUnique="true" Nullable="false" |

Limitations If the Type system has unique = "true", you cannot override it at the Integration Object level by uploading an ImpEx script with an integrationObjectItemAttribute with unique =
"false". In such a case, the debug logger displays a warning that describes the limitation.

## Deep Persistence

Deep persistence refers to the ability to simultaneously persist two related items in SAP Commerce Cloud. This topic describes the available deep persistence methods and modications to the EDMX schema in support of deep persistence.

The deep persistence behavior in the type system uses the partOf attribute to create a dependent relationship and to enforce deep persistence on certain items. For example, an Order Entry cannot exist in the system without an Order. Therefore, when you create an Order Entry item, the system also persists a related Order item, using the partOf attribute to indicate the dependent relationship.

To deep-persist an item that does not exist in the type system, or to deep-persist an existing item for which the partOf attribute is false, you can do one of the following:
For new or existing items that do not have partOf=true in the type system, set the autoCreate ag to true. For example, you might need to create a Unit attribute while persisting the Product object as part of the same Product Integration Object.

Expert users only: For existing items, update items.xml with partOf=true. Restart SAP Commerce, rebuilding and redeploying the extensions.

 Note If partOf=true for an item in the type system, you cannot override this setting.

You can see whether partOf=true for an Integration Object Item in the Backoffice Integration UI Tool. For more information, see the Viewing Details section in Modeling Features.

Differences between partOf and autoCreate The partOf attribute is a type system feature, while autoCreate is a feature of the Integration API module. The partOf attribute, when set to true, species a relationship and also creates a dependency between two items. For example, because the Order Entry item cannot exist in the system without an Order item, deleting an Order item also deletes the related Order Entry items.

The autoCreate annotation, however, species a relationship and enforces deep persistence, but does not create a dependency between two items. For example, if you use autoCreate to set up a deep persistence relationship between Product and Catalog, and later delete a Product item, the API does not delete the associated Catalog item.

For more information about partOf behavior, see Relations.

Deep persistence using autoCreate Set the autoCreate ag to true in the IntegrationObjectItemAttribute denition at the attribute level to deep-persist a nested integration object. You can make this change using the autoCreate checkbox in the Backoffice Integration UI Tool, or by importing an ImpEx script. You can view a sample ImpEx script and EDMX schema in the Deep persistence examples section of this topic.

 Note While you can change abstract types, you cannot mark them as autocreate or use them as the root type of an Integration Object.

For information about modeling Integration Objects in Backoffice, see Modeling Integration Object Metadata.

Supporting EDMX schema modications While the partOf ag in the type system indicates whether the assigned attribute value belongs to the current instance of the specied type, the partOf ag does not appear in the EDMX schema generated for the Integration API. Therefore, the EDMX schema's NavigationProperty contains the engineered annotations, IsPartOf and IsAutoCreate, to indicate whether the related type is deep-persisted. In the EDMX schema:
IsPartOf appears when partOf=true in the type system or in items.xml. IsAutoCreate appears when you set autoCreate to true as described in this topic.

If both the partOf and autoCreate ags are false, the IsPartOf andIsAutoCreate annotations do not appear in the EDMX schema's NavigationProperty.

The following table describes the behavior of the IsPartOf annotation depending on its value and the type of attribute it belongs to.

Deep persistence examples

| attribute                                   | IsPartOf="true"         | IsPartOf="false"              | IsAutoCreate="true"   | IsAutoCreate="false"   |
|---------------------------------------------|-------------------------|-------------------------------|-----------------------|------------------------|
| not created, but existence is veried        | deep insert             | not created, but existence is |                       |                        |
| of the reference item                       | veried                  |                               |                       |                        |
| not created, but existence of all is veried | append with deep insert | not created, but existence of |                       |                        |
| to be the owner of the collection item      | all is veried           |                               |                       |                        |

The following ImpEx script creates a product, MyProduct, with a unit attribute of the type Unit. In the type system, the Unit attribute's partOf value is set to false. The example ImpEx sets the attribute's autoCreate value to true.

INSERT_UPDATE IntegrationObject; code[unique = true]; integrationType(code) ; MyProduct; INBOUND INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code) ; MyProduct ; Product ; Product ; MyProduct ; Unit ; Unit The autoCreate override in the preceding ImpEx adds the IsAutoCreate="true" annotation to the unit navigation property of MyProduct in the EDMX schema, as shown.

| INSERT_UPDATE IntegrationObjectItemAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = true]; attr ; MyProduct:Unit ; code ; Unit:code ; ; ; ; MyProduct:Unit ; name ; Unit:name ; ; ; ; MyProduct:Unit ; unitType ; Unit:unitType ; ; ; ; MyProduct:Product ; code ; Product:code ; ; ; ; MyProduct:Product ; name ; Product:name ; ; ; ; MyProduct:Product ; unit ; Product:unit ; MyProduct:Unit ; ; true   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<?xml version='1.0' encoding='UTF-8'?> <edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" Version="1.0"> <edmx:DataServices m:DataServiceVersion="1.0" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"> <Schema Namespace="HybrisCommerceOData" xmlns="http://schemas.microsoft.com/ado/2008/09/edm"> <EntityType Name="Unit"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="code" Type="Edm.String" s:IsUnique="true" Nullable="false"/> <Property Name="name" Type="Edm.String" IsLanguageDependent="true" Nullable="true"/> <Property Name="unitType" Type="Edm.String" Nullable="false"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" s:Alias="Unit_code"/>
 </EntityType>
 <EntityType Name="Product"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="code" Type="Edm.String" s:IsUnique="true" Nullable="false"/> <Property Name="name" Type="Edm.String" IsLanguageDependent="true" Nullable="true"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" s:Alias="Product_code"/> <NavigationProperty Name="unit" Relationship="HybrisCommerceOData.FK_Product_unit" FromRole="Product" ToRole="Unit" Nullable="true" s </EntityType> <Association Name="FK_Product_unit"> <End Type="HybrisCommerceOData.Product" Multiplicity="0..1" Role="Product"/> <End Type="HybrisCommerceOData.Unit" Multiplicity="0..1" Role="Unit"/> </Association> <EntityContainer Name="Container" m:IsDefaultEntityContainer="true"> <EntitySet Name="Units" EntityType="HybrisCommerceOData.Unit"/> <EntitySet Name="Products" EntityType="HybrisCommerceOData.Product"/> <AssociationSet Name="Product_Units" Association="HybrisCommerceOData.FK_Product_unit"> <End EntitySet="Products" Role="Product"/> <End EntitySet="Units" Role="Unit"/> </AssociationSet> </EntityContainer> </Schema> </edmx:DataServices> </edmx:Edmx>
After overriding the type system, IsAutoCreate is added to unit in the returned EDMX schema. The unit's IsAutoCreate annotation ag is now set to true, as shown.

As this example shows, when persisting a product for which a unit doesn't exist in SAP Commerce Cloud, the system deeply persists the new unit rst and then the product.

{
"@odata.context": "$metadata\#Products/$entity", "code": "my_new_product", "name": "My New Product", "unit" : {
"code": "new_unit_pieces",
 "unitType": "new_unit_pieces", "name": "new_unit_pieces"
}
}
Deep persistence errors Persistence happens in an all-or-nothing manner. If an exception occurs during persistence, the whole Integration Object, including all deeply-inserted dependent objects, rolls back. Additionally, dependent objects do not persist when the partOf attribute is set to false in the items.xml le. Attempting to persist a new item to an attribute with false values for both partOf and autoCreate produces an error. Using the MyProduct example, when the Unit attribute's partOf and autoCreate values are set to false, attempting to persist the Product with a new Unit returns an error, as shown:
{ "error": { "code": "missing_nav_property", "message": { "lang": "en", "value": "Required NavigationProperty for EntityType [Unit] does not exist in the System." }, "innererror": "my_new_product" } }
For more information about errors, see Error Messages.

## Root Items For Integration Objects

Specify a root item for every Integration Object to ensure full outbound sync and Backoffice Integration Object modeling functionality.

The root property is a mandatory Boolean property set on the IntegrationObjectItem type. By default, it is set to false. If you have existing Integration Object denitions for which a root item is not specied, you might not be able to use some of the advanced outbound sync features. Additionally, Integration Objects that contain circular dependencies may not display properly in Backoffice.

 Note You cannot use abstract types as the root type of an Integration Object or mark them as autocreate.

The root item designates the main item in an Integration Object, which means that it's the primary item being exchanged with an external system inbound or outbound. There can only be one root item for each Integration Object. The following example is for an Outbound Customer Integration Object with the root item Customer:
INSERT_UPDATE IntegrationObject; code[unique = true] ; OutboundCustomer INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code); root ; OutboundCustomer ; Customer ; Customer ; true ; OutboundCustomer ; Address ; Address ; false $integrationItem = integrationObjectItem(integrationObject(code), code) $attributeDescriptor = attributeDescriptor(enclosingType(code), qualifier) $returnItem = returnIntegrationObjectItem(integrationObject(code), code) INSERT_UPDATE IntegrationObjectItemAttribute; $integrationItem[unique = true]; attributeName[unique = true]; $attributeDescriptor; $returnItem ; OutboundCustomer:Customer ; uid ; Customer:uid ; ; OutboundCustomer:Customer ; addresses ; Customer:addresses ; OutboundCustomer:A ; OutboundCustomer:Address ; owner ; Address:owner ; OutboundCustomer:C ; OutboundCustomer:Address ; email ; Address:email ; 
In the example above, specifying true for the Integration Object Item Customer designates it as the primary item for processing while Address is a detail about the customer. This means that even if it's only the address that needs to be updated, the change must be processed as part of the Customer payload. In the example above, Customer and Address represent a parentchild relationship. A child Integration Object Item is dened as an Integration Object Item that has a reference to the root Integration Object Item (parent). For example, the address is always associated with an owner such as a Customer, Employee, or Company. For information on how root items affect outbound sync, see Conguring Outbound Sync.

## Classication Attributes

This topic describes how the Integration API supports classication attributes for Product and its subtypes, and how they are congured. The Integration API supports classication attributes in the GET, POST, and DELETE APIs, for the Product type and its subtypes only. While changes to the type system require updates to items.xml les and restarting SAP Commerce, classication attributes allow you to dynamically assign attributes to Products at runtime. An example of a classication attribute value for a Product item is weight. For more information about classication attributes, see Classication.

In Backoffice, you can view classication attributes in the EDMX view in the Integration UI Tool. See Integration Object Modeling via Backoffice for more information. When you view an Integration Object that includes classication attributes using the GET API, the classication attributes do not look different from other attributes. Additionally, localization for Integration Objects with classication attributes behaves the same as localized, non-classication attributes in a GET request. For more information, see Localization for GET requests.

This is   For more    the SAP Help  17 However, there are some differences in how the Integration API supports classication attributes. The Integration API:
only supports conguration of Integration Objects with classication attributes using ImpEx only supports the Product type and its subtypes does not support ltering by classication attribute does not support localization for multivalue and reference type classication attributes Supported Data Types The following table shows which data types Integration API supports for ClassAttributeAssignment items. The API supports only the items listed as supported. For more information about ClassAttributeAssignment items, see Classication System API.

 Note The API does support the range data type. Although the API does not support the unit data type, it returns unit values as primitives. For example, instead of returning 2 cm, the API returns 2.

| Class Attribute Assignment Items String   | Number                                                                  | Date      | Boolean   | Enum   | Reference   |
|-------------------------------------------|-------------------------------------------------------------------------|-----------|-----------|--------|-------------|
| Localized                                 | Supported Supported Supported Not supported Not supported Not supported |           |           |        |             |
| Multivalued                               | Supported Supported Supported Supported                                 | Supported | Supported |        |             |

Products with and without Classication Attributes in Backoffice This section shows how Products with and without classication attributes appear in Backoffice. In the examples in this section, the Product, box1, includes classication attributes, while box2

![17_image_0.png](17_image_0.png)

does not.

In the Backoffice Administration Cockpit, locate box1 in the Product view. In the Attributes tab, the classication attributes depth, height, and width all have values, as shown. When you select box2, however, the Classication Attributes section indicates <No classication attributes available>. In this example, Product box2 is not assigned to the dimensions

![17_image_1.png](17_image_1.png) classifying category, so there is no way to assign depth, height, and width feature values. However, to maintain a consistent behavior between standard (nonclassication) and classication attributes, depth, height, and width return as null, instead of omitting them from the payload.

Products with and without Classication Attributes in a GET Request The following example assumes the classication attributes and ClassAttributeAssignments exist and are associated with the ProductIO Integration Object used to create the box1 and box2 products. In the example, the response returns the dimension category's classication attribute values for box1, height, width, and depth. The box2 product returns null. A successful response returns a 200 status code.

Request URL
https://localhost:9002/odata2webservices/ProductIO/Products Response Body
{ "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/ProductIO/Products('Staged%7CElectronics%7Cbox1')", "uri": "https://localhost:9002/odata2webservices/ProductIO/Products('Staged%7CElectronics%7Cbox1')", "type": "HybrisCommerceOData.Product" },
This is   For more    the SAP Help  18
 "depth": "50.0",
 "height": "25.0", "code": "box1", "width": "70.0", "integrationKey": "Staged|Electronics|box1", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/ProductIO/Products('Staged%7CElectronics%7Cbox1')/catalogVersion" } }
 },
 { "__metadata": { "id": "https://localhost:9002/odata2webservices/ProductIO/Products('Staged%7CElectronics%7Cbox2')", "uri": "https://localhost:9002/odata2webservices/ProductIO/Products('Staged%7CElectronics%7Cbox2')", "type": "HybrisCommerceOData.Product" }, "depth": null, "height": null, "code": "box2", "width": null, "integrationKey": "Staged|Electronics|box2", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/ProductIO/Products('Staged%7CElectronics%7Cbox2')/catalogVersion" } } } ] } }

## Conguring An Integration Object With Classication Attributes

Congure Integration Objects with classication attributes. The following code samples show how to create an example Integration Object that has classication attributes and how to dene a Product type Integration Object and values for the classication attributes. Keep in mind when you congure Integration Objects with classication attributes that there are multiple conguration steps. You must:
1. Create the classication attributes if they do not exist.

2. Create an Integration Object with classication attributes. 3. Create a Product with classication attributes for that Integration Object. 4. Assign the classication classes to the Product and set values for the Product's classication attributes.

For more information on classication attribute and classication category setup, see Classication.

Creating an Integration Object with Classication Attributes When you dene regular type system attributes as part of an Integration Object, you use IntegrationObjectItemAttribute. To dene classication attributes, however, use IntegrationObjectItemClassificationAttribute.

 Note If classication attributes (features) have the same name in two different classication systems, provide a unique name in the IntegrationObjectItemAttribute and IntegrationObjectItemClassificationAttribute.

The following example creates the classication category dimensions with the attributes height, width, and depth.

$SYSTEM = Electronics $VERSION = Staged $SYSTEM_VERSION = $SYSTEM:$VERSION $catalogVersionHeader = catalogVersion(catalog(id), version) $systemVersionHeader = systemVersion(catalog(id), version) INSERT_UPDATE ClassificationSystem; id[unique = true] ; $SYSTEM INSERT_UPDATE ClassificationSystemVersion; catalog(id)[unique = true]; version[unique = true] ; $SYSTEM ; $VERSION INSERT_UPDATE ClassificationClass; code[unique = true]; $catalogVersionHeader[unique = true] ; dimensions ; $SYSTEM_VERSION INSERT_UPDATE ClassificationAttributeUnit; $systemVersionHeader[unique = true]; code[unique = true]; symbol; unitType ; $SYSTEM_VERSION ; centimeters ; cm ; measurement INSERT_UPDATE ClassificationAttribute; code[unique = true]; $systemVersionHeader[unique = true] ; height ; $SYSTEM_VERSION ; width ; $SYSTEM_VERSION ; depth ; $SYSTEM_VERSION $class = classificationClass($catalogVersionHeader, code) $attribute = classificationAttribute($systemVersionHeader, code)
This is   For more    the SAP Help  19 INSERT_UPDATE ClassAttributeAssignment; $class[unique = true] ; $attribute[unique = true]; unit($systemVersionHeader, code); attributeType(code)
 ; $SYSTEM_VERSION:dimensions; $SYSTEM_VERSION:height ; $SYSTEM_VERSION:centimeters ; number ; $SYSTEM_VERSION:dimensions; $SYSTEM_VERSION:width ; $SYSTEM_VERSION:centimeters ; number ; $SYSTEM_VERSION:dimensions; $SYSTEM_VERSION:depth ; $SYSTEM_VERSION:centimeters ; number The following ImpEx denes a Product type Integration Object that includes the height, width, and depth classication attributes associated with dimensions, in addition to normal type system attributes.

$SYSTEM = Electronics $VERSION = Staged $SYSTEM_VERSION = $SYSTEM:$VERSION $IO = ProductIO INSERT_UPDATE IntegrationObject; code[unique = true]; integrationType(code) ; $IO ; INBOUND INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code); root[default = false] ; $IO ; Product ; Product ; true ; $IO ; Catalog ; Catalog ; $IO ; CatalogVersion ; CatalogVersion $item = integrationObjectItem(integrationObject(code), code) $descriptor = attributeDescriptor(enclosingType(code), qualifier) $attributeType = returnIntegrationObjectItem(integrationObject(code), code) INSERT_UPDATE IntegrationObjectItemAttribute; $item[unique = true]; attributeName[unique = true]; $descriptor ; $attributeType; ; $IO:Product ; code ; Product:code ; $IO:Product ; catalogVersion ; Product:catalogVersion; $IO:CatalogVersion ; $IO:CatalogVersion ; version ; CatalogVersion:version ; $IO:CatalogVersion ; catalog ; CatalogVersion:catalog; $IO:Catalog ; $IO:Catalog ; id ; Catalog:id $systemVersionHeader = systemVersion(catalog(id), version) $classificationClassHeader = classificationClass(catalogVersion(catalog(id), version), code) $classificationAttributeHeader = classificationAttribute($systemVersionHeader, code) $classificationAssignment = classAttributeAssignment($classificationClassHeader, $classificationAttributeHeader) INSERT_UPDATE IntegrationObjectItemClassificationAttribute; $item[unique = true]; attributeName[unique = true]; $classificationAssignment ; $IO:Product ; height ; $SYSTEM_VERSION:dimensions:$SYSTEM_VE ; $IO:Product ; depth ; $SYSTEM_VERSION:dimensions:$SYSTEM_VE ; $IO:Product ; width ; $SYSTEM_VERSION:dimensions:$SYSTEM_VE
Viewing an Integration Object with Classication Attributes You can view the imported Integration Object and its attributes in Backoffice or by making a GET request to the Meta API. See Related Information for more information.

Related Information Integration Object Modeling via Backoffice Model Classication Attributes by Meta API
References The Integration API allows you to congure and consume reference classication attributes. References are attributes that refer to types. The following examples show how to congure a reference classication attribute before creating an instance of the reference classication attribute.

Conguring a Reference Classication Attribute As with any classication attribute, you must create the prerequisite elements listed in Conguring an Integration Object with Classication Attributes to congure a reference classication attribute. The following examples show or describe how to congure each of the prerequisites for a reference attribute. Congure Integration Objects and classication attributes Before you can work with reference classication objects, create and congure all of the elements of the Product and the classication elements. As an example, the rst part of the following ImpEx congures two Catalogs, a CatalogVersion, and a Product Integration Object called Ultimate Gear. The second part congures the ClassicationSystem, ClassicationSystemVersion, ClassicationClass, and ClassicationAttribute.

$prod1 = prod1 $catalog = Default $catalog1 = CustomCatalog1 $version = Staged $catalogVersion = $catalog:$version INSERT_UPDATE Catalog; id[unique = true]; name[lang = en]; defaultCatalog ; $catalog ; $catalog ; true ; $catalog1 ; $catalog1 ; true INSERT_UPDATE CatalogVersion; catalog(id)[unique = true]; version[unique = true]; active ; $catalog ; $version ; true INSERT_UPDATE Product; code[unique = true]; catalogVersion(catalog(id), version); name ; $prod1 ; $catalogVersion ; Ultimate Gear $prod1 = prod1 $prod1Key = Default:Staged:$prod1 This is   For more    the SAP Help  20

$classSystem = Sports
$classVersion = Hockey $classSystemVersion = $classSystem:$classVersion $classificationClass = skate $SYSTEM_VERSION_HEADER = systemVersion(catalog(id), version) INSERT_UPDATE ClassificationSystem; id[unique = true] ; $classSystem INSERT_UPDATE ClassificationSystemVersion; catalog(id)[unique = true]; version[unique = true] ; $classSystem ; $classVersion INSERT_UPDATE ClassificationClass; code[unique = true] ; catalogVersion(catalog(id), version)[unique = true]; products(catalogVersion(catalog(id), v
 ; $classificationClass ; $classSystemVersion ; $prod1Key INSERT_UPDATE ClassificationAttribute; code[unique = true]; $SYSTEM_VERSION_HEADER[unique = true] ; relatedCatalog ; $classSystemVersion Congure the ClassAttributeAssignment For the existing ClassicationAttribute, create a ClassAttributeAssignment of the attributeType reference, providing the referenceType that denes the itemType this attribute represents.

Then associate that ClassicationAttributeAssignment to an existing Product.

As an example, the following ImpEx creates a new ClassAttributeAssignment of the type reference for the Catalog itemType.

$classSystem = Sports $classVersion = Hockey $classSystemVersion = $classSystem:$classVersion $classificationClass = skate $CATALOG_VERSION_HEADER = catalogVersion(catalog(id), version) $SYSTEM_VERSION_HEADER = systemVersion(catalog(id), version) $CLASS_HEADER = classificationClass($CATALOG_VERSION_HEADER, code) $SYSTEM_VERSION_HEADER = systemVersion(catalog(id), version) $CLASS_ATTRIBUTE_HEADER = classificationAttribute($SYSTEM_VERSION_HEADER, code) INSERT_UPDATE ClassAttributeAssignment; $CLASS_HEADER[unique = true] ; $CLASS_ATTRIBUTE_HEADER[unique = true]; attributeType(code); refer ; $classSystemVersion:$classificationClass ; $classSystemVersion:relatedCatalog ; reference ; Catal Congure the Integration Object denitions Create the Integration Object denitions for the types.

$ITEM_HEADER = integrationObjectItem(integrationObject(code), code) INSERT_UPDATE IntegrationObject; code[unique = true] ; IO INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code) ; root[default = false] ; IO ; Product ; Product ; true ; IO ; CatalogVersion ; CatalogVersion ; ; IO ; Catalog ; Catalog ; INSERT_UPDATE IntegrationObjectItemAttribute; $ITEM_HEADER[unique = true]; attributeName[unique = true]; attributeDescriptor(enclosingType(code), qua ; IO:Catalog ; id ; Catalog:id ; IO:Product ; code ; Product:code
 ; IO:Product ; catalogVersion ; Product:catalogVersion 
 ; IO:CatalogVersion ; version ; CatalogVersion:version ; IO:CatalogVersion ; catalog ; CatalogVersion:catalog Congure the IntegrationObjectItemClassicationAttribute Create an IntegrationObjectItemClassicationAttribute to represent a nonprimitive attribute for the ClassicationAttributeAssignment. This creates the metadata that allows the use of the reference ClassicationAttribute with the Integration API.

 Note The returnIntegrationObjectItem value is required for reference classication attributes, similar to how the returnIntegrationObjectItem is required when dening a IntegrationObjectItemAttribute to represent a referenced Item or nonprimitive attribute. $CATALOG_VERSION_HEADER = catalogVersion(catalog(id), version) $SYSTEM_VERSION_HEADER = systemVersion(catalog(id), version) $CLASS_HEADER = classificationClass($CATALOG_VERSION_HEADER, code) $CLASS_ATTRIBUTE_HEADER = classificationAttribute($SYSTEM_VERSION_HEADER, code) $CLASS_ASSIGNMENT_HEADER = classAttributeAssignment($CLASS_HEADER, $CLASS_ATTRIBUTE_HEADER) $ITEM_HEADER = integrationObjectItem(integrationObject(code), code) INSERT_UPDATE IntegrationObjectItemClassificationAttribute; $ITEM_HEADER[unique = true]; attributeName[unique = true]; $CLASS_ASSIGNMENT_HEADER ; IO:Product ; relatedCatalog ; Sports:Hockey:skate:Sports:H
Creating an Instance of the Reference Classication Attribute After conguring the required elements of the reference classication attribute, you can create an instance of the attribute that includes values. You can accomplish this in the Backoffice Administration Cockpit by navigating to Products, selecting the product, and clicking the Attributes tab. Add attributes from the selection option and select the appropriate catalog version.

Alternatively, you can add attributes using ImpEx, following the example shown. Use the format reference, primarykey for reference classication attributes. The following example shows this value as reference, 8796093054981, where 8796093054981 represents the primary key of the Catalog to which the ImpEx assigns the relatedCatalog attribute.

This is   For more    the SAP Help  21

$CATALOG_VERSION_HEADER = catalogVersion(catalog(id), version) $SYSTEM_VERSION_HEADER = systemVersion(catalog(id), version) $CLASS_HEADER = classificationClass($CATALOG_VERSION_HEADER, code) $CLASS_ATTRIBUTE_HEADER = classificationAttribute($SYSTEM_VERSION_HEADER, code) $CLASS_ATTR_ASSIGNMENT_HEADER = classificationAttributeAssignment($CLASS_HEADER, $CLASS_ATTRIBUTE_HEADER) $product = product($CATALOG_VERSION_HEADER, code) INSERT_UPDATE ProductFeature; $product[unique = true]; $CLASS_ATTR_ASSIGNMENT_HEADER[unique = true] ; qualifier ; valu ; Default:Staged:prod1 ; Sports:Hockey:skate:Sports:Hockey:relatedCatalog ; Sports/Hockey/skate.relatedCatal Retrieving Reference Classication Attributes After setting up the classication attribute instance, you can view it in a GET payload as shown in this example. Request URL Using the example scenario, make a GET request to the following URL.

https://localhost:9002/odata2webservices/IO/Products?$expand=relatedCatalog Response Body The response payload includes the relatedCatalog reference classication attribute, as shown.

{ "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/IO/Products('Staged%7CDefault%7Cprod1')", "uri": "https://localhost:9002/odata2webservices/IO/Products('Staged%7CDefault%7Cprod1')", "type": "HybrisCommerceOData.Product" }, "code": "prod1", "integrationKey": "Staged|Default|prod1", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/IO/Products('Staged%7CDefault%7Cprod1')/catalogVersion" } }, "classCatalog": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/IO/Products('Staged%7CDefault%7Cprod1')/classCatalog" } }, "relatedCatalog": { "__metadata": { "id": "https://localhost:9002/odata2webservices/IO/Catalogs('CustomCatalog1')", "uri": "https://localhost:9002/odata2webservices/IO/Catalogs('CustomCatalog1')", "type": "HybrisCommerceOData.Catalog"
 },
 "id": "CustomCatalog1", "integrationKey": "CustomCatalog1" } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/IO/Products('Staged%7CDefault%7Cplayer1')", "uri": "https://localhost:9002/odata2webservices/IO/Products('Staged%7CDefault%7Cplayer1')", "type": "HybrisCommerceOData.Product" }, "code": "player1", "integrationKey": "Staged|Default|player1", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/IO/Products('Staged%7CDefault%7Cplayer1')/catalogVersion" } }, "classCatalog": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/IO/Products('Staged%7CDefault%7Cplayer1')/classCatalog" } }, "relatedCatalog": null } ] } }
Related Information References

## Multivalue Enumerations

The Integration API supports conguring and consuming Integration Objects with multivalue classication attributes.

Multivalue enums are useful for dynamically assigning multiple values to a Product's attributes. For example, a multi-color Product can have a color attribute with the values blue, yellow, and green, and you can assign both yellow and green attribute values to the Product.

When the multiValued ag for a ClassAttributeAssignment item is true, it indicates that the classication attribute holds a collection of objects. The objects can be of primitive or reference types. The following samples provide a complete example of how to work with multivalue enums. The steps in the process are as follows.

1. Create classications.

2. Create an Integration Object with classication attributes. 3. Create a Product. 4. Assign classication classes to the Product. 5. Set values for the classication attributes on the Product.

Create Classications To set up the classications, import them using ImpEx, as shown in this example.

$catalogVersionHeader = catalogVersion(catalog(id), version) $systemVersionHeader = systemVersion(catalog(id), version) $classificationClassHeader = classificationClass(catalogVersion(catalog(id), version), code) $classificationAttributeHeader = classificationAttribute($systemVersionHeader, code) $systemVersion = Electronics:Photography $weightAttr = $systemVersion:weight $heightAttr = $systemVersion:height $descAttr = $systemVersion:description $lensClass = $systemVersion:lens $imgStabtAttr = $systemVersion:imageStabilizerAvailable $focalLengthAttr = $systemVersion:focalLength $focalLengthsAttr = $systemVersion:focalLengths $hoodAttr = $systemVersion:hood $tripodClass = $systemVersion:tripod $cameraClass = $systemVersion:camera $qualifierPrefix = Electronics/Photography $product = Default:Staged:photographypackage INSERT_UPDATE ClassificationSystem; id[unique = true]; name[lang = en]
 ; Electronics ; Electronics INSERT_UPDATE ClassificationSystemVersion; catalog(id)[unique = true]; version[unique = true] ; Electronics ; Photography INSERT_UPDATE ClassificationClass; code[unique = true]; name[lang = en]; $catalogVersionHeader[unique = true] ; tripod ; Tripod ; $systemVersion ; camera ; Camera ; $systemVersion ; lens ; Lens ; $systemVersion INSERT_UPDATE ClassificationAttributeUnit; code[unique = true]; symbol; unitType ; $systemVersionHeader[unique = true] ; centimeters ; cm ; measurement ; $systemVersion ; millimeters ; mm ; measurement ; $systemVersion ; meters ; m ; measurement ; $systemVersion ; grams ; g ; measurement ; $systemVersion ; kilograms ; kg ; measurement ; $systemVersion

INSERT_UPDATE ClassificationAttribute; code[unique = true] ; name[lang = en] ; $systemVersionHeader[unique = true] ; weight ; Weight ; $systemVersion ; focalLength ; Focal Length ; $systemVersion ; focalLengths ; Focal Lengths ; $systemVersion ; imageStabilizerAvailable ; Image Stabilizer Available ; $systemVersion ; description ; Description ; $systemVersion ; height ; Height ; $systemVersion ; hood ; Lens Hood ; $systemVersion

|                                                                                                                                                                                                                                                                                                                                                                                                                      | ; imageStabilizerAvailable ; Image Stabilizer Available ; $systemVersion   |               |                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|---------------|------------------|
|                                                                                                                                                                                                                                                                                                                                                                                                                      | ; description                                                              | ; Description | ; $systemVersion |
|                                                                                                                                                                                                                                                                                                                                                                                                                      | ; height                                                                   | ; Height      | ; $systemVersion |
|                                                                                                                                                                                                                                                                                                                                                                                                                      | ; hood                                                                     | ; Lens Hood   | ; $systemVersion |
| INSERT_UPDATE ClassAttributeAssignment; classificationClass($catalogVersionHeader, code)[unique = true]; classificationAttribute($systemVersionHeader  ; $systemVersion:tripod ; $systemVersion:height   ; $systemVersion:camera ; $systemVersion:weight   ; $systemVersion:camera ; $systemVersion:description   ; $systemVersion:lens ; $systemVersion:weight   ; $systemVersion:lens ; $systemVersion:focalLength |                                                                            |               |                  |
| This is custom documentation. For more information, please visit the SAP Help Portal                                                                                                                                                                                                                                                                                                                                 | 23                                                                         |               |                  |

 ; $systemVersion:lens ; $systemVersion:focalLengths 
 ; $systemVersion:lens ; $systemVersion:imageStabilizerAvailable ; $systemVersion:lens ; $systemVersion:description ; $systemVersion:lens ; $systemVersion:hood Create an Integration Object with Classication Attributes The following ImpEx congures an Integration Object with both regular attributes and classication attributes and shows a ClassAttributeAssignment for focalLengths with the multiValued ag set to true. Setting multiValued to true means the focalLengths classication attribute can have many values, such as 50 or 85, stored as a collection. In this case, the stored values are primitives of doubles. In the IntegrationObjectItemClassicationAttribute section, lensFocalLengths is an attribute that references the focalLengths ClassicationAttribute.

INSERT_UPDATE IntegrationObject; code[unique = true] ; integrationType(code) ; InboundProductFeature ; INBOUND INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code) ; InboundProductFeature ; Catalog ; Catalog ; InboundProductFeature ; Product ; Product ; InboundProductFeature ; CatalogVersion ; CatalogVersion

| INSERT_UPDATE IntegrationObjectItemAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = true]; attr  ; InboundProductFeature:Catalog ; id ; Cata  ; InboundProductFeature:Product ; code ; Prod  ; InboundProductFeature:Product ; catalogVersion ; Prod  ; InboundProductFeature:Product ; name ; Prod  ; InboundProductFeature:CatalogVersion ; version ; Cata  ; InboundProductFeature:CatalogVersion ; active ; Cata  ; InboundProductFeature:CatalogVersion ; catalog ; Cata INSERT_UPDATE IntegrationObjectItemClassificationAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique  ; InboundProductFeature:Product ; lensWeight   ; InboundProductFeature:Product ; lensImgStabilizer   ; InboundProductFeature:Product ; lensDescription   ; InboundProductFeature:Product ; lensFocalLengths   ; InboundProductFeature:Product ; lensHood   ; InboundProductFeature:Product ; tripodHeight   ; InboundProductFeature:Product ; cameraWeight   ; InboundProductFeature:Product ; cameraDescription   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Create a Product Import an ImpEx, such as the following, to create an instance of the Product.

INSERT_UPDATE Product; code[unique = true]; name[lang = en] ; $catalogVersionHeader[unique = true] ; universalLensHood ; Universal Lens Hood ; Default:Staged INSERT_UPDATE Product; code[unique = true]; name[lang = en] ; $catalogVersionHeader[unique = true] ; photographypackage ; Photograph Package ; Default:Staged Assign Classication Classes to the Product The following ImpEx assigns the tripod, camera, and lens classication classes to the Product.

INSERT_UPDATE ClassificationClass; code[unique = true]; catalogVersion(catalog(id), version)[unique = true]; products($catalogVersionHeader, code) ; tripod ; $systemVersion ; $product ; camera ; $systemVersion ; $product ; lens ; $systemVersion ; $product Set Values for the Classication Attributes on the Product Import an ImpEx to set values for the Product's classication attributes.

INSERT_UPDATE ProductFeature; product($catalogVersionHeader, code)[unique = true]; classificationAttributeAssignment($classificationClassHeader, $cla ; $product ; $lensClass:$descAttr ; $product ; $lensClass:$weightAttr ; $product ; $lensClass:$imgStabtAttr ; $product ; $lensClass:$focalLengthsAttr ; $product ; $lensClass:$focalLengthsAttr # ; $product ; $lensClass:$hoodAttr ; $product ; $tripodClass:$heightAttr ; $product ; $cameraClass:$weightAttr ; $product ; $cameraClass:$descAttr 

Multivalue Attributes and Schema Generation The Integration API's generated EDMX schema displays classication attributes in the same way as standard attributes. Therefore, the following EDMX schema, generated for the preceding example, shows the lensFocalLengths attribute as a navigation property with a one-to-many association, indicating a collection of doubles for lensFocalLengths.

<EntityType Name="Product"> ... <NavigationProperty Name="lensFocalLengths" Relationship="HybrisCommerceOData.FK_Product_lensFocalLengths" FromRole="Product" ToRole="java.lang.D ... </EntityType> <EntityType Name="Double"> <Key> <PropertyRef Name="value"/> </Key> <Property Name="value" Type="Edm.Double" Nullable="false"/> </EntityType> <Association Name="FK_Product_lensFocalLengths"> <End Type="HybrisCommerceOData.Product" Multiplicity="0..1" Role="Product"/> <End Type="HybrisCommerceOData.Double" Multiplicity="*" Role="java.lang.Double"/> </Association>
ValueLists The Integration API allows you to congure and consume ValueList classication attributes. Enums or enumerations are predened values for attributes. ValueList classication enums enable a multiple attribute eld from which a single attribute is assignable. For example, a ValueList for a single-color Product can offer yellow, blue, and green, but the Product can take only one color attribute. Additionally, ValueLists are dynamic, meaning you can change them without restarting SAP Commerce Cloud. The dynamic nature of ValueLists differs from type system enums, which are created at compile time and require restarting SAP Commerce Cloud to change.

 Note This topic describes the behavior and conguration of ValueLists for integration. The Integration API treats type system enums as reference attributeType ClassAttributeAssignments.

Congure type system enums as described in Classication Attributes.

When you retrieve an IntegrationObjectItemClassicationAttribute or view it in the EDMX schema, it is treated like a primitive standard attribute. For example:
<Property Name="singleEnum" Type="Edm.String" Nullable="true"/>
The following conguration example provides a more descriptive illustration of this treatment.

Conguring a ValueList Classication Attribute As with any type of classication attribute, the prerequisites listed in Classication Attributes are required to set up for the conguration of ValueList classication enums. However, when you create the ClassAttributeAssignment for ValueLists, provide values for an additional attribute on the ItemType. This attribute is called attributeValues and is of the type ClassificationAttributeValueList. To do so, rst create ClassAttributeValues to include in the attributeValues for the ClassAttributeAssignment. The following examples walk through this setup and the conguration of ValueLists. Congure Integration Objects and classication attributes Create and congure the elements of the Product and the classication elements. As an example, the rst part of the following ImpEx congures a Product Integration Object called player1. The second part congures the ClassicationSystem, ClassicationSystemVersion, ClassicationClass, and the ClassicationAttributes medals, created to hold a multivalue enum, and league, created for a ValueList.

INSERT_UPDATE Product; code[unique = true]; catalogVersion(catalog(id), version)[unique = true]
 ; player1 ; Default:Staged $CATALOG_VERSION_HEADER = catalogVersion(catalog(id), version) $SYSTEM_VERSION_HEADER = systemVersion(catalog(id), version) INSERT_UPDATE ClassificationSystem; id[unique = true] ; Sports INSERT_UPDATE ClassificationSystemVersion; catalog(id)[unique = true]; version[unique = true] ; Sports ; Hockey INSERT_UPDATE ClassificationClass; code[unique = true]; $CATALOG_VERSION_HEADER[unique = true]; products($CATALOG_VERSION_HEADER, code) ; skate ; Sports:Hockey ; Default:Staged:player1 INSERT_UPDATE ClassificationAttribute; code[unique = true]; $SYSTEM_VERSION_HEADER[unique = true] ; medals ; Sports:Hockey ; league ; Sports:Hockey Congure the Enumerated ClassicationAttributeValues Provide the ValueList values in the attributeValues attribute on the ClassicationAttributeValueList itemType. The following ImpEx denes the values for the medals and league classication attributes.

$SYSTEM_VERSION_HEADER = systemVersion(catalog(id), version) \# Values for `medals` multivalued dynamic enum $gold = Gold $silver = Silver $bronze = Bronze \# Values for `league` dynamic enum $miniMite = Mini Mite $mite = Mite $squirt = Squirt $peeWee = Peewee This is   For more    the SAP Help  25

| INSERT_UPDATE ClassificationAttributeValue; $SYSTEM_VERSION_HEADER[unique = true]; code[unique = true]  ; Sports:Hockey ; $gold  ; Sports:Hockey ; $silver  ; Sports:Hockey ; $bronze  ; Sports:Hockey ; $miniMite  ; Sports:Hockey ; $mite  ; Sports:Hockey ; $squirt  ; Sports:Hockey ; $peeWee   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Congure the ClassAttributeAssignment For the existing ClassicationAttribute, create a ClassAttributeAssignment, providing the ClassAttributeValues created in the preceding step. Associate the ClassicationAttributeAssignment to an existing Product.

This example ImpEx creates a new ClassAttributeAssignment with the multiValued ag set to true, along with the attributeValues for medals and league.

\# Values for `medals` multivalued dynamic enum $gold = Gold $silver = Silver $bronze = Bronze \# Values for `league` dynamic enum $miniMite = Mini Mite $mite = Mite $squirt = Squirt $peeWee = Peewee $CATALOG_VERSION_HEADER = catalogVersion(catalog(id), version) $SYSTEM_VERSION_HEADER = systemVersion(catalog(id), version) $CLASS_HEADER = classificationClass($CATALOG_VERSION_HEADER, code) $ATTRIBUTE_HEADER = classificationAttribute($SYSTEM_VERSION_HEADER, code) INSERT_UPDATE ClassAttributeAssignment; $CLASS_HEADER[unique = true]; $ATTRIBUTE_HEADER[unique = true]; attributeType(code); multiValued; attributeVa ; Sports:Hockey:skate ; Sports:Hockey:medals ; enum ; true ; $gold:Sport ; Sports:Hockey:skate ; Sports:Hockey:league ; enum ; false ; $mite:Sport Congure the Integration Object denitions Now that a Product, player1, exists for the ClassicationClass and there are ClassAttributeAssignments and ClassAttributeValues for league and medals, add the values for either the league or medals classication attributes to the Product. You can select the attribute values in Backoffice or using the Integration API.

To congure attribute values in the Backoffice Administration Cockpit, navigate to Product, search for and select the product, and click the Attributes tab. Choose variables for each attribute as desired. To congure attribute values using the Integration API, rst provide integration denitions as shown in the following example ImpEx.

\#\# Create IO Definitions for Types INSERT_UPDATE IntegrationObject; code[unique = true] ; DynamicEnumIO INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code) ; root[default = false] ; DynamicEnumIO ; Product ; Product ; true ; DynamicEnumIO ; CatalogVersion ; CatalogVersion ; ; DynamicEnumIO ; Catalog ; Catalog ; INSERT_UPDATE IntegrationObjectItemAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = true]; attr ; DynamicEnumIO:Catalog ; id ; Cata ; DynamicEnumIO:Product ; code ; Prod ; DynamicEnumIO:Product ; catalogVersion ; Prod ; DynamicEnumIO:CatalogVersion ; version ; Cata ; DynamicEnumIO:CatalogVersion ; catalog ; Cata $CATALOG_VERSION_HEADER = catalogVersion(catalog(id), version) $SYSTEM_VERSION_HEADER = systemVersion(catalog(id), version) $CLASS_HEADER = classificationClass($CATALOG_VERSION_HEADER, code) $ATTRIBUTE_HEADER = classificationAttribute($SYSTEM_VERSION_HEADER, code) $CLASS_ASSIGNMENT_HEADER = classAttributeAssignment($CLASS_HEADER, $ATTRIBUTE_HEADER) INSERT_UPDATE IntegrationObjectItemClassificationAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique ; DynamicEnumIO:Product ; medals ; DynamicEnumIO:Product ; league Retrieving ValueList Classication Attributes When you retrieve an Integration Object with enum classication attributes, whether in a GET request or in the Backoffice Integration UI Tool Modeling view, the enum classication attributes appear the same as standard primitive attributes.

Drawing on the example used throughout this topic, the ValueList classication attribute league returns as a primitive string.

<Property Name="league" Nullable="true" Type="Edm.String"/> 
The API returns the multivalue class attribute medals as a NavigationProperty, as it does any standard attribute that represents a collection of a primitive type.

<NavigationProperty Name="medals" Relationship="HybrisCommerceOData.FK_Product_medals" FromRole="Product" ToRole="java.lang.String" Nullable="true"/>

## Classication Attribute Architecture Enhancements

Although there is no extension in the Integration API associated with classication attributes, there are some architectural modications in support of the feature that are helpful to know as

![26_image_0.png](26_image_0.png) you work with the API.

As illustrated in the following diagram, the IntegrationObjectItemAttributeModel has an attributeDescriptor property that is of type AttributeDescriptorModel. To support classication attributes, which belong to the unrelated type ClassificationAttributeModel, the Integration API provides an intermediate type called AbstractIntegrationObjectItemAttributeModel.

## Model Classication Attributes By Meta Api

Create a Product Integration Object with classication attributes using the Meta API. In addition to conguring Integration Objects with classication attributes using ImpEx, you can also use the Meta API. See Conguring an Integration Object with Classication Attributes for more information about conguring using ImpEx. As the following example shows, you can add classication attributes to the payload in the same way as you add regular attributes. The example requires ClassicationSystem and ClassicationSystemVersion to exist. Use the following ImpEx to congure the prerequisite ClassicationSystem and ClassicationSystemVersion.

$SYSTEM = Electronics $VERSION = Demo $CLASSIFICATION_CLASS = 3D $SYSTEM_VERSION = $SYSTEM:$VERSION INSERT_UPDATE ClassificationSystem; id[unique = true] ; $SYSTEM INSERT_UPDATE ClassificationSystemVersion; catalog(id)[unique = true]; version[unique = true] ; $SYSTEM ; $VERSION $catalogVersionHeader = catalogVersion(catalog(id), version) INSERT_UPDATE ClassificationClass; code[unique = true]; $catalogVersionHeader[unique = true] ; $CLASSIFICATION_CLASS ; $SYSTEM_VERSION $systemVersionHeader = systemVersion(catalog(id), version) INSERT_UPDATE ClassificationAttributeUnit; $systemVersionHeader[unique = true]; code[unique = true]; symbol; unitType ; $SYSTEM_VERSION ; centimeters ; cm ; measurement INSERT_UPDATE ClassificationAttribute; code[unique = true]; $systemVersionHeader[unique = true]; name; ; status ; $SYSTEM_VERSION ; relatedProduct ; $SYSTEM_VERSION ; inStock ; $SYSTEM_VERSION ; availableSince ; $SYSTEM_VERSION ; name ; $SYSTEM_VERSION ; height ; $SYSTEM_VERSION ; tallness ; width ; $SYSTEM_VERSION ; depth ; $SYSTEM_VERSION ; brand ; $SYSTEM_VERSION ; model ; $SYSTEM_VERSION $class = classificationClass($catalogVersionHeader, code) $attribute = classificationAttribute($systemVersionHeader, code) INSERT_UPDATE ClassAttributeAssignment; $class[unique = true]; $attribute[unique = true] ; unit($systemVersionHeader, code); attributeType(code) ; $SYSTEM_VERSION:$CLASSIFICATION_CLASS ; $SYSTEM_VERSION:status ; ; ; $SYSTEM_VERSION:$CLASSIFICATION_CLASS ; $SYSTEM_VERSION:relatedProduct ; ; ; $SYSTEM_VERSION:$CLASSIFICATION_CLASS ; $SYSTEM_VERSION:availableSince ; ; ; $SYSTEM_VERSION:$CLASSIFICATION_CLASS ; $SYSTEM_VERSION:inStock ; ; 
This is   For more    the SAP Help  27
 ; $SYSTEM_VERSION:$CLASSIFICATION_CLASS ; $SYSTEM_VERSION:name ; ; 
 ; $SYSTEM_VERSION:$CLASSIFICATION_CLASS ; $SYSTEM_VERSION:height ; $SYSTEM_VERSION:centimeters ; ; $SYSTEM_VERSION:$CLASSIFICATION_CLASS ; $SYSTEM_VERSION:width ; $SYSTEM_VERSION:centimeters ; ; $SYSTEM_VERSION:$CLASSIFICATION_CLASS ; $SYSTEM_VERSION:depth ; $SYSTEM_VERSION:centimeters ; ; $SYSTEM_VERSION:$CLASSIFICATION_CLASS ; $SYSTEM_VERSION:brand ; ; ; $SYSTEM_VERSION:$CLASSIFICATION_CLASS ; $SYSTEM_VERSION:model ; ; 
After creating the ClassicationSystem and ClassicationSystemVersion, run the following POST request with the provided request body. You can then view the created Integration Object with a GET request to see that the classication attributes appear in the same way as nonclassication attributes. Request URL
POST https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects Request Body
{ "code": "3D-Product", "integrationType": { "code": "INBOUND" }, "items": [ { "code": "Product", "root": true, "type": { "code": "Product" }, "integrationObject": { "code": "3D-Product" }, "attributes": [ { "integrationObjectItem": { "code": "Product", "type": { "code": "Product" }, "integrationObject": { "code": "3D-Product" } }, "attributeDescriptor": { "qualifier": "code", "enclosingType": { "code": "Product" } }, "unique": true, "attributeName": "code" },
 {
 "integrationObjectItem": { "code": "Product", "type": { "code": "Product" }, "integrationObject": { "code": "3D-Product" } }, "attributeDescriptor": { "qualifier": "name", "enclosingType": { "code": "Product" } }, "attributeName": "name" },
 { "returnIntegrationObjectItem": { "code": "CatalogVersion", "type": { "code": "CatalogVersion" }, "integrationObject": { "code": "3D-Product" } }, "integrationObjectItem": { "code": "Product", "type": { "code": "Product"
 },
 "integrationObject": { "code": "3D-Product" } }, "attributeDescriptor": { "qualifier": "catalogVersion", "enclosingType": { "code": "Product" }
 },
 "unique": true, "attributeName": "catalogVersion" } ], "classificationAttributes": [ { "classAttributeAssignment": { "classificationAttribute": { "code": "width", "systemVersion": { "catalog": { "id": "Electronics" }, "version": "Demo" } }, "classificationClass": { "catalogVersion": { "catalog": { "id": "Electronics" }, "version": "Demo" }, "code": "3D" } }, "attributeName": "width", "integrationObjectItem": { "code": "Product", "type": { "code": "Product" }, "integrationObject": { "code": "3D-Product" } } }, { "classAttributeAssignment": { "classificationAttribute": { "code": "height", "systemVersion": { "catalog": { "id": "Electronics" }, "version": "Demo" } }, "classificationClass": { "catalogVersion": { "catalog": { "id": "Electronics" }, "version": "Demo" }, "code": "3D" } }, "attributeName": "height", "integrationObjectItem": { "code": "Product", "type": { "code": "Product" }, "integrationObject": { "code": "3D-Product" } } }, { "classAttributeAssignment": {
 "classificationAttribute": {
 "code": "depth", "systemVersion": { "catalog": { "id": "Electronics" }, "version": "Demo" } }, "classificationClass": {
 "catalogVersion": {
 "catalog": { "id": "Electronics" }, "version": "Demo" }, "code": "3D" } }, "attributeName": "depth", "integrationObjectItem": { "code": "Product", "type": { "code": "Product" }, "integrationObject": { "code": "3D-Product" } } } ] }, { "code": "Catalog", "type": { "code": "Catalog" }, "integrationObject": { "code": "3D-Product" }, "attributes": [ { "integrationObjectItem": { "code": "Catalog", "type": { "code": "Catalog" }, "integrationObject": { "code": "3D-Product" } }, "attributeDescriptor": { "qualifier": "id", "enclosingType": { "code": "Catalog" } }, "unique": true, "attributeName": "id" } ] }, { "code": "CatalogVersion", "type": { "code": "CatalogVersion" }, "integrationObject": { "code": "3D-Product" }, "attributes": [ { "returnIntegrationObjectItem": { "code": "Catalog", "type": { "code": "Catalog" }, "integrationObject": { "code": "3D-Product" } }, "integrationObjectItem": {
This is   For more    the SAP Help  30
 "code": "CatalogVersion",
 "type": { "code": "CatalogVersion" }, "integrationObject": { "code": "3D-Product" } }, "attributeDescriptor": { "qualifier": "catalog",
 "enclosingType": {
 "code": "CatalogVersion" } }, "unique": true, "attributeName": "catalog" }, { "integrationObjectItem": { "code": "CatalogVersion", "type": { "code": "CatalogVersion" }, "integrationObject": { "code": "3D-Product" } }, "attributeDescriptor": { "qualifier": "version", "enclosingType": { "code": "CatalogVersion" } }, "unique": true, "attributeName": "version" } ] } ] }

## Map Attributes

The Integration API supports primitive, or AtomicType, map attributes for schema generation. The Integration API's EDMX schema represents map values as collections. Because OData does not support map types, the Integration API uses, for example, a String2StringMapType entity that represents a key-value pair. The API treats the map type as a collection of key-value pairs with a one-to-many relationship. In the following example, the map type is a String2StringMapType.

"additionalProperties":[ { "key": "key 2", "value": "value 2" }, { "key": "key 1", "value": "value 1" } ]
When you dene an Integration Object, dene map attributes in the same way you dene other attributes. For example, the following ImpEx denes an additionalProperties attribute on ConsumedDestination. The type system denes the additionalProperties attribute as a map type property in the attribute descriptor. The property, named String2StringMapType, maps the definition.key of type AtomicType java.lang.String to the value of AtomicType java.lang.String.

INSERT_UPDATE IntegrationObjectItemAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = true]; attr ; OutboundChannelConfig:ConsumedDestination When the schema generates, the map type appears as shown in the following example. The name of the entity, String2StringMapType, corresponds to the name of the map type in the type system. The key of the entity points to the unique, non-nullable property named key. The value property is nullable. The ConsumedDestination entity type has a navigation property to additionalProperties of the type String2StringMapType.

Request example GET https://localhost:9002/odata2webservices/OutboundChannelConfig/$metadata Response example
 <EntityType Name="String2StringMapType"> <Key> <PropertyRef Name="key"/> </Key> <Property Name="key" Type="Edm.String" Nullable="false" s:IsUnique="true"/> <Property Name="value" Type="Edm.String" Nullable="true"/> </EntityType>
This example shows a new one-to-many association between ConsumedDestination and String2StringMapType. Because each String2StringMapType entity type represents a single map entry key and value, multiple map entries are represented as a collection of String2StringMapType entity types.

<Association Name="FK_ConsumedDestination_additionalProperties"> <End Type="HybrisCommerceOData.ConsumedDestination" Multiplicity="0..1" Role="ConsumedDestination"/> <End Type="HybrisCommerceOData.String2StringMapType" Multiplicity="*" Role="String2StringMapType"/> </Association>
For information about map attribute handling in POST and PATCH requests, see the following topics.

Modeling Map Attributes in Backoffice The Integration UI Tool in Backoffice supports the modeling of primitive map types. You can add map types to the selected Integration Object and view selected map types in all tabs of the META (Metadata) view. For example, the Visualizer shows the following ConsumedDestination's additionalProperties attribute as a String2StringMapType.

![31_image_0.png](31_image_0.png)

{ "bigIntegerMap": [ { "Key": "123456_1", "Value": "123456" } ], "bigDecimalMap": [ { "Key": "123456.00_1", "Value": "123456.00" } ], "code": "Test_code", "integrationKey": "TEST_KEY" }

 Note Because localized map types are not "true" map types in the type system, they display differently in the JSON view. The following example shows the display of localized attributes.

{ "code": "Test_code", "catalogVersion": { "version": "Test_version", "catalog": { "id": "Test_id", "integrationKey": "TEST_KEY"
This is   For more    the SAP Help  32

 },
 "integrationKey": "TEST_KEY" }, "localizedAttributes": [ { "language": "en", "remarks": "Test_remarks", "manufacturerTypeDescription": "Test_manufacturerTypeDescription", "description": "Test_description", "segment": "Test_segment",
 "summary": "Test_summary",
 "name": "Test_name", "classificationIndexString": "Test_classificationIndexString" } ], "integrationKey": "TEST_KEY" }
 Note

![32_image_0.png](32_image_0.png)

Map attributes that have keys or values of a complex type are not supported. Unsupported map types appear in strikethrough text and are not selectable from the list. Attempting to select an unsupported map type results in an error message. In the following image, the attribute buyerIDS is not supported.

Related Information

![32_image_1.png](32_image_1.png)

Map Attributes for POST Map Attributes for PATCH Map and Collection Attributes for GET
Runtime Attributes Runtime attributes allow you to extend the capabilities of Integration Objects. You can add runtime attributes to Types from the Type System for Integration Objects. Runtime attributes integration allows you to congure Integration Objects to perform additional tasks at runtime without having to restart and reinitialize SAP Commerce Cloud because runtime attributes are not dened in an items.xml le. When a runtime attribute is added, it's treated like a standard attribute for an Integration Object Item for Integration APIs. For more information, see Congured Types vs Runtime Types.

 Note Runtime attributes are removed and not recreated during a system initialization. If you require runtime attributes to be included when initializing SAP Commerce Cloud, export their denitions into an items.xml le.

You can use runtime attributes for both inbound and outbound scenarios, retrieval and persistence, GET requests, as well as orderby, expand, and ltering query parameters. For implementation scenarios showing how you can take advantage of runtime attributes, see Runtime Attribute Implementation Examples. For information on how to quickly and easily create runtime attributes in Backoffice, see Setting Up Different Types of Attributes in Backoffice. Once a runtime attribute has been created for a Type, it's available to use with Integration Objects via the Backoffice Integration UI Tool.

## Runtime Attribute Meta Api

The Runtime Attribute Meta API provides RESTful endpoints to POST (create), GET (read), PATCH (update), and DELETE runtime attributes.

 Note The following content applies only to patch version 2011.4 and later.

 Note To access the Runtime Attribute Meta API, users must be part of the integrationadmingroup.

The Runtime Attribute Meta API is available via the RuntimeAttributeService service. The API supports the following types for runtime attributes:
Primitive Composed Type Note The Composted Type must already be dened in an extension's items.xml le.

Optional and Non-Optional (Required) Localized Note The localized attribute is determined by whether or not the localized: prex is present in the attributeType..

Unique The following runtime attribute scenarios are not supported:
Runtime Types Maps Relations For examples on how to use the Runtime Attribute Meta API, see Runtime Attribute Meta API Implementation Examples.

## Virtual Attributes

Virtual attributes allow you to extend the capabilities of the Integration API. Virtual attributes are not part of the type sytem for the type that the Integration Object Item references, but they can be added and congured as part of a type and dened in an Integration Object Item. You can create virtual attributes for Integration Object Items and add them at runtime. This means that you can add an additional attribute without needing to update the items.xml le, then restart and re-initialize SAP Commerce Cloud, which saves valuable time.

Virtual attributes offer the following advantages:
Data formatting - For example, dates and numbers. Payload Enrichment - Adding details that may not exist on the Item Type. For example, append a list of coupon codes to a product. Payload Flattening - Customize the payload to reduce the number of nested objects. For example, Customer and Address.

For for information, see Virtual Attribute Implementation Examples.

Virtual Attribute Characteristics Virtual attributes do not support auto-create; cannot be part of an integration key (no option to congure them as unique); and require unique names within Integration Object Items that do not conict with existing standard or classication attribute names.

 Note There are no authorization restrictions for virtual attributes since they rely on the scripting engine.

Virtual attributes support only primitive types. The following are supported:
java.lang.Integer java.lang.Boolean java.lang.Byte java.lang.Double java.lang.Float java.lang.Long java.lang.Short java.lang.String java.lang.Character java.util.Date Conguring Virtual Attributes This is   For more    the SAP Help  34 java.math.BigInteger java.math.BigDecimal Virtual attributes use the following two types: IntegrationObjectItemVirtualAttribute and IntegrationObjectVirtualAttributeDescriptor. retrievalDescriptor is a required eld in IntegrationObjectItemVirtualAttribute.

Virtual Attributes via impEX
The following example creates an Integration Object (VirtualAttributeIO) with an Integration Object Item that includes a virtual attribute named myVirtualAttribute1 associated with it.

1. Load the following ImpEX:
 Sample Code INSERT_UPDATE IntegrationObject; code[unique = true] ; VirtualAttributeIO INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code) ; VirtualAttributeIO ; UnitItem ; Unit INSERT_UPDATE IntegrationObjectItemAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = tru ; VirtualAttributeIO:UnitItem ; code INSERT_UPDATE Script; code[unique = true]; scriptType(code); content ; logLoc ; GROOVY ; hello world from model INSERT_UPDATE IntegrationObjectVirtualAttributeDescriptor; code[unique = true] ; logicLocation ; type(code) ; retrieveVirtualBatman ; model://logLoc ; java.lang.String INSERT_UPDATE IntegrationObjectItemVirtualAttribute; integrationObjectItem(integrationObject(code), code); attributeName[unique = true]; retr ; VirtualAttributeIO:UnitItem ; myVirtualAttribute1 ; retr Note When creating a virtual attribute, the retrieval script is required. The script that backs the retrieval logic can be congured in the following three ways:
ImpEX (as shown in the above example) The Backoffice Administration Cockpit The Meta API
2. Run the following GET request to get the Integration Object metadata: https://localhost:9002/odata2webservices/VirtualAttributeIO/$metadata The following EDMX schema containing the virtual attribute myVirtualAttribute1 is returned (similar to the other attributes):
 Sample Code
<?xml version='1.0' encoding='UTF-8'?> <edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" Version="1.0"> <edmx:DataServices m:DataServiceVersion="1.0" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"> <Schema Namespace="HybrisCommerceOData" xmlns="http://schemas.microsoft.com/ado/2008/09/edm" s:schema-version="1" xmlns:s="http://schemas.s <EntityType Name="UnitItem"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="code" Type="Edm.String" Nullable="false" s:IsUnique="true"/> <Property Name="myVirtualAttribute1" Type="Edm.String" Nullable="true"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" s:Alias="UnitItem_code"/> </EntityType> <EntityContainer Name="Container" m:IsDefaultEntityContainer="true"> <EntitySet Name="UnitItems" EntityType="HybrisCommerceOData.UnitItem"/> </EntityContainer> </Schema> </edmx:DataServices> </edmx:Edmx>
 Note After creating the virtual attribute, when metadata is retrieved, there is no distinction between the virtual attribute and standard attributes.

Virtual Attributes via Meta API The following example creates an Integration Object (VirtualAtributeIO) containing the virtual attribute virtualName associated with it.

1. POST to https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects with the following body:
 Sample Code
{ "code": "VirtualAttributeIO", "integrationType": { "code": "INBOUND" }, "items": [ { "code": "UnitItem", "root": true, This is   For more    the SAP Help  35
 "type": { "code": "Unit" },
 "integrationObject": { "code": "VirtualAttributeIO" }, "attributes": [ { "integrationObjectItem": { "code": "UnitItem", "type": { "code": "Unit"
 },
 "integrationObject": { "code": "VirtualAttributeIO" } }, "attributeDescriptor": { "qualifier": "code", "enclosingType": { "code": "Unit" } }, "unique": true, "attributeName": "code" } ], "virtualAttributes": [ { "integrationObjectItem": { "code": "UnitItem", "integrationObject": { "code": "VirtualAttributeIO" } }, "attributeName": "formattedCode", "retrievalDescriptor": { "code": "formattedUnitCode", "logicLocation": "model://logLoc", "type": { "code": "java.lang.String" } } } ] } ] }
2. Make a GET request to https://localhost:9002/odata2webservices/VirtualAttributeIO/$metadata and obtain the following EDMX:

![35_image_0.png](35_image_0.png)

 Sample Code
<?xml version='1.0' encoding='UTF-8'?> <edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" Version="1.0"> <edmx:DataServices m:DataServiceVersion="1.0" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"> <Schema Namespace="HybrisCommerceOData" xmlns="http://schemas.microsoft.com/ado/2008/09/edm" s:schema-version="1" xmlns:s="http://sch <EntityType Name="UnitItem"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="code" Type="Edm.String" Nullable="false" s:IsUnique="true"/> <Property Name="formattedCode" Type="Edm.String" Nullable="true"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" s:Alias="UnitItem_code"/> </EntityType> <EntityContainer Name="Container" m:IsDefaultEntityContainer="true"> <EntitySet Name="UnitItems" EntityType="HybrisCommerceOData.UnitItem"/> </EntityContainer> </Schema> </edmx:DataServices> </edmx:Edmx>
 Note After creating the virtual attribute, when metadata is retrieved, there is no distinction between the virtual attribute and standard attributes.

Script Service Meta API for Virtual Attributes The Script Service Meta API provides RESTful endpoints to POST (create), GET (read), PATCH (update), and DELETE scripts used for virtual attributes.

 Note To access the Script Service Meta API, users must be part of both the integrationadmingroup and the scriptservicegroup.

Scripts provide the backing logic that controls how the virtual attribute is retrieved. The Script Service Meta API is accessible via the ScriptService service, and it supports virtual attributes in the GET (read) API. For examples on how to send requests using the Script Service Meta API, see Script Service Meta API Implementation Examples.

Creating Virtual Attributes in the Backoffice Integration UI Tool Create virtual attributes in the Backoffice Integration UI Tool.

Procedure 1. Log in to Backoffice.

2. From the dropdown arrow in the upper-left corner of the page, select Integration UI Tool. 3. From the leftside menu, select Integration Object Modeling. 4. Select an Integration Object. 5. Select (Create Virtual Attribute). 6. Do one of the following:
Select an existing virtrual attribute descriptor from the dropdown menu. All elds except for "Virtual Attribute Alias" will be populated. Create a new virtual attribute and ll in the following elds:

| Field                    | Description                                                                                                                                                                                                                                                  |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Virtual Attribute        | The name of the virtual attribute descriptor. More than one virtual attribute can share the same descriptor code, but each virtual attribute must have a unique alias                                                                                        |
| Descriptor Code          | to differentiate it from the others.                                                                                                                                                                                                                         |
| Script Location          | The location of the script used for the virtual attribute. Select a script location from the dropdown menu. There is no type verication to match the virtual attribute type and script's return type. Example script location: model://logLoc.               |
| Virtual Attribute's Type | The virtual attribute's type. If a value isn't specied, it defaults to java.lang.String. Make sure that the type selected matches the return type of the selected script. There is no type verication. See Virtual Attributes for a list of supported types. |
| Virtual Attribute Alias  | Alternative name for a virtual attribute descriptor. An alias is only required when one or more attributes share the same name (either a qualier or a descriptor). Otherwise, providing an alias is optional.                                                |

7. Select Create.

 Note To remove a virtual attribute, deselect it from the Integration Object, then save the change. To delete a virtual attribute descriptor model, go to Backoffice Administration Cockpit System Types , then search for the virtual attribute descriptor and delete it.

## Conguring Item Type Match For Integration Objects And Items

You can congure the search behavior for all request methods in the Integration API.

 Note For information on how to congure item type match restrictions via the Backoffice Integration UI Tool, see Modeling Features.

Using conguration properties, you can change how the Integration API searches for Integration Objects and Integration Object Items.

To set the search behavior for Integration Objects, congure the property integrationservices.flexsearch.itemtypematch. To set the search behavior for Integration Object Items, congure IntegrationObjectItem.itemTypeMatch. If the value for this property is null, the Integration API uses the value for integrationservices.flexsearch.itemtypematch.

The available values for both properties are:
ALL_SUB_AND_SUPER_TYPES - Searches for matching items in all supertypes, subtypes, and the current item type ALL_SUBTYPES - Searches for matching items in all subtypes and the current item type RESTRICT_TO_ITEM_TYPE - Searches for matching items of the same item type Note For ALL_SUB_AND_SUPER_TYPES, SAP Commerce Cloud does not add any search restrictions (personalization rules) to the nal query. Search restrictions (personalization rules) are applied when either ALL_SUBTYPES or RESTRICT_TO_ITEM_TYPE is used.

For abstract or enum types, the Integration API always searches ALL_SUBTYPES. The value of integrationservices.flexsearch.itemtypematch has no effect on abstract or enum type searches.

This is   For more    the SAP Help  37 Additionally, if a referenced IntegrationObjectItemAttribute has a returnIntegrationObjectItem that denes its own itemTypeMatch, the Integration API uses the

![37_image_0.png](37_image_0.png) itemTypeMatch to search for the attribute's value in the following cases:
The referenced attribute is in the request URL. The referenced attribute is in the payload for a persistence request.

The following sections describe how the ex search congurations behave for each request method. Each of the examples uses the sample Integration Object Item hierarchy shown in the following image, where:
TestItem has the attributes a and b.

TestItemType2 inherits attributes a and b and extends TestItem with the attribute foo. TestItemType3 inherits the attributes a, b, and foo, and extends TestItemType 2 with the attribute xxx.

GET
When performing GET requests, the API returns the items specied in the following table depending on the value of the integrationservices.flexsearch.itemtypematch property.

| Example Request                                                                            | Flex Search Property Setting                                    | Returned Items         |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| https://localhost:9002/odata2webservices/ArticialKey/TestItemType2s                        | ALL_SUB_AND_SUPER_TYPES Existing parent, exact item type, child |                        |
| https://localhost:9002/odata2webservices/ArticialKey/TestItemTypes2s RESTRICT_TO_ITEM_TYPE | Exact item type                                                 |                        |
| https://localhost:9002/odata2webservices/ArticialKey/TestItemType2s                        | ALL_SUBTYPES                                                    | Exact item type, child |

## Post And Patch

POST and PATCH requests can nd and update existing items that are supertypes, subtypes, or the exact item type of the item specied in the request. When you create an item, the POST API creates an instance of the exact item type in the request URL, unless you POST to an abstract item type. When you POST to an abstract item type, the API creates an instance of one of the types that extend the abstract item type specied in the request.

## Note

Avoid making IntegrationObjectItemAttributes unique unless they are unique in the type system. If any integrationKey includes attributes that are unique only on the IntegrationObjectItemAttribute, two items could persist with the same integrationKey when using ALL_SUBTYPES or RESTRICT_TO_ITEMTYPE. If you do use IntegrationObjectItemAttributes that are not unique in the type system, you need to set integrationservices.flexsearch.itemtypematch to ALL_SUB_AND_SUPER_TYPES to avoid this situation.

If the value for the integrationservices.flexsearch.itemtypematch property restricts the search from nding an item specied in a POST or PATCH request, the API returns an

![37_image_1.png](37_image_1.png) error. For example, take a case where ComplexTestIntegrationItem extends TestIntegrationItem. If the request includes the same integrationKey attribute of an existing TestIntegrationItem and the ex search property is set to RESTRICT_TO_ITEMTYPE or ALL_SUBTYPES, the response indicates "ambiguous unique keys" as shown in the following error.

{ "error": { "code": "internal_error", "message": { "lang": "en", "value": "An error occurred while attempting to save entries for entityType: ComplexTestIntegrationItem. ambiguous unique keys {code=itemCode} for model ComplexTestIntegrationItemModel (<unsaved>) - found 1 item(s) using the same keys" }, "innererror": "itemCode" } }
The following example creates an IntegrationObjectItem.itemTypeMatch.

Request URL
POST https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects Request Payload
{ "code": "TestIO", "items": [ { "root": false, "code": "Product", "type": { "code": "Product" }, "itemTypeMatch": { "code": "ALL_SUBTYPES" } } ] }
DELETE
The DELETE API uses the integrationKey provided in the request URL to locate the item designated for deletion. The API deletes item if the value for the integrationservices.flexsearch.itemtypematch property does not restrict the search from nding the item. If the search restriction prevents the API from locating the item, the request returns a 404 not found error. Additionally, if you set the ex search property to RESTRICT_TO_ITEM_TYPE or ALL_SUBTYPES and attempt to delete a supertype item, the request returns a 404 error, even if a matching item exists as a supertype of the specied item.

## Odata Services

OData is a protocol for building and using RESTful APIs that the Integration API uses and extends. This section provides an in-depth look at the features and enhancements in the Integration API, including EDMX schema modications and persistence details.

 Note The Integration API only supports batch POST, GET, and DELETE requests for an individual entity. The full OData v2 specication is not supported. To learn more, see The POST API and Persistence and Using the OData2 GET API with Dened Integration Objects.

Integration Objects and OData The Integration API uses and extends the OData protocol for building and using RESTful APIs. This section describes how to use the Integration API within this framework. Conguration Changes to Support Integration The EDMX schema uses and enhances the OData v2 specication to address gaps between the OData v2 schema and the type system. The POST API and Persistence The Integration API includes persistence from a couple of perspectives as well as tools to empower usage. The PATCH API Update the attributes of an existing Integration Object using a PATCH request. Using the OData2 GET API with Dened Integration Objects The odata2webservices extension supports part of the OData2 GET API. If an item is part of SAP Commerce Cloud, it is possible to get OData2 representation through this API.

The OData2 DELETE API
Delete Integration Object Items by integrationKey.

Error Messages Integration API errors can result from missing keys, properties, system errors, or other scenarios. Understanding the error responses can help you identify the source of errors.

## Integration Objects And Odata

The Integration API uses and extends the OData protocol for building and using RESTful APIs. This section describes how to use the Integration API within this framework. An Integration Object describes the structure of a business-level entity. Integration objects are the foundation for an EDMX schema and for the APIs used for Process Integration and Master Data Synchronization of SAP Commerce Cloud. OData is a protocol for building and using RESTful APIs that the Integration API uses and extends. The EDMX schema uses and enhances the OData v2 specication to address gaps between the OData v2 schema and the type system. The Integration API validates the EDMX schema before returning it. SAP Cloud Integration uses the EDMX schema to prepare data sets from other systems for import into SAP Commerce Cloud. The OData v2 schema is still useable in its pure form. Each Integration Object:
This is   For more    the SAP Help  39 almost always has a corresponding OData service with one or more endpoints for each Integration Object Item exposed in the Integration Object denes the structure of the payload that the endpoint accepts or serves has a payload structure that is exportable to EDMX object representations, which you can then use on SAP Cloud Integration for IFlow development can be pushed to an external API through HTTP consists of a compilation of standard SAP Commerce Cloud types and attributes intended to represent the real-world view of the entity ensures transactional process integrity denes the granularity for end-to-end integration monitoring can be dened and extended at runtime The topics in this section describe how to use OData services when working with the Integration API.

Getting the Service Document for an Integration Object To retrieve a list of all the IntegrationObjectItems that belong to a particular IntegrationObject, send a GET request to the service root URI of the specied Integration Object. Creating an EDMX Schema The odata2webservices extension allows you to create an EDMX schema for an imported Integration Object.

The EDMX Key Value For each EDMX entity type, a Key property exists whose value is always integrationKey.

EDMX Schema Collections The Type System denes relationships between item type and attribute type as collections. The EDMX schema uses an Association to represent attributes that are dened as collections.

Related Information OData v2 Documentation Getting the Service Document for an Integration Object To retrieve a list of all the IntegrationObjectItems that belong to a particular IntegrationObject, send a GET request to the service root URI of the specied Integration Object. You can retrieve a list of Integration Object items in XML or JSON format. To get a response in JSON format, include the header ‹Accept:application/json›. For example, the following requests all of the items for the InboundProduct integration object.

The request returns the list of associated Integration Object items in XML, as shown:
https://localhost:9002/odata2webservices/InboundProduct <?xml version='1.0' encoding='utf-8'?> <service xml:base="https://localhost:9002/odata2webservices/InboundProduct/" xmlns="http://www.w3.org/2007/app" xmlns:atom="http://www.w3.org/2005/At <workspace> <atom:title>Default</atom:title>
 <collection href="Categories">
 <atom:title>Categories</atom:title> </collection> <collection href="Warehouses"> <atom:title>Warehouses</atom:title> </collection> <collection href="PriceRows"> <atom:title>PriceRows</atom:title> </collection> <collection href="ProductTaxGroups"> <atom:title>ProductTaxGroups</atom:title> </collection> <collection href="Products"> <atom:title>Products</atom:title> </collection> <collection href="Vendors"> <atom:title>Vendors</atom:title> </collection> <collection href="Catalogs"> <atom:title>Catalogs</atom:title> </collection> <collection href="ProductPriceGroups"> <atom:title>ProductPriceGroups</atom:title> </collection> <collection href="ProductDiscountGroups"> <atom:title>ProductDiscountGroups</atom:title> </collection> <collection href="VariantTypes"> <atom:title>VariantTypes</atom:title> </collection> <collection href="CatalogVersions"> <atom:title>CatalogVersions</atom:title>
This is   For more    the SAP Help  40

 </collection>
 <collection href="Units"> <atom:title>Units</atom:title> </collection> </workspace> </service>
A request for the same items in JSON format returns:
{ "d": { "EntitySets": [ "Categories", "Warehouses", "PriceRows", "ProductTaxGroups", "Products", "Vendors", "Catalogs", "ProductPriceGroups", "ProductDiscountGroups", "VariantTypes", "CatalogVersions", "Units" ] } }
For more information about the OData endpoint this request invokes, see the OData Service Root URI documentation.

## Creating An Edmx Schema

The odata2webservices extension allows you to create an EDMX schema for an imported Integration Object. Using a REST tool or browser, enter the query [https://localhost:9002/odata2webservices/[integrationObject.code]/$metadata, where <integrationObject.code> is InboundProduct. The query creates an EDMX schema and passes it to a validation routine, which is described later in this topic.

If the schema is valid, it returns to the requestor. If the schema is not valid, the API returns an HTTP 400 (Bad Request) response. Additionally, the system writes an error to the logle, as shown in this example.

<?xml version='1.0' encoding='UTF-8'?> <error xmlns="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"> <code/> <message xml:lang="en">The EDMX schema could not be generated. Please make sure that your Integration Object is defined correctly.</message> </error>
If cyclic dependencies between Integration Objects are found when generating a schema, the system generates an error:
<?xml version='1.0' encoding='UTF-8'?>
<error xmlns="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">
 <code>schema_generation_error</code> <message xml:lang="en">The EDMX schema could not be generated. Please make sure that your Integration Object is defined correctly.</message> </error>
This code block provides an example of an EDMX schema:
<?xml version='1.0' encoding='UTF-8'?> <edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" Version="1.0"> <edmx:DataServices m:DataServiceVersion="1.0" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"> <Schema Namespace="HybrisCommerceOData" xmlns="http://schemas.microsoft.com/ado/2008/09/edm"> <EntityType Name="Product"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="name" Type="Edm.String" IsLanguageDependent="true" Nullable="true"/> <Property Name="code" Type="Edm.String" s:IsUnique="true" Nullable="false"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" s:Alias="CatalogVersion_version|Catalog_id|Product_code"/> <NavigationProperty Name="catalogVersion" Relationship="HybrisCommerceOData.FK_Product_catalogVersion" FromRole="Product" ToRole="Cat <NavigationProperty Name="unit" Relationship="HybrisCommerceOData.FK_Product_unit" FromRole="Product" ToRole="Unit" Nullable="true"/> </EntityType> <EntityType Name="Unit"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="code" Type="Edm.String" s:IsUnique="true" Nullable="false"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" s:Alias="Unit_code"/> </EntityType> <EntityType Name="CatalogVersion"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="version" Type="Edm.String" s:IsUnique="true" Nullable="false"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" s:Alias="CatalogVersion_version|Catalog_id"/> <NavigationProperty Name="catalog" Relationship="HybrisCommerceOData.FK_CatalogVersion_catalog" FromRole="CatalogVersion" ToRole="Cat </EntityType> <EntityType Name="Catalog"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="id" Type="Edm.String" s:IsUnique="true" Nullable="false"/>
This is   For more    the SAP Help  41
 <Property Name="integrationKey" Type="Edm.String" Nullable="false" s:Alias="Catalog_id"/>
 </EntityType> <Association Name="FK_Product_catalogVersion"> <End Type="HybrisCommerceOData.Product" Multiplicity="0..1" Role="Product"/> <End Type="HybrisCommerceOData.CatalogVersion" Multiplicity="0..1" Role="CatalogVersion"/> </Association> <Association Name="FK_Product_unit"> <End Type="HybrisCommerceOData.Product" Multiplicity="0..1" Role="Product"/> <End Type="HybrisCommerceOData.Unit" Multiplicity="0..1" Role="Unit"/> </Association> <Association Name="FK_CatalogVersion_catalog"> <End Type="HybrisCommerceOData.CatalogVersion" Multiplicity="0..1" Role="CatalogVersion"/> <End Type="HybrisCommerceOData.Catalog" Multiplicity="0..1" Role="Catalog"/> </Association>
 <EntityContainer Name="Container" m:IsDefaultEntityContainer="true">
 <EntitySet Name="Products" EntityType="HybrisCommerceOData.Product"/> <EntitySet Name="Units" EntityType="HybrisCommerceOData.Unit"/> <EntitySet Name="CatalogVersions" EntityType="HybrisCommerceOData.CatalogVersion"/> <EntitySet Name="Catalogs" EntityType="HybrisCommerceOData.Catalog"/> <AssociationSet Name="Product_CatalogVersions" Association="HybrisCommerceOData.FK_Product_catalogVersion"> <End EntitySet="Products" Role="Product"/> <End EntitySet="CatalogVersions" Role="CatalogVersion"/> </AssociationSet> <AssociationSet Name="Product_Units" Association="HybrisCommerceOData.FK_Product_unit"> <End EntitySet="Products" Role="Product"/> <End EntitySet="Units" Role="Unit"/> </AssociationSet> <AssociationSet Name="CatalogVersion_Catalogs" Association="HybrisCommerceOData.FK_CatalogVersion_catalog"> <End EntitySet="CatalogVersions" Role="CatalogVersion"/> <End EntitySet="Catalogs" Role="Catalog"/> </AssociationSet> </EntityContainer> </Schema> </edmx:DataServices> </edmx:Edmx>
Schema Validation When you get metadata, the returned schema could be invalid because the original ImpEx might not have been set up correctly. However, the Integration API validates the generated schema before returning it to the caller. If the schema validates correctly, for example, when all the related entities are present, and associations are generated correctly, then the schema returns an HTTP 200 status code. However, if the schema is not valid, the system returns the error message HTTP 400 (Bad Request). Error message:
<?xml version='1.0' encoding='UTF-8'?> <error xmlns="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">
<code/> <message xml:lang="en">The EDMX schema could not be generated. Please make sure that your Integration Object is defined correctly.</message>
</error>

## The Edmx Key Value

For each EDMX entity type, a Key property exists whose value is always integrationKey. The integrationKey property is an engineered EDMX property. It acts as a unique identier for each EDMX entity. There are different contexts for using the integrationKey:
1. integrationKey is always in the metadata (EDMX). It is not optional. It is constructed from other EDMX properties.

2. integrationKey is always present and thus not optional in the response to a GET request.

3. integrationKey in the body of a POST request is optional. Using the other properties present in the request body, the Integration API creates the integrationKey value programmatically. The Integration API ignores any existing integrationKey values and creates a new one.

4. If using the pipe ( |) character in the integrationKey as a value and not as a delimiter, then escape the pipe character within the integrationKey.

 Restriction Never change the value of an integrationKey or map the integrationKey property to anything. Its use is strictly internal.

This example shows the PropertyRef key with a value of integrationKey.

<Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="integrationKey" Type="Edm.String" Alias="CatalogVersion_version|Catalog_id|Product_code"/>
The Alias is a concatenated String of unique "segments." A segment is the Entity Type, followed by an underscore, followed by the property's unique name. For example, for a Product entity type with the code property marked as unique, the resulting property and Alias value is:
<Key> <PropertyRef Name="integrationKey"/> </Key> <Property name="integrationKey" Type="Edm.String" Alias="Product_code"/>
An entity type can have multiple properties marked as unique. In such a case, the Alias value contains all of the unique properties. A pipe character delimits the value in alphabetical order. For example, for a Product entity type with the code and id properties marked as unique, the resulting property and Alias value is:
<Key> <PropertyRef Name="integrationKey"/> </Key> <Property name="integrationKey" Type="Edm.String" Alias="Product_code|Product_id"/>

A more realistic scenario includes a couple of different properties marked as unique. Some are "simple" and some are relationships (navigation properties). The associated entity types also have a mix of properties. Take, for example, a product that has:
a String property named code, which is unique a navigation property, CatalogVersion, which is unique within CatalogVersion, a String property named version, which is unique a navigation property, Catalog, which is unique within Catalog, a String property named id, which is unique The resulting property and Alias value is:
<Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="integrationKey" Type="Edm.String" Alias="CatalogVersion_version|Catalog_id|Product_code" />
In the context of this system, the Key value compensates for these limitations:
Navigation properties cannot be part of OData keys, yet in the Type System they can be part of keys. The OData V2 spec does not support complex types.

Further, a semantic key can be easily formulated to look up a value, rather than using a key that is meaningless to an end user.

Nullable Values in Optional Attributes When attributes that are optional in the Type system are part of the integrationKey, the attributes can be nullable="true". When nullable="true" for these attributes, you can send the attribute with a null value in the request body. If you do not send the attribute in the request, the API treats the attribute as nullable="true".

Nullable Values in Reference Attributes The Integration API supports non-reference type key attributes with null values as part of the integrationKey. However, the API does not support null reference type key attributes as part of an integrationKey. This restriction applies even if the attribute is nullable="true". If you do not provide a key reference attribute, the POST API returns a 400 missing_key error. An example of a null reference type key attribute as part of an integrationKey would be a Product integrationKey of CatalogVersion_version|Catalog_id|Product_code. Providing a payload without a catalogVersion or with a null value for catalogVersion, as shown, returns the error.

 { "code": "someProductCode", "catalogVersion": null }

## Edmx Schema Collections

The Type System denes relationships between item type and attribute type as collections. The EDMX schema uses an Association to represent attributes that are dened as collections.

Composed Type Collections Attributes dened as collections in the Type System have one-to-many relationships between the item type and the attribute type. For example, a B2BUnit type has attribute addresses dened as a collection of type Address. This example shows how the Type System uses items.xml to dene a relationship:
<collectiontype code="AddressCollection" elementtype="Address" autocreate="true" generate="false"/><itemtype code="B2BUnit" …>
<attributes>
<attribute autocreate="true" qualifier="addresses" type="AddressCollection"> … </attribute>
</attributes>
</itemtype><itemtype code="Address" …>
<attributes>
…
</attributes>
</itemtype> 
In the EDMX schema denition, an Association represents this relationship. The Association is from one EntityType (B2BUnit) to another EntityType (Address), where you dene the relationship as the multiplicity (0..1-to-*). This example shows how a relationship looks in an EDMX schema:
<edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" Version="1.0"> <edmx:DataServices xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" m:DataServiceVersion="1.0"> <Schema xmlns="http://schemas.microsoft.com/ado/2008/09/edm" Namespace="HybrisCommerceOData"> <EntityType Name="B2BUnit"> <Key> <PropertyRef Name="integrationKey"/> </Key>
 <Property Name="integrationKey" Type="Edm.String" s:Alias="Address_publicKey|B2BUnit_uid"/>
This is   For more    the SAP Help  43

 <Property Name="name" Type="Edm.String" Nullable="true"/>
 <Property Name="uid" Type="Edm.String" Nullable="false" s:IsUnique="true"/> <NavigationProperty Name="addresses" Relationship="HybrisCommerceOData.FK_B2BUnit_Address" FromRole="B2BUnit" ToRole="Address" Nullab </EntityType> <EntityType Name="Address"> <Key> <PropertyRef Name="integrationKey"/> </Key>
 <Property Name="integrationKey" Type="Edm.String" s:Alias="Address_publicKey"/>
 <Property Name="publicKey" Type="Edm.String" Nullable="false" s:IsUnique="true"/>
 </EntityType>
 <Association Name="FK_B2BUnit_addresses"> <End Type="HybrisCommerceOData.B2BUnit" Multiplicity="0..1" Role="B2BUnit"/> <End Type="HybrisCommerceOData.Address" Multiplicity="*" Role="Address"/>
 </Association> <EntityContainer Name="Container" m:IsDefaultEntityContainer="true">
...

 </EntityContainer>
 </Schema> </edmx:DataServices> </edmx:Edmx> 
Primitive Type Collections Because OData v2 does not support an EntityType property with a type of Collection, the system denes collections in the schema as one-to-many associations. To dene an association, the system denes the two ends of the association as EntityType. ( ComplexType and EdmSimpleType are not allowed as part of an association.) For this reason, the system denes an EntityType per primitive and creates a one-to-many association between the type, which has a Collection property, and the primitive type.

 Note Only primitive attributes can be localized and not entities or complex objects.

Example for Collection[java.lang.Integer]
The following example shows an EntityType called OrderEntry with a property called entryGroupNumbers, which is a Collection[java.lang.Integer] (a collection of the primitive type Integer). The system creates an EntityType called Integer. Integer has a single property, called value. The schema for the EntityType:
<EntityType Name="Integer"> <Key> <PropertyRef Name="value"/> </Key> <Property Name="value" Type="Edm.Int32" Nullable="false"/> </EntityType>
The system then creates an association between the OrderEntry and Integer EntityTypes.

<Association Name="FK_OrderEntry_entryGroupNumbers"> <End Type="HybrisCommerceOData.OrderEntry" Multiplicity="0..1" Role="OrderEntry"/> <End Type="HybrisCommerceOData.Integer" Multiplicity="*" Role="Integer"/> </Association>
Additionally, entryGroupNumbers is declared as a navigation property on the OrderEntry EntityType.

<EntityType Name="OrderEntry"> <Key> <PropertyRef Name="integrationKey"/> </Key> ... <NavigationProperty Name="entryGroupNumbers" Relationship="HybrisCommerceOData.FK_OrderEntry_entryGroupNumbers" FromRole="OrderEntry" </EntityType>
To make collections of primitives work, the schema treats the primitive type like any other EntityType. This type is then included in the schema, containing only one property called value. The Entity container then includes the AssociationSet corresponding to the primitive collection.

<EntityContainer Name="Container" m:IsDefaultEntityContainer="true"> <EntitySet Name="Integer" EntityType="HybrisCommerceOData.Integer"/> <EntitySet Name="OrderEntries" EntityType="HybrisCommerceOData.OrderEntries"/> <AssociationSet Name="OrderEntry_Integers" Association="HybrisCommerceOData.FK_OrderEntry_entryGroupNumbers"> <End EntitySet="OrderEntries" Role="OrderEntry"/> <End EntitySet="Integers" Role="Integer"/> </AssociationSet> </EntityContainer>
Example for Collection[java.lang.String] The following example shows an EntityType called Catalog with a NavigationProperty called urlPatterns, which is a Collection[java.lang.String] (a collection of the primitive type String). The schema for the EntityType is as shown:
<EntityType Name="Catalog"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="id" Type="Edm.String" Nullable="false" s:IsUnique="true"/> <Property Name="name" Type="Edm.String" s:IsLanguageDependent="true" Nullable="true"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" s:Alias="Catalog_id"/>
This is   For more    the SAP Help  44
 <NavigationProperty Name="urlPatterns" Relationship="HybrisCommerceOData.FK_Catalog_urlPatterns" FromRole="Catalog" ToRole="java.lang.String" Nullable="true"/> <NavigationProperty Name="localizedAttributes" Relationship="HybrisCommerceOData.FK_Catalog_localizedAttributes" FromRole="Catalog" ToRole="Localized___Catalog" Nullable="true"/> </EntityType>
The system then creates an association between the Catalog and String EntityTypes, as shown:
<Association Name="FK_Catalog_urlPatterns"> <End Type="HybrisCommerceOData.Catalog" Multiplicity="0..1" Role="Catalog"/> <End Type="HybrisCommerceOData.String" Multiplicity="*" Role="java.lang.String"/>
 </Association>
The Entity container includes the AssociationSet corresponding to the primitive collection, as shown:
<EntityContainer Name="Container" m:IsDefaultEntityContainer="true"> <EntitySet Name="Localized___Catalogs" EntityType="HybrisCommerceOData.Localized___Catalog"/> <EntitySet Name="Strings" EntityType="HybrisCommerceOData.String"/> <EntitySet Name="Catalogs" EntityType="HybrisCommerceOData.Catalog"/> <AssociationSet Name="Catalog_Strings" Association="HybrisCommerceOData.FK_Catalog_urlPatterns"> <End EntitySet="Catalogs" Role="Catalog"/> <End EntitySet="Strings" Role="java.lang.String"/> </AssociationSet> <AssociationSet Name="Catalog_Localized___Catalogs" Association="HybrisCommerceOData.FK_Catalog_localizedAttributes"> <End EntitySet="Catalogs" Role="Catalog"/> <End EntitySet="Localized___Catalogs" Role="Localized___Catalog"/> </AssociationSet> </EntityContainer>

## Conguration Changes To Support Integration

The EDMX schema uses and enhances the OData v2 specication to address gaps between the OData v2 schema and the type system. The enhancements to the OData EDMX schema include a number of annotations and extra features that simplify the back-end persistence logic. The annotations do not affect the OData schema specication. The OData v2 schema is still useable in its pure form.

Enhancements to the OData EDMX schema include several custom annotations. Annotations that belong to the custom namespace HybrisCommerceOData, such as IsUnique, Alias, and IsAutoCreate are identied with the prex s:. For example, the schema can show annotations on Entity properties such as s:IsUnique="true". See the following topics for further details about specied custom annotations.

Related Information IsLanguageDependent Nullable

## Islanguagedependent

The IsLanguageDependent annotation indicates whether or not a property is localized. Within the type system, some types support localization. EDMX does not natively accommodate localized content. The EDMX annotation IsLanguageDependent bridges this gap. The annotation maps into the Type System localized types and only appears in the EDMX schema if its value is true. The type system denes a property as localizable by prepending a property's type attribute with localized:. For example, a Catalog item type has a property called description, which has the type localized:java.lang.String. If the description property maps to an integrationObjectItemAttribute, the property has the annotation IsLanguageDependent="true" in the EDMX schema.

## Nullable

Use Nullable to identify elements in the EDMX schema as optional. In the Type system, if an optional element is set to false, it becomes required. EDMX does not have an "optional" concept, but Nullable serves the same purpose. The Nullable feature eliminates the need to look up whether a eld is nullable from SAP Commerce Cloud.

Values for Nullable are true or false. The annotation is present in the elements regardless of its value. The default value of the attribute is dened in the Type system as defaultValuePresent. Nullable is dened in the generated EDMX representation of an IntegrationObjectItemAttribute. The value is generated every time EDMX returns for an IntegrationObjectItemAttribute. The value of Nullable is derived from the rules listed in the following table.

| Unique                                                                               | Optional   | defaultValuePresent?   | Nullable   | Description                                                                                                                                                                |
|--------------------------------------------------------------------------------------|------------|------------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| True                                                                                 | N/A        | N/A                    | False      | If an attribute is unique, Nullable must be false to guarantee that a value is provided.                                                                                   |
| False                                                                                | False      | No                     | False      | If unique is false, then consider the optional ag and whether a default value is present. If the attribute is not optional, provide a value. Therefore, Nullable is false. |
| This is custom documentation. For more information, please visit the SAP Help Portal | 45         |                        |            |                                                                                                                                                                            |

| Unique   | Optional   | defaultValuePresent?   | Nullable   | Description                                                                                                                                                                  |
|----------|------------|------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| False    | N/A        | Yes                    | True       | If unique is false, and a default value is provided, Nullable is true. This is because the default value can always be used regardless of whether the attribute is optional. |

## The Post Api And Persistence

The Integration API includes persistence from a couple of perspectives as well as tools to empower usage. After you import the Integration Object into SAP Commerce Cloud, the environment is ready for you to POST the data through the exposed endpoint. A POST endpoint appears as a RESTful web service and takes an XML-based ATOM format or JSON representation of one or more Integration Objects as a request. Additionally, POST requests in the Integration API provide UPSERT functionality, allowing the creation and update of Integration Objects with a POST request.

A successful request returns the HTTP Status code 201 and an ODataResponse as a JSON payload. A JSON-formatted response looks similar to the following:
{
"error": {
"code": "runtime_error", "message": (
"lang": "en", "value": "There was an error encountered during the processing of the integration object. The detailed cause of this error i
}
}
}
 Note The Integration API does not support polyglot persistence. See Polyglot Persistence for feature details.

How Integration API Persistence Works This topic provides an overview of how Integration API persistence works, and how POST and PATCH request payload arrangements affect both persistence and the request result. Referencing Outer Items This topic provides an overview of how to reference outer items in Integration Object payloads to simplify payload data structures. Item Persistence You can create an item based on a previously dened IntegrationObject denition.

Batch and Bulk Persistence Bulk persistence allows you to update or create multiple Integration Objects with one POST request. Attribute Handling The Integration API handles attributes in POST payloads and metadata as described in this topic. Persistence Hooks Use persistence hooks to execute business logic before or after a request to persist an item. Localization for POST requests Persist Integration Objects in multiple languages and view localizedAttributes as a deferred link.

## How Integration Api Persistence Works

This topic provides an overview of how Integration API persistence works, and how POST and PATCH request payload arrangements affect both persistence and the request result. The sections that follow expand on the following key points:
Elements of the payload are persisted in the order in which they appear in the payload: From top to bottom, and from outer elements to the deepest inner elements. While processing POST requests, Integration API searches for an item in the system that corresponds to the payload element based on the key attributes present in the payload. If the element is detected it's updated with the content from the payload. If it's not found, a new item is created if it's the root element in the payload or a nested element and that element is nested into an attribute that has autoCreate=true in the Integration Object denition, or if that attribute has partOf=true in the type system. Otherwise, an error is returned.

How a Payload is Processed: Persistence Flow Here is an example POST Product payload:
 Sample Code
{ "code": "Men's Beret", "catalogVersion": { "catalog": { "id": "Fall Fashion" }, "version": "2020" }, "unit": { "code": "pieces" This is   For more    the SAP Help  46
 }
}
The above payload is processed in the following way:
1. The Product key is derived from the payload attributes (Product.code + CatalogVersion.version + Catalog.id. If key attributes are not present or empty, the missing_key_attribute error is returned. For error code message descriptions, see Error Messages.

2. The key attributes search for the Product item in the platform. If found, the existing item is used and its attributes are populated with values from the payload. If the item doesn't exist, it is created and then populated.

3. Once the item is resolved its attributes start populating. From the example above, the rst attribute code is assigned the value Men's Beret, then the next attribute catalogVersion is populated, etc.

4. catalogVersion refers to a nested item, so the key attributes search for CatalogVersion.version and Catalog.id. If found, catalogVersion is updated with attribute values in the payload rst. Only then it is assigned to the Product's catalogVersion attribute. If not found and the attribute is autoCreate=true, then it's created automatically. If not found and it's not an autoCreate attribute, the missing_nav_property error is returned. For this example, the CatalogVersion item was found.

5. The CatalogVersion.catalog attribute is populated similarly to how catalogVersion is populated. 6. The CatalogVersion.version attribute is assigned the primitive value 2020. 7. The Product.unit attribute is populated by searching for then creating the Unit item similarly to how the catalogVersion and catalog attributes are populated. 8. Once all of the payload attributes have been applied, all updated and created items are saved in a single transaction. For example, if the unit attribute isn't populated, then changes to Catalog, CatalogVersion, and Product made up to this point are ignored (rolled back).

When a Payload Contains References Betweeen Items It's especially important to understand the persistence ow when a payload contains references between items. Using the example POST Product payload above, when dening the Integration Object for Product, make sure that the Integration Object Item is dened before it's referenced from an Integration Object Item attribute's returnIntegrationObjectItem element. For example:
 Sample Code
{ "code": "pcm", "items": [ { "code": "Catalog", "attributes": [ ... ] }, { "code": "CatalogVersion", "attributes": [ ... { "attributeName": "catalog", "returnIntegrationObjectItem": { "code": "Catalog"
 },
 ... } ] }, { "code": "Unit", "attributes": [ ... ] }, { "code": "Product", "attributes": [ { "attributeName": "code", ... }, { "attributeName": "catalogVersion", "returnIntegrationObjectItem": { "code": "CatalogVersion" }, ... }, { "attributeName": "unit", "returnIntegrationObjectItem": { "code": "Unit" }, ... }
In the example above, each item is dened before it's used in an attribute: Catalog before CatalogVersion.catalog attribute is dened, CatalogVersion before Product.catalogVersion is dened, etc. Unit can be dened before or after Catalog and CatalogVersion because it's not referenced from those types, but it's important to dene Unit before Product.unit attribute is dened.

Cyclical References Sometimes item dependencies in an Integration Object form a graph, not a tree. That is the case when two or more items reference each other. Most often, such references are expressed as relations in the type system's items.xml. For example, Customer (subtype of User) and Address form such cyclical reference through this relation in core-items.xml:
 Sample Code
<relation code="User2Addresses" generate="true" localized="false" autocreate="true"> <sourceElement type="User" cardinality="one" qualifier="owner"> <modifiers read="true" write="false" initial="true" search="true" removable="false" optional="false"/> </sourceElement> <targetElement type="Address" cardinality="many" qualifier="addresses"> <modifiers read="true" write="true" search="true" optional="true" partof="true"/> <custom-properties> <property name="condition.query"> <value>"{original} is null"</value> </property> </custom-properties> </targetElement> </relation>
If you try to expose this relation in an Integration Object: If you rst dene Address then the Address.owner attribute fails because Customer doesn't exist yet. If you rst dene Customer, then the Customer.address attribute fails because Address doesn't exist yet. To solve this problem, the item denitions must be split into two parts: First, an item is dened without the referenced attribute; second, the other item can be dened with attributes referencing it, then the rst item can be dened again with the reference attributes. Below are examples illustrating different approaches to solving this problem for Customer and Address types. Adress - Customer - Address: In this payload, the Address denition is split into two parts.

 Sample Code
{ "code": "InboundCustomer", "items": [ { "code": "Address", "type": { "code": "Address" }, "attributes": [ {
 "attributeName": "publicKey",
 "unique": true, "attributeDescriptor": { "qualifier": "publicKey", "enclosingType": { "code": "Address" } } } ] }, { "code": "Customer", "root": true, "type": { "code": "Customer" }, "attributes": [ { "attributeName": "uid", "attributeDescriptor": { "qualifier": "uid", "enclosingType": { "code": "Customer" } } }, { "attributeName": "name", "attributeDescriptor": { "qualifier": "name", "enclosingType": {
This is   For more    the SAP Help  48
 "code": "Customer"

![48_image_0.png](48_image_0.png)

 } } }, { "attributeName": "addresses", "attributeDescriptor": { "qualifier": "addresses", "enclosingType": { "code": "Customer"
 }
 }, "returnIntegrationObjectItem": { "code": "Address" } } ] }, { "code": "Address", "type": { "code": "Address" }, "attributes": [ { "attributeName": "owner", "unique": true, "attributeDescriptor": { "qualifier": "owner", "enclosingType": { "code": "Address" } }, "returnIntegrationObjectItem": { "code": "Customer" } } ] } ] }
Customer - Address - Customer: In this payload, the Customer denition is split into two parts.

 Sample Code
{ "code": "InboundCustomer", "items": [ { "code": "Customer", "type": { "code": "Customer" }, "attributes": [ { "attributeName": "uid", "attributeDescriptor": { "qualifier": "uid", "enclosingType": { "code": "Customer" } } }, { "attributeName": "name", "attributeDescriptor": { "qualifier": "name", "enclosingType": { "code": "Customer" } } } ] }, { "code": "Address", "type": { "code": "Address" }, "attributes": [

 {
 "attributeName": "publicKey", "unique": true, "attributeDescriptor": { "qualifier": "publicKey", "enclosingType": { "code": "Address" } } },
 {
 "attributeName": "owner", "unique": true, "attributeDescriptor": { "qualifier": "owner", "enclosingType": { "code": "Address" } }, "returnIntegrationObjectItem": { "code": "Customer" } } ] }, { "code": "Customer", "root": true, "type": { "code": "Customer" }, "attributes": [ { "attributeName": "addresses", "attributeDescriptor": { "qualifier": "addresses", "enclosingType": { "code": "Customer" } }, "returnIntegrationObjectItem": { "code": "Address" } } ] } ] }
Address - Customer - Address - Customer: In this payload, all items are rst dened without attributes, then dened with attributes, The Customer and Address denitions are split into two parts.

 Sample Code
{ "code": "InboundCustomer", "items": [ { "code": "Address", "type": { "code": "Address" } }, { "code": "Customer", "type": { "code": "Customer" } }, { "code": "Address", "type": { "code": "Address" }, "attributes": [ { "attributeName": "publicKey", "unique": true, "attributeDescriptor": { "qualifier": "publicKey", "enclosingType": {
 "code": "Address"

![50_image_0.png](50_image_0.png)

 } } }, { "attributeName": "owner", "unique": true, "attributeDescriptor": { "qualifier": "owner", "enclosingType": {
 "code": "Address"
 } }, "returnIntegrationObjectItem": { "code": "Customer" } } ] }, { "code": "Customer", "root": true, "type": { "code": "Customer" }, "attributes": [ { "attributeName": "uid", "attributeDescriptor": { "qualifier": "uid", "enclosingType": { "code": "Customer" } } }, { "attributeName": "name", "attributeDescriptor": { "qualifier": "name", "enclosingType": { "code": "Customer" } } }, { "attributeName": "addresses", "attributeDescriptor": { "qualifier": "addresses", "enclosingType": { "code": "Customer" } }, "returnIntegrationObjectItem": { "code": "Address" } } ] } ] }

## Referencing Outer Items

This topic provides an overview of how to reference outer items in Integration Object payloads to simplify payload data structures. Because outer items are created before their nested items are, it's possible to reference them from the nested items. For example, when you create an Integration Object using the Integration Service Meta API, you create a new Integration Object Item, then reference it from the nested Integration Object Item elements. Here is an example reduced to just the essential elements:
 Sample Code
{ "code": "pcm", "items": [ { "code": "Catalog", "type": { "code": "Catalog" }, "integrationObject": { "code": "pcm" } } ] }
In the above example, the Integration Object Item for Catalog type (/items/integrationObject/code element) references the outer root Integration Object Item (value of/code element). In order to reference any item in the payload, it's sufficient to include only its key attribute in place of the reference. If that item has been created already in the persistence ow, it is resolved. If you get a missing_required_attribute error from the item reference elements, it means that the Integration API is attempting to create the nested referenced item, which means the referenced item has not yet been created and that the payload elements need to be rearranged into an order where the referenced element is created before the reference is reached. For convenience, the referenced items can be implied if an item contains nested items referring back to it. You can omit those references in the payload like this:

![51_image_0.png](51_image_0.png)

![51_image_1.png](51_image_1.png)

The integrationObject attribute is completely removed from the payload. Its value is derived automatically from the persistence context by the attribute type and path in the payload. The type of the integrationObject attribute is IntegrationObject, so while persisting the Integration Object Item for Catalog type, the Integration Object Item detects that the integrationObject attribute is required and is not provided in the payload, so the application searches for Integration Object Items in the path from the current element, that is, the Integration Object Item to the root item in the payload. This feature allows you to simplify payloads signicantly, but you should use caution when the payload contains multiple items of the omitted type. The following is an example based on an Integration Object payload used above:
 Sample Code

![51_image_2.png](51_image_2.png) "code": "pcm", "items": [ }, }, } }, }, } } }, } }, }, } } } ] }, }, }, { // IntegrationObjectItemAttribute "attributeName": "version", "attributeDescriptor": { // AttributeDescriptor "qualifier": "version", "enclosingType": { // ComposedType "code": "CatalogVersion" } }, "integrationObjectItem": { // IntegrationObjectItem "code": "CatalogVersion", "type": { // ComposedType
This is   For more    the SAP Help  52
 "code": "CatalogVersion"

![52_image_0.png](52_image_0.png)

![52_image_1.png](52_image_1.png)

 }, "integrationObject": { // IntegrationObject "code": "pcm" } } }, { // IntegrationObjectItemAttribute "attributeName": "catalog", "attributeDescriptor": { // AttributeDescriptor "qualifier": "catalog", "enclosingType": { // ComposedType "code": "CatalogVersion" }
 },
 "returnIntegrationObjectItem": { // IntegrationObjectItem "code": "Catalog", "integrationObject": { // IntegrationObject "code": "pcm" } }, "unique": true, "integrationObjectItem": { // IntegrationObjectItem "code": "CatalogVersion", "type": { // ComposedType "code": "CatalogVersion" }, "integrationObject": { // IntegrationObject "code": "pcm" } } } ] } ] }
 Note

![52_image_2.png](52_image_2.png)

Comments are not permitted in JSON content but they are used here to show type system types corresponding to the JSON elements and to demonstrate the dependency tree that way.

The following list details which nested elements from the above code sample can be safely omitted or not:
The top-level **IntegrationObject**: The // path is required because it's not a reference to another item in this payload. Only nested elements can reference other items. The **IntegrationObjectItem** for **Catalog** type: The //items[0] path is not a reference to another existing IntegrationObjectItem in this payload. Therefore, it should remain with all of the required attributes in the payload. The same is true for the IntegrationObjectItem for CatalogVersion type, that is, the //items[1] path. The **ComposedType** for the top-level **IntegrationObjectItem**: The //items[*]/type path refers to the type in the type system corresponding to the IntegrationObjectItem. It's a required attribute and therefore cannot be skipped in the //items[*] content. The **integrationObject** attribute in the **IntegrationObjectItem** always refers to top level IntegrationObject: The //items[*]/integrationObject and //items[*]/attributes/integrationObjectItem/integrationObject and //items[1]/attributes[1]/returnIntegrationObjectItem/integrationObject paths. There is only one instance of IntegrationObject created by this payload, which is the root item, which means that it's always on the direct path from the nested item to the root. Therefore, it's safe to imply that attribute value and to omit it in the payload.

The **IntegrationObjectItemAttribute** type: The //items[*]/attributes[*] path is always a top-level IntegrationObjectItemAttribute. There are no other IntegrationObjectItemAttribute items in the payload above those occurrences. Therefore, they are not references and must be present. The **AttributeDescriptor**: The //items[*]/attributes[*]/attributeDescriptor path refers to an attribute descriptor in the type system corresponding to the IntegrationObjectItemAttribute. This path must be present with all of its key attributes because it does not refer to an item already present in the payload at higher levels.

Although it can still be resolved from the persistence context, it's never on the direct path from the nested item to the root, which means that resolution is not deterministic and randomly picks a rst AttributeDescriptor in that context. Since a specic reference is required, the value cannot be implied and therefore must be explicitly present. The **enclosingType** attribute: The //items[*]/attributes[*]/attributeDescriptor/enclosingType path, is a key attribute for the AttributeDescriptor and therefore should present with its own key attribute(s) to enable search of the AttributeDescriptor in the type system. The **integrationObjectItem** attribute: The //items[*]/attributes[*]/integrationObjectItem path is always a reference to the IntegrationObjectItem containing the IntegrationObjectItemAttribute. It's always a reference to the item on the direct path to the root and therefore is safe to omit even though the payload contains multiple IntegrationObjectItem items. The **type** attribute in the referenced IntegrationObjectItem **items**: The //items[*]/attributes[*]/integrationObjectItem/type path, although required, is not a key attribute. References only need key attributes and therefore this path can be omitted.

The **returnIntegrationObjectItem** attribute: The //items[1]/attributes[1]/returnIntegrationObjectItem path is a reference to an IntegrationObjectItem that already exists within the context of the payload. However, this reference is not to an item on the direct path to the root. Therefore, it's better to explicitly specify which item it references. Otherwise, if omitted, it always implies that the IntegrationObjectItem containing the IntegrationObjectItemAttribute references the returnIntegrationObjectItem attribute.

Based on the above list of considerations, you can simplify the payload to this:
 Sample Code
{ "code": "pcm", "items": [ { "code": "Catalog", "type": { "code": "Catalog" }, "attributes": [ { "attributeName": "id", "attributeDescriptor": { "qualifier": "id", "enclosingType": { "code": "Catalog" } } }, { "attributeName": "name", "attributeDescriptor": { "qualifier": "name", "enclosingType": {

![53_image_0.png](53_image_0.png)

 ] }, { ] } ] }
Item Persistence You can create an item based on a previously dened IntegrationObject denition.

Request Body The following headers are included in a single item persistence request.

| Key                                                                                                                                           | Accepted Values                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Content-Type                                                                                                                                  | application/json application/json;charset=utf-8 application/xml application/xml;charset=utf-8                |
| Accept                                                                                                                                        | application/json application/json;charset=utf-8 application/xml application/xml;charset=utf-8                |
| Content-Language                                                                                                                              | A character string that represents the language tag, or locale, in which to save the item's localized data   |
| Accept-Language                                                                                                                               | A character string that represents the language tag, or locale, in which to return the item's localized data |
| Model the body of requests on an existing EDMX schema and include all key elements dened in the IntegrationKey for the IntegrationObjectItem. |                                                                                                              |

To learn more about IntegrationKey, see The EDMX Key Value.

The following POST request to the InboundProduct service creates a Product type.

https://localhost:9002/odata2webservices/InboundProduct/Products The following code is an example of the request body sent in JSON format.

{ "@odata.context": "$metadata\#Products/$entity", "code": "test_article1", "name": "product description 1", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } } 
Response Body The following code example shows the response body that results from the request. Each uri in the response is a link to the items that were created in the request.

{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')", "type": "HybrisCommerceOData.Product" }, "code": "test_article1", "name": "product description 1", "integrationKey": "Staged|Default|test_article1", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')/catalogVersion"
 }
 }, "localizedAttributes": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')/localizedAttributes" } } } } 
When a request is successful, the system responds with HTTP code 201. A 201 response code indicates that the entity Product is created and is persisted in SAP Commerce Cloud. Example POST Request for a Single Item with a Collection of Primitive Types The POST request body for a single item with a collection of primitive types looks like the following, where urlPatterns is a NavigationProperty that refers to a primitive collection.

{ "@odata.context": "$metadata\#Catalogs/$entity", "id": "Default", "urlPatterns": [ { "value": "catalog1" }, { "value": "catalog2" } ] } 
For more information about schema modeling, see EDMX Schema Collections.

## Batch And Bulk Persistence

Bulk persistence allows you to update or create multiple Integration Objects with one POST request.

For batch requests, the POST endpoint for the odata2webservices extension is protocol://url:port/odata2webservices/{integrationObject}/$batch. The endpoint consumes a request with the Content-Type <multipart/mixed>, containing multiple message body parts to persist an Integration Object. Format the request as described in https://www.w3.org/Protocols/rfc1341/7_2_Multipart.html . Each body part within the request must comply with the specication used to persist a single Integration Object. The following header is also required in each request. The boundary specied in the header must match the boundary dened in the payload.

Content-Type multipart/mixed; boundary=batch Each changeset, delimited by --changeset_boundary, has its own Content-Language. Therefore, batch and bulk persistence also supports an Accept-Language header for each changeset element in the POST request body.

A bulk request contains multiple batches, with a limit of 200 batches. For example, the following bulk request contains two batches, each with two changeset sections. The boundary for each batch is batch_boundary, which you dene when you create the request, and the boundary for the changeset is changeset_boundary. If any part of a changeset fails, the API does not persist the entire changeset.

 Note To ensure valid character encoding, add two newlines between the header information and the batch body as shown in the following sample payloads. In the following example, the text <-- NEWLINE --> indicates where a newline is necessary.

 Sample Code POST {{host}}/odata2webservices/InboundCategories/$batch Authorization: Basic {{user}} {{password}} Content-Type: multipart/mixed; boundary=batch --batch Content-Type: multipart/mixed; boundary=changeset --changeset Content-Type: application/http Content-Transfer-Encoding: binary POST Categories HTTP/1.1 Accept: application/json Content-Type: application/json { "@odata.context": "$metadata\#Categories/$entity",
This is   For more    the SAP Help  55

 "code": "category-21",
 "name": "Category 21" } --changeset Content-Type: application/http Content-Transfer-Encoding: binary POST Categories HTTP/1.1 Accept: application/json Content-Type: application/json {
 "@odata.context": "$metadata\#Categories/$entity",
 "code": "category-22", "name": "Category 22" } --changeset-- --batch Content-Type: multipart/mixed; boundary=changeset --changeset Content-Type: application/http Content-Transfer-Encoding: binary POST Categories HTTP/1.1 Accept: application/json Content-Type: application/json { "@odata.context": "$metadata\#Categories/$entity", "code": "category-23", "name": "Category 23" } --changeset Content-Type: application/http Content-Transfer-Encoding: binary POST Categories HTTP/1.1 Accept: application/json Content-Type: application/json { "@odata.context": "$metadata\#Categories/$entity", "code": "category-24", "name": "Category 24" } --changeset-- --batch--
A successful request persists the Integration Object and returns the HTTP status code 202 along with a 201 response for each successfully created body part.

If a request fails because some part of the content is invalid or does not persist, the changeset which contains that request rolls back. The rollback includes the already persisted Integration Objects. Additionally, the rst error code encountered during persistence returns back to the caller. To learn more, see Error Messages. For bulk responses, the changeset has an all-or-nothing strategy, which means that if there is an error while processing a single changeset, only the operations related to that changeset revert. The following example deletes an Integration Object with its inbound channel conguration in a batch. You can replace the values inside }} with real key literal values, for example, {{{}MyIO.

 Sample Code POST {{host}}/odata2webservices/InboundCategories/$batch Authorization: Basic {{user}} {{password}} Content-Type: multipart/mixed; boundary=batch --batch Content-Type: multipart/mixed; boundary=changeset --changeset Content-Type: application/http Content-Transfer-Encoding: binary DELETE InboundChannelConfigurations('_classificationSystemIO') HTTP/1.1 --changeset Content-Type: application/http Content-Transfer-Encoding: binary DELETE IntegrationObjects('_classificationSystemIO') HTTP/1.1 --changeset-- --batch--
The odata2services.batch.limit Property The odata2services.batch.limit sets a threshold on the number of batches in a changeset. The default value of this congurable property is 200. When the congured threshold is reached, the whole request does not process. A response such as the following appears:
HTTP/1.1 400 DataServiceVersion: 1.0 Content-Type: application/json;charset=UTF-8 { "error": { "code": "batch_limit_exceeded", "message": {
This is   For more    the SAP Help  56

## Batch Performance

This topic describes the behavior and capabilities of batch persistence in the Integration API module.

Sequential processing Sequential processing: Changesets within a batch request process sequentially, in the order they are submitted in the batch request. The response returns the batch entities in the same order in which the requests were sent.

Posting multiple Integration Objects Within a request that includes batchparts and changesets, batch is the transaction unit. This means the API attempts to persist an entire batch at once. If a changeset or entry within a batch is invalid, the entire batch with the invalid changeset does not persist and returns a 400 Bad Request response. For example, if you post two batches with two changesets in each batch, and the rst batch is entirely valid while the second batch contains an invalid entry among otherwise valid entries, only the Integration Objects from the rst batch persist successfully. The entire second batch is considered invalid and returns an error.

Batch size considerations In general, batch request performance is improved with fewer, larger batches, up to an upper threshold of batch size. It is recommended that you consider the Integration Object denition and the setup of the environment in determining the optimal batch size. The following table shows the change in performance that resulted from tests of 100,000 categories with minimal payloads.

 Note Be aware of the following considerations.

Categories were only created and no updates were performed in the tests. Using different (bigger) payloads result in different throughput numbers. The results do not reect network latency. The tests and results are provided only as an example of how changes in batch size can potentially affect performance.

| Scenario Conditions                           | Percent change in performance compared to baseline              |          |
|-----------------------------------------------|-----------------------------------------------------------------|----------|
| Baseline 100,000 requests, one item at a time | n/a                                                             |          |
| 1.1                                           | 100 requests x 100 batches x 10 categories (changeset) +5.32%   |          |
| 1.2                                           | 100 requests x 10 batches x 100 categories (changeset) +112.68% |          |
| 1.3                                           | 100 requests x 1 batch x 1000 categories (changeset)            | +127.89% |
| 2.1                                           | 10 requests x 100 batches x 100 categories (changeset) -7.33%   |          |
| 2.2                                           | 10 requests x 10 batches x 1000 categories (changeset) +104.17% |          |
| 2.3                                           | 10 requests x 1 batch x 10000 categories (changeset)            | +1.70%   |

## Attribute Handling

The Integration API handles attributes in POST payloads and metadata as described in this topic. The API handles attributes differently in some cases. Refer to the topics in this section for information about the handling of primitive, multivalue, collection, map, reference, valueList, autocreate, and classication attributes.

Long, BigDecimal, and BigInteger Values as Strings Due to limitations in the OData v2 specication, send Long, BigDecimal, and BigInteger attribute values in POST and PATCH payloads as strings. For example:
{ "code": "actualCode1", "long": "9223372036854775807", "bigInteger": "9223372036854775806", "bigDecimal": "922337203685477.7" }
The resulting EDMX schema displays the type for each of these attributes as Edm.String, as shown:
<edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" Version="1.0"> <edmx:DataServices xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" m:DataServiceVersion="1.0"> <Schema xmlns="http://schemas.microsoft.com/ado/2008/09/edm" xmlns:s="http://schemas.sap.com/commerce" Namespace="HybrisCommerceOData" s:schema-v <EntityType Name="TestIntegrationItem">
This is   For more    the SAP Help  57

 <Key>
 <PropertyRef Name="integrationKey"/> </Key> <Property Name="bigInteger" Type="Edm.String" Nullable="true"/> <Property Name="long" Type="Edm.String" Nullable="true"/> <Property Name="code" Type="Edm.String" Nullable="false" s:IsUnique="true"/> <Property Name="bigDecimal" Type="Edm.String" Nullable="true"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" s:Alias="TestIntegrationItemDetail_code"/> </EntityType> <EntityContainer Name="Container" m:IsDefaultEntityContainer="true">
 <EntitySet Name="TestIntegrationItems" EntityType="HybrisCommerceOData.TestIntegrationItem"/>
 </EntityContainer> </Schema> </edmx:DataServices> </edmx:Edmx>
Classication Attribute Handling The API treats classication attributes like standard collection attributes in most cases. However, there are differences for collection and ValueList classication attributes. The API ignores the autocreate value for ValueList classication attributes.

Autocreate Attributes Persistence behavior for autocreate attributes in the Integration API varies depending on the content of the payload. Circular Reference Attributes In some cases, the Integration API allows you to post payloads without references to circular dependencies. Collection Attributes The handling of collection attributes in the Integration API varies based on whether required or optional attributes are included in the payload. Map Attributes for POST The Integration API's POST API handles required and optional map type attributes similarly to collection attributes. Multivalue Attributes In the Integration API, the persistence behavior for collections of optional and required multivalue primitive attributes depends on whether values are provided in the payload. Primitive Attributes Persistence behavior for required primitive attributes in the Integration API depends on whether attributes are required or optional, and whether a value is included in the payload. Reference Attributes The Integration API's handling of required and optional single value reference attributes and of referenced collection attributes in a POST request varies depending on the values included in the payload. ValueList Attributes In the Integration API, handling of required ValueList attributes varies depending on the POST payload.

## Autocreate Attributes

Persistence behavior for autocreate attributes in the Integration API varies depending on the content of the payload.

The following scenarios assume that the autocreateUnit reference type attribute is not mandatory or multivalue. The currencies reference type attribute is not mandatory but is

multivalue.

| multivalue. POST Scenario   | Value provided in payload   | Example payload                                                                                                                                                                         | Result   | Response code   |
|-----------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------|
| Create a Product with a     | provided                    | Product persists the newUnit                                                                                                                                                            | 201      |                 |
| nonexistent, autocreate,    | attribute                   |                                                                                                                                                                                         |          |                 |
| referenced attribute        | {                           | "code": "test_article12a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "autocreateUnit": { "code": "newUnit", "name": "newUnit", "unitType": "newUnit" } |          |                 |
| }                           |                             |                                                                                                                                                                                         |          |                 |

| 7/6/2024 POST Scenario                      | Value provided in payload                                                                                                                                                                             | Example payload   | Result   | Response code   |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------|-----------------|
| Create a Product with a referenced provided | Persists the new items for the                                                                                                                                                                        | 201               |          |                 |
| autocreate collection                       | collection                                                                                                                                                                                            |                   |          |                 |
| {                                           | "code": "test_article12b", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "currencies": [ { "isocode": "peso", "symbol": "Mex$" }, { "isocode": "rand", "symbol": "R" } ] |                   |          |                 |
| }                                           |                                                                                                                                                                                                       |                   |          |                 |

## Circular Reference Attributes

In some cases, the Integration API allows you to post payloads without references to circular dependencies.

Circular references can occur when an integration item has an attribute of the same type and the same integrationKey as its parent. For example, in the following payload, the code item in the inner context references the code item in the outer context.

{ "code": "0025000501", "entries": [{ "quote": { "code": "0025000501" } }] } 
When performing a POST or PATCH to an Integration API endpoint, you can provide a payload that includes all attributes for a referenced integration item. However, you do not have to dene a key attribute or a required attribute that references another Integration Object itemType if that key or required attribute is already dened in the outer context of the payload. The API can infer the referenced item if the key or required attribute is included in the outer context of the simplied payload.

 Note If there is more than one matching item type for a property without a reference to its parent, then the system populates the property with the closest detected itemType in the upward hierarchy. For example, in a scenario in which Child.parent is a required or key property for the Child entity type, and given the following payload, the API would take the values from the innerParent of type Parent to populate the missing Child.parent reference.

{ "id": "outerParentId", "innerParent": { "id": "innerParentId", "child": { "id": "childId" } } } 
The following examples show complete and simplied payloads. Complete Payload with Circular References Included
 { "code": "ExampleProduct", "integrationType": { "code": "INBOUND" }, "items": [ { "code": "Catalog", "type": { "code": "Catalog" }, "integrationObject": { "code": "ExampleProduct" }, "attributes": [ { "attributeName": "id", "attributeDescriptor": { "qualifier": "id", "enclosingType": { "code": "Catalog" } },
This is   For more    the SAP Help  59
 "integrationObjectItem": {
 "code": "Catalog", "type": { "code": "Catalog" }, "integrationObject": { "code": "ExampleProduct" } } }, { "attributeName": "name", "attributeDescriptor": { "qualifier": "name",
 "enclosingType": { "code": "Catalog" }
 }, "integrationObjectItem": { "code": "Catalog", "type": { "code": "Catalog" }, "integrationObject": { "code": "ExampleProduct" } } } ] }, { "code": "CatalogVersion", "type": { "code": "CatalogVersion" }, "integrationObject": { "code": "ExampleProduct" }, "attributes": [ { "attributeName": "version", "attributeDescriptor": { "qualifier": "version", "enclosingType": { "code": "CatalogVersion" } }, "integrationObjectItem": { "code": "CatalogVersion", "type": { "code": "CatalogVersion" }, "integrationObject": { "code": "ExampleProduct" } } }, { "attributeName": "catalog", "attributeDescriptor": { "qualifier": "catalog", "enclosingType": { "code": "CatalogVersion" } }, "returnIntegrationObjectItem": { "code": "Catalog", "integrationObject": { "code": "ExampleProduct" } }, "unique": true, "integrationObjectItem": { "code": "CatalogVersion", "type": { "code": "CatalogVersion" }, "integrationObject": { "code": "ExampleProduct" } } } ] }, { "code": "Unit", "type": { "code": "Unit" }, "integrationObject": { "code": "ExampleProduct" }, "attributes": [ { "attributeName": "code", "attributeDescriptor": { "qualifier": "code", "enclosingType": { "code": "Unit" } }, "integrationObjectItem": { "code": "Unit", "type": { "code": "Unit" }, "integrationObject": { "code": "ExampleProduct" } } }, { "attributeName": "unitType", "attributeDescriptor": { "qualifier": "unitType", "enclosingType": { "code": "Unit" } }, "integrationObjectItem": { "code": "Unit", "type": { "code": "Unit" },
This is   For more    the SAP Help  60
 "integrationObject": { "code": "ExampleProduct" }
 } } ] }, { "code": "Product", "type": { "code": "Product" }, "integrationObject": { "code": "ExampleProduct" }, "root": true,
 "attributes": [
 { "attributeName": "code", "attributeDescriptor": { "qualifier": "code", "enclosingType": { "code": "Product" } }, "integrationObjectItem": { "code": "Product", "type": { "code": "Product"}, "integrationObject": { "code": "ExampleProduct" } } }, { "attributeName": "catalogVersion", "attributeDescriptor": { "qualifier": "catalogVersion", "enclosingType": { "code": "Product" } }, "returnIntegrationObjectItem": { "code": "CatalogVersion", "integrationObject": { "code": "ExampleProduct"} }, "integrationObjectItem": { "code": "Product", "integrationObject": { "code": "ExampleProduct" } } }, { "attributeName": "name", "attributeDescriptor": { "qualifier": "name", "enclosingType": { "code": "Product" } }, "integrationObjectItem": { "code": "Product", "integrationObject": { "code": "ExampleProduct" } } }, { "attributeName": "description", "attributeDescriptor": { "qualifier": "description", "enclosingType": { "code": "Product" } }, "integrationObjectItem": { "code": "Product", "integrationObject": { "code": "ExampleProduct" } } }, { "attributeName": "unit", "attributeDescriptor": { "qualifier": "unit", "enclosingType": { "code": "Product" } }, "integrationObjectItem": { "code": "Product", "integrationObject": { "code": "ExampleProduct" } }, "returnIntegrationObjectItem": { "code": "Unit", "integrationObject": { "code": "ExampleProduct"} } }, { "attributeName": "order", "attributeDescriptor": { "qualifier": "order", "enclosingType": { "code": "Product" } }, "integrationObjectItem": {
This is   For more    the SAP Help  61
 "code": "Product",
 "integrationObject": { "code": "ExampleProduct" } } } ] } ] }
Simplied Payload without Circular References
 { "code": "ExampleProduct", "integrationType": { "code": "INBOUND" }, "items": [ { "code": "Catalog", "type": { "code": "Catalog" }, "integrationObject": { "code": "ExampleProduct" }, "attributes": [ { "attributeName": "id", "attributeDescriptor": { "qualifier": "id", "enclosingType": { "code": "Catalog" } } }, { "attributeName": "name", "attributeDescriptor": { "qualifier": "name", "enclosingType": { "code": "Catalog" } } } ] }, { "code": "CatalogVersion", "type": { "code": "CatalogVersion" }, "integrationObject": { "code": "ExampleProduct" }, "attributes": [ { "attributeName": "version", "attributeDescriptor": { "qualifier": "version", "enclosingType": { "code": "CatalogVersion" } }
 },
 { "attributeName": "catalog", "attributeDescriptor": { "qualifier": "catalog", "enclosingType": { "code": "CatalogVersion" } }, "returnIntegrationObjectItem": { "code": "Catalog", "integrationObject": { "code": "ExampleProduct" } }, "unique": true } ] }, { "code": "Unit", "type": { "code": "Unit" }, "integrationObject": { "code": "ExampleProduct" }, "attributes": [ { "attributeName": "code", "attributeDescriptor": { "qualifier": "code", "enclosingType": { "code": "Unit" } } }, { "attributeName": "unitType", "attributeDescriptor": { "qualifier": "unitType", "enclosingType": { "code": "Unit" }
This is   For more    the SAP Help  62

 }
 } ] }, { "code": "Product", "type": { "code": "Product" }, "integrationObject": { "code": "ExampleProduct" }, "root": true, "attributes": [
 {
 "attributeName": "code", "attributeDescriptor": { "qualifier": "code", "enclosingType": { "code": "Product" } } }, { "attributeName": "catalogVersion", "attributeDescriptor": { "qualifier": "catalogVersion", "enclosingType": { "code": "Product" } }, "returnIntegrationObjectItem": { "code": "CatalogVersion", "integrationObject": { "code": "ExampleProduct"} } }, { "attributeName": "name", "attributeDescriptor": { "qualifier": "name", "enclosingType": { "code": "Product" } } }, { "attributeName": "description", "attributeDescriptor": { "qualifier": "description", "enclosingType": { "code": "Product" } } }, { "attributeName": "unit", "attributeDescriptor": { "qualifier": "unit", "enclosingType": { "code": "Product" } }, "returnIntegrationObjectItem": { "code": "Unit", "integrationObject": { "code": "ExampleProduct"} } }, { "attributeName": "order", "attributeDescriptor": { "qualifier": "order", "enclosingType": { "code": "Product" } } } ] } ] }

## Collection Attributes

The handling of collection attributes in the Integration API varies based on whether required or optional attributes are included in the payload. In general, for required collections of any type, the API:
Accepts a new item with an empty collection as a value Fails when sending a new item with null, or without a required attribute When updating an existing item with a required collection, the API:
Appends the sent values to the existing values Accepts null and empty values without affecting existing values Merges duplicate values The following tables provide examples of how the API handles required and optional reference collection attributes and valueList attributes.

Required Reference Collection Attributes

| The example scenarios assume that the multivalue countries attribute is mandatory, not autocreate, not nullable. POST Scenario Value provided in payload Example payload   | Result                                                                                                                                                                                                                                                                       | Response code                                                                                                          |     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|-----|
| Create a Product with a null                                                                                                                                               | null                                                                                                                                                                                                                                                                         | Returns a missing navigation                                                                                           | 400 |
| value for a required referenced                                                                                                                                            | property error                                                                                                                                                                                                                                                               |                                                                                                                        |     |
| collection                                                                                                                                                                 | {                                                                                                                                                                                                                                                                            | "code": "test_article9a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "countries": null |     |
| }                                                                                                                                                                          |                                                                                                                                                                                                                                                                              |                                                                                                                        |     |
| Create a Product without a value                                                                                                                                           | not provided                                                                                                                                                                                                                                                                 | Returns a missing navigation                                                                                           | 400 |
| for a required referenced                                                                                                                                                  | property error                                                                                                                                                                                                                                                               |                                                                                                                        |     |
| collection                                                                                                                                                                 | {                                                                                                                                                                                                                                                                            | "code": "test_article9b", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }                    |     |
| }                                                                                                                                                                          |                                                                                                                                                                                                                                                                              |                                                                                                                        |     |
| Create a Product using an empty                                                                                                                                            | empty                                                                                                                                                                                                                                                                        | Persists an empty collection                                                                                           | 201 |
| collection value for a required attribute                                                                                                                                  | {                                                                                                                                                                                                                                                                            | "code": "test_article9c", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "countries": []   |     |
| }                                                                                                                                                                          |                                                                                                                                                                                                                                                                              |                                                                                                                        |     |
| Create a Product using a value that contains a nonexistent item for a required reference to a nonautocreate collection                                                                                                                                                                            | provided with a nonexistent item                                                                                                                                                                                                                                             | Returns a missing navigation                                                                                           | 400 |
| property error                                                                                                                                                             |                                                                                                                                                                                                                                                                              |                                                                                                                        |     |
| {                                                                                                                                                                          | "code": "test_article9d", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "countries": [ {"isocode": "bldr"}, {"isocode": "fakeCountry"}{ "code": "test_article13a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, ] |                                                                                                                        |     |
| }                                                                                                                                                                          |                                                                                                                                                                                                                                                                              |                                                                                                                        |     |
| Create a Product using a value that includes a collection of existing items for a required referenced collection                                                           | provided                                                                                                                                                                                                                                                                     | Persists all collection items                                                                                          | 201 |
| {                                                                                                                                                                          | "code": "test_article9e", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "countries": [ {"isocode": "bldr"}, {"isocode": "dnvr"} ]                                                                                                               |                                                                                                                        |     |
| }                                                                                                                                                                          |                                                                                                                                                                                                                                                                              |                                                                                                                        |     |
| Update a Product using a null                                                                                                                                              | null                                                                                                                                                                                                                                                                         | Keeps existing values because                                                                                          | 201 |
| value for a required referenced                                                                                                                                            | the request provides no new                                                                                                                                                                                                                                                  |                                                                                                                        |     |
| collection                                                                                                                                                                 | values                                                                                                                                                                                                                                                                       |                                                                                                                        |     |
| {                                                                                                                                                                          | "code": "test_article9e", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "countries": null                                                                                                                                                       |                                                                                                                        |     |
| }                                                                                                                                                                          |                                                                                                                                                                                                                                                                              |                                                                                                                        |     |

This is   For more    the SAP Help  64

| 7/6/2024 POST Scenario                   | Value provided in payload                                                                                            | Example payload                                                                                                                            | Result   | Response code   |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------|
| Update a Product without                 | not provided                                                                                                         | Keeps existing values because                                                                                                              | 201      |                 |
| providing a value for a required         | the request provides no new                                                                                          |                                                                                                                                            |          |                 |
| referenced collection                    | values                                                                                                               |                                                                                                                                            |          |                 |
| {                                        | "code": "test_article9e", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }                  |                                                                                                                                            |          |                 |
| }                                        |                                                                                                                      |                                                                                                                                            |          |                 |
| Update a Product using an empty          | provided as an empty collection                                                                                      | Keeps existing values because                                                                                                              | 201      |                 |
| collection for a required                | the request provides no new                                                                                          |                                                                                                                                            |          |                 |
| referenced collection                    | values                                                                                                               |                                                                                                                                            |          |                 |
| {                                        | "code": "test_article9e", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "countries": [] |                                                                                                                                            |          |                 |
| }                                        |                                                                                                                      |                                                                                                                                            |          |                 |
| Update a Product using another           | provided                                                                                                             | Item persists along with the                                                                                                               | 201      |                 |
| existing item as the value for a         | existing attribute values                                                                                            |                                                                                                                                            |          |                 |
| required referenced collection           | {                                                                                                                    | "code": "test_article9e", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "countries": [ {"isocode": "lngmt"} ] |          |                 |
| }                                        |                                                                                                                      |                                                                                                                                            |          |                 |
| Optional Reference Collection Attributes |                                                                                                                      |                                                                                                                                            |          |                 |

The following examples illustrate the POST request behavior for Integration Objects with optional reference collection attributes. For the examples, the autocreateUnit reference type attribute is not mandatory or multivalue. The currencies reference type attribute is not mandatory but is multivalue. The optionalCountries attribute is a referenced attribute type.

| attribute is not mandatory or multivalue. The currencies reference type attribute is not mandatory but is multivalue. The optionalCountries attribute is a referenced attribute type. POST Scenario Value provided in payload Example payload Result Response code Create a Product with a null null Creates the Product because the 201 value for an optional referenced referenced collection is not collection required { "code": "test_article13a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "optionalCountries": null } Create a product without not provided Creates the Product because the 201 providing a value for an optional referenced collection is not referenced collection required { "code": "test_article13b", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } } Create a Product with an empty provided with empty collection Creates the Product and persists 201 collection for an optional the attribute with an empty referenced collection collection { "code": "test_article13c", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "optionalCountries": [] }   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| 7/6/2024 POST Scenario                   | Value provided in payload                                                                                                                                                      | Example payload                                                                                                                                     | Result   | Response code   |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------|
| Create a Product using a nonexistent item in the values for an optional referenced, nonautocreate collection                                          | provided with a nonexistent item                                                                                                                                               | The API returns a missing navigation property error because it cannot persist a nonexistent collection item                                         |          |                 |
| {                                        | "code": "test_article13d", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "optionalCountries": [ {"isocode": "bldr"}, {"isocode": "fakeCountry"} ] |                                                                                                                                                     |          |                 |
| }                                        | 400                                                                                                                                                                            |                                                                                                                                                     |          |                 |
| Create Product using a collection        | provided with collection of                                                                                                                                                    | Persists the Product with the                                                                                                                       | 201      |                 |
| of existing items as the values for      | existing items                                                                                                                                                                 | attribute values                                                                                                                                    |          |                 |
| an optional referenced collection        | {                                                                                                                                                                              | "code": "test_article13e", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "optionalCountries": [ {"isocode": "lngmt"} ] |          |                 |
| }                                        |                                                                                                                                                                                |                                                                                                                                                     |          |                 |
| Required ValueList Collection Attributes |                                                                                                                                                                                |                                                                                                                                                     |          |                 |

| The following scenarios assume the paymentMethod valueList attribute is mandatory and multivalue. Existing values for the valueList include newArrival and sale. POST Scenario Value provided in payload Example payload Result Response code Create a Product with a null null Cannot persist an Integration Object without providing a value value for the required ValueList collection for a required valueList. Returns a missing navigation property error. { "code": "test_article11a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "tags": null } 400 Create Product without providing not provided Returns a missing navigation 400 values for a required ValueList property error collection { "code": "test_article11b", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } } Create a Product with an empty provided as an empty collection Persists valueList with empty 201 collection for a required ValueList collection collection { "code": "test_article11c", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "tags": [] } Create a Product using existing provided with existing valueList Persists valueList with existing 201 values for a required valueList values values Collection { "code": "test_article11d", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "tags": [ {"value": "newArrival"}, {"value": "sale"} ] }   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| 7/6/2024 POST Scenario                     | Value provided in payload                                                                                          | Example payload                                                                                                                                                   | Result   | Response code   |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------|
| Update a Product using new                 | provided with new values                                                                                           | Adds new value to existing values                                                                                                                                 | 201      |                 |
| values for a required valueList collection | {                                                                                                                  | "code": "test_article11d", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "tags": [ {"value": "bestSelling"} ]                        |          |                 |
| }                                          |                                                                                                                    |                                                                                                                                                                   |          |                 |
| Update a Product using an empty            | provided as empty list                                                                                             | Existing values merge with the                                                                                                                                    | 201      |                 |
| list for a required valueList              | updated POST and because the                                                                                       |                                                                                                                                                                   |          |                 |
| collection                                 | request adds no new values, the collection keeps the original values                                               |                                                                                                                                                                   |          |                 |
| {                                          | "code": "test_article11d", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "tags": []   |                                                                                                                                                                   |          |                 |
| }                                          |                                                                                                                    |                                                                                                                                                                   |          |                 |
| Update Product using a null                | null                                                                                                               | Existing values merge with the                                                                                                                                    | 201      |                 |
| value for a required valueList             | updated POST and because the                                                                                       |                                                                                                                                                                   |          |                 |
| collection                                 | request adds no new values, the collection keeps the original values                                               |                                                                                                                                                                   |          |                 |
| {                                          | "code": "test_article11d", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "tags": null |                                                                                                                                                                   |          |                 |
| }                                          |                                                                                                                    |                                                                                                                                                                   |          |                 |
| Update Product without providing           | not provided                                                                                                       | The request provides no new                                                                                                                                       | 201      |                 |
| values for a required valueList            | values, so the existing values                                                                                     |                                                                                                                                                                   |          |                 |
| collection                                 | remain                                                                                                             |                                                                                                                                                                   |          |                 |
| {                                          | "code": "test_article11d", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }               |                                                                                                                                                                   |          |                 |
| }                                          |                                                                                                                    |                                                                                                                                                                   |          |                 |
| Create Product using nonexistent           | provided with nonexistent values                                                                                   | Adds the new value to the existing                                                                                                                                | 201      |                 |
| values for a required ValueList            | values                                                                                                             |                                                                                                                                                                   |          |                 |
| Collection                                 | {                                                                                                                  | "code": "test_article11e", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "tags": [ {"value": "newArrival"}, {"value": "clearance"} ] |          |                 |
| }                                          |                                                                                                                    |                                                                                                                                                                   |          |                 |

## Map Attributes For Post

The Integration API's POST API handles required and optional map type attributes similarly to collection attributes.

A POST payload provides map attributes as a collection of map entry, or key-value, pairs. For example, the following payload shows an Integration Object for a ConsumedDestination item type that includes the additionalProperties attribute. In SAP Commerce Cloud, the additionalProperties attribute has a String2StringMapType.

{ "id": "cloud-1", "url": "https://localhost:9002/blah", "destinationTarget": { "id": "cloud-1-target" }, "endpoint": { "id": "cloudDestinations", "name": "cloud destinations endpoint", "version": "1.0", "specUrl": "https://localhost:9002/blah" }, "additionalProperties": [ { "key": "key1", "value": "value 1"

 },
 { "key": "key2", "value": "value 2" } ] }
A POST request using the example payload creates a ConsumedDestination with additionalProperties, as shown:
key1=value 1 key2=value 2 The Integration API ignores autoCreate for map attributes. Although additionalProperties has the String2StringMapType in the schema, also represented as an entity type, there is no need to model the additionalProperties attribute using autoCreate=true. For primitive types such as additionalProperties, where both the key and value are of primitive types, the API always creates the map values. Further, the API treats map attributes according to the following rules. For examples, see the table.

POST requests append map attribute entries to existing entries. In other words, the API adds new, additional key values to existing values, while updated values for existing keys replace the previous values.

The key value in a payload cannot be null. However, the value property can be empty or null.

In general, map attributes behave in the same way as required and optional multivalue primitive attributes. For examples of specic scenarios, see the applicable examples in Multivalue Attributes.

Related Information Map Attributes

## Multivalue Attributes

In the Integration API, the persistence behavior for collections of optional and required multivalue primitive attributes depends on whether values are provided in the payload. The following tables describe the persistence behavior for POST upsert scenarios.

Required Multivalue Primitive Attributes

| In the following example scenarios, the colors attribute is required and multivalue. POST Scenario Value provided in payload Example payload   | Result                                                                                                              | Response code                                                                                                                                                                |     |
|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| Create a Product with new values                                                                                                               | provided                                                                                                            | Attribute persists with values                                                                                                                                               | 201 |
| for a required, multivalue attribute                                                                                                           | {                                                                                                                   | "code": "test_article7a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "colors": [ {"value": "black"}, {"value": "white"}, {"value": "blue"} ] |     |
| }                                                                                                                                              |                                                                                                                     |                                                                                                                                                                              |     |
| Update a Product using an empty                                                                                                                | provided as an empty collection                                                                                     | Existing values merge with the                                                                                                                                               |     |
| collection for a required, multivalue                                                                                                          | updated POST and since no new                                                                                       |                                                                                                                                                                              |     |
| attribute                                                                                                                                      | values are added, the collection keeps the original values                                                          | 201                                                                                                                                                                          |     |
| {                                                                                                                                              | "code": "test_article7a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "colors": []   |                                                                                                                                                                              |     |
| }                                                                                                                                              |                                                                                                                     |                                                                                                                                                                              |     |
| Update Product with a null value                                                                                                               | null                                                                                                                | Existing values merge with the                                                                                                                                               |     |
| for a required, multivalue attribute                                                                                                           | updated POST and since no new values are added, the collection keeps the original values                            | 201                                                                                                                                                                          |     |
| {                                                                                                                                              | "code": "test_article7a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "colors": null |                                                                                                                                                                              |     |
| }                                                                                                                                              |                                                                                                                     |                                                                                                                                                                              |     |

| 7/6/2024 POST Scenario                                                                                                                                                                             | Value provided in payload                                                                                                                                                    | Example payload                                                                                                   | Result                           | Response code   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------|-----------------|
| Update a Product without providing not provided                                                                                                                                                    | Existing values merge with the                                                                                                                                               |                                                                                                                   |                                  |                 |
| the required multivalue attribute or                                                                                                                                                               | updated POST and since no new                                                                                                                                                |                                                                                                                   |                                  |                 |
| value                                                                                                                                                                                              | values are added, the collection keeps the original values                                                                                                                   |                                                                                                                   |                                  |                 |
| {                                                                                                                                                                                                  | "code": "test_article7a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }                                                                          |                                                                                                                   |                                  |                 |
| }                                                                                                                                                                                                  | 201                                                                                                                                                                          |                                                                                                                   |                                  |                 |
| Update a Product with new values                                                                                                                                                                   | provided                                                                                                                                                                     | New values merge with the existing 201                                                                            |                                  |                 |
| for required multivalue attribute                                                                                                                                                                  | values                                                                                                                                                                       |                                                                                                                   |                                  |                 |
| {                                                                                                                                                                                                  | "code": "test_article7a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "colors": [ {"value": "green"}, {"value": "red"} ]                      |                                                                                                                   |                                  |                 |
| }                                                                                                                                                                                                  |                                                                                                                                                                              |                                                                                                                   |                                  |                 |
| Update a Product with duplicate                                                                                                                                                                    | duplicate values provided                                                                                                                                                    | The following example includes two existing values,                                                               | Merges the duplicate values with | 201             |
| values for a required multivalue                                                                                                                                                                   | black and white, and one new value, pink:                                                                                                                                    | the original values and adds the                                                                                  |                                  |                 |
| attribute                                                                                                                                                                                          | new value                                                                                                                                                                    |                                                                                                                   |                                  |                 |
| {                                                                                                                                                                                                  | "code": "test_article7a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "colors": [ {"value": "black"}, {"value": "white"}, {"value": "pink"} ] |                                                                                                                   |                                  |                 |
| }                                                                                                                                                                                                  |                                                                                                                                                                              |                                                                                                                   |                                  |                 |
| Create Product with an empty                                                                                                                                                                       | provided as empty collection                                                                                                                                                 | attributes persist without values                                                                                 | 201                              |                 |
| collection for a required multivalue attribute                                                                                                                                                     | {                                                                                                                                                                            | "code": "test_article7b", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "colors": [] |                                  |                 |
| }                                                                                                                                                                                                  |                                                                                                                                                                              |                                                                                                                   |                                  |                 |
| Create a Product without providing                                                                                                                                                                 | not provided                                                                                                                                                                 | Because the collection attribute is                                                                               | 400                              |                 |
| a required, multivalue attribute                                                                                                                                                                   | required and not provided, the API returns an error                                                                                                                          |                                                                                                                   |                                  |                 |
| {                                                                                                                                                                                                  | "code": "test_article7c", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }                                                                          |                                                                                                                   |                                  |                 |
| }                                                                                                                                                                                                  |                                                                                                                                                                              |                                                                                                                   |                                  |                 |
| Create a Product with a null value null                                                                                                                                                            | Because null is not a valid value                                                                                                                                            | 400                                                                                                               |                                  |                 |
| for a required multivalue attribute                                                                                                                                                                | for a new, required collection attribute, the API returns an error                                                                                                           |                                                                                                                   |                                  |                 |
| {                                                                                                                                                                                                  | "code": "test_article7d", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "colors": null                                                          |                                                                                                                   |                                  |                 |
| }                                                                                                                                                                                                  |                                                                                                                                                                              |                                                                                                                   |                                  |                 |
| Optional Multivalue Primitive Attributes The following examples assume the existence of the optional, multivalue sizesAvailable attribute. POST Scenario Value provided in payload Example payload | Result                                                                                                                                                                       | Response code                                                                                                     |                                  |                 |

| 7/6/2024 POST Scenario                                           | Value provided in payload        | Example payload                                                                                                                                                                  | Result   | Response code   |
|------------------------------------------------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------|
| Create an Integration Object                                     | provided                         | Persists all provided values                                                                                                                                                     | 201      |                 |
| including values for an optional, multivalue primitive attribute | {                                | "code": "test_article6a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "sizesAvailable":[ {"value":28}, {"value":30}, {"value":32}, {"value":34} ] |          |                 |
| }                                                                |                                  |                                                                                                                                                                                  |          |                 |
| Create a Product with an empty                                   | provided as an empty collection  | Creates the Integration Object with                                                                                                                                              | 201      |                 |
| collection for an optional,                                      | empty values for the attribute   |                                                                                                                                                                                  |          |                 |
| multivalue primitive attribute                                   | {                                | "code": "test_article6b", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "sizesAvailable":[]                                                         |          |                 |
| }                                                                |                                  |                                                                                                                                                                                  |          |                 |
| Create an Integration Object                                     | not provided                     | Creates the Integration Object with                                                                                                                                              | 201      |                 |
| without a value for an optional,                                 | an empty value for the attribute |                                                                                                                                                                                  |          |                 |
| multivalue primitive attribute                                   | {                                | "code": "test_article6c", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }                                                                              |          |                 |
| }                                                                |                                  |                                                                                                                                                                                  |          |                 |
| Create an Integration Object with a                              | null                             | Creates the Integration Object with                                                                                                                                              | 201      |                 |
| null value for an optional,                                      | an empty value for the attribute |                                                                                                                                                                                  |          |                 |
| multivalue primitive attribute                                   | {                                | "code": "test_article6d", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "sizesAvailable": null                                                      |          |                 |
| }                                                                |                                  |                                                                                                                                                                                  |          |                 |

## Primitive Attributes

Persistence behavior for required primitive attributes in the Integration API depends on whether attributes are required or optional, and whether a value is included in the payload.

 Note Only primitive attributes can be localized and not entities or complex objects.

The following tables describe how the Integration API handles POST requests for creating and updating a Product Integration Object with a primitive attribute. In the example scenarios, only the prodName attribute is mandatory=true, or required, by the Integration Object denition. Required Primitive Attributes

| POST Scenario                      | Value provided in payload                                                                           | Example payload                    | Result   | Response code   |
|------------------------------------|-----------------------------------------------------------------------------------------------------|------------------------------------|----------|-----------------|
| Create a Product without providing | not provided                                                                                        | The API returns a missing property | 400      |                 |
| the mandatory primitive attribute  | error and does not persist the                                                                      |                                    |          |                 |
| in payload                         | payload.                                                                                            |                                    |          |                 |
| {                                  | "code": "test_article3a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } |                                    |          |                 |
| }                                  |                                                                                                     |                                    |          |                 |

| 7/6/2024 POST Scenario                               | Value provided in payload                                                                                             | Example payload                                                                                                                                  | Result   | Response code   |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------|
| Create a Product using a null                        | null                                                                                                                  | The API returns a missing property                                                                                                               | 400      |                 |
| error and does not persist the                       |                                                                                                                       |                                                                                                                                                  |          |                 |
| value for a mandatory primitive attribute            | payload.                                                                                                              |                                                                                                                                                  |          |                 |
| {                                                    | "code": "test_article3b", "prodName": null, "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } |                                                                                                                                                  |          |                 |
| }                                                    |                                                                                                                       |                                                                                                                                                  |          |                 |
| Optional Primitive Attributes POST Scenario          | Value provided in payload                                                                                             | Example payload                                                                                                                                  | Result   | Response code   |
| Update an existing Product with a                    | null                                                                                                                  | Updates the prodDesc value to                                                                                                                    | 201      |                 |
| null value for an optional                           | null                                                                                                                  |                                                                                                                                                  |          |                 |
| attribute                                            | {                                                                                                                     | "code": "test_article1a", "prodName": "name 1a new", "prodDesc": null, "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } |          |                 |
| }                                                    |                                                                                                                       |                                                                                                                                                  |          |                 |
| Create a Product without including                   | not provided                                                                                                          | Value for prodDesc sets to null                                                                                                                  | 201      |                 |
| an optional primitive attribute in the payload       | {                                                                                                                     | "code": "test_article2a", "prodName": "name 2a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }                       |          |                 |
| }                                                    |                                                                                                                       |                                                                                                                                                  |          |                 |
| Create a Product using an optional                   | null                                                                                                                  | Sets prodDesc value to null                                                                                                                      | 201      |                 |
| primitive attribute with a null value in the payload | {                                                                                                                     | "code": "test_article2b", "prodName": "name 2b", "prodDesc": null, "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }     |          |                 |
| }                                                    |                                                                                                                       |                                                                                                                                                  |          |                 |

## Reference Attributes

The Integration API's handling of required and optional single value reference attributes and of referenced collection attributes in a POST request varies depending on the values included in the payload. References are attributes that refer to types. The following tables detail the persistence behavior for required and optional reference attributes in various scenarios.

Required Reference Attributes The example scenarios in this table assume the requiredCountry attribute is mandatory, not multivalue, not nullable, and of the type Country.

| The example scenarios in this table assume the requiredCountry attribute is mandatory, not multivalue, not nullable, and of the type Country. POST Scenario Value provided in payload Example payload Result   | Response code                                                                                                                                 |                                    |     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|-----|
| Create a Product with the required                                                                                                                                                                             | provided                                                                                                                                      | Persists the attributes and values | 201 |
| reference value in the payload                                                                                                                                                                                 | as provided                                                                                                                                   |                                    |     |
| {                                                                                                                                                                                                              | "code": "test_article8a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "requiredCountry": { "isocode": "bldr" } |                                    |     |
| }                                                                                                                                                                                                              |                                                                                                                                               |                                    |     |

| 7/6/2024 POST Scenario                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Value provided in payload                                                                                                                       | Example payload                                                                                                                                   | Result   | Response code   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------|
| Update a Product using a new value provided                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Replaces the existing value with the 201                                                                                                        |                                                                                                                                                   |          |                 |
| for the required reference value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | new value                                                                                                                                       |                                                                                                                                                   |          |                 |
| {                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | "code": "test_article8a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "requiredCountry": { "isocode": "gnbrrl" } |                                                                                                                                                   |          |                 |
| }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                 |                                                                                                                                                   |          |                 |
| Create a Product without the                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | not provided                                                                                                                                    | Returns a missing navigation                                                                                                                      | 400      |                 |
| required reference value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | property error                                                                                                                                  |                                                                                                                                                   |          |                 |
| {                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | "code": "test_article8b", "catalogVersion": { "catalog": { "id": "Default" }, "version": "                                                      |                                                                                                                                                   |          |                 |
| Create a Product using a null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | null                                                                                                                                            | Returns a missing navigation                                                                                                                      | 400      |                 |
| value for a required reference value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | property error                                                                                                                                  |                                                                                                                                                   |          |                 |
| {                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | "code": "test_article8c", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "requiredCountry": null                    |                                                                                                                                                   |          |                 |
| }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                 |                                                                                                                                                   |          |                 |
| Create a Product using a                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | provided with invalid reference                                                                                                                 | Returns a missing navigation                                                                                                                      | 400      |                 |
| nonexistent value for a required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | property error                                                                                                                                  |                                                                                                                                                   |          |                 |
| reference value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | {                                                                                                                                               | "code": "test_article8d", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "requiredCountry": { "isocode": "nonSense" } |          |                 |
| }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                 |                                                                                                                                                   |          |                 |
| Optional Reference Attributes The example scenarios in the following table assume that the prodUnit attribute value, pieces, exists in the system and that none of the associated attributes are set to autocreate. POST Scenario Value provided in payload Example payload Result Response code Create a Product using a value that references and existing item for an optional reference attribute provided Creates the Product and 201 persists the reference attribute { "code": "test_article4a", "prodName": "name 4a", "prodDesc": "this description 4a", "prodUnit": { "code": "pieces", "name": "pieces", "unitType": "pieces" }, "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } } Create a Product with a null Creates the Product and 201 null value for an optional persists a null value for reference attribute prodUnit { "code": "test_article4b", "prodName": "name 4b", "prodDesc": "this description 4b", "prodUnit": null, "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } } |                                                                                                                                                 |                                                                                                                                                   |          |                 |

| 7/6/2024 POST Scenario       | Value provided in payload                                                                                                                                                                                                                                          | Example payload                                                                                                                   | Result   | Response code   |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|----------|-----------------|
| Create a Product with a      | provided with nonexistent,                                                                                                                                                                                                                                         | The attribute                                                                                                                     |          |                 |
| nonexistent, non-autocreate, | non-autocreate reference                                                                                                                                                                                                                                           | nonExistingUnit does not                                                                                                          |          |                 |
| referenced attribute         | attribute                                                                                                                                                                                                                                                          | exist and is not created because autocreate is not set to true for the item. The API returns a missing navigation property error. |          |                 |
| {                            | "code": "test_article5a", "prodName": "name 5a", "prodDesc": "this description 5a", "prodUnit": { "code": "nonExistingUnit", "name": "nonExistingUnit", "unitType": "nonExistingUnit" }, "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } |                                                                                                                                   |          |                 |
| }                            | 400                                                                                                                                                                                                                                                                |                                                                                                                                   |          |                 |

## Valuelist Attributes

In the Integration API, handling of required ValueList attributes varies depending on the POST payload.

The following scenarios describe the persistence behavior for required valueList attributes. The examples assume the paymentMethod valueList attribute is mandatory, not multivalue, and not nullable. Existing values for the valueList include Mastercard and Visa.

 Note For information about valueList collections, see Collection Attributes.

| POST Scenario                       | Value provided in payload                                                                                                   | Example payload                                                                                                                 | Result   | Response code   |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|----------|-----------------|
| Create a Product using a null value | null                                                                                                                        | The API cannot persist a new                                                                                                    |          |                 |
| for a required valueList            | valueList without values and returns a missing navigation property error                                                    | 400                                                                                                                             |          |                 |
| {                                   | "code": "test_article10a", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "paymentMethod": null |                                                                                                                                 |          |                 |
| }                                   |                                                                                                                             |                                                                                                                                 |          |                 |
| Create a Product without providing  | not provided                                                                                                                | Returns a missing navigation                                                                                                    | 400      |                 |
| a value for a required ValueList    | property error                                                                                                              |                                                                                                                                 |          |                 |
| {                                   | "code": "test_article10b", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }                        |                                                                                                                                 |          |                 |
| }                                   |                                                                                                                             |                                                                                                                                 |          |                 |
| Create Product using existing       | provided with existing values                                                                                               | Persists the provided values                                                                                                    | 201      |                 |
| values for a required ValueList     | {                                                                                                                           | "code": "test_article10c", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "paymentMethod": "visa"   |          |                 |
| }                                   |                                                                                                                             |                                                                                                                                 |          |                 |
| Create a Product, providing         | provided with nonexistent values                                                                                            | Autocreates and persists the new,                                                                                               | 201      |                 |
| nonexistent values for a required   | additional value                                                                                                            |                                                                                                                                 |          |                 |
| ValueList                           | {                                                                                                                           | "code": "test_article10d", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" }, "paymentMethod": "paypal" |          |                 |
| }                                   |                                                                                                                             |                                                                                                                                 |          |                 |

## Persistence Hooks

Use persistence hooks to execute business logic before or after a request to persist an item.

Persistence Hooks SAP Cloud Integration OData Adapter in its current version does not support functions. Persistence hooks provide a stopgap measure. Invoke the hook by specifying its name in the header of an HTTP POST request. There are two types of hooks:
PrePersistHook PostPersistHook You can invoke, at most, only one PrePersistHook and one PostPersistHook per request. If there is no value in a Pre- or PostPersistHook header, the header is ignored and the object is persisted as usual.

PrePersistHook The execute method for the PrePersistHook invokes right before the Integration Object sent in the POST request persists in the SAP Commerce Cloud platform. To create a PrePersistHook, implement the following interface:
/** * A procedure to be executed before persisting an item model. Name of this procedure must be submitted with a POST request in * request header named Pre-Persist-Hook. */ public interface PrePersistHook {
/** * Executes this hook before persisting the given item. * @param item an item to execute this hook with. * @param context to provide information about the item to be persisted * @return result of processing/modification of the item by this hook to be persisted. * If empty, that means there is no item to persist. * @see PersistenceContext\#getPrePersistHook() */ Optional<ItemModel> execute(ItemModel item, PersistenceContext context);
}
The parameter item is the item being persisted. The return type is Optional<ItemModel>. If the PrePersistHook returns Optional.empty(), then the PostPersistHook is not called and the item passed in does not persist. If the Optional contains the item (Optional.isPresent() == true), then the item persists after the hook execution completes. To specify the PrePersistHook to execute, specify the name of the hook as a header parameter in the POST request. For example, to trigger a hook called preProcessingHook, provide a header with the key Pre-Persist-Hook and a value of preProcessingHook.

Exceptions During Execution of a PrePersistHook If an exception is thrown during the execution of the PrePersistHook, the exception is logged, and the integration item included in the POST request does not persist. An error response code, pre_persist_error, and the status code 400 return with a message containing the item <integrationKey>.

PostPersistHook The execute method for the PostPersistHook invokes right after the item persists in the SAP Commerce Cloud platform. To create a PostPersistHook, implement the following interface:
/** * A procedure to be executed after persisting an item model. Name of this procedure must be submitted with a POST request in * request header named Post-Persist-Hook. */
public interface PostPersistHook
{
/** * Executes this hook after persisting the given item. * @param item an item to execute this hook with. * @param context to provide information about the item to be persisted. * @see PersistenceContext\#getPostPersistHook() */ void execute(ItemModel item, PersistenceContext context);
}
The parameter item is the persisted item. To specify the PostPersistHook to execute, dene the name of the hook as a header parameter in the POST request. For example, to trigger a hook called postProcessingHook, provide a header with the key <Post-Persist-Hook> and a value of postProcessingHook.

Using Hooks in Batch and Bulk In both batch and bulk modes, there is a single header per changeSet. Place your hook call between the POST and the end of the header. Using Hooks in Batch Mode When you create each changeSet, dene the following JSON body and headers:
--batch Content-Type: multipart/mixed; boundary=changeset --changeset Content-Type: application/http Content-Transfer-Encoding: binary POST Products HTTP/1.1 Content-Language: en This is   For more    the SAP Help  74 Accept: application/json Content-Type: application/json Pre-Persist-Hook: sampleQaPrePersistHook Transaction Management A new transaction begins before execution of the PrePersistHook. The transaction commits after the PostPersistHook completes its execution and includes the persistence of the Integration Object in between the pre- and post-persist hooks. If an exception occurs at any point while the transaction is open, the whole transaction rolls back, and the Integration Object does not persist. If you start a new transaction within a PrePersistHook or a PostPersistHook, the transaction you started commits, and an exception occurs within a pre- or post-persistence hook, your transaction might not roll back, which could lead to an inconsistent state. The same is true for starting a new thread within a pre- or post-persistence hook. For this reason, do not start a new database transaction or thread within a persistence hook.

Missing Hooks Do not specify a hook name in a PrePersistHook or a PostPersistHook header if a Spring bean with that name or ID is not on the classpath. If a hook name is specied in such a case, the provided Integration Object does not persist. Additionally, an error returns with the code hook_not_found and status code 400.

## Creating A Persistence Hook

To create a persistence hook, dene a new PrePersistHook or PostPersistHook and then specify that persistence hook in a persistence request.

Dening a New PrePersistHook

## Note

Persistence hooks use PersistenceContext, which is accessible via the de.hybris.platform.inboundservices.persistence.hook.PrePersistHook and de.hybris.platform.inboundservices.persistence.hook.PostPersistHook APIs. The de.hybris.platform.inboundservices.persistence.PersistenceContext API provides access to some request attributes, for example, content and accept locales, as well as to the Integration Object metadata and the request payload. Persistence hooks created using the legacy APIs de.hybris.platform.odata2services.odata.persistence.hook.PrePersistHook and de.hybris.platform.odata2services.odata.persistence.hook.PostPersistHook are still supported, but it's recommended that you convert pesistence hooks created using legacy APIs to the new APIs.

To create a PrePersistHook, create a class that implements the PrePersistHook interface. Consider the following example:
import de.hybris.platform.core.model.ItemModel; import de.hybris.platform.inboundservices.persistence.hook.PrePersistHook; import java.util.Optional; import java.util.Set; import org.slf4j.Logger; import org.slf4j.LoggerFactory; import com.google.common.collect.Sets; /** * PrePersistHook example for demonstrating usage of the request Content-Language and the contextual Integration Object metadata. */ public class NewPrePersistHook implements PrePersistHook {
@Override public Optional<ItemModel> execute(final ItemModel item, final PersistenceContext context) {
return item instanceof CategoryModel
? executeCategory((CategoryModel) item, context) : Optional.empty();
} private Optional<ItemModel> executeCategory(final CategoryModel item, final PersistenceContext context) {
assert item != null; if (ioHasNameAttribute(context)) {
final var locale = context.getContentLocale(); final var name = item.getName(locale); if (name != null) {
item.setName(name.toLowerCase(locale) + " - updated by new hook (" + locale.getLanguage() + ")", locale);
}
} return Optional.of(item);
} private boolean ioHasNameAttribute(final PersistenceContext context) {
You need to register the PrePersistHook in a Spring context for it to be available in the application. For example:
 Sample Code
<bean id="newPrePersistHook" class="biz.customer.hooks.NewPrePersistHook"/>
 Note This step enables referencing to the Spring Bean IDs in the request headers, for example, Pre-Persist-Hook=newPrePersistHook or Pre-PersistHook=bean://newPrePersistHook. The "bean://" schema is reserved to specically invoke a Spring Bean hook implementation.

Dening a New PostPersistHook To create a PostPersistHook, create a class that implements the PostPersistHook interface. Consider the following example:
import de.hybris.platform.core.model.ItemModel; import de.hybris.platform.core.model.order.OrderModel; import de.hybris.platform.inboundservices.persistence.hook.PostPersistHook; import de.hybris.platform.order.OrderService; import org.slf4j.Logger; import org.slf4j.LoggerFactory; import org.springframework.beans.factory.annotation.Required; /** * PostPersistHook example for demonstrating usage of the request Content-Language and the payload in the hook logic. */ public class NewPostPersistHook implements PostPersistHook {
private static final Logger LOG = Log.getLogger(NewPostPersistHook.class); @Override public void execute(final ItemModel item, final PersistenceContext context) {
if (payloadContainsNameValue(context)) {
LOG.info("Post-processed {} with {}", item, context);
}
} private boolean payloadContainsNameValue(final PersistenceContext context) {
final LocalizedValue nameValue = (LocalizedValue) context.getIntegrationItem().getAttribute("name"); return nameValue != null && nameValue.get(context.getContentLocale()) != null;
}
}
You need to register the PostPersistHook in a Spring context for it to be available in the application. For example:
 Sample Code
<bean id="newPostPersistHook" class="biz.customer.hooks.NewPostPersistHook"/>
 Note This step enables referencing to the Spring Bean IDs in the request headers, for example, Post-Persist-Hook=newPostPersistHook or Post-PersistHook=bean://newPostPersistHook. The "bean://" schema is reserved to specically invoke a Spring Bean hook implementation.

Dening a Persistence Hook with a Different Persistence Hook Provider You can dene a PrePersistHook or PostPersistHook by registering a new persistence hook provider with the application instead of using Spring Bean. The following example is for a PostPersistHook that uses an external microservice (ConsumedDestination) as a persistence hook. The rst step is to use ConsumedDestination to dene the supported microservices. For example:
 Sample Code import de.hybris.platform.apiregistryservices.model.ConsumedDestinationModel; import de.hybris.platform.core.model.ItemModel; import de.hybris.platform.inboundservices.persistence.PersistenceContext; import de.hybris.platform.inboundservices.persistence.hook.PostPersistHook; import de.hybris.platform.outboundservices.facade.impl.RemoteSystemClient; import java.util.Collections; import java.util.Map; import javax.annotation.Nonnull; import org.springframework.http.HttpEntity; public class MicroservicePostPersistenceHookAdapter implements PostPersistHook This is   For more    the SAP Help  76

{
private final RemoteSystemClient microserviceClient; private final ConsumedDestinationModel destination; public MicroservicePostPersistenceHookAdapter(
@Nonnull final RemoteSystemClient client, @Nonnull final ConsumedDestinationModel dest)
{
microserviceClient = client; destination = dest;
} @Override public void execute(final ItemModel item, final PersistenceContext context)
{
microserviceClient.post(destination, toPayload(item, context));
} private HttpEntity<Map<String, Object>> toPayload(final ItemModel item, final PersistenceContext context) {
// provide actual implementation here to create and populate the payload return new HttpEntity<>(Collections.emptyMap());
}
}
 Note In the above example, your extension must depend on the apiregistryservices, inboundservices, and outboundservices extensions if you use the imported classes. They are included to simplify the example. You can use a different API or implement the logic yourself.

Once the hook adapter is implemented, you can implement a provider for this hook. For example:
 Sample Code import de.hybris.platform.apiregistryservices.model.ConsumedDestinationModel; import de.hybris.platform.apiregistryservices.services.DestinationService; import de.hybris.platform.inboundservices.persistence.PersistenceContext; import de.hybris.platform.inboundservices.persistence.hook.PersistenceHookProvider; import de.hybris.platform.inboundservices.persistence.hook.PostPersistHook; import de.hybris.platform.inboundservices.persistence.hook.PrePersistHook; import de.hybris.platform.outboundservices.facade.impl.RemoteSystemClient; import java.util.Objects; import java.util.Optional; import javax.annotation.Nonnull; public class MicroserviceHookProvider implements PersistenceHookProvider {
private static final String SUPPORTED_HOOK_SCHEMA = "dest://"; private static final String DESTINATION_TARGET = "Microservices"; private final DestinationService<ConsumedDestinationModel> destinationService; private final RemoteSystemClient remoteSystemClient; public MicroserviceHookProvider(
 @Nonnull final DestinationService<ConsumedDestinationModel> service,
 @Nonnull final RemoteSystemClient client) {
destinationService = service; remoteSystemClient = client;
} @Override public Optional<PostPersistHook> getPostPersistHook(final PersistenceContext context)
{
return Optional.of(context)
.map(PersistenceContext::getPostPersistHook) .filter(this::isSupportedHookName) .map(this::toDestinationId) .map(this::toDestination) .filter(Objects::nonNull) .map(dest -> new MicroservicePostPersistenceHookAdapter(remoteSystemClient, dest));
} private boolean isSupportedHookName(final String hookName) {
// a check that the hook name starts with "our" schema or has no schema at all, e.g: "sampleHook" or "dest://sampleHook" return hookName != null && (hookName.startsWith(SUPPORTED_HOOK_SCHEMA) || !hookName.contains("/"));
} private String toDestinationId(final String hookName) {
// strips out the schema, if it's present return hookName.startsWith(SUPPORTED_HOOK_SCHEMA) ? hookName.substring(SUPPORTED_HOOK_SCHEMA.length()) : hookName; 
} private ConsumedDestinationModel toDestination(final String destId) {
// we assumed all microservice destinations are grouped in the special "Microservices" destination target. return destinationService.getDestinationByIdAndByDestinationTargetId(destId, DESTINATION_TARGET);
} @Override public Optional<PrePersistHook> getPrePersistHook(final PersistenceContext context) {
// if needed implement a PrePersistHook adapter as we did for the PostPersistHook and instantiate it here. return Optional.empty();
}
}
Now you need to register the hook provider in the spring context. For example:

<alias name="defaultMicroserviceHookProvider" alias="microserviceHookProvider"/> <bean id="defaultMicroserviceHookProvider" class="....MicroserviceHookProvider"/> <bean depends-on="inboundPersistenceHookProviders" parent="listMergeDirective"> <property name="add" ref="microserviceHookProvider"/> </bean>
This conguration adds the new provider to the list of persistence hook providers in inboundservices. Hook names with a schema specic to your provider or without a schema are supported, which provides the exibility to override other hook providers when a hook name doesn't contain a specic schema, or to use a very specic provider if the hook name contains that provider's schema. In the above example, the provider is at the end of the provider list so when the request contains a hook name without the schema, for example, "sampleHook", then all providers preceding the specied provider in the list have a chance to react to that name rst. If the preceding providers return a java.util.Optional containing a hook, then the search stops and the last provider in the list is never reached. For example, if there is a post-persistence hook Spring Bean with a "sampleHook" bean ID in the application context, that hook is used instead. To override Spring Bean hooks with your microservice hooks, you need to place your provider at the beginning of the list, or at least before the Spring Bean providers in the list. For details on how you can do that, see ListMergeDirective. However, if the hook name contains the schema specic to your provider, for example, "dest://sampleHook", then only your provider reacts to this name. It's important to support a name without the schema and with a specic schema in every custom provider, if the ability to override other providers is desired.

Exceptions During Execution of a PostPersistHook If an exception is thrown during the execution of a PostPersistHook, the system logs the exception and rolls back the entire transaction. As a result, the integration item included in the POST
request does not persist. The system returns the error response code post_persist_error and the status code 400, along with a message that includes the item's integrationKey.

## Persistence Hook Example

Persistence differs for single item and batch POST requests.

Single Item Persistence Hook Example

| Headers for the Entire Body of the POST Request   |                                                    |
|---------------------------------------------------|----------------------------------------------------|
| Key                                               | Value                                              |
| Content-Type                                      | application/json                                   |
| Accept                                            | application/json                                   |
| Content-Language                                  | en                                                 |
| Pre-Persist-Hook                                  | sampleQaPrePersistHook                             |
| Post-Persist-Hook                                 | beanIdForPostPersistHookThatWasAlsoPreviouslyDened |
| Post Request Body                                 |                                                    |

{
"code": "TEST_PRODUCT", "name": "Name des Testproduktes",
"catalogVersion": {
"version": "Staged", "catalog": {
"id": "Default"
} } }
Batch Item Persistence Hook Example The <multipart/mixed;> value signals a batch request and the <boundary=batch> value denes the boundary that signals the beginning and end of the batch request.

| Headers for the Entire Body of the POST Request   |                                 |
|---------------------------------------------------|---------------------------------|
| Key                                               | Value                           |
| Content-Type                                      | multipart/mixed; boundary=batch |
| POST Request Body                                 |                                 |

This batch example posts two items. Each item included in this request body is separated by "–changeset_43f93393-1ab6-41fb-bed8-c4eb68ff683". The boundary for each item is dened by Content-Type: multipart/mixed; boundary=changeset_43f93393-1ab6-41fb-bed8-c4eb68ff683d , which is dened in the second line of the request body. A header is dened for each <--changeset>, directly above the item payload. A <Pre-Persist-Hook> and <Post-Persist-Hook> is dened in the header for each <--changeset>.

 --batch Content-Type: multipart/mixed; boundary=changeset_43f93393-1ab6-41fb-bed8-c4eb68ff683d -changeset_43f93393-1ab6-41fb-bed8-c4eb68ff683d - Content-Type: application/http Content-Transfer-Encoding: binary POST /odata2webservices/InboundProduct/Products HTTP/1.1 This is   For more    the SAP Help  78 Content-Length: \#\#\#
Content-Language: en Accept: application/json Content-Type: application/json Pre-Persist-Hook: beanIdForPrePersistHook Post-Persist-Hook: beanIdForPostPersistHook { "code": "TEST_PRODUCT", "name": "name of test product", "catalogVersion": { "version": "Staged", "catalog": { "id": "Default"
 }
 } } --changeset_43f93393-1ab6-41fb-bed8-c4eb68ff683d Content-Type: application/http Content-Transfer-Encoding: binary POST /odata2webservices/InboundProduct/Products HTTP/1.1 Content-Length: \#\#\# Content-Language: de Accept: application/json Content-Type: application/json Pre-Persist-Hook: beanIdForPrePresistHook Post-Persist-Hook: beanIdForPostPersistHook { "code": "TEST_PRODUCT", "name": "Name des Testproduktes", "catalogVersion": { "version": "Staged", "catalog": { "id": "Default" } } } --changeset_43f93393-1ab6-41fb-bed8-c4eb68ff683d-- --batch--

## Localization For Post Requests

Persist Integration Objects in multiple languages and view localizedAttributes as a deferred link. The POST command supports the Content-Language command, as well as the localizedAttributes NavigationProperty, to persist an IntegrationObject item in multiple languages. You can also use the Accept-Language header in your POST request to return the persisted items in their localized languages in the response to your POST request. The localizedAttributes property represents a collection of localized entities that contain each Item Type's localized attributes. A localized property is any property annotated with IsLanguageDependent, such as the description property in Product. The table that follows describes how the presence or absence of localized properties in a request affects persistence. For example, the following POST request persists all category attributes in all available languages when you provide a localizedAttribute, the localizedAttribute's localized properties, and the Content-Language header in your request.

POST https://localhost:9002/odata2webservices/LocalizedProduct/Categories Depending on whether a POST request contains all or some of the localization values, the system persists the provided values using the logic shown in the following table.

 Note Removing values for localizedAttributes is possible only through a PATCH request. For more information, see Localization for PATCH Requests.

| localizedAttributes                                                                  | localized properties   | Content-Language header   | Result                                                                                                  | Example Payload                                                                                                                     |
|--------------------------------------------------------------------------------------|------------------------|---------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| provided                                                                             | provided               | provided                  | Merges the results of localizedAttributes and localizedProperties; localizedAttributes takes precedence | { "code": "clothing", "name": "Clothing Category 1", "localizedAttributes": [{ "language": "en", "name": "Clothing Category 2" }] } |
| not provided                                                                         | provided               | provided                  | Stores the localized properties in the language that the Content-Language header species                | { "code": "clothing", "name": "Clothing Category" }                                                                                 |
| not provided                                                                         | provided               | not provided              | Stores the localized properties in the default platform language                                        | { "code": "clothing", "name": "Clothing Category Default" }                                                                         |
| provided                                                                             | not provided           | not provided              | Stores all localizedAttributes                                                                          | { "code": "clothing", "localizedAttributes": [{ "language": "en", "name": "Clothing Category" }] }                                  |
| This is custom documentation. For more information, please visit the SAP Help Portal | 79                     |                           |                                                                                                         |                                                                                                                                     |

| 7/6/2024 localizedAttributes                 | localized properties   | Content-Language header   | Result                                                                                                  | Example Payload                                                                                                                     |
|----------------------------------------------|------------------------|---------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| provided                                     | provided               | not provided              | Merges the results of localizedAttributes and localizedProperties; localizedAttributes takes precedence | { "code": "clothing", "name": "Clothing Category 1", "localizedAttributes": [{ "language": "en", "name": "Clothing Category 2" }] } |
| provided                                     | not provided           | provided                  | Stores all localizedAttributes                                                                          | { "code": "clothing", "localizedAttributes": [{ "language": "en", "name": "Clothing Category 2" }] }                                |
| Content-Language and Accept-Language Headers |                        |                           |                                                                                                         |                                                                                                                                     |

Depending on how you provide the values for the Content-Language and Accept-Language headers, the system saves and returns integration Object item attributes as shown in the following table. The table uses the English (en) and German (de) values as examples.

| Scenario                           | Content-Language            | Accept-Language             | Language used to persist   | Language used to retrieve persisted item   |
|------------------------------------|-----------------------------|-----------------------------|----------------------------|--------------------------------------------|
| Valid Content-Language and AcceptLanguage headers                                    | en                          | de                          | en                         | de                                         |
| Valid Content-Language header only | en                          | en                          | en                         |                                            |
| No language header provided        | platform's default language | platform's default language |                            |                                            |
| Valid Accept-Language header only  | de                          | platform's default language | de                         |                                            |

If the Content-Language or Accept-Language header value does not exist in the platform, the system does not persist the item and returns a 400-Bad Request error similar to the following. In the example error response, en is the platform default language and invalidLanguageTagFromLanguageHeader is the invalid language provided in the Content-Language or Accept-Language header.

{ "error": { "code": "invalid_language", "message": { "lang": "en", "value": "The language provided [invalidLanguageTagFromLanguageHeader] is not available." } } }

## The Patch Api

Update the attributes of an existing Integration Object using a PATCH request. All Integration Objects have a PATCH endpoint for updating attribute values. The PATCH operation is a partial update that replaces only the attributes values delivered in the payload, with the caveats listed in the PATCH API Constraints section of this topic. This functionality is in contrast to the POST request, which creates a new Integration Object in the Integration API. You can only update one Integration Object per PATCH request. If you do not include existing Integration Object attributes in the payload of a PATCH request, the values for the omitted attributes remain unchanged.

Like the POST request, the PATCH API supports the Content-Language command, as well as the localizedAttributes NavigationProperty, to update attributes for an Integration Object Item in multiple languages. See the Related Link at the end of this topic for more information about localized properties. To make a successful PATCH request:
Be a member of the integrationadmingroup or integrationcreategroup. Include an integration key for the Integration Object in the request URL. For example, PATCH https://localhost:9002/odata2webservices/InboundProduct/Products('Staged|Default|123')
A successful request returns a 200 response code with the updated payload. Inbound Monitoring captures a record of the PATCH request.

PATCH API Constraints Keep the following considerations in mind when performing PATCH updates.

While the service veries that any part of the integration key you provide in the Integration Object payload matches the integration key in the request URL, you cannot change an integration key using a request. You can only update one item at a time.

It is not possible to use query lters with a PATCH request. If a PATCH request includes fewer values than currently exist for an attribute, the service deletes the existing values and persists only the values provided in the PATCH request body. For example, if Mike Smith has three email addresses in the system, the following request sent by an administrator deletes all three addresses and persists only mike@charity.org.

PATCH https://localhost:9002/odata2webservices/InboundCustomer/Customers('Administrator%7Cadmin') { "description": "It's Mike Smith.", "addresses": [{ "firstname": "Mike", "lastname": "Smith", "email": "mike@charity.org" }] }
Localized elds also update to include only the values present in the PATCH request. For example, if a eld has existing en and fr language values, but the PATCH body contains only the values de and es, the attribute updates to include only de and es values. For more information, see the Related Links section of this topic. You can set collections to an empty collection, but you cannot set a collection to null. While you can replace complex types using a PATCH request, you cannot set them to null. You can set primitive types to null.

You cannot patch inbound and outbound monitoring records.

## Localization For Patch Requests

Update attributes for an Integration Object in multiple languages.

Like the POST request, the PATCH API supports the Content-Language command, as well as the localizedAttributes NavigationProperty, to update attributes for an Integration Object Item in multiple languages. See the Related Link at the end of this topic for more information about localized properties. Depending on whether you provide the values for the Content-Language and header and whether the PATCH request contains all or some of the localization values, the system persists the provided values using the logic shown in the following table. To remove a localized language or attribute, either provide the Content-Language header or localized attributes in the payload. If you provide both within a request, localized attributes take precedence over the Content-Language header value and localized properties. Except where otherwise specied in the table, the example payload and results assume the existence of the following localized attributes in the system before making a PATCH request:
code: clothing name [EN]: this item name [ES]: este producto description [EN]: product original description description [ES]: descripción original del producto

| Content-Language header                                                                                                                                | Example Payload                                                                                                                                                | Result                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| not provided                                                                                                                                           | Nulls the name property for all languages:                                                                                                                     |                                                                                                                |
| { "code": "clothing", "name": null                                                                                                                     | code: clothing name [EN]: null                                                                                                                                 |                                                                                                                |
| }                                                                                                                                                      | name [ES]: null description [EN]: product original description description [ES]: descripción original del producto                                             |                                                                                                                |
| es                                                                                                                                                     | Replaces the name property only for the specied Content-Language:                                                                                              |                                                                                                                |
| { "code": "clothing", "name": "nuevo nombre"                                                                                                           | code: clothing name [EN]: this item                                                                                                                            |                                                                                                                |
| }                                                                                                                                                      | name [ES]: nuevo nombre                                                                                                                                        |                                                                                                                |
| es                                                                                                                                                     | Existing values:                                                                                                                                               | Replaces only the value for the localized attribute provided in the payload, for the specied content language: |
| code: clothing name [EN]: this item name [ES]: null description [EN]: product original description description [ES]: descripción original del producto | code: clothing name [EN]: this item name [ES]: nuevo nombre description [EN]: product original description description [ES]: descripción original del producto |                                                                                                                |
| Payload: { "code": "clothing", "name": "nuevo nombre" }                                                                                                |                                                                                                                                                                |                                                                                                                |
| provided or not provided                                                                                                                               | In this case, the localized attributes take precedence, replacing all localized data to the localizedAttributes provided in the payload:                       |                                                                                                                |
| { "code": "clothing", "name": "nuevo nombre", "localizedAttributes": [{ "language": "es", "name": "Nuevo Nombre en español" }] }                       | code: clothing name [EN]: null name [ES]: Nuevo Nombre en español description [EN]: null description [ES]: null                                                |                                                                                                                |
| This is custom documentation. For more information, please visit the SAP Help Portal                                                                   | 81                                                                                                                                                             |                                                                                                                |

| 7/6/2024 Content-Language header                                                                                                                                                                 | Example Payload                                                                                                                                                  | Result   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| not provided                                                                                                                                                                                     | Empty value replaces all localized attributes to null:                                                                                                           |          |
| { "code": "clothing",                                                                                                                                                                            | code: clothing                                                                                                                                                   |          |
| "localizedAttributes": []                                                                                                                                                                        |                                                                                                                                                                  |          |
| }                                                                                                                                                                                                | name [EN]: null name [ES]: null description [EN]: null description [ES]: null                                                                                    |          |
| provided or not provided                                                                                                                                                                         | Because Olingo does not support resetting localizedAttributes, this request preserves the existing data:                                                         |          |
| { "code": "clothing", "localizedAttributes": null }                                                                                                                                              | code: clothing name [EN]: this item name [ES]: este producto description [EN]: product original description description [ES]: descripción original del producto  |          |
| es                                                                                                                                                                                               | Replaces all localized attributes for the provided Content-Language (es), without affecting the other, existing languages:                                       |          |
| { "code": "clothing", "localizedAttributes": [] }                                                                                                                                                | code: clothing name [EN]: this item name [ES]: null description [EN]: product original description description [ES]: null                                        |          |
| provided or not provided                                                                                                                                                                         | Replaces all localized attributes to the values provided in localizedAttributes in the payload:                                                                  |          |
| { "code": "clothing", "description": "nueva descripción" "localizedAttributes": [ { "language": "es", "name": "Nuevo Nombre en español" } , { "language": "en", "name": "new english name" } ] } | code: clothing name [EN]: new english name name [ES]: Nuevo Nombre en español description [EN]: product original description description [ES]: nueva descripción |          |
| Related Information Localization for POST requests Map Attributes                                                                                                                                |                                                                                                                                                                  |          |

## Map Attributes For Patch

The Integration API's PATCH API handles required and optional map type attributes similarly to collection attributes. PATCH requests replace existing map attribute values when the payload provides new values. Further, if you include an existing atribute without providing values, the API deletes the values. For example, assume you have a ConsumedDestination has an additionalProperties map attribute with the existing values key1=value 1, key2=value 2. Including the following payload in a PATCH request replaces the two existing key1 and key2 values with one value, key3=value 3.

 "additionalProperties": [ { "key": "key3", "value": "value 3" } ]
To replace existing values with new values in a PATCH request, you must include the existing attribute in the payload with a non-null value. If you do not include an existing attribute in a payload, the API retains the existing values. For example, the following payload retains the original, existing values of key1=value 1, key2=value 2 for the additionalProperties attribute and creates the new value for someOtherProperty.

 "someOtherProperty": [ { "key": "key3", "value": "value 3" } ]
Additionally, a null value for the attribute itself, as shown in "additionalProperties": null, preserves any existing values. Setting the map attribute to an empty collection, for example, "additionalProperties": [], resets the previous attribute value to an empty Map. Key property in the payload You must provide a key property that is equal to a non-null value for any map attribute you include in a payload. When a payload includes a map attribute with a missing key property or a key property set to null, the API returns a 400 Bad Request error. A value property can be missing or null, but is treated according to the rules previously described in this topic.

Using the OData2 GET API with Dened Integration Objects The odata2webservices extension supports part of the OData2 GET API. If an item is part of SAP Commerce Cloud, it is possible to get OData2 representation through this API.

Getting a Single Entity using a Dened Integration Object You can retrieve a single entity via a dened Integration Object using the integrationKey.

Getting Multiple Entities using Dened Integration Objects Retrieve multiple entities using dened Integration Objects in one request using one or more query options. Query Options Use query options in your GET requests to lter results and specify the format and range of returned items. Getting an Attribute from an Integration Object Retrieve an attribute for an Integration Object. Map and Collection Attributes for GET
The odata2webservices extensions allow you to access collection or map attributes.

Localization for GET requests During the GET operation, you can retrieve localized categories and Integration Object Items. GET for Virtual Attributes When retrieving an Integration Object Item (IOI), you can see any dened virtual attributes along with the IOI.

## Getting A Single Entity Using A Dened Integration Object

You can retrieve a single entity via a dened Integration Object using the integrationKey. You can also retrieve localized attributes of a single Integration Object. The $expand query option allows you to retrieve multiple levels of expanded navigation properties.

Getting a Single Entity Provide an integration key to retrieve a single item. For example, the following URL retrieves a Product item from the MyProduct service using the integration key Staged|Default|myproduct.

https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Cmyproduct')
The GET response contains the data for simple properties and deferred links for navigation properties. The deferred links prevent an overly large response and allow you to get the data for the navigation properties separately. To see the navigation property data inline, use the $expand query parameter in the GET request. For more information about the $expand parameter, see Expand.

If there are localized attributes specied in the Integration Object Item Attributes, all the localized values for those attributes are available under the localizedAttributes navigation property in the response. You can use the deferred link to get the localized attributes. For example:
https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Cmyproduct')/localizedAttributes)
Alternatively, you can get localized attributes inline in the response using the $expand=localizedAttributes expression in the GET request. For example, the following request returns the localized attributes inline:
https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Cmyproduct')?$expand=localizedAttributes)
 Note Because localizedAttributes is a reserved property name, do not use it in an Integration Object Item Attribute denition.

For information on getting the localized attributes of a Product, see Localization for GET requests.

Getting Multiple Entities using Dened Integration Objects Retrieve multiple entities using dened Integration Objects in one request using one or more query options. To get multiple entities, send a GET request to a URL that species a collection of objects, such as:
https://localhost:9002/odata2webservices/MyProduct/Products For more information on the query options you can use with a GET request for multiple entities, see Query Options.

## Query Options

Use query options in your GET requests to lter results and specify the format and range of returned items.

You can retrieve multiple integration items using one or more of the query options, $filter, $top, $skip, $inlinecount, $count, and $expand. The $expand option also supports GET
requests for single Integration Objects. Each option described in the following sections adheres to the OData specication. For more information and for further examples, see the OData2 documentation .

Query Option Defaults This is   For more    the SAP Help  83 The following defaults apply to the OData2 GET API.

For security reasons, the max value for the $top parameter (page size) is 1000. When $top and $skip are not provided, the default behavior returns a page size of 10.

Although the default values for $top and $skip are dened as system properties, a system administrator can modify them. The property names are:
odata2services.page.size.max=1000 odata2services.page.size.default=10 If you specify a $top value that exceeds the dened default max value, the system returns the default max page size with a link to the next page in the response. For example, if the max page size is set to 5, a response to the following request returns only ve results, but includes a link to the next page:
https://localhost:9002/odata2webservices/InboundProduct/Products?$top=45 See the link to the next page at the bottom of the response:
 { "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct001%257Cwith%257Cpipes')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct001%257Cwith%257Cpipes')" "type": "HybrisCommerceOData.Product" }, "code": "testProduct001|with|pipes", "name": "product name 1", "integrationKey": "Staged|Default|testProduct001%7Cwith%7Cpipes", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct001%257Cwith%257Cpipe } }, "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct001%257Cwith%257Cpipe } } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct002%257Cwith%257Cpipes')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct002%257Cwith%257Cpipes')" "type": "HybrisCommerceOData.Product" }, "code": "testProduct002|with|pipes", "name": "product name 2", "integrationKey": "Staged|Default|testProduct002%7Cwith%7Cpipes", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct002%257Cwith%257Cpipe } }, "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct002%257Cwith%257Cpipe } } }, {
 "__metadata": {
 "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct003%257Cwith%257Cpipes')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct003%257Cwith%257Cpipes')" "type": "HybrisCommerceOData.Product" }, "code": "testProduct003|with|pipes", "name": "product name 3", "integrationKey": "Staged|Default|testProduct003%7Cwith%7Cpipes", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct003%257Cwith%257Cpipe } }, "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct003%257Cwith%257Cpipe } } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct004%257Cwith%257Cpipes')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct004%257Cwith%257Cpipes')" "type": "HybrisCommerceOData.Product" }, "code": "testProduct004|with|pipes", "name": "product name 4", "integrationKey": "Staged|Default|testProduct004%7Cwith%7Cpipes", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct004%257Cwith%257Cpipe } }, "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct004%257Cwith%257Cpipe } } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct005%257Cwith%257Cpipes')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct005%257Cwith%257Cpipes')"
This is   For more    the SAP Help  84
 "type": "HybrisCommerceOData.Product"
 }, "code": "testProduct005|with|pipes", "name": "product name 5", "integrationKey": "Staged|Default|testProduct005%7Cwith%7Cpipes", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct005%257Cwith%257Cpipe } }, "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7CtestProduct005%257Cwith%257Cpipe }
 }
 } ], "__next": "https://localhost:9002/odata2webservices/InboundProduct/Products?$top=45&$skiptoken=5" } }
Filter Use the $filter query option with a collection endpoint to retrieve a specied subset of collection entries.

Top and Skip The query options $top and $skip allow you to specify the number of entries to return, or to specify a subset of a collection to return. Count and Inline Count Use $count to indicate the number of entries to return, or $inlinecount to set the number of entries returned from a specied collection. Expand Use $expand to retrieve entries associated with a single integration object, or for a Collection of entries.

Order By The $orderby lter allows you to set the order of the results you get from the Integration API.

## Filter

Use the $filter query option with a collection endpoint to retrieve a specied subset of collection entries.

 Note Only Logical Operators are supported.

The $filter query supports the following logical operators:
eq (equals) gt (greater than) lt (less than) ge (greater than or equals) le (less than or equals) ne (not equal) and (logical and) or (logical or)
 Note When using special characters or decimals in a $filter query:
URL-encode any special characters in the $filter expression. For example, use code eq '%5B1000005%5D' to lter on code eq '[1000005]'. Add M after any decimal value. For example, 4.1M. For more information about this requirement, see the Primitive Data Types specication in the OData2 documentation .

Unsupported **$filter** option attributes The $filter query option supports all Integration Object attributes with the following exceptions.

Because integrationKey is unique for each item type, ltering on the topmost level by integrationKey returns a single item. Instead of using the $filter option to get this single item, you can use the following request:
https://localhost:9002/odata2webservices/InboundProduct/Products('prod1|Staged|Default')
For localized attributes, the $filter query option only supports the platform's installation language. Attributes more than one level deep are not supported. For example, $filter=catalogVersion/version eq 'Online' is a valid lter, but $filter=catalogVersion/catalog/id eq 'Default' is not.

The following examples show how to lter by various attributes and properties using the supported operators. For more information about localization for GET requests, see Localization for GET requests. Filter by a simple attribute https://localhost:9002/odata2webservices/InboundProduct/Products?$filter=code eq 'prod1' This is   For more    the SAP Help  85 Filter by the navigation property's **integrationKey**
https://localhost:9002/odata2webservices/InboundProduct/Products?$filter=catalogVersion/integrationKey ne 'Staged|Default' Filter by the localized attribute **name**
https://localhost:9002/odata2webservices/InboundProduct/Products?$filter=name eq 'english product name' Filter the localized attribute **name** to those not including the 'english product **name'**
https://localhost:9002/odata2webservices/InboundProduct/Products?$filter=name ne 'english product name' Filter by multiple predicates https://localhost:9002/odata2webservices/InboundProduct/Products?$filter=code eq 'prod1' or catalogVersion/integrationKey eq 'Staged|Default' Filter by the **price** attribute with values greater than 8 and less than 9 https://localhost:9002/odata2webservices/InboundPriceRow/PriceRows?$filter=price gt 8m and price le 9m The following example shows the expected date time format for a GET request to the Integration API.

https://localhost:9002/odata2webservices/InboundProduct/Products?$filter=modifiedTime lt DateTime'2012-05-29T09:13:28'

## Top And Skip

The query options $top and $skip allow you to specify the number of entries to return, or to specify a subset of a collection to return.

$top Use the $top query option to specify the total number of entries to return for each page of results. The value for $top must be an integer greater than or equal to 0 (zero). If the specied value is less than 0, the URI is considered malformed and the request results in an error.

The query parameter $orderby is not supported, so the data service must return a fully ordered Collection.

For example, the following request returns the rst two Product entries for the specied service.

https://localhost:9002/odata2webservices/InboundProduct/Products?$top=2 The system returns a response with a link to the next page that you can use to view additional retrieved items.

{ "d": { "results": [ { "__metadata": {
 "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')",
 "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')", "type": "HybrisCommerceOData.Product" }, "code": "test_article1", "name": "test_article1", "integrationKey": "Staged|Default|test_article1", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')/catalogVersion" } }, "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')/unit" } } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article2')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article2')", "type": "HybrisCommerceOData.Product" }, "code": "test_article2", "name": "test_article2", "integrationKey": "Staged|Default|test_article2", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article2')/catalogVersion" } }, "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article2')/unit" } } } ], "__next": "https://localhost:9002/odata2webservices/InboundProduct/Products?$top=2&$skiptoken=2" } }
This is   For more    the SAP Help  86

$skip Use the $skip query option to retrieve a subset of the collection, starting at the element after the value specied. The value of $skip must be an integer greater than or equal to 0 (zero). If the value specied is less than 0, the URI is considered malformed and the request results in an error.

The query parameter $orderby is not supported, so the data service must return a fully ordered Collection.

For example, the following request returns products starting with the third product listed. The data service denes the order of the product list. The default page size determines the number of items returned. See the Query Option Defaults section of this topic.

https://localhost:9002/odata2webservices/InboundProduct/Products?$skip=2 The request returns the following response:
 { "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article3')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article3')", "type": "HybrisCommerceOData.Product" }, "code": "test_article3", "name": "test_article3", "integrationKey": "Staged|Default|test_article3", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article3')/catalogVersion" } }, "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article3')/unit" } } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article4')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article4')", "type": "HybrisCommerceOData.Product" }, "code": "test_article4", "name": "test_article4", "integrationKey": "Staged|Default|test_article4", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article4')/catalogVersion" } }, "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article4')/unit" } } } ], "__next": "https://localhost:9002/odata2webservices/InboundProduct/Products?$skiptoken=4" } }
Pagination using $top and $skip Using the $top and $skip options together, you can specify the number of entries to return for each page in a list of paginated results that starts at the element after the value set for $skip. For example, to view page 3 of the results with 10 results per page, use the parameters $top=10, $skip=20. The system returns items 21 through 30. If you do not provide either or both of the $top and $skip values, the system uses the default values, described in the Query Option Defaults section of this topic. The following request uses $skip and $top to paginate a collection of Product Entries that the service returns, starting after the fourth item.

https://localhost:9002/odata2webservices/InboundProduct/Products?$top=2&$skip=4 The response returns two Products, starting with the fth item, from the ordered collection of Entries that the service returns, as shown.

 { "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article5')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article5')", "type": "HybrisCommerceOData.Product" }, "code": "test_article5", "name": "test_article5", "integrationKey": "Staged|Default|test_article5", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article5')/catalogVersion" } }, "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article5')/unit" } } }, { "__metadata": {
This is   For more    the SAP Help  87

 "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article6')",
 "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article6')", "type": "HybrisCommerceOData.Product" }, "code": "test_article6", "name": "test_article6", "integrationKey": "Staged|Default|test_article6", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article6')/catalogVersion" } }, "unit": { "__deferred": {
 "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article6')/unit"
 } } } ] } }
Count and Inline Count Use $count to indicate the number of entries to return, or $inlinecount to set the number of entries returned from a specied collection.

$count Provide $count to return the total number of entries of the specied type that exist in the system.

The following request asks for the total number of inbound products.

https://localhost:9002/odata2webservices/InboundProduct/Products/$count The request returns the response 6.

$inlinecount Use the $inlinecount query option to specify the number of Entries to return from the collection specied by the resource path of the URI. Only the following values are valid:
allpages returns a count of the number of entities in the collection. none returns a response without a count. Using none is the same as sending a request without the $inlineCount query parameter.

The following request uses the $inlinecount query parameter to return the count of the total number of records along with the set of products being returned.

https://localhost:9002/odata2webservices/InboundProduct/Products?$top=2&$skip=4&$inlinecount=allpages In the response, the value of inline count appears in the line "__count": "6", as shown.

 {
 "d": {
 "__count": "6", "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article5')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article5')", "type": "HybrisCommerceOData.Product" }, "code": "test_article5", "name": "test_article5", "integrationKey": "Staged|Default|test_article5", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article5')/catalogVersion" } }, "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article5')/unit" } } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article6')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article6')", "type": "HybrisCommerceOData.Product" }, "code": "test_article6", "name": "test_article6", "integrationKey": "Staged|Default|test_article6", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article6')/catalogVersion" } }, "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article6')/unit" } } } ]
This is   For more    the SAP Help  88 Expand Use $expand to retrieve entries associated with a single integration object, or for a Collection of entries.

 }
}
Retrieve a single integration object To retrieve entries associated with a single integration object, with the unit navigation property expanded, make the following request.

https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')?$expand=unit The response shows the expanded unit navigation property for the integration item.

{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')", "type": "HybrisCommerceOData.Product" }, "name": null, "code": "test_article1", "integrationKey": "Staged|Default|test_article1", "unit": { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Units('pieces')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Units('pieces')", "type": "HybrisCommerceOData.Unit" }, "unitType": "pieces", "code": "pieces", "name": "Piece", "integrationKey": "pieces" }, "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')/catalogVersion" } } } }
Retrieve a collection of entries To obtain a collection of entries using a single URI with, for example, an expanded unit navigation property, use the $expand option in your request as shown.

https://localhost:9002/odata2webservices/InboundProduct/Products?$top=1&$expand=unit In the response, the value for the unit navigation property is inlined, or expanded, for the collection of entries.

{ "d": { "results": [
 {
 "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')", "type": "HybrisCommerceOData.Product" }, "name": "test_article1", "code": "test_article1", "integrationKey": "Staged|Default|test_article1", "unit": { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Units('pieces')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Units('pieces')", "type": "HybrisCommerceOData.Unit" }, "unitType": "pieces", "code": "pieces", "name": "Piece", "integrationKey": "pieces" }, "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')/catalogVersion" } } } ], "__next": "https://localhost:9002/odata2webservices/InboundProduct/Products?$top=1&$expand=catalogVersion/catalog&$skiptoken=1" } }
Retrieve an integration object with expanded or nested navigation properties The $expand option also allows you to expand more than one navigation property as well as nested navigation properties.

To expand multiple navigation properties, separate properties in your request using a comma, as shown in this GET request.

https://localhost:9002/odata2webservices/InboundProduct/Products?$top=1&$expand=unit,catalogVersion This is   For more    the SAP Help  89 A successful response returns the following.

{ "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')", "type": "HybrisCommerceOData.Product" }, "name": "test_article1", "code": "test_article1",
 "integrationKey": "Staged|Default|test_article1",
 "unit": { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Units('pieces')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Units('pieces')", "type": "HybrisCommerceOData.Unit" }, "unitType": "pieces", "code": "pieces", "name": "Piece", "integrationKey": "pieces" }, "catalogVersion": { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/CatalogVersions('Staged%7CDefault')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/CatalogVersions('Staged%7CDefault')", "type": "HybrisCommerceOData.CatalogVersion" }, "version": "Staged", "active": false, "integrationKey": "Staged|Default", "catalog": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/CatalogVersions('Staged%7CDefault')/catalog" } } } } ], "__next": "https://localhost:9002/odata2webservices/InboundProduct/Products?$top=1&$expand=catalogVersion/catalog&$skiptoken=1" } }
To expand nested navigation properties, identify the path in the request, as shown in the following GET request.

https://localhost:9002/odata2webservices/InboundProduct/Products?$top=1&$expand=catalogVersion/catalog A successful response returns the nested properties, as shown in this example.

{ "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')", "type": "HybrisCommerceOData.Product" }, "name": "test_article1", "code": "test_article1", "integrationKey": "Staged|Default|test_article1", "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7Ctest_article1')/unit" } }, "catalogVersion": { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/CatalogVersions('Staged%7CDefault')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/CatalogVersions('Staged%7CDefault')", "type": "HybrisCommerceOData.CatalogVersion" }, "version": "Staged", "active": false, "integrationKey": "Staged|Default", "catalog": { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundProduct/Catalogs('Default')", "uri": "https://localhost:9002/odata2webservices/InboundProduct/Catalogs('Default')", "type": "HybrisCommerceOData.Catalog" }, "id": "Default", "integrationKey": "Default" } } } ], "__next": "https://localhost:9002/odata2webservices/InboundProduct/Products?$top=1&$expand=catalogVersion/catalog&$skiptoken=1" } }

## Order By

The $orderby lter allows you to set the order of the results you get from the Integration API. You can order results by one or more attributes in ascending or descending order. If you do not specify a direction for a eld, results return in ascending order. The $orderby lter supports only "at" ordering, meaning you can only sort on the immediate attributes of the Integration Object type you are retrieving. For example, when you retrieve Products, you can only order results by attributes of Product.

 Note The API does not support ordering by:
integrationKey - A request to order by integration key returns the error message order_by_integration_key_not_supported nested properties (properties of navigation properties) - A request to order by nested attribute returns the error message order_by_nested_attribute_not_supported Sort in Ascending Order To sort in ascending order, use asc or provide no directional sorting indicator, as shown. Both requests return the same response.

https://localhost:9002/odata2webservices/OutboundProduct/Products?$orderby=code asc https://localhost:9002/odata2webservices/OutboundProduct/Products?$orderby=code Sort in Descending Order To sort in descending order, use desc as shown.

https://localhost:9002/odata2webservices/OutboundProduct/Products?$orderby=code desc Order by Multiple Fields To order results by multiple elds, use a comma to separate the attributes. The following example request orders results by name in descending order, and, within results with the same name, by code in ascending order.

https://localhost:9002/odata2webservices/OutboundProduct/Products?$orderby=name desc, code asc Order by Navigation Property When you sort results by a navigation property, the response orders results by the primary key of the navigation property. For example, the following response orders the results by the primary key of catalogVersion.

https://localhost:9002/odata2webservices/OutboundProduct/Products?$orderby=catalogVersion desc Order by Localized Property The API also supports ordering by localized properties and determines which localized language to use by the following order of priority.

1. The rst language in the Accept-Language header attribute. If there is no value or a wildcard value (*), the API applies the next criterion of priority.

2. The language specied in SAP Commerce Cloud. 3. The default language, English.

The following example sorts the responses by the localized property name.

https://localhost:9002/odata2webservices/OutboundProduct/Products?$orderby=name

## Getting An Attribute From An Integration Object

Retrieve an attribute for an Integration Object.

You can retrieve information about an attribute using a GET request. This example uses the catalogVersion attribute to nd catalogVersion attribute information from the URL https://electronics.local:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7C1000003')/catalogVersion.

GET https://electronics.local:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7C1000003')/catalogVersion {
"d": {
"__metadata": {
"id": "https://electronics.local:9002/odata2webservices/InboundProduct/CatalogVersions('Staged%7CDefault')", "uri": "https://electronics.local:9002/odata2webservices/InboundProduct/CatalogVersions('Staged%7CDefault')", "type": "HybrisCommerceOData.CatalogVersion"
} "version": "Staged", "active": true, "integrationKey": "Staged|Default", "catalog": {
"__deferred": {
"uri": "https://electronics.local:9002/odata2webservices/InboundProduct/CatalogVersions('Staged%7CDefault')/catalog"
}
}
}
}
Map and Collection Attributes for GET
The odata2webservices extensions allow you to access collection or map attributes.

The Integration API handles map and collection attributes in the same way. When you run a GET request for an IO with map attributes, the response includes all available map entries. The following examples pertain to both types.

This is   For more    the SAP Help  91 Preparing a Product for Demonstration Create some categories and assign them all to a Product.

POST https://electronics.local:9002/odata2webservices/InboundProduct/Categories
{
"@odata.context": "$metadata\#Categories/$entity", "code": "category1", "name": "the name in english1"
}
POST https://electronics.local:9002/odata2webservices/InboundProduct/Categories
{
"@odata.context": "$metadata\#Categories/$entity", "code": "category2", "name": "the name in english2"
}
POST https://electronics.local:9002/odata2webservices/InboundProduct/Categories
{
"@odata.context": "$metadata\#Categories/$entity", "code": "category3", "name": "the name in english3"
}
POST https://electronics.local:9002/odata2webservices/InboundProduct/Products
{
"@odata.context": "$metadata\#Products/$entity", "code": "1000003", "catalogVersion": {
"version": "Staged",
catalog": {
"id": "Default"
}
},
"supercategories": [ { "code" : "category1" }, { "code" : "category2" }, { "code" : "category3" } ]
}
Accessing Attributes that are Collections The process is similar to accessing other attributes that are Integration Objects by themselves:
GET https://electronics.local:9002/odata2webservices/InboundProduct/Products('Staged%7CDefault%7C1000003')/supercategories
{
"d": {
"results": [
{
"__metadata": {
"id": "https://electronics.local:9002/odata2webservices/InboundProduct/Categories('category1')", "uri": "https://electronics.local:9002/odata2webservices/InboundProduct/Categories('category1')", "type": "HybrisCommerceOData.Category"
}, "code": "category1", "name": "the name in english", "integrationKey": "category1"
} {
"__metadata": {
"id": "https://electronics.local:9002/odata2webservices/InboundProduct/Categories('category2')", "uri": "https://electronics.local:9002/odata2webservices/InboundProduct/Categories('category2')", "type": "HybrisCommerceOData.Category"
}, "code": "category2", "name": "the name in english2", "integrationKey": "category2"
}, {
"__metadata": {
"id": "https://electronics.local:9002/odata2webservices/InboundProduct/Categories('category3')", "uri": "https://electronics.local:9002/odata2webservices/InboundProduct/Categories('category3')", "type": "HybrisCommerceOData.Category"
}, "code": "category3", "name": "the name in english3",
This is   For more    the SAP Help  92

## Localization For Get Requests

During the GET operation, you can retrieve localized categories and Integration Object Items.

The Accept-Language Header The GET API honors the Accept-Language header. If you do not include the header in your request, the response includes the requested item in the platform default language only. The following examples describe how to get s single category with localized data, a collection with localized data, and all localized data for an integration object in one request.

Getting a Single Product with Expanded Localized Attributes GET https://{{host}}/odata2webservices/MyProduct/Products('Staged|Default|product2')?$expand=localizedAttributes Accept-Language: de
{ "d": { "__metadata": { "id": "https://api.cxmbk-stoutsub3-p2-public.model-t.myhybris.cloud:443/odata2webservices/MyProduct/Products('Staged%7CDefault%7Cproduct2 "uri": "https://api.cxmbk-stoutsub3-p2-public.model-t.myhybris.cloud:443/odata2webservices/MyProduct/Products('Staged%7CDefault%7Cproduct "type": "HybrisCommerceOData.Product" }, "name": "Remote Control", "description": "<p>An electronic device used to operate the device from a distance</p>", "code": "product2", "integrationKey": "Staged|Default|product2", "supercategories": { "__deferred": { "uri": "https://api.cxmbk-stoutsub3-p2-public.model-t.myhybris.cloud:443/odata2webservices/MyProduct/Products('Staged%7CDefault%7Cpro } }, "catalogVersion": { "__deferred": { "uri": "https://api.cxmbk-stoutsub3-p2-public.model-t.myhybris.cloud:443/odata2webservices/MyProduct/Products('Staged%7CDefault%7Cpro } }, "localizedAttributes": { "results": [ { "__metadata": { "id": "https://api.cxmbk-stoutsub3-p2-public.model-t.myhybris.cloud:443/odata2webservices/MyProduct/Localized___Products('de' "uri": "https://api.cxmbk-stoutsub3-p2-public.model-t.myhybris.cloud:443/odata2webservices/MyProduct/Localized___Products('de "type": "HybrisCommerceOData.Localized___Product" }, "description": "<p>&nbsp;</p>\n<p>Ein elektronisches Ger&auml;t, das zur Fernsteuerung des Ger&auml;ts verwendet wird</p>", "name": " Fernbedienung", "language": "de" }, { "__metadata": { "id": "https://api.cxmbk-stoutsub3-p2-public.model-t.myhybris.cloud:443/odata2webservices/MyProduct/Localized___Products('en' "uri": "https://api.cxmbk-stoutsub3-p2-public.model-t.myhybris.cloud:443/odata2webservices/MyProduct/Localized___Products('en "type": "HybrisCommerceOData.Localized___Product" }, "description": "<p>An electronic device used to operate the device from a distance</p>", "name": "Remote Control", "language": "en" } ] } } }
Getting Multiple Products GET https://{{host}}/odata2webservices/MyProduct/Products?$expand=localizedAttributes Accept-Language: de
{ "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Cproduct2')", "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Cproduct2')", "type": "HybrisCommerceOData.Product" }, "code": "product2", "name": "German Name", "description": "German Description", "integrationKey": "Staged|Default|product2", "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Cproduct2')/unit" } }, "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Cproduct2')/catalogVersion" }
This is   For more    the SAP Help  93

 },
 "supercategories": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Cproduct2')/supercategories" } }, "localizedAttributes": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('de')", "uri": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('de')", "type": "HybrisCommerceOData.Localized___Product" },
 "description": "German Description",
 "name": "German Name", "language": "de" }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('en')", "uri": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('en')", "type": "HybrisCommerceOData.Localized___Product" }, "description": "English Description", "name": "P2NAME", "language": "en" } ] } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_2')", "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_2')", "type": "HybrisCommerceOData.Product" }, "code": "test_product_2", "name": "the German name", "description": null, "integrationKey": "Staged|Default|test_product_2", "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_2')/unit" } }, "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_2')/catalogVersion" } }, "supercategories": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_2')/supercategories" } }, "localizedAttributes": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('de')", "uri": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('de')", "type": "HybrisCommerceOData.Localized___Product" }, "name": "the German name", "language": "de" }, { "__metadata": {
 "id": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('en')",
 "uri": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('en')", "type": "HybrisCommerceOData.Localized___Product" }, "name": "the English name", "language": "en" } ] } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_3')", "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_3')", "type": "HybrisCommerceOData.Product" }, "code": "test_product_3", "name": "the name [DE]", "description": null, "integrationKey": "Staged|Default|test_product_3", "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_3')/unit" } }, "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_3')/catalogVersion" } }, "supercategories": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_3')/supercategories" } }, "localizedAttributes": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('de')", "uri": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('de')", "type": "HybrisCommerceOData.Localized___Product" },
This is   For more    the SAP Help  94
 "name": "the name [DE]",

![94_image_0.png](94_image_0.png)

 "language": "de" }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('en')", "uri": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('en')", "type": "HybrisCommerceOData.Localized___Product" }, "name": "the name [EN]", "language": "en" } ] }
 },
 { "__metadata": { "id": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_4')", "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_4')", "type": "HybrisCommerceOData.Product" }, "code": "test_product_4", "name": "the name [DE]", "description": null, "integrationKey": "Staged|Default|test_product_4", "unit": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_4')/unit" } }, "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_4')/catalogVersion" } }, "supercategories": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/MyProduct/Products('Staged%7CDefault%7Ctest_product_4')/supercategories" } }, "localizedAttributes": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('de')", "uri": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('de')", "type": "HybrisCommerceOData.Localized___Product" }, "name": "the name [DE]", "language": "de" }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('en')", "uri": "https://localhost:9002/odata2webservices/MyProduct/Localized___Products('en')", "type": "HybrisCommerceOData.Localized___Product" }, "name": "the name [EN]", "language": "en" } ] } } ] } }
Getting All Localized Data in One Request To get all localized data for an Integration Object, use the $expand query option in your request. If you do not provide the Accept-Language header when using the $expand option for localized attibutes, the response provides the item in the default platform language. The following example shows a GET request for a product with values in multiple locales.

GET https://{{host}}/odata2webservices/MyProduct/Products?$expand=localizedAttributes Accept-Language: en The request returns the payload with an array for each available language.

{ "code": "MyProduct", "name": "My Product", "description": "This is the English description", "integrationKey": "Staged|Default|MyProduct", "catalogVersion": { "version": "Staged", "integrationKey": "Staged|Default", "catalog": { "id": "Default", "integrationKey": "Default", "name": "My Catalog", "localizedAttributes": [ { "language": "en", "name": "My Catalog" } ] }
 },
 "localizedAttributes": [ { "language": "en", "name": "My Product", "description": "This is the English description" }, { "language": "fr", "name": "Mon Produit",
 "description": "C'est la description française" 
 }, { "language": "de", "name": "Mein Produkt", "description": "" }, { "language": "es", "name": "Mi producto" } ] }
Getting Information about a Locale that Does Not Have Any Information When trying to GET information about a certain Locale that does not have any information, the system returns a null value.

GET https://{{host}}/odata2webservices/MyProduct/Categories('category1') Accept-Language: de
{
"d": {
"__metadata": {
"id": "https://electronics.local:9002/odata2webservices/MyProduct/Categories('category1')", "uri": "https://electronics.local:9002/odata2webservices/MyProduct/Categories('category1')", "type": "HybrisCommerceOData.Category"
}, "code": "category1", "name": null, "integrationKey": "category1"
}
}

## Get For Virtual Attributes

When retrieving an Integration Object Item (IOI), you can see any dened virtual attributes along with the IOI. The following example:
Creates an Integration Object (VirtualAttributeIO) and Integration Object Item (UnitItem) with a virtual attribute (formattedCode). Creates a script that holds logic for retrieving the value of a UnitItem's formattedCode virtual attribute. Creates an instance of a Unit using the UnitItem Integration Object Item. VirtualAttributeIO. Retrieves a single Integration Object Item (UnitItem) displaying the IOI with its formattedCode virtual attribute.

1. POST to https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects with the following body:
 Sample Code
{ "code": "VirtualAttributeIO", "items": [ { "code": "UnitItem", "type": { "code": "Unit" }, "attributes": [ { "attributeName": "code", "attributeDescriptor": { "qualifier": "code", "enclosingType": { "code": "Unit" } } } ], "virtualAttributes": [ { "attributeName": "formattedCode",
This is   For more    the SAP Help  96
 "retrievalDescriptor": {
 "code": "formattedUnitCode", "logicLocation": "model://logLoc", "type": { "code": "java.lang.String" ![96_image_0.png](96_image_0.png) } } ] }
 ]
}
2. POST to https://localhost:9002/odata2webservices/ScriptService/Scripts with the following body:
 Sample Code
{ "code": "logLoc", "scriptType": { "code": "GROOVY" }, "description": "This script formats the Unit's code to uppercase", "autodisabling": false, "disabled": false, "content": "(de.hybris.platform.core.model.product.UnitModel) itemModel.code.toUpperCase()" }
3. Create a UnitModel using the dened UnitItem Integration Object Item (IOI) by sending a POST request to https://localhost:9002/odata2webservices/VirtualAttributeIO/UnitItems with the following body:
 Sample Code
{ "code": "pieces", "unitType": "EA" }
4. Retrieve the UnitItem's formattedCode by making the following GET request: https://localhost:9002/odata2webservices/UnitItem/Units('pieces')
Here is the response body that is returned:
 Sample Code
{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/UnitItem/Units('pieces')", "uri": "https://localhost:9002/odata2webservices/UnitItem/Units('pieces')", "type": "HybrisCommerceOData.Unit" }, "code": "pieces", "formattedCode": "PIECES", "integrationKey": "pieces" } }

## The Odata2 Delete Api

Delete Integration Object Items by integrationKey.

You can send a DELETE request to an endpoint with an integrationKey for a specied Integration Object Item. For example, the following endpoint shows the syntax to delete an Inbound Product.

https://localhost:9002/odata2webservices/InboundDiscountRow/Products('Staged%7CDefault%7Cp1')
If the deleted Item has any attributes or properties that include partOf="true" in the type system, the Items represented by those attributes are also deleted. You can check an Item's EDMX schema for isPartOf="true".

It is not possible to delete Items using lters. It is also not possible to delete convenience APIs such as IntegrationService, InboundIntegrationMonitoring, and OutboundIntegrationMonitoring.

Deleting an Integration Object Item Delete an Integration Object Item using an integrationKey.

Prerequisites Deleting an Integration Object Item requires the odata2webservices extension. You must also be a member of the integrationdeletegroup or integrationadmingroup.

Context Send a DELETE request to the endpoint with the integrationKey. For example, for a Product dened with the integrationKey Staged|Default|p1, send the DELETE request to the endpoint:
https://localhost:9002/odata2webservices/InboundDiscountRow/Products('Staged%7CDefault%7Cp1')
A successful request returns the response code 200, with no payload.

## Error Messages

Integration API errors can result from missing keys, properties, system errors, or other scenarios. Understanding the error responses can help you identify the source of errors.

## Note

This page may contain information about features that were only introduced in an update release. Ensure you are always on the latest release to be able to make use of all xes, security updates, and features. For a complete list of what was introduced in each update release, see What's New.

| HTTP                                                                                                                                                                                                                                                                                             | Code                                                                                                                                                                                                                                                                                                                                             | Method                                                                                                                           | Message                                                                                    | Reason                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Response Code 400 lter_not_supported                                                                                                                                                                                                                                                             | GET                                                                                                                                                                                                                                                                                                                                              | Nested lter [nested entity types] of more than one level is not supported.                                                       | Integration API does not support nested l                                                  |                                                                                                                         |
| 400                                                                                                                                                                                                                                                                                              | invalid_attribute_value                                                                                                                                                                                                                                                                                                                          | POST,                                                                                                                            | An error occurred while attempting to save entries for entityType: [name of entity type],  | An attribute value present in the payload i                                                                             |
| PATCH                                                                                                                                                                                                                                                                                            | with error message [reason].                                                                                                                                                                                                                                                                                                                     | be used in combination with other attribut entity type. The [reason] portion of the me which attribute value is invalid and why. |                                                                                            |                                                                                                                         |
| 400                                                                                                                                                                                                                                                                                              | invalid_language                                                                                                                                                                                                                                                                                                                                 | POST,                                                                                                                            | The language provided [invalidLanguageTagFromLanguageHeader] is not available in the       | The Content-Language or Accept-Language                                                                                 |
| PATCH                                                                                                                                                                                                                                                                                            | system.                                                                                                                                                                                                                                                                                                                                          | exist in the platform.                                                                                                           |                                                                                            |                                                                                                                         |
| 400                                                                                                                                                                                                                                                                                              | invalid_key                                                                                                                                                                                                                                                                                                                                      | PATCH,                                                                                                                           | PATCH: Key [integrationKey] in the payload does not match the key [integrationKey] in      |                                                                                                                         |
| GET                                                                                                                                                                                                                                                                                              | the path. GET: The integration key [SomeInvalidKey] is invalid. Please consult the IntegrationKey denition of [entity type] for conguration details.                                                                                                                                                                                             | PATCH: The integration keys in the reques are different. GET: Invalid integrationKey provided.                                   |                                                                                            |                                                                                                                         |
| 400                                                                                                                                                                                                                                                                                              | missing_key                                                                                                                                                                                                                                                                                                                                      | POST                                                                                                                             | One of the following messages:                                                             | A key property or navigation property that does not exist in the incoming data, but is schema as key or nullable=false. |
| Message 1: Key [name of key] is required for EntityType [ name of entity type]. Message 2: Key NavigationProperty [key navigation property name] is required for EntityType [name of entity type]. Message 3: Key Property [key property name] is required for EntityType [name of entity type]. |                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                  |                                                                                            |                                                                                                                         |
| 400                                                                                                                                                                                                                                                                                              | missing_nav_property                                                                                                                                                                                                                                                                                                                             | POST,                                                                                                                            | POST: One of the following messages:                                                       |                                                                                                                         |
| PATCH                                                                                                                                                                                                                                                                                            | Message 1: NavigationProperty [name of property] is required for EntityType [name of entity type]. Message 1: Item referenced by attribute [catalogVersion] in [name of entity type] item does not exist in the system. Cannot create referenced item for this attribute because it is not partof or autocreate for the item that it belongs to. |                                                                                                                                  |                                                                                            |                                                                                                                         |
| PATCH: Item referenced by attribute [attribute name] in [entity type] item does not exist in the system. Cannot create referenced item for this attribute because it is not partof or autocreate for the item that it belongs to.                                                                | A navigation property that does not exist i nor in the database, is specied in the sch Nullable=false.                                                                                                                                                                                                                                           |                                                                                                                                  |                                                                                            |                                                                                                                         |
| 400                                                                                                                                                                                                                                                                                              | missing_property                                                                                                                                                                                                                                                                                                                                 | POST,                                                                                                                            | Property [name of property] is required for EntityType [ name of entity type].             | Any non-key property that does not exist i                                                                              |
| PATCH                                                                                                                                                                                                                                                                                            | nor in the database, is specied in the sch Nullable=false. It is not possible to update with a null value.                                                                                                                                                                                                                                       |                                                                                                                                  |                                                                                            |                                                                                                                         |
| 400                                                                                                                                                                                                                                                                                              | odata_error                                                                                                                                                                                                                                                                                                                                      | POST                                                                                                                             | An error occurred while processing the request. The most likely cause of this error is the | One of the following reasons:                                                                                           |
| formatting of your OData request payload. Please verify the request payload format                                                                                                                                                                                                               | The request attempted to post an                                                                                                                                                                                                                                                                                                                 |                                                                                                                                  |                                                                                            |                                                                                                                         |
| corresponds to the EDMX metadata for the Entity that you are attempting to create.                                                                                                                                                                                                               | (collection) to a simple property. The request attempted to post a s OData Entry (collection). API cannot translate the payload to the destination EntitySet.                                                                                                                                                                                    |                                                                                                                                  |                                                                                            |                                                                                                                         |

| 7/6/2024 HTTP Code                                                                                                                                 | Method                                                                                                                                                                         | Message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Response Code 400 runtime_error                                                                                                                    | POST                                                                                                                                                                           | One of the following messages:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | One of the following reasons:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                     |
| Message 1: There was an error encountered during the processing of the Integration Object. The detailed cause of this error is visible in the log. | This message returns in any case cause is unknown.                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                     |
| Message 2: There was an unexpected error encountered during the retrieval of the [formattedName] property for EntityType [Product].                | Indicates a problem with execution in a virtual attribute conguration. attribute conguration is valid, tha found and loaded, but the script c execution. The crash may indicate unexpected script parameter inpu script crashes at least once, it bec Therefore, correcting the payload o repeating the request might not be script might need to be re-enabled well. See "Autodisabling of ModelScripting Engine.                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                     |
| 400                                                                                                                                                | invalid_property                                                                                                                                                               | POST                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | An entity contains [property] that is not dened in the Integration Object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The attribute is not dened on the Integrat                          |
| 400                                                                                                                                                | invalid_property_denition                                                                                                                                                      | POST,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | POST: Invalid attribute found [ItemThisAttributeBelongsTo.abstractAttribute]. Cannot                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                     |
| GET                                                                                                                                                | dene attribute of an abstract item type as autocreate or partof for the item that it belongs to. GET: Cannot generate unique navigation property for collections [entity type] | POST: You cannot create a new instance of reference an abstract type where autocr GET: A non-localized collection type navig as unique=true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                     |
| 400                                                                                                                                                | invalid_key_denition                                                                                                                                                           | GET                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | There is no valid integration key dened for the current entityType [name of entity type].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The IntegrationObjectItemAttributes are no Integration Object Item. |
| 400                                                                                                                                                | integration_key_not_supported                                                                                                                                                  | GET                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Filtering by integration key is not supported. Please supply the key with the Integration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Integration API does not support ltering b                          |
| Object (e.g. https://.../InboundProduct/Products('Staged|Default|MyProduct'))                                                                      |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                     |
| 400                                                                                                                                                | invalid_query_parameter                                                                                                                                                        | GET                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [query parameter] and [query parameter] query parameters cannot be combined in the                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integration API does not support certain qu                         |
| same get request.                                                                                                                                  | the same request.                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                     |
| 400                                                                                                                                                | miscongured_attribute                                                                                                                                                          | GET                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | One of the following messages: Message 1: Cannot generate unique property for localized attribute [name] set on item [Product]. Message 2: Key attribute [IntegrationItemC.itemB] forms a circular reference back to [IntegrationItemB] Message 3: Conguration for virtual attribute formattedName in item Product is invalid. One of the following reasons: For message 1: Localized values a keys. For message 2: Circular dependen integrationKey. For message 3: Indicates a problem related to a vi conguration. Such exceptions ind problems with retrieving/providing attribute's values regardless of the {@code ItemModel} or other chang example, time of execution, permi problem is consistent and can be changing the virtual attribute den |                                                                     |
| 400                                                                                                                                                | operator_not_supported                                                                                                                                                         | GET                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Operator [unsupported operator] is not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Request includes an unsupported lter.                               |
| 400                                                                                                                                                | lter_by_virtual_attribute_not_supported                                                                                                                                        | Filtering by virtual attribute formattedName is not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | When a user attempts to use the URL quer `lterBy` with a virtual attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                     |
| 400                                                                                                                                                | order_by_virtual_attribute_not_supported                                                                                                                                       | Ordering by virtual attribute formattedName is not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | When a user attempts to use the URL quer `orderBy` with a virtual attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                     |
| 400                                                                                                                                                | deletion_failure                                                                                                                                                               | DELETE One of the following messages: Message 1: The InboundChannelConguration cannot be deleted, because it is used by the [DestinationTarget name]. Please delete the ExposedDestination [name] and try again. Message 2: The [Integration Object name] cannot be deleted because it is exposed as an API. Please delete the related InboundChannelConguration and try again. Message 3: The root [OutboundSyncEvent] cannot be removed or changed for the integration object [OutboundSyncEvent_Pojo_IO_AC1], because the integration object is associated with at least one existing webhook conguration. One of the following reasons: For message 1: Attempting to dele InboundChannelConguration befo exposed destination it's associate For message 2: Attempting to dele Object before deleting the InboundChannelConguration it's a For Message 3: An error occurred w save entries for entityType: Webho |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                     |
| 400                                                                                                                                                | hook_not_found                                                                                                                                                                 | POST,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | <hook_type>PersistHook [<hook_name_from_the_request_header>] does not exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Not a single persistence hook provider wa                           |
| PATCH                                                                                                                                              | Payload will not be persisted.                                                                                                                                                 | matching the name. Another possibility is found but the provider failed to load/activ should be in the log (DEBUG level may nee see them).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                     |
| 400                                                                                                                                                | pre_persist_error                                                                                                                                                              | POST,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Exception occurred during the execution of PrePersistHook:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | A hook was found but it crashed (threw a R                          |
| PATCH                                                                                                                                              | [<hook_name_from_the_request_header>].                                                                                                                                         | that left the hook code) while processing t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                     |
| 400                                                                                                                                                | post_persist_error                                                                                                                                                             | POST,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Exception occurred during the execution of PostPersistHook:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | A hook was found but it crashed (threw a R                          |
| PATCH                                                                                                                                              | [<hook_name_from_the_request_header>].                                                                                                                                         | that left the hook code) while processing t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                     |

| 7/6/2024 HTTP Code                                                                                                                                                                                                                                                                                                         | Method                                                                                                                                                                                                                                                                                                                              | Message                                                                                       | Reason                                                                                                                                                                                                                                                                 |                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Response Code 400 invalid_attribute_name                                                                                                                                                                                                                                                                                   | POST                                                                                                                                                                                                                                                                                                                                | One of the following messages:                                                                | An error occurred while attempting to save entityType: InboundChannelConguration.                                                                                                                                                                                      |                                                                                   |
| Message 1: attributeName [<attribute name>] for class [<class path>] of IntegrationObject [<integration object code>] does not exist. Message 2: attributeName [unit] for class [de.hybris.platform.core.model.product.ProductModel] of IntegrationObject [POJO-1-2] does not match the returnIntegrationObjectClass type. |                                                                                                                                                                                                                                                                                                                                     |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| 400                                                                                                                                                                                                                                                                                                                        | invalid_read_method                                                                                                                                                                                                                                                                                                                 | POST                                                                                          | One of the following messages:                                                                                                                                                                                                                                         | An error occurred while attempting to save entityType: InboundChannelConguration. |
| Message 1: readMethod [readMethodThatDoesNotExist] for class [de.hybris.platform.core.model.test.TestItemModel] of IntegrationObject [POJOIO-2-a] does not exist. Message 2: readMethod [doVoid] for class [de.hybris.platform.integrationservices.TestPojo] of IntegrationObject [POJO-IO2-b] is VOID. Message 3: readMethod [getParameterized] for class [de.hybris.platform.integrationservices.TestPojo] of IntegrationObject [POJO-IO2-c] has non-empty parameters. Message 4: readMethod [getDouble] return type for class [de.hybris.platform.core.model.test.TestItemModel] of IntegrationObject [POJO4-a] does not match the returnIntegrationObjectClass type.                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                     |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| 400                                                                                                                                                                                                                                                                                                                        | invalid_class_type                                                                                                                                                                                                                                                                                                                  | CREATE Class [<IntegrationObjectClass.code>] for IntegrationObject [<IntegrationObject.code>] | Attempting to create an IntegrationObjectC                                                                                                                                                                                                                             |                                                                                   |
| cannot be set to type [<IntegrationObjectClass.type>]. IntegrationObjectClasses cannot                                                                                                                                                                                                                                     | IntegrationObjectClass type set as any pri                                                                                                                                                                                                                                                                                          |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| be a primitive type.                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                     |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| 400                                                                                                                                                                                                                                                                                                                        | invalid_pojo_class                                                                                                                                                                                                                                                                                                                  | POST                                                                                          | The IntegrationObjectClass [class.path.that.does.not.exist.for.TestItemModel] does not                                                                                                                                                                                 | Request includes an invalid class path.                                           |
| exist in the specied classpath.                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                     |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| 400                                                                                                                                                                                                                                                                                                                        | invalid_pojo_item_modeling                                                                                                                                                                                                                                                                                                          | POST                                                                                          | Integration object [POJO-6] has integration object item(s) [Customer] assigned. Mixing                                                                                                                                                                                 | An error occurred while attempting to save                                        |
| IntegrationObjectClass and IntegrationObjectItem models in an Integration Object is not                                                                                                                                                                                                                                    | entityType: InboundChannelConguration.                                                                                                                                                                                                                                                                                              |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| allowed.                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                     |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| 400                                                                                                                                                                                                                                                                                                                        | invalid_root_pojo                                                                                                                                                                                                                                                                                                                   | CREATE Class [<IntegrationObjectClass.code>] of atomic type [<IntegrationObjectClass.type>]   | Attempting to create an IntegrationObjectC                                                                                                                                                                                                                             |                                                                                   |
| cannot have root set to true for IntegrationObject [<IntegrationObjectClass.code>].                                                                                                                                                                                                                                        | IntegrationObjectClass with type set as an                                                                                                                                                                                                                                                                                          |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| 400                                                                                                                                                                                                                                                                                                                        | missing_io_root                                                                                                                                                                                                                                                                                                                     | POST                                                                                          | Cannot create WebhookConguration with IntegrationObject [<root.code>] because it has When no root congured. toggle.webhookservices.busines is set to true while attempting to create a WebhookConguration with an Integration Integration Object does not have a dened |                                                                                   |
| 400                                                                                                                                                                                                                                                                                                                        | root_in_use                                                                                                                                                                                                                                                                                                                         | DELETE, The root [<IntegrationObjectItem.code>] cannot be removed or changed for the          | Attempting to delete or update the root for                                                                                                                                                                                                                            |                                                                                   |
| UPDATE integration object [%s], because the integration object is associated with at least one                                                                                                                                                                                                                             | Object that is associated with an existing                                                                                                                                                                                                                                                                                          |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| existing webhook conguration.                                                                                                                                                                                                                                                                                              | WebhookConguration.                                                                                                                                                                                                                                                                                                                 |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| 400                                                                                                                                                                                                                                                                                                                        | cannot_update_root_class                                                                                                                                                                                                                                                                                                            | UPDATE Updating the IntegrationObjectClass [<IntegrationObjectClass.code>] root for           | When toggle.root.update.restric                                                                                                                                                                                                                                        |                                                                                   |
| IntegrationObject [<IntegrationObject.code>] is not permitted.                                                                                                                                                                                                                                                             | set to true while attempting to change the existing IntegrationObjectClass                                                                                                                                                                                                                                                          |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| 400                                                                                                                                                                                                                                                                                                                        | root_ioc_requires_abstract_event_child                                                                                                                                                                                                                                                                                              | POST                                                                                          | Class [<IntegrationObjectClass.code>] for IntegrationObject [<IntegrationObject.code>]                                                                                                                                                                                 | When a root IntegraionObjectClass with th                                         |
| cannot be set with type [<IntegrationObjectClass.type>]: only sub-classes of the                                                                                                                                                                                                                                           | that does not extend the Abstract Event cl                                                                                                                                                                                                                                                                                          |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| AbstractEvent class can be modeled as the root.                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                     |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| 400                                                                                                                                                                                                                                                                                                                        | business_event_root_mismatch                                                                                                                                                                                                                                                                                                        | POST,                                                                                         | The WebhookConguration BusinessEvent eventType does not match the integration                                                                                                                                                                                          |                                                                                   |
| PATCH                                                                                                                                                                                                                                                                                                                      | object [OutboundSyncEvent_Pojo_IO_AC_2_3] root class type [class de.hybris.platform.outboundsync.events.OutboundSyncEvent]. The WebhookConguration eventType must be a valid BusinessEvent matching the root class type. Attempting to create a WebhookCongurat eventType that does not match the root ty Integration Object Class. |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| 400                                                                                                                                                                                                                                                                                                                        | business_events_cannot_extend_webhookevent POST                                                                                                                                                                                                                                                                                     | Integration object [Pojo_IO] root class type [class                                           | Attempting to create a POJO Integration O                                                                                                                                                                                                                              |                                                                                   |
| de.hybris.platform.webhookservices.event.ItemCreatedEvent] must be a Business Event                                                                                                                                                                                                                                        | root type that implements the WebhookEv                                                                                                                                                                                                                                                                                             |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| that extends AbstractEvent, excluding any that implement WebhookEvent.                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                     |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| 400                                                                                                                                                                                                                                                                                                                        | feature_not_enabled                                                                                                                                                                                                                                                                                                                 | POST                                                                                          | Please set the [toggle.webhookservices.businessevents.enabled] to true to enable this                                                                                                                                                                                  | Attempting to create a WebhookCongurat                                            |
| feature.                                                                                                                                                                                                                                                                                                                   | IntegrationObject with a root IntegrationOb feature is not enabled.                                                                                                                                                                                                                                                                 |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| 403                                                                                                                                                                                                                                                                                                                        | forbidden                                                                                                                                                                                                                                                                                                                           | POST, PATCH, DELETE, GET One of the following messages:                                       | One of the following reasons:                                                                                                                                                                                                                                          |                                                                                   |
| Message 1: User is not authorized for the operation.                                                                                                                                                                                                                                                                       | For message 1: Access to the spec Object is restricted.                                                                                                                                                                                                                                                                             |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| Message 2: Credentials provided are not authorized for the operation.                                                                                                                                                                                                                                                      | For message 2: Access to the spe Object is restricted.                                                                                                                                                                                                                                                                              |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| Message 3: The user lacks [create, read, update, or delete] privileges for accessing the [item type name] type.                                                                                                                                                                                                            | For message 3:The user lacks a sp access right that they are trying to                                                                                                                                                                                                                                                              |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |
| Message 4: The user lacks [create, read, update, or delete] privileges for accessing the Integration Object types.                                                                                                                                                                                                         | For message 4: A user is attempti Integration Object's metadata but Object doesn't have a root item.                                                                                                                                                                                                                                |                                                                                               |                                                                                                                                                                                                                                                                        |                                                                                   |

| 7/6/2024 HTTP Code                                | Method                                                                                                                                                                                                                                                                   | Message                                                                                                                                                                                                                                           | Reason                                                                              |                                                        |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------|
| Response Code 404 not_found                       | POST,                                                                                                                                                                                                                                                                    | POST: Could not nd an entity set or function import for 'Products'.                                                                                                                                                                               |                                                                                     |                                                        |
| PATCH, GET                                        | PATCH: [Integration Object item] with integration key [integration key] was not found. GET: One of the following messages: Message 1: [Entity type] with integration key [integration key] was not found. Message 2: Could not nd property with name: '[attributeName]'. | POST: The Integration Object Item does no specied service. PATCH: The Integration Object Item or the request URL does not exist for the specie GET: One of the following reasons: For message 1: Item not found. For message 2: Requested attribu |                                                                                     |                                                        |
| 404                                               | invalid_key                                                                                                                                                                                                                                                              | DELETE The integration key [integrationKey] is invalid. Please consult the IntegrationKey                                                                                                                                                         | The Integration Object Item or the integrat                                         |                                                        |
| denition of [entityType] for conguration details. | URL does not exist for the specied servic                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                   |                                                                                     |                                                        |
| 405                                               | method_not_allowed                                                                                                                                                                                                                                                       | PATCH,                                                                                                                                                                                                                                            | The request dispatcher does not allow the HTTP method used for the request.         | PATCH: The request is invalid because it d             |
| DELETE                                            | integrationKey, attempts to update multip includes a lter condition. DELETE: The request is invalid because it integrationKey or includes lters.                                                                                                                         |                                                                                                                                                                                                                                                   |                                                                                     |                                                        |
| 405                                               | inaccessible_integration_object                                                                                                                                                                                                                                          | GET,                                                                                                                                                                                                                                              | Only $metadata requests are supported for Integration Objects modeled with          | You can't use POJO Integration Objects in R            |
| POST,                                             | IntegrationObjectClass.                                                                                                                                                                                                                                                  | either post data to, or retrieve data from, t                                                                                                                                                                                                     |                                                                                     |                                                        |
| PATCH,                                            | database. Only $metadata requests are                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                   |                                                                                     |                                                        |
| DELETE                                            | Integration Objects modeled with Integrati GET, POST, PATCH, and DELETE requests                                                                                                                                                                                         |                                                                                                                                                                                                                                                   |                                                                                     |                                                        |
| 415                                               | POST,                                                                                                                                                                                                                                                                    | Media type [media type] is not supported.                                                                                                                                                                                                         | Request includes an invalid contentType h                                           |                                                        |
| PATCH                                             |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                   |                                                                                     |                                                        |
| 500                                               | internal_error                                                                                                                                                                                                                                                           | POST,                                                                                                                                                                                                                                             | There was an error encountered during the processing of the Integration Object. The | The system encountered an error during th              |
| PATCH,                                            | detailed cause of this error is visible in the log.                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                   |                                                                                     |                                                        |
| GET, DELETE                                       |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                   |                                                                                     |                                                        |
| 501                                               | lter_not_supported                                                                                                                                                                                                                                                       | GET                                                                                                                                                                                                                                               | Filtering by classication attribute [attributeName] is not supported.               | Integration API does not support ltering o attributes. |

## Outbound Features

Congure outbound services for publication and localization of Integration Objects, Items, and item attributes. You can congure services to send Integration Objects outbound, to detect Items updated in SAP Commerce and publish them to external systems, to localize Integration Object item attributes for outbound POST requests, and to congure the maximum number of HTTP connections for outbound services. Using the Outbound Sync Meta API, you can congure the following scenarios:
Creating Outbound Sync Congurations Retrieving Outbound Sync Congurations Updating Outbound Sync Congurations Deleting Outbound Sync Congurations For more information, see Outbound Sync Meta API. Additionally, all outbound requests are decorated with an SAP Passport ID. For more information, see the SAP Passport ID section of Modifying Outbound Requests.

Integration Object Outbound Services Set up and congure the outboundservices extension as well as extensions that support Outbound Services to send Integration Objects to outbound endpoints.

Outbound Sync Use outbound sync to publish new and modied Integration Objects to external systems. Outbound Response Handling This topic covers response handling measures that are in place for outbound requests. Localization Localize Integration Object item attributes for outbound POST requests. Setting Maximum HTTP Connections for Outbound Services Specify the maximum number of HTTP connections made from SAP Commerce Cloud for outbound requests. Webhooks Webhooks allow SAP Commerce Cloud to send notications to a congured destination URL when an item is saved (created or updated) or deleted.

## Integration Object Outbound Services

Set up and congure the outboundservices extension as well as extensions that support Outbound Services to send Integration Objects to outbound endpoints.

After you congure an Integration Object, you can send outbound Integration Objects to congured endpoints as a map of key-value pairs. This topic describes the extensions and class denitions that support outbound Integration Objects.

This is   For more    the SAP Help  101 Additionally, you can monitor outbound Integration API requests in Backoffice. For more information, see Integration API Request Monitoring. For an advanced level of conguration, developer users can modify headers and payloads to enrich outbound requests, as described in Modifying Outbound Requests. To send data to an outbound destination based on an SAP Commerce event or process, see Tutorial: Using the Outbound Service.

Outbound Service Extensions The following three extensions support Outbound Services:
outboundservices: The outboundservices extension allows monitoring for outbound Integration API requests. apiregistryservices: This SAP Commerce Cloud extension allows you to congure endpoint and credential details. integrationservices: This SAP Commerce Cloud extension encapsulates the services that an API exposes. These services, or Integration Object denitions, are dened with the ImpEx les.

Class Denitions The OutboundServiceFacade uses a single method to send Integration Objects out to a congured endpoint. It orchestrates the action to convert the Type System ItemModel to a payload based on the Integration Object denition, and integrates with the endpoint.

The IntegrationObjectConversionService allows you to convert any Type System item based on an Integration Object denition to a Java Map< String, Object> format.

To achieve this, the Converters and Populators pattern from the Type System was adapted. Converters create instances of target objects and then call the Populators, which populate the target objects from the given source.

## Note

Sample SSL certicates are provided for developer environments and allow you to use localhost only. For production environments new certicates should be generated. The system needs to trust the new certicates, so remember to add them to default JVM trust store or congure an additional trust store in a similar way as the platform does for the sample certicates. For an example, see the advanced.properties le in platform/resources:
\# Additional trust store. If configured the trust store (in the JKS format) is added as a fallback trust store to the default one provided \# by the JVM. Its intention is to provide a trusted self-signed CA certificate for developers/testers convenience. additional.javax.net.ssl.trustStore=${platformhome}/resources/devcerts/ydevelopers.jks additional.javax.net.ssl.trustStorePassword=123456

## Outbound Sync

Use outbound sync to publish new and modied Integration Objects to external systems. Outbound sync uses Delta Detection to identify new and modied Items in SAP Commerce Cloud. You can congure which items to publish, when, and where. Outbound sync supports POST (create, update) and DELETE requests. For more information, see Conguring Outbound Sync.

The outboundsync extension relies on the deltadetect extension to identify changes in SAP Commerce Cloud. The following diagram illustrates how outboundsync interacts with the system components.

 Note Because polyglot persistence is not compatible with delta detection, outbound sync does not support polyglot persistence. See Polyglot Persistence for feature details.

![101_image_0.png](101_image_0.png)

 Note For information on outbound request security measures, see Outbound Response Handling.

To congure and trigger the outbound sync job, see the Outbound Sync Implementation section.

Outbound Sync Meta API

The Integration API also provides a Meta API for outbound sync functionality. For more information, see Outbound Sync Meta API.

Supported Services and Expected Response Outbound sync functions only with the POST service and expects a 201 response from other systems.

Related Information Outbound Monitoring Outbound Sync Implementation Outbound Sync Attempt Retry If the outbound sync extension fails to send a payload to its destination, it retries delivery. The number of retries is congurable. The OutboundSyncJob is congured to retry publication during the next scheduled or manual execution of the outboundSyncCronJob after a failed attempt. The outboundRetryCleanupCronJob deletes records of failed attempts after a congurable retention period. The item-destination retry record still remains in the OutboundSyncRetry table until its retention period expires. If an item attempt to pulish to a destination fails the maximum number of times as specied for outbound sync retry, the item is no longer eligible for publication. In this case, you can look at Outbound Monitoring for possible reasons for the failure. The retention period is 7 days by default, after which all retry records that have exceeded the maximum number of retries, and passed the retention period are deleted.

Related Information Setting the Outbound Sync Retry Record Retention Period Setting the Outbound Sync Retry Maximum Attempts Change Log The outbound sync audit report details changes made to an outbound sync conguration.

 Note Only an administrator can generate audit reports.

Use the outbound sync audit report to view changes, listed by user, to an outbound sync conguration. Details include:
changingUser - name of the user who made changes payload - OutboundChannelConguration timestamp - date and time of the last change to the payload To access the outbound sync audit report:
1. In the Backoffice Integration UI Tool, select Outbound Sync Conguration Channels .

2. Select an outbound channel.

3. Click the (Outbound Sync Audit Report Downloader).

Payloads are listed in timestamp order from newest to oldest. Changes to payloads are color-coded: Changes to a payload are color-coded:
Green (added since the last payload) Red (deleted since the last payload) Yellow (status changed since the last payload, for example, an attribute value changes from true to false)

![103_image_0.png](103_image_0.png)

Outbound Response Handling This topic covers response handling measures that are in place for outbound requests.

Outbound Request Timeout Response To prevent outbound requests consuming HTTP connections for a prolonged period of time, outbound requests are limited to 5 seconds of execution time, which includes the time to make the connection and the time the remote system completes its response to SAP Commerce Cloud. If the request does not complete within 5 seconds, it's aborted and the request results in a timeout error. You can view information related to the timeout error under Outbound Monitoring in the Backoffice Integration UI Tool. The following error message is displayed: "Request timed out after 5000 ms". For webhooks, if the request times out, it isn't retried.

For outbound sync, the number of retry attempts depends on the number specied for the outboundsync.max.retries property.

Outbound Response Body Size For both performance and security reasons, an outbound response body is limited to 1024 bytes. If the response body is too big, it can cause slow response processing and a potential security threat in the form of out-of-memory errors. If the response body is larger than the maximum allowed value it isn't read in-memory, and the OutboundRequest.error produces the following message: "The error response message exceeded the allowed size."
Outbound Error Messages For both outbound sync and webhooks to process error messages from the destination server, the expected format for error messages is the following:
 Sample Code

{ ![104_image_0.png](104_image_0.png) }
If the error is returned in an unexpected format, you'll see the message "Please see the log for details."

## Localization

Localize Integration Object item attributes for outbound POST requests.

An Integration Object Item's attributes can have localized values. For example, you can localize a Product's name attribute for different languages. When the Integration Object Outbound Services sends the Integration Object, it includes all the localized attribute values in the map output.

The following output example shows an Integration Object called MyProduct that has localizations for the name and description attributes in English, French, German, and Spanish. The localizedAttributes property is an array that contains the localized values for name and description. The language property identies the language associated to the translation.

In the example, the description value for the German (de) localization is an empty string because it is stored as an empty string in the system. For the Spanish (es) localization, the description attribute does not appear because its value is null in the system. Each Integration Object in the output has its own localizedAttributes property. In the example, the Product's catalog has its own localizedAttributes for the Catalog's name attribute. For backward compatibility with previous versions, the default localized properties are still sent as the default in the default platform language.

The following example sends four translations for My Product, but sends only one translation for My Catalog because Catalog has only one available translation. CatalogVersion has no exposed localizations, so it doesn't have any localized attributes.

{

![104_image_2.png](104_image_2.png)

![104_image_3.png](104_image_3.png)

![104_image_4.png](104_image_4.png) ![104_image_1.png](104_image_1.png) { "language": "en", "name": "My Catalog" } ] } }, "localizedAttributes": [ { "language": "en",
 "name": "My Product",
 "description": "This is the English description" }, { "language": "fr", "name": "Mon Produit", "description": "C'est la description française" }, { "language": "de", "name": "Mein Produkt", "description": "" }, { "language": "es", "name": "Mi producto" } ] }

## Setting Maximum Http Connections For Outbound Services

![104_Image_5.Png](104_Image_5.Png)

Specify the maximum number of HTTP connections made from SAP Commerce Cloud for outbound requests.

Prerequisites The outboundservices.httpclient.max.connections property species the maximum number of HTTP connections made from SAP Commerce Cloud for outbound requests. It's part of the outboundservices extension's project.properties le. The outboundHttpClientFactory spring bean uses outboundservices.httpclient.max.connections, which you can see in the outboundservices-spring.xml le. For example:
 Sample Code
<alias name="defaultOutboundHttpClientFactory" alias="outboundHttpClientFactory" /> <bean id="defaultOutboundHttpClientFactory" class="de.hybris.platform.outboundservices.client.impl.DefaultOutboundHttpClientFactory">
This is   For more    the SAP Help  105

## 

 <property name="maxConnections" value="${outboundservices.httpclient.max.connections}" />
 <property name="keepAlive" value="${outboundservices.httpclient.connections.keep-alive}" /> <property name="timeout" value="${outboundservices.httpclient.connections.connectionTimeout}" /> <property name="validity" value="${outboundservices.httpclient.connections.validity}" /> </bean>
From DefaultOutboundHttpClientFactory.java, the maxConnections value specied is set to the PoolingHttpClientConnectionManager of the created HTTPClient. maxConnections is a pool size for connections used for outbound communications. For example:
 Sample Code private PoolingHttpClientConnectionManager createPoolingHttpClientConnectionManager() { final PoolingHttpClientConnectionManager connectionManager = getConnectionManager(); connectionManager.setDefaultMaxPerRoute(getMaxConnections()); connectionManager.setMaxTotal(getMaxConnections()); connectionManager.setValidateAfterInactivity(getValidity()); return connectionManager; }
For PoolingHttpClientConnectionManager, refer to Pooling connection manager from the Apache documentation. PoolingHttpClientConnectionManager maintains a maximum limit of connections on a per route basis and in total. By default, this implementation creates no more than 2 concurrent connections per given route and no more 20 connections in total. The default value for both DefaultMaxPerRoute and MaxTotal is set to 10. Adjust this property accordingly to make sure you don't meet with a connection request timeout error.

## Context

Congure the outboundservices.httpclient.max.connections property to change the number of HTTP connections the origin system makes when synchronizing with a destination.

By default, the value is 5.

 Note You cannot change the property at runtime. Restart SAP Commerce Cloud to enable changes.

Procedure 1. Log in to the Administration Console.

2. Click Platform Conguration .

3. Search for outboundservices.httpclient.max.connections.

4. In the Value eld, enter the maximum number of connections to open for each outbound request. 5. Click the checkmark to apply the changes. 6. Restart SAP Commerce Cloud for the changes to take effect.

## Webhooks

Webhooks allow SAP Commerce Cloud to send notications to a congured destination URL when an item is saved (created or updated) or deleted. You can use webhooks to receive notications in response to After Save Events for specic item types, for example, using a webhook to receive a notication every time a Product is saved (created or updated) or deleted to better capture and manage activities that are taking place. Webhook notications send decorated headers with the binary CloudEvents specication, which includes the following header information: ce-source, ce-id, ce-specversion, ce-type, ce-subject, ce-time (optional), ce-sappassport (optional).

## Note

The ce-subject header is for the item integration key, which might contain personal data.

Webhooks are enabled via the webhookservices extension. A WebhookConfiguration consists of an Integration Object and a Consumed Destination. The webhook conguration autodiscovers changes when an item is saved (created or updated) or deleteted based on the root of the Integration Object. Once any change occurs on the root type, an event is red, and the payload dened by the Integration Object is sent to its destination. The following diagram shows how webhooks work. When SAP Commerce Cloud is running as a cluster, each SAP Commerce Cloud instance processes its own webhook events.

![105_image_0.png](105_image_0.png)

## Webhook Conguration

 Note This page may contain information about features that were only introduced in an update release. Ensure you are always on the latest release to be able to make use of all xes, security updates, and features. For a complete list of what was introduced in each update release, see What's New.

A WebhookConfiguration requires the following two parts:
Integration Object or POJO Integration Object - This denes the notication payload. The Integration Object or POJO Integration Object's root indicates whether the WebhookConfiguration is applicable to the Integration Object model. For example, if the Integration Object's root item is a Product, and the saved item is a subtype of Product, for example, VariantProduct, the WebhookConfiguration can send the VariantProduct. For more information about root items, see Root Items for Integration Objects. For more information about POJO Integration Objects that require an Integration Object Class as the root, see Modeling POJO Integration Objects for Outbound Events.

 Note If a referenced or partOf item is saved, SAP Commerce Cloud does not send a notication for the owner or parent item. For example, a WebhookConguration congured for an Integration Object Item with Order set as the root item. If the owner of an OrderEntry is the Order and only the OrderEntry is saved, then it does not send an Order notication for the saved OrderEntry. However, if there is an Integration Object root item as OrderEntry, then the WebhookConguration sends the OrderEntry.

Consumed Destination - Species the URL of the webhook subscriber. The consumed destination must have the webhookServices Destination Target, and the consumed destination requires specied credentials even if the webhook destination doesn't expect them. For information about destinations, see Endpoints and Destinations.

 Note When toggle.webhookservices.businessevents.enabled is set to false, The WebhookConfiguration also contains an optional eventType attribute that doesn't need to be specied when creating the conguration. The event is always the ItemSavedEvent. ItemSavedEvents are only published for Item type changes that have a qualifying WebhookConfiguraiton. When toggle.webhookservices.businessevents.enabled is set to true (the default value is true), you can create a WebhookConguration with the same eventType as the IntegrationObjectClass type. You can either explicitly provide the eventType when sending a request to create a WebhookConguration for the Integration Object or you can leave the eventType value blank and it matches the root IntegrationObectClass AbstractEvent type by default. Any type that extends the AbstractEvent type is considered a business event.

![106_image_0.png](106_image_0.png)

This example creates a WebhookConfiguration via ImpEX for a Integration Object called MyProduct and a consumed destination called MyExternalDestination without the EventConguration. The Integration Object and Consumed Destination are predened.

 Sample Code INSERT_UPDATE WebhookConfiguration; integrationObject(code)[unique = true]; destination(id)[unique = true] ; MyProduct ; MyExternalDestination For SAP Commerce Cloud, if the webhook isn't receiving any items, make sure that the apiregistryservices.events.exporting property is set to true in the deployment manifest or the environment service where API Registry is running.

To prevent webhook notications being sent when the webhook's consumed destination is inactive, toggle.webhookservices.destination.active.enabled is set to true by default.

 Note To use webhooks with POJO Integration Objects, see Webhooks for POJO Integration Objects.

## Webhooks For Pojo Integration Objects

You can use webhooks for POJO Integration Objects.

Context Note This page may contain information about features that were only introduced in an update release. Ensure you are always on the latest release to be able to make use of all xes, security updates, and features. For a complete list of what was introduced in each update release, see What's New.

When an Integration Object has an Integration Object Class as its root (POJO IO), to use webhooks, toggle.webhookservices.destination.active.enabled must be set to "true".

The default value is true.

Procedure To deactivate this feature, in the properties list in the manifest.json le, set the value to "false" for toggle.webhookservices.destination.active.enabled:
"properties": [ {
 ...,
 "key": "toggle.webhookservices.businessevents.enabled", "value": "false" } ]
 Note To deactivate the feature that prevents webhook notications from being sent when the webhook's consumed destination is inactive, set toggle.webhookservices.destination.active.enabled to false by following the same step above. The default value is true.

## Item Filtering For Webhooks

Filters allow you to control which items are sent to a webhook and which ones are ltered out. For example, you can create lters so that only certain items are delivered based on their attribute values. Filters should avoid manipulating the item attributes. If certain values need to be formatted differently in the payload, use virtual attributes. If items need to be persisted with changed attribute values, use persistence interceptors. For information about virtual attributes and interceptors, see Virtual Attributes and Interceptors respectively. Although webhooks are processed asynchronously, it's still important to avoid slow-running operations in the lter as it can impact webhook processing performance. For more information, see the "Performance Implications for Webhooks" section of this topic.

Conguration Example This example demonstrates the steps to lter for products only found in an Online catalog to send any applicable product changes to a webhook. The rst step is to create a lter. Filters must be written as platform scripts, and they must implement de.hybris.platform.webhookservices.filter.WebhookFilter interface.

For more information about how to implement an interface and how dependencies can be injected, see the "Using Return Objects as Interfaces" section in Scripting Engine. Create a Groovy script:
 Sample Code import de.hybris.platform.core.model.ItemModel import de.hybris.platform.webhookservices.filter.WebhookFilter new WebhookFilter() { @Override public <T extends ItemModel> Optional<T> filter(final T item) {
 Optional.ofNullable(item)
 .filter { it.catalogVersion.version == 'Online' } } }
The second step is to save the script in the platform. You can do this using Backoffice, ImpEX, or the Script Service Meta API. This example uses the Script Service Meta API (for more information, see Script Service Meta API for Virtual Attributes). To create the lter script in the platform, execute this POST request:
 Sample Code POST {{host}}/odata2webservices/ScriptService/Scripts Authorization: Basic {{user}} {{password}} Content-Type: application/json Accept: application/json { "code":"onlineProductFilter", "content":"import de.hybris.platform.core.model.ItemModel\nimport de.hybris.platform.webhookservices.filter.WebhookFilter\n new WebhookFilter "scriptType":{ "code":"GROOVY" } }
 Note The root item of the Integration Object is passed automatically to the script.

The third step is to create a WebhookConfiguration. This example uses the same Integration Object and consumed destinaton from the above webhook conguration example.

 Sample Code INSERT_UPDATE WebhookConfiguration; integrationObject(code)[unique = true]; destination(id)[unique = true]; filterLocation ; MyProduct ; MyExternalDestination ; model://onlineProductFilter Now that the WebhookConfiguration including the lter has been created, only changes for products in the Online catalog are sent to the external webhook site.

 Note Only lter locations of type model:// are supported. Specifying a location other than model:// results in an error.

Because lters can be used to prevent sensitive data from being sent to an external system, any of the following issues prevent items from being sent to the external webhook site:
The filterLocation contains an invalid or malformed URL. The lter script specied by the filterLocation does not exist. The lter script does not implement de.hybris.platform.webhookservices.filter.WebhookFilter interface.

The lter script throws an exception during its execution. The lter script returns an item that is not of a type or a subtype of the original item sent through the lter.

 Note If the autodisabling attribute of the lter script is set to true, the script is disabled after a rst failure, and any subsequent invocations of the lter results in failure and the item is not sent.

If a lter is no longer needed, you can remove it by updating the filterLocation attribute in the WebhookConfiguration to null or an empty value.

Use Filtering for General Data Protection Regulation (GDPR)
You can use ltering for situations that require specic customer data to be protected based on GDPR requirements. For example, not exposing a customer's email address when sending an Order. Because an Order Integration Object contains a customer's name, address, and email, ltering can mask the email address so that it's not exposed. The following is a sample Order Integration Object:
 Sample Code INSERT_UPDATE IntegrationObject; code[unique = true]; integrationType(code) ; Order ; INBOUND INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code); root[default = false]; itemTypeMatch ; Order ; Order ; Order ; true ; ALL_SUB_AND_SU ; Order ; Address ; Address ; ; ALL_SUB_AND_SU

INSERT_UPDATE IntegrationObjectItemAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = true]; at ; Order:Order ; code ; Or ; Order:Order ; deliveryAddress ; Or ; Order:Address ; email ; Ad ; Order:Address ; firstname ; Ad ; Order:Address ; lastname ; Ad ; Order:Address ; line1 ; Ad ; Order:Address ; city ; Ad ; Order:Address ; state ; Ad ; Order:Address ; postalcode ; Ad

The following script masks the email address before sending the Order:
 Sample Code import de.hybris.platform.core.model.ItemModel import de.hybris.platform.webhookservices.filter.WebhookFilter new WebhookFilter() { @Override public <T extends ItemModel> Optional<T> filter(final T item) { item.deliveryAddress.email = '*****' Optional.of item } }
 Note The item is an OrderModel. The script masks the delivery address' email by setting it to asterisks. The mask only applies when sending the Order to the webhook and is not persisted.

The resulting payload looks like this:
 Sample Code
{ "code": "1", "deliveryAddress": {
This is   For more    the SAP Help  109

 "email": "*****", 
 "firstname": "John", "lastname": "Doe", "line1": "111 Main St", "city": "Some Town", "postalcode": "12345", "integrationKey": "*****" }, "integrationKey": "1" }
 Note The deliveryAddress integrationKey is also masked because the email is used as the integration key.

Event Type for Webhooks You can congure webhooks to send notications triggered by item-specic events. For example, every time a new item is created. You can choose from the following four event types:
Item Saved (ItemSavedEvent) - when a new item is created (ItemCreatedEvent) or an existing item is updated (ItemUpdatedEvent). This is the default event type. Item Created (ItemCreatedEvent) - only when a new item is created. Item Updated (ItemUpdatedEvent) - only when an item is updated. Item Deleted (ItemDeletedEvent) - when an item is deleted.

Webhook events are consolidated and sent to their respective webhook congurations based on the following rules: Webhook Congurations Exist for Item Created, Item Updated, and Item Saved Events Rule 1 - when an ItemCreatedEvent is followed by an ItemUpdatedEvent within the congured timeframe, only the ItemCreatedEvent with the nal state is sent to the Created webhook conguration. The ItemSavedEvent (of EventType: Created) with the nal state is sent to the Saved webhook conguration. Rule 2 - when an ItemUpdatedEvent is followed by another ItemUpdatedEvent within the congured timeframe, a single ItemUpdatedEvent with the nal state is sent to the Updated webhook conguration. The ItemSavedEvent (of EventType: Updated) with the nal state is sent to the Saved webhook conguration. Valid Webhook Congurations Exist for Both a Parent Item Type and a Child Item Type When an event occurs for a parent item type followed by an event for a child item type, only the child event is sent to the child webhook without modication.

 Note Item Deleted (ItemDeletedEvent) is not considered for any consolidation.

Webhooks for Parent-Child Relationships You can use webhooks to receive notications in response to an AfterSaveEvent for an Integration Object Item attribute (child) or an Integration Object item (parent). For example, using a

![109_image_0.png](109_image_0.png)

![109_image_1.png](109_image_1.png) webhook to receive a notication every time a Payment Transaction (child) is created, updated, or deleted for an Order (parent). The following example models an Order with paymentTransactions (as children) of the PaymentTransaction type. The PaymentTransaction type has paymentTransactionEntries (grandchildren to the root Order) of PaymentTransactionEntry type, which sets up the following hierarchy:

![109_image_2.png](109_image_2.png)

If an AfterSaveEvent for a create, update, or delete event for a child (or grandchild) is caught, and there is no Event caught for the parent and root type itself, then an ItemSavedEvent (update) and ItemUpdatedEvent are sent out for the parent (or granparent) as long as the parent root has a corresponding WebhookConguratoin with these event types. For example, for both ItemSavedEvent (update) and ItemUpdatedEvent to be sent out for an Order (parent) for a PaymentTransaction or PaymentTransactionEntry create, update, or delete event, you need the following WebhookConguration:
 Sample Code INSERT_UPDATE WebhookConfiguration; integrationObject(code)[unique = true]; destination(id)[unique = true]; eventType[unique = true] ; OrderIO ; destination1 ; de.hybris.platform.webhookservices.even ; OrderIO ; destination1 ; de.hybris.platform.webhookservices.even For the Integration Object denition where Order has a path down to its children (or grandchildren) through Integration Object Item Attributes, the children (or grandchildren) need a path back up to the root that is the parent (or grandparent) for the created, updated, or deleted events. If not, create, update, or delete events aren't triggered from the child to the root of the IO.

Example Use Cases The following examples assume that both the OrderIO Integration Object where Order is the root of the Integration Object and the WebhookConguration above already exist. The examples use POST, but you can also use Backoffice.

When a Child is Created via a POST Request to the Child (or Grandchild) System Type (or Entity Type) Directly Note This example assumes that an Order exists with code=order1 (making up its 1 unique key attribute).

Send POST request https://localhost:9002/odata2webservices/OrderIO/PaymentTransactions to create a new child referencing Order with its integrationKey attributes provided (only Order.code) with the following body:
 Sample Code
{ "code": "paymentTransaction1a", "order": { "code": "order1" } }
The ItemSavedEvent (update) and ItemUpdatedEvent are sent for the parent order1 pk.

When a Child is Updated via a POST Request to the Child (or grandchild) System Type (or EntityType) Directly Note This example assumes that an Order exists with code=order1 (making up its 1 unique key attribute), and the PaymentTransaction created for order1 also exists with a code=paymentTransaction1a (making up its 1 unique key attribute).

Send POST request https://localhost:9002/odata2webservices/OrderIO/PaymentTransactions to update paymentTransaction1a with the following body:
 Sample Code
{
 "code": "paymentTransaction1a", "requestId": "Updated-RequestId", "order": { "code": "order1" } }
The ItemSavedEvent (update) and ItemUpdatedEvent are sent for the parent order1 pk.

## Immediate Retry For Webhooks

By default, webhooks include an immediate retry mechanism. When webhooks make a request to a Consumed Destination, the external system might return an error response for the following reasons:
4xx errors are returned if the congured destination endpoint doesn't exist, the request is malformed, or other errors related to an incorrect request. You need to address 4xx errors from the sender system conguration. The request is not retried. 5xx errors are the result of a temporary issue with the destination system, for example an Internal Server Error or an intermittent outage. In both cases, the request is correct, and making the request when the system is back up results in a success response. For 5xx errors, the request is retried once with a ten-second interval from the previous attempt.

## Performance Implications And Best Practices For Webhooks

As a performance optimization measure, webhooks are processed asynchronously. Each SAP Commerce Cloud instance uses an internal queue to to temporarily store ItemSavedEvents events prior to processing. There is a congurable number of threads consuming ItemSavedEvents from the internal queue. Webhooks are generally processed in near real-time. However, if webhooks are processed slower than they are produced, ItemSavedEvents can begin accumulating in the internal queue while waiting for processing. When the queue capacity is reached, new ItemSavedEvents are discarded until the queue can accept more items for processing. The time it takes for the webhook subscriber to receive a webhook and return an HTTP response to SAP Commerce Cloud directly affects how many webhooks are processed. Therefore, webhook subscribers should be optimized to process the webhook asynchronously and immediately return an HTTP 20x response to SAP Commerce Cloud.

This is   For more    the SAP Help  111 The following table contains the related conguration parameters:

| Default                                                                                                                     |       |                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameter                                                                                                                   | Value | Description                                                                                                                                                                                                                                                                                                                                   |
| webhookservices.taskexecutor.pool.size                                                                                      | 10    | The number of threads processing the webhook notications. Increasing the value of the webhookservices.taskexecutor.pool.size property increases the number of webhooks that are concurrently sent to the webhook subscriber. Be careful not to increase the concurrent sending of webhooks to a level that overwhelms the webhook subscriber. |
| webhookservices.taskexecutor.queue.capacity 10 000 The maximum number of items awaiting notication processing in the queue. |       |                                                                                                                                                                                                                                                                                                                                               |

Delivery Guarantees for Webhooks Due to the concurrent nature of webhook processing, events are not guaranteed to be delivered in the order they are generated. At Least Once (ALO) delivery of webhooks is currently not guaranteed. See the above section "Performance implications and Best Practices for Webhooks" for information on usage scenarios that can result in events being discarded.

Webhook Deleted Items Cache The deleted items are cached in two cache regions, webhookDeletedItemCacheRegion and webhookConvertedItemCacheRegion, to provide the needed information to generate the webhook payload after the items are deleted. The cached values are cleared from the cache as soon as they are retrieved from the cache. Clearing these two cache regions is disabled from the SAP Commerce Cloud Administration Console.

Parameter

Default Value Description

webhookservices.cache.maxEntries 10000 The cache region size. webhookservices.cache.eviction.policy First In,

First Out (FIFO)

The Eviction strategy. Elements are evicted in the same order as they come in. When a PUT call is made for a new element, and assuming that the maximum limit is reached for the memory store, the element that was placed rst (First-In) in the store is the candidate for eviction (First-Out). For more information, see Region Cache.

webhookservices.cache.ttlSeconds 120 The maximum number of seconds an element can exist in the cache.

POJO Integration Object Webhook Business Event Type Cache For POJO Integration Object webhooks, the business event listener listens to all events that extend the AbstractEvent type. Due to the high volume of events, WebhookBusinessEventTypeCache lters out the events that aren't congured as webhook business events and stores the event types that are congured as webhook business events in WebhookConguration therefore making them supported Business Events.

 Note WebhookBusinessEventTypeCache is disabled when webhookservices.businessEventTypeCache.maxEntries=0 or cache.legacymode=true. Disabling WebhookBusinessEventTypeCache can negatively impact the smooth operation of the system. Keep the cache enabled to ensure optimal performance and efficiency.

| Default                                                                      |                                                                                                                                    |                        |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| Parameter                                                                    | Value                                                                                                                              | Description            |
| webhookservices.businessEventTypeCache.maxEntries                            | 1000                                                                                                                               | The cache region size. |
| webhookservices.businessEventTypeCache.eviction.policy Least                 | The Eviction strategy. For each GET call on the element, the number of hits is updated. When a PUT call is made for a new element, |                        |
| Frequently                                                                   | and assuming that the maximum limit is reached for the memory store, the element with least number of hits, the Less Frequently    |                        |
| Used (LFU) Used element, is evicted. For more information, see Region Cache. |                                                                                                                                    |                        |

## Webhook Service Meta Api

The Webhook Service Meta API provides RESTful endpoints to POST (create), GET (read), PATCH (update), and DELETE webhook congurations.

 Note To access the Webhook Service Meta API, users must be part of both the integrationadmingroup and the webhookservicegroup.

The Webhook Service Meta API is available via the WebhookService service and is included with the webhookservices extension. The API allows creation and auto-creation of consumed destinations and their related entities. Integration Objects can be referenced from the webhook congurations but cannot be created or auto-created using this API. For examples on how to use the Webhook Service Meta API, see Webhook Service Meta API Implementation Examples.

Creating Webhooks Using the Backoffice Integration UI Tool Create webhooks in the Backoffice Integration UI Tool.

Context Note This page may contain information about features that were only introduced in an update release. Ensure you are always on the latest release to be able to make use of all xes, security updates, and features. For a complete list of what was introduced in each update release, see What's New.

Procedure This is   For more    the SAP Help  112 1. Log in to Backoffice.

2. From the dropdown arrow in the upper-left corner of the page, select Integration UI Tool. 3. From the leftside menu, select Webhooks. 4. Select the Add icon to create a WebhookConguration. 5. Select an Integration Object. 6. Do one of the following:
Select a Consumed Destination.

 Note Valid consumed destinations for webhooks must contain the "webhookServices" Destination Target.

Select Create a New Consumed Destination, then provide the following mandatory values:
a. ID b. URL
c. Destination Target (select "webhookServices" as the Destination Target)
d. (Optional) Credential (select an existing one or create a new one)
 Note To prevent webhook notications being sent when the webhook's consumed destination is inactive, toggle.webhookservices.destination.active.enabled is set to true by default. For more information on conguring consumed destinations, see Destination Conguration.

7. (Optional) Select a lter.

 Note Only lter locations of type model:// are supported. When editing a filterLocation, specifying a location other than model:// results in an error. Also, make sure that the filterLocation points to a script with proper formatting or an error is thrown when trying to use the webhook.

8. Select one of the following event types to trigger webhook notications:
Item Saved (default) Item Created Item Updated Item Deleted 9. Select Create.

 Note To delete a webhook, choose one from the list of available webhooks, then select the Delete icon. When deleting an Integration Object associated with a webhook, you must rst delete the webhook before you are able to delete the Integration Object.

## Validating Webhook Congurations

Validate webhook congurations to conrm that the congurations work, including any optional lters.

Context Using a mocked JSON payload based on the webhook conguration for the selected Integration Object, or either creating or selecting an Integration Object instance, you can test webhook congurations to ensure that they are sent successfully. Webhook lters are validated only against ITEM SELECTION.

Procedure 1. Log in to Backoffice.

2. From the dropdown arrow in the upper-left corner of the page, select Integration UI Tool. 3. From the leftside menu, select Webhooks. 4. Select a webhook conguration. 5. Select (Validate Webhook Conguration). 6. Select either the MOCK JSON or ITEM SELECTION tab. 7. Select Send Payload.

If the request isn't successful, check the warning or error message or error log.

Integration Object Modeling via Backoffice Use Modeling to create Integration Objects and Plain Old Java Object (POJO) Integration Objects.

 Note This page may contain information about features that were only introduced in an update release. Ensure you are always on the latest release to be able to make use of all xes, security updates, and features. For a complete list of what was introduced in each update release, see What's New.

This is   For more    the SAP Help  113 In the Backoffice Integration UI Tool, you can:
Create an Integration Object or a Plain Old Java Object (POJO) Integration Object.

 Note An Integration Object uses any Type located in the Type system as its root, whereas the POJO Integration Object is based off of a class that extends AbstractEvent as its root.

Delete an Integration Object. View Integration Object metadata in an ImpEx format, JSON, or in an EDMX schema.

The Impex View displays the ImpEx representation to create the Integration Object. This view is helpful for debugging problems with the metadata associations. Save any changes to an Integration Object in the editor before you can view it in the Metadata Viewer. The EDMX View displays the XML schema that denes the Integration Object. This view shows the entities, properties, and associations that formulate the Integration Object. The JSON View uses the EDMX schema attributes to dynamically generate the structure of a dummy payload, and provides an example of the service's structure. The Endpoint Path eld displays the path to view the service's endpoint. Map of map attributes are unsupported in the JSON view due to the complexity of nesting. If you select such attributes, the generated JSON indicated the attributes that are unsupported.

 Note You can copy-paste the JSON example payload as a starting point for your own example payload. Do not import the JSON example payload as it is unlikely to work due to the inability to predict payload requirements such as data persistence references and expected hooks.

Classication Attributes The Modeling view supports viewing classication attributes and their details, renaming classication attributes, and cloning Integration Objects that contain classication attributes. Perform each of these actions in the same way as you do for regular attributes. However, you cannot set most classication attributes to Unique, Autocreate, or change their type. The exception is reference type classication attributes, which you can set to Autocreate.

 Note Before modeling an Integration Object, please keep in mind that only primitive attributes can be localized and not entities or complex objects. Also, POJO Integration Objects do not support classication attributes.

Meta API Permissions For each request and method type in the following table, membership in both of the user groups listed is required.

| Request and Method                                                                       | Required User Groups                           |
|------------------------------------------------------------------------------------------|------------------------------------------------|
| GET /IntegrationService/<someURLsegment>                                                 | integrationservicegroup, integrationadmingroup |
| POST /IntegrationService/<someURLsegment> integrationservicegroup, integrationadmingroup |                                                |

## Modeling Features

The Modeling interface in the Backoffice Integration UI Tool provides several useful features such as a details view, and the options to rename attributes and clone Integration Objects.

 Note This page may contain information about features that were only introduced in an update release. Ensure you are always on the latest release to be able to make use of all xes, security updates, and features. For a complete list of what was introduced in each update release, see What's New.

The following features are available for creating, editing, and viewing Integration Objects in the Integration Object Modeling view.

Filter Click (Filter) to view all or some of the available attributes of the selected Integration Object. The options are Show All and Only Selected. Click Only Selected to display only the attributes marked with a checkmark. You can select an attribute by clicking on its row. Some attributes are preselected.

Refresh Make sure to save any changes to an Integration Object before clicking Refresh. Clicking Refresh when editing an Integration Object clears the tree view and refreshes the dropdown list to show changes to the Integration Objects made in Backoffice or by ImpEx. Any unsaved changes are lost. However, the view refreshes automatically after you save.

META (Metadata View)
 Note This feature is not available for POJO Integration Objects.

Clicking (META) while modifying an Integration Object shows only the saved version of the object. Save your changes to see them in the META view. You can view and download a representation of the Integration Object in ImpEx, EDMX, or a sample JSON format.

 Note For JSON, there are two views: The Persistence view and the Outbound view. The Persistence view displays information included in a request message. The Outbound view is a representation of what the system is sending in a payload, which includes any read-only and virtual attributes.

This is   For more    the SAP Help  114 Visualizer On the Visualizer tab, you can view attributes and attribute data types for the selected Integration Object in a graphical format. The visualizer also shows the relationships between attributes. Use the zoom buttons or scroll to zoom in and out. Click and drag to move the image frame or use the arrow buttons. Hover over any box for a tooltip and click and drag to rearrange the boxes. To reset a rearranged view to show all nodes, click . Click Download to save a PNG copy of the graph. The image saves in its current arrangement. The relationships between parent and child nodes in the visualizer are displayed in the following way:
"0..1": The parent node points to a single child node. "*": The parent node points to multiple child nodes.

 Note When "Nullable=true" is specied for a navigation property in the Integration Object EDMX le, the parent node might not point to any instance of a child node.

Clone Integration Object The cloning operation attempts to determine the root item. If you do not set a root item for the Integration Object, the cloning operation attempts to determine the root using an algorithm. If the process cannot determine a root, a warning message appears. If you set two roots for the item, the process attempts to nd a single, appropriate root item.

1. To create a copy of a selected Integration Object, click (Clone Integration Object).

2. Enter a new, unique name for the cloned Integration Object. 3. Select the Integration Object type. 4. Click Conrm.

Audit Report Downloader An audit report details changes that have been made to a specic Integration Object, including modied properties, attributes and items that have been added or removed, the name of the user who made changes, and the date and time of the last update. The payloads are listed in timestamp order from newest to oldest.

 Note Only an administrator can generate audit reports.

1. Select an Integration Object from the drop-down menu.

2. Click the (Audit Report Downloader).

The audit report downloads as an HTML le. The report contains the following information:
Payload (levels: IntegrationObject IntegrationObjectItems IntegrationObjectItemAttributes ) changingUser (name of the user who made changes) TimeStamp (date and time of the last change to the payload)
Changes to a payload are color-coded:
Green (added since the last payload) Red (deleted since the last payload) Yellow (status changed since the last payload, for example, an attribute value changes from true to false)
Add Classication Class Note This feature is not available for POJO Integration Objects.

To add classication attributes to Product types and subtypes, click . In the window that appears, the list on the left shows available classication attributes. Select an attribute and click Add to move an attribute into the included attributes on the right side. When you click the Add button at the bottom of the window to save your selections, the tool validates your selections and adds all valid attributes. If any of the selected attributes have duplicate names, a warning appears and the tool highlights the duplicate attributes. You can resolve the warning by deselecting or providing unique names for each of the attributes. If an attribute is mandatory, it automatically appears in the list of included attributes.

 Note The Add Classication Class tool does not support non-Product type entities. When you select a non-Product type object, the icon is disabled.

View Details Note This feature is not available for POJO Integration Objects.

This is   For more    the SAP Help  115 Click and select View Details to view an attribute's properties, as provided by the Type system. Attributes with the parameters Optional=false and Unique=true are preselected and disabled.

For classication attributes, the details view shows only the attributes relevant to classication attributes. The system displays only details from the Type system, and does not show userdened details.

For both the Unique and Autocreate columns, a greyed-out checkbox that's unchecked means that option is either not applicable to or supported for that particular attribute. For the Unique column, a greyed-out checkbox that's checkmarked means that attribute is unique by default. Checkmarked attributes that are highlighted in blue can be deselected, but greyed-out checkmarked attributes are required and can't be deselected. All checkmarked attributes are included in the Integration Object.

Type system unique attributes are unique by default (greyed-out checkbox) and are read-only. If the attribute is not unique by default, you can select that option by checkmarking the box. You can't mark Map or Collection attributes as unique. For more information on the unique feature, see IsUnique. You can't mark Primitive attributes as autocreate. You can mark CollectionType attributes as autocreate if they aren't Primitive or Abstract. For more information on the autocreate feature, see Deep Persistence.

 Note You can't mark most classication attributes as unique or autocreate. The exception is reference type classication attributes, which you can set to autocreate.

Rename Attributes Note This feature is not available for POJO Integration Objects.

An attribute name, or alias, appears in the metadata and persists with the Integration Object. Renaming an attribute does not change the name of the attribute in the Type system. The Alias eld accepts only alphanumeric characters. You cannot rename an attribute to any of the original qualier names of any attributes within the same Composed Type. Additionally, all attribute names must be unique within the same entity. Attributes with the same name under different entities do not change.

1. Click and select Rename Attributes.

2. Enter a new attribute name in the Alias (New) eld.

 Note For classication attributes and virtual attributes, the qualier name (classication attributes) and the descriptor name (virtual attributes) can be identitcal to other classication or virtual attributes, but the aliases must be different for each attribute.

3. Click Conrm.

To revert to the original attribute name, you can enter the original name in the Alias (New) eld or leave the eld blank.

Change Attribute Type Note This feature is not available for POJO Integration Objects.

You can change the type of a composed type attribute to any inherited type one level below the current type. If an attribute does not have any subtypes or is an Atomic type, the Change Type option does not appear in the menu. Because the attribute tree view in Backoffice is structured by subtype, changing an attribute type can restructure the attribute tree view. If there is more than one reference to an attribute in the selected Integration Object, changing the subtype in one attribute changes it in all references. You can revert to the original type by selecting it from the Select Subtype list.

 Note While you can change abstract types, you cannot mark them as autocreate. Additionally, you cannot change the type of reference classication types.

1. Click and select Change Type.

2. Select a new type from the Select Subtype list. 3. Click Conrm.

Attribute Status Denitions Note This feature is not available for POJO Integration Objects.

You can view Integration Object attribute statuses under the Status column.

Required - must be included in the Integration Object's denition (cannot be removed). Read Only - attributes are read only at the API-level, but can still be used for modeling. Values can only be requested (GET), not posted (POST), or patched (PATCH). The requested values are used in outbound-sync payloads. Not Supported - attributes that are not handled by APIs (cannot be modeled).

This is   For more    the SAP Help  116 Multiple Type Denitions Note You can't create multiple type denitions via Backoffice. Use either ImpEx or Meta API.

You can import an Integration Object that contains multiple denitions for a type. For example, the following ImpEx is for an Integration Object that contains the type "Media" with one denition as "Media" and the other denition as "Media2": When making any changes to a type that has multiple denitions, only the type that contains the denition you're modifying is affected. For example, if you change the type for an attribute with the type code "Media", it's only changed for "Media" and not attributes with the Integration Object Item code "Media2". The same is true when renaming or retyping an attribute.

Item Type Match Note This feature is not available for POJO Integration Objects.

You can use the Item Type Match feature to set item type match restrictions when searching for Integration Object Items.

1. Select an Integration Object.

2. Click . 3. From the drop-down menu, select the item type restriction for an Integration Object Item. The available values are:
ALL_SUB_AND_SUPER_TYPES - Searches for matching items in all supertypes, subtypes, and the current item type ALL_SUBTYPES - Searches for matching items in all subtypes and the current item type RESTRICT_TO_ITEM_TYPE - Searches for matching items of the same item type Note For abstract or enum types, the only available value is ALL_SUBTYPES. When using multiple type denitions, only one ItemTypeMatch per type is allowed. If you import an Integration Object that contains different matches for the same type, whether by ImpEx or Meta API, the rst entry for the same type is the one that applies and the rest are ignored.

4. Click Save.

For more information, see Conguring Item Type Match for Integration Objects and Items.

Create Virtual Attribute Note This feature is not available for POJO Integration Objects.

You can create virtual attributes to add to Integration Objects.

1. Select an Integration Object.

2. Select (Create Virtual Attribute). 3. Do one of the following:
Select an existing virtrual attribute descriptor from the dropdown menu. All elds except for "Virtual Attribute Alias" will be populated. Create a new virtual attribute and ll in the following elds:

| Field             | Description                                                                                                                                                                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Virtual Attribute | The name of the virtual attribute descriptor. More than one virtual attribute can share the same descriptor code, but each virtual attribute must have a unique alias                                                                          |
| Descriptor Code   | to differentiate it from the others.                                                                                                                                                                                                           |
| Script Location   | The location of the script used for the virtual attribute. Select a script location from the dropdown menu. There is no type verication to match the virtual attribute type and script's return type. Example script location: model://logLoc. |

| Field                    | Description                                                                                                                                                                                                                                                  |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Virtual Attribute's Type | The virtual attribute's type. If a value isn't specied, it defaults to java.lang.String. Make sure that the type selected matches the return type of the selected script. There is no type verication. See Virtual Attributes for a list of supported types. |
| Virtual Attribute Alias  | Alternative name for a virtual attribute descriptor. An alias is only required when one or more attributes share the same name (either a qualier or a descriptor). Otherwise, providing an alias is optional.                                                |

4. Select Create.

 Note To remove a virtual attribute, deselect it from the Integration Object, then save the change. To delete a virtual attribute descriptor model, go to Backoffice Administration Cockpit System Types , then search for the virtual attribute descriptor and delete it.

Modeling Integration Object Metadata You can congure metadata in the Backoffice Integration Tool UI to dene the data load pattern for an Integration Object.

Prerequisites Install Backoffice and have log in credentials.

Context You can model Integation Objects with various methods, including ImpEx, or the IntegrationService API. This topic describes how to model metadata for an Integration Object in Backoffice.

Procedure 1. Log in to Backoffice.

2. Select the dropdown arrow at the top of the page and select Integration UI Tool. 3. From the left menu, select Integration Object Modeling. 4. Select + to open the Create Integration Object window. 5. In the Name eld, enter the name of the new service. 6. In the Root Type list, select the root type of the object. 7. From the Integration Type list, select the type of integration. If no type is selected, the system defaults to Inbound. 8. Select Create. Select OK to conrm the new service.

On the left side of the window, a tree view populates with the Type System composed types. The right side shows a list of the Integration Object attributes.

9. Dene the Integration Object by selecting attributes of the composed types under the root type in the hierarchy.

10. Select any additional attributes. Required attributes are selected by default. Marking any attribute as unique automatically selects the attribute. To add classication attributes, select
. For more information, see Add Classication Class in Modeling Features.

 Note An error message that the Integration Object needs further conguration means that the base Integration Object is created and saved, but a unique key is likely missing for one or more of the minimal entity types in the Integration Object's denition. Mark at least one attribute as unique to correct this issue.

11. Starting from the root, dene at least one attribute for any composed type that you selected as part of the denition. Select to check the Unique box for at least one attribute to use as a key.

 Note The other composed types listed are optional. You do not need to associate attributes.

12. To save the metadata, select Save. Select Save Denition to conrm.

Modeling POJO Integration Objects via Backoffice Use the Backoffice Integration UI Tool to model POJO Integration Objects.

Prerequisites Install Backoffice and have log in credentials.

Context Note This page may contain information about features that were only introduced in an update release. Ensure you are always on the latest release to be able to make use of all xes, security updates, and features. For a complete list of what was introduced in each update release, see What's New.

You can model Integation Objects with various methods, including ImpEx, or the IntegrationService API. This topic describes how to model metadata for an Integration Object in Backoffice.

Procedure 1. Log in to Backoffice.

2. From the dropdown arrow in the upper-left corner of the page, select Integration UI Tool. 3. From the left menu, select Integration Object Modeling. 4. Select Class Modeling. 5. Select + to open the Create Integration Object for Class Modeling window. 6. In the Name eld, enter the name of the new service.

7. In the Root Class eld, select the root class 8. Select Create. Select OK to conrm the new service.

On the left side of the window, a tree view populates with the root class. The right side shows a list of the Integration Object attributes.

9. Dene the Integration Object by selecting attributes of the classes under the root type in the hierarchy.

10. Select any additional attributes.

 Note An error message that the Integration Object needs further conguration means that the base Integration Object is created and saved, but a unique key is likely missing for one or more of the minimal entity types in the Integration Object's denition. Mark at least one attribute as unique to correct this issue.

11. Starting from the root, dene at least one attribute for any class that you selected as part of the denition. Select to check the Unique box for at least one attribute to use as a key.

 Note If you want to restrict the ability to update the root class of a POJO Integration Object, set toggle.root.update.restriction.enabled to true. The default value is false.

12. To save the metadata, select Save. Select Save Denition to conrm.

Integration Object Authentication In Backoffice, you can authenticate an Integration Object with OAuth or Basic authentication. Exposing Integration Objects as APIs with enhanced authentication requires an InboundChannelConguration, which denes the type of authentication used for API requests. You can set the authentication type to Basic or OAuth in Backoffice or using the InboundChannelConguration Meta API. In Backoffice, you can also search for, add, delete, and edit InboundChannelCongurations.

 Note Some icons in the Authentication view are standard widgets that are not functional for conguring exposed APIs. Export to CSV, Compare, and Bulk Edit are not functional. See Exposing an Integration Object as an API for more information about the Backoffice and InboundChannelConguration Meta API functionality.

For more information about the enhanced authorization and authentication feature, see Enhanced Authentication.

Integration Object Authorization In the Backoffice Integration UI Tool, you can view type-level permissions and set up access rights for users working with Integration Objects.

Integration API Request Monitoring View the results of inbound and outbound Integration API requests using the Integration UI Tool in Backoffice, and manage the data retention period for such requests. You can enable request monitoring for inbound and outbound requests, get information about request statuses, payloads, and errors. You can also manage the retention duration and data cleanup job schedule for persisted request data. You can perform an advanced search based on specic properties of the request or use the search icon to collapse the search section.

Monitoring Setup To disable or enable data monitoring, set the Boolean value for the inbound and outbound monitoring properties separately. The default setting for both is false.

For inbound monitoring, set inboundservices.monitoring.enabled. For outbound monitoring, set outboundservices.monitoring.enabled.

 Note You can enable both properties at runtime using the instructions provided here: Applying Properties to All Platform Services.

The following topics describe how to use monitoring.

Inbound Monitoring You can view the details of inbound requests and any errors in Backoffice or by using the Meta API. Outbound Monitoring You can monitor outbound Integration Object requests via Meta API or by using Backoffice.

This is   For more    the SAP Help  119 Monitoring Retention Policy You can adjust the retention policies for the data that the system persists for inbound and outbound requests. Conguring Payload Retention You can change whether, and for how long, the system retains payloads for inbound and outbound integration requests.

## Inbound Monitoring

You can view the details of inbound requests and any errors in Backoffice or by using the Meta API. An Inbound Request object captures information about Integration API requests. An Inbound Request includes the following elds, by which you can also search for requests using the search lters:
integrationMessageId - The integrationMessageId provided in the request header. The integrationMessageId allows the user to trace the Inbound Request back to the original request. This eld is optional, and it can be blank.

integrationKey - Derived from the payload. For more information, see The EDMX Key Value. type - Set to the Integration Object type, for example InboundProduct, which comes from the service part of the request URI (for example, https://localhost:9002/odata2webservices/InboundProduct/Products). payload - Payload of the request. The payload persists as IntegrationApiMedia in Backoffice. If the payload fails to persist, the eld can be empty. status - Status of the request. Values can be SUCCESS or ERROR. SUCCESS means that the Integration Object persisted successfully. Otherwise, the status is set to ERROR. user - User who made the request. The API logs the user whether the request status is SUCCESS or ERROR.

sapPassport - The value of the SAP-PASSPORT header, when provided with the request. HTTP Method - Indicates whether the request type was POST, DELETE, or PATCH.

To learn about some of the less common uses of the Integration UI Tool for monitoring inbound requests, see Inbound Batch API Monitoring and Inbound Bulk API Monitoring.

Inbound Request Errors Errors is a collection of InboundRequestErrors that may have occurred during a request. It consists of:
code: The code for the error that occurred. message: An informative exception message for the error.

Monitoring Inbound Integration Requests using the Meta API
You can view inbound monitoring data using the Meta API. To do so, membership is required in the following user groups:

| Request and Method                                                            | Required User Groups   |
|-------------------------------------------------------------------------------|------------------------|
| GET /InboundIntegrationMonitoring/<someURLsegment> integrationmonitoringgroup |                        |

The following example requests data for inbound requests with error statuses expanded in the response. Request URL Response Body GET https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests?$expand=status,errors { "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568915657343%7C%7C')", "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568915657343%7C%7C')", "type": "HybrisCommerceOData.InboundRequest" }, "requestIntegrationKey": "", "sapPassport": null, "type": "IntegrationService", "creationtime": "/Date(1568915657343)/", "messageId": "", "integrationKey": "1568915657343||", "errors": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequestErrors('1568915657339%7C15 "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequestErrors('1568915657339%7C1 "type": "HybrisCommerceOData.InboundRequestError" }, "creationtime": "/Date(1568915657339)/", "message": "Media type text/plain is not supported.", "code": "unknown_error",
This is   For more    the SAP Help  120
 "integrationKey": "1568915657339|1568915657343||",
 "inboundRequest": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequestErrors('1568915657339 } } } ] }, "status": {
 "__metadata": {
 "id": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/IntegrationRequestStatuses('ERROR')", "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/IntegrationRequestStatuses('ERROR')", "type": "HybrisCommerceOData.IntegrationRequestStatus" }, "code": "ERROR", "integrationKey": "ERROR" }, "user": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568915657343%7C%7C')/user" } } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568915679339%7C%7Cpcm')", "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568915679339%7C%7Cpcm')", "type": "HybrisCommerceOData.InboundRequest" }, "requestIntegrationKey": "pcm", "sapPassport": null, "type": "IntegrationService", "creationtime": "/Date(1568915679339)/", "messageId": "", "integrationKey": "1568915679339||pcm", "errors": { "results": [] }, "status": { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/IntegrationRequestStatuses('SUCCESS')", "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/IntegrationRequestStatuses('SUCCESS')", "type": "HybrisCommerceOData.IntegrationRequestStatus" }, "code": "SUCCESS", "integrationKey": "SUCCESS" }, "user": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568915679339%7C%7Cpcm')/user" } } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568916370473%7C%7CExampleProduct') "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568916370473%7C%7CExampleProduct' "type": "HybrisCommerceOData.InboundRequest" }, "requestIntegrationKey": "ExampleProduct", "sapPassport": null, "type": "IntegrationService", "creationtime": "/Date(1568916370473)/", "messageId": "", "integrationKey": "1568916370473||ExampleProduct", "errors": { "results": [] }, "status": { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/IntegrationRequestStatuses('SUCCESS')", "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/IntegrationRequestStatuses('SUCCESS')", "type": "HybrisCommerceOData.IntegrationRequestStatus" }, "code": "SUCCESS", "integrationKey": "SUCCESS" }, "user": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568916370473%7C%7CExampleProd }
This is   For more    the SAP Help  121

 }
 }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568923304103%7C%7CExampleProduct') "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568923304103%7C%7CExampleProduct' "type": "HybrisCommerceOData.InboundRequest" }, "requestIntegrationKey": "ExampleProduct", "sapPassport": null,
 "type": "IntegrationService",
 "creationtime": "/Date(1568923304103)/", "messageId": "", "integrationKey": "1568923304103||ExampleProduct", "errors": { "results": [] }, "status": { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/IntegrationRequestStatuses('SUCCESS')", "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/IntegrationRequestStatuses('SUCCESS')", "type": "HybrisCommerceOData.IntegrationRequestStatus" }, "code": "SUCCESS", "integrationKey": "SUCCESS" }, "user": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568923304103%7C%7CExampleProd } } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568925726594%7C%7C')", "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568925726594%7C%7C')", "type": "HybrisCommerceOData.InboundRequest" }, "requestIntegrationKey": "", "sapPassport": null, "type": "IntegrationService", "creationtime": "/Date(1568925726594)/", "messageId": "", "integrationKey": "1568925726594||", "errors": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequestErrors('1568925726565%7C15 "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequestErrors('1568925726565%7C1 "type": "HybrisCommerceOData.InboundRequestError" }, "creationtime": "/Date(1568925726565)/", "message": "Could not find an entity set or function import for 'IntegrationObject'.", "code": "unknown_error", "integrationKey": "1568925726565|1568925726594||", "inboundRequest": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequestErrors('1568925726565 } } } ] }, "status": { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/IntegrationRequestStatuses('ERROR')", "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/IntegrationRequestStatuses('ERROR')", "type": "HybrisCommerceOData.IntegrationRequestStatus" }, "code": "ERROR", "integrationKey": "ERROR" }, "user": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568925726594%7C%7C')/user" } } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568925735812%7C%7Cmpc')",
 "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568925735812%7C%7Cmpc')",
 "type": "HybrisCommerceOData.InboundRequest" }, "requestIntegrationKey": "mpc", "sapPassport": null, "type": "IntegrationService", "creationtime": "/Date(1568925735812)/", "messageId": "", "integrationKey": "1568925735812||mpc", "errors": {
 "results": []
 }, "status": { "__metadata": { "id": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/IntegrationRequestStatuses('SUCCESS')", "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/IntegrationRequestStatuses('SUCCESS')", "type": "HybrisCommerceOData.IntegrationRequestStatus" }, "code": "SUCCESS", "integrationKey": "SUCCESS" }, "user": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/InboundIntegrationMonitoring/InboundRequests('1568925735812%7C%7Cmpc')/user" } } } ] } }

## Inbound Batch Api Monitoring

When creating or updating an integration object in a batch with multiple change sets, the change sets are recorded as a single Inbound Request. Changesets within a batch request are persisted sequentially, in the order they are submitted in the batch request. The response returns the batch entities in the same order in which the requests were sent. The API attempts to persist an entire batch at once. If a changeset or entry within a batch is invalid, the entire batch with the invalid changeset does not persist and returns a 400 Bad Request response. In general, batch request performance is improved with fewer, larger batches, up to an upper threshold of batch size. You may want to experiment with the best batch size for your setup. In the following example, the client submits a batch request that includes two change sets, one for English and one for German. The Inbound Request created contains data both change sets in the payload. If one change set results in an error, the status of the Inbound Request changes to ERROR. The status is SUCCESS when both change sets process correctly.

--batch Content-Type: multipart/mixed; boundary=changeset
--changeset Content-Type: application/http Content-Transfer-Encoding: binary POST Products HTTP/1.1 Content-Language: en Accept: application/json Content-Type: application/json { "@odata.context": "$metadata\#Products/$entity", "code": "1000003", "name": "the name", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } } --changeset Content-Type: application/http Content-Transfer-Encoding: binary POST Products HTTP/1.1 Content-Language: de Accept: application/json Content-Type: application/json { "@odata.context": "$metadata\#Products/$entity", "code": "1000003", "name": "der Name", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } } --changeset-- --batch--
The following image shows a listing of an Inbound Request for one batch that contains two change sets.

## Inbound Bulk Api Monitoring

When creating or updating an integration object in bulk, for example a payload with multiple batches, each batch is recorded as a separate Inbound Request. In the following example, the client submits a bulk request that includes two different batches, one for English and one for German. The system records two Inbound Requests. Each Inbound Request has a separate payload and status. If one request fails, the other request is not affected.

--batch Content-Type: multipart/mixed; boundary=changeset --changeset Content-Type: application/http Content-Transfer-Encoding: binary POST Products HTTP/1.1 Content-Language: en Accept: application/json Content-Type: application/json { "@odata.context": "$metadata\#Products/$entity", "code": "1000003", "name": "the name", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } } --changeset-- --batch Content-Type: multipart/mixed; boundary=changeset --changeset Content-Type: application/http Content-Transfer-Encoding: binary POST Products HTTP/1.1 Content-Language: de Accept: application/json Content-Type: application/json { "@odata.context": "$metadata\#Products/$entity", "code": "1000003", "name": "der Name", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } } --changeset-- --batch--
The following image shows a listing of Inbound Requests for two batches. One batch loaded successfully, the other has an Error.

| 7/6/2024   |
|------------|

## Troubleshooting Inbound Request Errors

Inbound request error handling follows the guidelines outlined in this topic.

Request Formatted Incorrectly If the request body to create or update an integration object is malformed and cannot be parsed, then the system records one Inbound Request. The payload of the Inbound Request contains the entire request body.

Batch Request Exceeds Limits If the number of batches in a bulk request exceeds the limit allowed, then the system records one Inbound Request without saving the payload. This is to prevent overwhelming the system with too much data.

Request Results in a Global Problem If the batch or bulk change set request results in a global problem, then the system records one Inbound Request that contains the entire request body.

## Outbound Monitoring

You can monitor outbound Integration Object requests via Meta API or by using Backoffice.

Each call to OutboundServiceFacade.send() creates a new OutboundRequest object in the system. Additionally, all requests initiated with outbound sync are visible in Outbound Monitoring. You can monitor these requests, along with the information stored for each outbound request, as well as search for requests and errors by eld. Outbound requests contain the following elds that can also be used for ltering requests in Backoffice:
integrationMessageId - The integrationMessageId provided in the request header. The integrationMessageId allows the user to trace the Outbound Request back to the original request. This eld is optional, and it can be blank.

integrationKey - Derived from the payload. For more information, see The EDMX Key Value. type - Set to the Integration Object type, for example OutboundProduct, which comes from the service part of the request URI (for example, https://localhost:9002/odata2webservices/OutboundProduct/Products). payload - Payload of the request. The payload persists as IntegrationApiMedia in Backoffice. If the payload fails to persist, the eld can be empty.

 Note To enable payload persistence, set outboundservices.monitoring.success.payload.retention=true.

status - Status of the request. Values can be SUCCESS or ERROR. SUCCESS means that the Integration Object persisted successfully. Otherwise, the status is set to ERROR. user - User who made the request. The API logs the user whether the request status is SUCCESS or ERROR. sapPassport - The value of the SAP-PASSPORT header, when provided with the request. HTTP Method - Indicates whether the request type was POST or DELETE.

All requests for outbound sync and webhooks are captured and displayed in Outbound Monitoring. If the source of the OutboundRequest isn't from either OUTBOUNDSYNC or WEBHOOKSERVICES, the source is set to UNKNOWN.

Outbound Request Errors For any errors that result from an outbound request, the system stores the error message.

 Note To enable outbound request error monitoring, set outboundservices.monitoring.error.payload.retention=true.

Monitoring Outbound Integration Requests using the Meta API
You can view outbound monitoring data using the Meta API. To do so, membership is required in the following user groups:

| Request and Method                                                             | Required User Groups   |
|--------------------------------------------------------------------------------|------------------------|
| GET /OutboundIntegrationMonitoring/<someURLsegment> integrationmonitoringgroup |                        |

The following example shows a request for outbound Integration API request data, with expanded statuses. Request URL
GET https://localhost:9002/odata2webservices/OutboundIntegrationMonitoring/OutboundRequests?$expand=status Response Body
{ "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/OutboundIntegrationMonitoring/OutboundRequests('2a54482a0300e6000053415020436f6d6 "uri": "https://localhost:9002/odata2webservices/OutboundIntegrationMonitoring/OutboundRequests('2a54482a0300e6000053415020436f6d "type": "HybrisCommerceOData.OutboundRequest" }, "requestIntegrationKey": "Online|Default|TESTPRoduct", "sapPassport": "2a54482a0300e6000053415020436f6d6d657263650000000000000000000000000000000000000000002761646d696e000000000000000000000 "type": "OutboundProduct", "destination": "https://localhost:9002/odata2webservices/OutboundProduct/Products", "messageId": "ac84d2e3-df97-44e3-a3d7-ab51c326a83c", "error": null, "integrationKey": "2a54482a0300e6000053415020436f6d6d657263650000000000000000000000000000000000000000002761646d696e000000000000000000 "status": { "__metadata": { "id": "https://localhost:9002/odata2webservices/OutboundIntegrationMonitoring/IntegrationRequestStatuses('SUCCESS')", "uri": "https://localhost:9002/odata2webservices/OutboundIntegrationMonitoring/IntegrationRequestStatuses('SUCCESS')", "type": "HybrisCommerceOData.IntegrationRequestStatus" }, "code": "SUCCESS", "integrationKey": "SUCCESS" } } ] } }
To display only webhook service requests, use the following request:
 Sample Code GET {{fullURL}}/OutboundIntegrationMonitoring/OutboundRequests?$filter=source/code eq 'WEBHOOKSERVICES'

## Monitoring Retention Policy

You can adjust the retention policies for the data that the system persists for inbound and outbound requests. The monitoring retention policy denes the request data that the system cleans up, or removes. This section describes the retention policy, how to customize the data retention settings and associated CronJobs, and how to enable or disable inbound and outbound request payload retention. See Integration API Request Monitoring for more details about inbound and outbound requests and monitoring errors.

Retention Policy Because the monitoring data that the inbound and outbound scenarios generate can take a lot of disk space and accumulate over time, it can be helpful to clean up old monitoring data on a regular basis. SAP Commerce Cloud offers a Data Retention Framework that the application uses to clean up old data. The system cleans up the following request types by default:
InboundRequest InboundRequestError IntegrationApiMedia OutboundRequest This is   For more    the SAP Help  126 OutboundRequestMedia The following CronJobs trigger the cleanup processes:
integrationApiMediaCleanupJob is available for users who updated their retention policies prior to version 1811 to clean up monitoring payloads for IntegrationApiMedia without subtypes inboundRequestCleanupCronJob for cleaning up InboundRequests and their associated InboundRequestErrors inboundRequestMediaCleanupCronJob for cleaning up IntegrationRequestMedia outboundRequestCleanupJob for cleaning up OutboundRequests outboundRequestMediaCleanupJob for cleaning up OutboundRequestMedia By default, the CronJobs run every day at midnight and delete data that is more than 7 days old. CronJob triggers and the retention period are congurable through Backoffice. See Conguring Integration API Cron Jobs for information about conguring cron jobs.

Congure Retention Period You can congure the retention period for:
inboundRequestCleanupRule inboundRequestMediaCleanupRule outboundRequestCleanupRule outboundRequestMediaCleanupRule To congure the retention period, follow these steps.

1. In a web browser, navigate to Backoffice.

2. In Backoffice, click System RetentionRule . 3. Select a rule to congure. 4. Update the Retention Time in Seconds. 5. Click Save.

## Conguring Payload Retention

You can change whether, and for how long, the system retains payloads for inbound and outbound integration requests.

Congure Payload Retention You can disable one or more of the payload retention properties, for example, to improve system performance. You can also congure the properties at runtime for troubleshooting purposes. The following values are set by default for each payload retention property:
inboundservices.monitoring.success.payload.retention=false outboundservices.monitoring.success.payload.retention=false inboundservices.monitoring.error.payload.retention=false outboundservices.monitoring.error.payload.retention=false To congure the payload retention settings in the SAP Commerce Cloud Administration Console, follow these steps.

1. In a web browser, navigate https://localhost:9002.

2. Click Platform Conguration . 3. Search for any of the payload retention properties.

4. In the <Value> eld, enter true or false as needed.

5. Click the checkmark to save changes.

Retention Policy Considerations In environments where Integration Objects are continually loaded at a high rate, persisting large amounts of monitoring data can quickly consume database and le system resources. Under these high volume conditions, you can control the amount of monitoring data being stored by adjusting the retention period within the Cleanup cronJobs. To do so, consider running the CronJobs more frequently and decreasing the retention time in the CleanupRules to retain data for a shorter period of time.

If you do not want to inspect the payloads, you can set the payload retention settings to false, as described in this topic.

## Integration Api Security

Secure Integration API endpoints using OAuth or Basic authentication, authorization, and SSL features. User groups and user roles provide security for dened groups and users. See the following topics for details.

Authentication Integration API security offers OAuth 2.0 and Basic security. Authorization There are two ways to handle authorization for Integration APIs. SSL The Integration API redirects requests using only HTTP to an SSL endpoint. Creating Integration API Users Create a new user and assign a user group to allow Integration API permissions. Integration Backoffice Security The Backoffice Integration UI Tool provides Integration Administrator and Integration Agent user roles.

## Authentication

Integration API security offers OAuth 2.0 and Basic security. The Integration API requires authentication. You can secure Integration Objects in the Integration API using OAuth 2.0 or Basic authentication. The Integration API's enhanced authentication feature allows you to secure an endpoint with OAuth 2.0 or Basic authentication. Enhanced authentication uses the InboundChannelConguration (ICC) item type, which exposes an Integration Object and associates it with a specied authentication type. Whether an ICC was created with OAuth 2.0 or Basic authentication, you have the ability to update the authentication type in the ICC. As shown in the following diagram, when determining what type of authentication an Integration Object uses, the Integration API rst determines whether the Integration Object is associated with an InboundChannelConguration. If there is an InboundChannelConguration, the API uses the authentication type specied. If not, the API checks the integrationservices.legacy.authentication.enabled feature ag. By default, the ag is set to false, which means that Integration Object endpoints are not exposed without an ICC. When the ag is set to true, APIs using legacy authentication continue to function.

## Note

When upgrading to SAP Commerce Cloud version 2011 and higher, because the integrationservices.legacy.authentication.enabled feature ag is set to false by default, an InboundChannelConguration is automatically created with Basic authentication for an Integration Object that doesn't have a corresponding ICC. Once created, to set the authentication to OAuth, update the authentication type in the ICC.

If an Integration Object is inaccessible, verify that an ICC was created for it. If no ICC exists, create one using the Integration UI Tool in Backoffice (select Integration API Authentication

![127_image_0.png](127_image_0.png)

Enhanced authentication allows you to authenticate Integration Objects as APIs using OAuth or Basic authentication.

## Legacy Authentication

Legacy authentication requires SearchRestrictions on user groups to secure OData2 Web Services.

 Note Enhanced authentication, which requires an InboundChannelConguration, is enabled by default and is the recommended authentication mode. Legacy authentication does not require an InboundChannelConguration. Legacy authentication is disabled by default (integrationservices.legacy.authentication.enabled=false).

Here are some important things to consider when using legacy authentication:
The odata2webservices extension supports HTTP basic authentication. To get access to any endpoint, provide an HTTP header in every call. For example: Authorization: Basic SomeBase64EncodedCredential. For more information, see HTTP Authentication Specication .

This is   For more    the SAP Help  128 The user must have an SAP Commerce Cloud account.

When the user provides no credentials (no Authorization header), the application returns a 401 error. When the user does not exist or the password does not match, the application returns a 401 error.

## Enhanced Authentication

Enhanced authentication allows you to authenticate Integration Objects as APIs using OAuth or Basic authentication.

 Note Enhanced authentication is the default authentication mode for SAP Commerce Cloud.

As an alternative to legacy authorization, enhanced authorization provides the ability to use OAuth or Basic authorization along with the SAP Commerce Cloud Platform's role-based access rights to securely expose your APIs. See Access Rights for information about the general use of access rights.

To enable APIs to use enhanced authentication, rst create an InboundChannelConfiguration that exposes an Integration Object by associating it with a specied authentication type. To use OAuth authorization, use the IntegrationClientCredentialsDetails item type to congure the client for the client_credentials client grant type. Finally, grant access permissions to the exposed type by user group. For a more detailed explanation of the types, see the sections below. Exposing an Integration Object as an API provides step-by-step examples for the process, from creating an Integration Object to sending a GET request with OAuth.

InboundChannelConguration Item Type An InboundChannelConguration denes the type of authentication used for an Integration Object. The InboundChannelConguration type's key is the Integration Object reference, and references an authenticationType attribute. The value of AuthenticationType comes from an enum.

IntegrationClientCredentialsDetails IntegrationClientCredentialsDetails denes the user authorized to make requests in a session. The item type extends the type system's client_credentials grant type and supports only the OAuth authentication ow. When dening the user, keep in mind:
User is a required eld. The user "admin" is not permitted.

You cannot change the user after dening it.

Related Information Integration Object Authentication Exposing an Integration Object as an API Exposing an Integration Object Using Backoffice

## Authorization

There are two ways to handle authorization for Integration APIs.

The enhanced Access Rights-based authorization option is enabled by default and allows administrators to ne-tune access to the Integration Objects and the underlying types. The ag integrationservices.authorization.accessRights.enabled allows you to congure whether Type Access Rights are used for authorization. The ag's default value is true.

The legacy option involves securing Integration Objects using Search Restrictions, as dened in Search Restrictions.

The two available modes are not mutually exclusive. Administrators can create Integration Objects and secure them using both Access Rights and Search Restrictions, however it is not recommended to use them together. Additionally, because platform Access Rights are associated with a Type in the type system, the Integration API's authorization implementation controls the action performed on the Type immediately before persistence or retrieval. This additional layer of security prevents problems such as updates to Types that have no update permissions using a POST request. Such a request might get through the rst layer of security, but the system then checks for the record and determines where changes are requested. The system then rechecks the access rights and applies them at the change level.

Access Rights The feature ag integrationservices.authorization.accessrights.enabled, which is enabled by default, provides a powerful authorization feature for administrators.

Setting Up Access Rights for Integration Objects In the Backoffice Integration UI Tool, set up access rights for users working with Integration Objects. Search Restrictions As part of legacy authentication, you can use SearchRestriction to secure access to Integration Objects that are exposed as OData2 web services.

## Access Rights

The feature ag integrationservices.authorization.accessrights.enabled, which is enabled by default, provides a powerful authorization feature for administrators. Enhanced authorization allows you to restrict access to each Type dened in the IntegrationObjectItemType of the Integration Object. Access Rights control the level of access to the following API verbs:
This is   For more    the SAP Help  129 Create - POST Read - GET
Update - POST, PATCH
Remove - DELETE
This allows integration administrators to nely tune the level of access to Integration Objects by only allowing interaction with certain IntegrationObjectItemTypes. For example, Access Rights could be congured so that a user has access to create Products (POST), but only has Read Access (GET) to Categories. Access Rights are assigned at the type level, not at the Integration Object level. That means that when a user is granted privileges to interact with, for example, the Product type, any Integration Object that contains that type in its denition observes the type-level Access Rights restrictions. For more information on Access Rights and how they work in general, see Access Rights. Access Rights for Administration Meta API Types: The administration Meta API types are the Integration Object Item types associated with the Integration Objects IntegrationService, ScriptService, and OutboundChannelCong. By default, these types are given Read, Create, Update, and Remove access rights for the user group integrationadmingroup. Access Rights for Monitoring Meta API Types: The monitoring Meta API types are the Integration Object Item types associated with the Integration Objects InboundIntegrationMonitoring and OutboundIntegrationMonitoring. By default, the types used for monitoring are only given Read access for the user group integrationmonitoringgroup. Setting Up Access Rights via API
You can enable the permissionswebservices extension to set up access rights (permissions) for users by adding permissions for system types. For more information, see permissionswebservices Extension. Setting Up Access Rights via ImpEX The following example sets up access rights to Create, Read, Update, and Remove for myusergroup for the Unit system type:
 Sample Code
$START_USERRIGHTS Type ; UID ; MemberOfGroups ; Password ; Target ; read ; change ; create ; remove UserGroup ; integrationadmingroup ; ; ; ; ; ; ; ; ; ; ; Unit ; + ; + ; + ; + $END_USERRIGHTS
To set up access rights using the Backoffice Integration UI Tool, see Setting Up Access Rights for Integration Objects. For some specic examples of how type Access Rights affect Integration APIs, see the following examples.

Example Scenarios Expanding a Type Without Read Permissions Access Rights Conguration Type Create Read Update Delete Order Yes Yes Yes Yes OrderEntry Yes No Yes Yes GET https://localhost:9002/odata2webservices/InboundOrder/Orders?$expand=entries 403 Forbidden - The user lacks read privileges for accessing the OrderEntry type. Access to a Navigation Property Without Read Permissions Type Create Read Update Delete Order Yes Yes Yes Yes OrderEntry Yes No Yes Yes Request URL
GET https://localhost:9002/odata2webservices/InboundOrder/Orders('ord1')/entries Response 403 Forbidden - The user lacks read privileges for accessing the OrderEntry type. Updating by POST Request on a Type with No Update Permissions This is   For more    the SAP Help  130 Request URL Response Access Rights Conguration In the following scenario, an order item with the code ord1 exists, and the POST request includes an updated value for date.

Access Rights Conguration Type Create Read Update Delete Order Yes Yes No Yes Request URL
POST https://localhost:9002/odata2webservices/InboundOrder/Orders Request Body
{ "code": "ord1", "date": "/Date(1540469763078)/" }
Response 403 Forbidden - The user lacks change privileges for accessing the Order type.

Updating a Subtype with No Permissions with a POST Request to the Root Type with Permissions In this scenario, the order and orderEntry exist. The order item has the code ord1 and the entry has the entryNumber 1. The request is to update an order with a nested entry that includes an updated value for quantity.

Access Rights Conguration Type Create Read Update Delete Order Yes Yes Yes Yes OrderEntry Yes Yes No Yes Request URL
POST https://localhost:9002/odata2webservices/InboundOrder/Orders Request Body
{ "code": "ord1", "entries": [ { "entryNumber": 1, "quantity": "7" } ] }
Response 403 Forbidden - The user lacks change privileges for accessing the OrderEntry type.

Updating a Nested Type with No Update Permissions with a POST Request This example assumes an order item, ord1, with an entryNumber of 1 exists. The POST request updates an existing order entry with a different value for quantity.

Access Rights Conguration Type Create Read Update Delete Order Yes Yes Yes Yes OrderEntry Yes Yes No Yes Request URL
POST https://localhost:9002/odata2webservices/InboundOrder/OrderEntries Request Body
{ "order": { "code": "ord1", }, "entryNumber": 1, "quantity": "2" }
Response 403 Forbidden - The user lacks change privileges for accessing the OrderEntry type.

This is   For more    the SAP Help  131 Setting Up Access Rights for Integration Objects In the Backoffice Integration UI Tool, set up access rights for users working with Integration Objects.

Prerequisites Note Only administrators can access the Authorization node.

Procedure 1. Log in to Backoffice.

2. From the dropdown arrow in the upper-left corner of the page, select Integration UI Tool. 3. From the leftside menu, select Authorization. 4. Select an Integration Object. 5. Select an Integration Object Item.

In the rightside view, the user role or group and related type-level permissions are displayed.

 Note To quickly look up a specic user group or role, use the Filter Context search.

6. Select the Add button, then enter the name of the user role or group to add. 7. Select any of the following type-level permissions for the newly added user role or group: Read (GET), Change (POST, PATCH), Create (POST), and Remove (DELETE).

To modify existing permissions, select the appropriate icon to either grant ( ) or deny ( ) a type-level permission. You can determine the permission status by consulting the access rights legend at the bottom of the screen:
 Note Inherited rights are type-level permissions inherited from the Integration Object Item. You can modify inherited rights, for example, change denied to granted and vice versa. The change only affects the type you are explicitly working on and not the permission status of the inherited source.

## Search Restrictions

As part of legacy authentication, you can use SearchRestriction to secure access to Integration Objects that are exposed as OData2 web services.

Context Note Access rights is the default and recommended authentication mode.

While access to the IntegrationServices, InboundIntegrationMonitoring, and OutboundIntegrationMonitoring services are controlled through the default group memberships available with the Integration API, you must prevent unauthorized exposure of other services by using SearchRestriction. You can restrict access by importing an ImpEx script or in Backoffice. For example, given a user group called productintegrationadmingroup, you can restrict access to the /ProductIO Integration Object so that only members of productintegrationadmingroup can access it. To do so using ImpEx, import the following.

INSERT_UPDATE SearchRestriction; code[unique = true] ; name[lang = en]; query; principal(UID); restrictedType(code); active; generate ; productIntegrationVisibility; Product IO Restriction; ({code}='ProductIO' AND EXISTS ( {{ select {ug:PK} from {UserGroup as ug} where {ug:PK} IN 
The query for the productIntegrationVisibility restriction, from the preceding ImpEx, shows that if the code of the Integration Object is /ProductIO, then the session user must be in the productintegrationadmingroup. If the code of the Integration Object is NOT /ProductIO, then the restriction is not applied. The following shows that section of the ImpEx.

( {code}='ProductIO' AND EXISTS ({{ select {ug:PK} from {UserGroup as ug} where {ug:PK} IN (?session.user.groups) and {ug:uid} = 'productintegrationadmingroup' }} ) ) OR ( {code}!='ProductIO' )
You can modify the ImpEx script shown to secure an Integration Object. Within the sample script below, only change the following items for each visibilty restriction.

MyIntegrationObject MyIntegrationObjectGroup MyIntegrationObject This is   For more    the SAP Help  132

({code}=**'MyIntegrationObject**' AND EXISTS ( {{ select {ug:PK} from {UserGroup as ug} where {ug:PK} IN (?session.user.groups) and {ug:uid} = '**MyIntegra**
After you secure the Integration Object, grant user access to the secured Integration Objects in Backoffice. See Granting User Access to a Secured Integration Object for instructions. You can also secure Integration Objects and grant access in Backoffice. To do so, perform the following tasks.

Securing an Integration Object in Backoffice Context Create a visibility restriction rule and a permitted user group for an Integration Object.

Procedure 1. Log in to Backoffice and open the Integration UI Tool perspective.

2. Create an Integration Object for the object you want to secure. To secure an existing Integration Object, skip this step. 3. Click Administration User User Groups .

4. Click + to create a new user group that is specic to the secured Integration Object. For example, you can create a user group named InboundProductUserGroup.

5. In the Administration perspective, click System Personalization .

6. Click + to create a new visibility rule that will restrict access to the Integration Object to a specied user group.

a. From the Restricted Type eld, always select IntegrationObject. b. In the Identier eld, enter an appropriate name for the visibility restriction.

c. From the Apply on: eld, always select integrationusergroup.

7. Complete the next task to grant access to the Integration Object for specied users.

Granting User Access to a Secured Integration Object in Backoffice Context When you create a user, you can add them to a group. To grant access to an existing user, complete the following steps.

Procedure 1. Log in to Backoffice.

2. In the Administration perspective, click User and select the user type. For example, Employees. 3. Locate and select the user. 4. On the General tab, under Properties, click the ellipses next to the Groups eld. 5. Select integrationcreategroup or integrationviewgroup, depending on the level and type of access the user needs. 6. Click the Groups ellipses again and select the Integration Object-specic group you created in the preceding task. 7. On the Password tab, make sure Disable Login is set to False. 8. Save the changes to the user. The user can access the Integration Object with the designated level of permissions.

## Users And Group Authorization

Only specied user groups, described in this topic, can access the Integration API's IntegrationServices, InboundIntegrationMonitoring, and OutboundIntegrationMonitoring services.

 Note You must also secure other OData2 Web Services, such as /Products and /Orders, using SearchRestriction.

At the Integration API level, group membership provides access control. To ensure endpoint security when creating new users, assign the lowest level of permissions necessary for each user. The following table describes the permissions available for each group. A user can be a member of multiple groups. An authenticated user without sufficient permissions making a REST request against the Integration API receives a 403 error.

| User group                                                                           | Permissions                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| integrationadmingroup                                                                | can reach all secured endpoints no HTTP method restrictions in the Integration API includes members of the admingroup with additional membership in the outboundsyncgroup, can use all HTTP methods in the Outbound Sync Meta API |
|  Note You are strongly encouraged to create a new user for this group.              |                                                                                                                                                                                                                                   |
| integrationcreategroup                                                               | can make POST and PATCH requests against the Integration API and view $metadata endpoints using a GET request                                                                                                                     |
| integrationviewgroup                                                                 | can make GET requests against the Integration API                                                                                                                                                                                 |
| This is custom documentation. For more information, please visit the SAP Help Portal | 133                                                                                                                                                                                                                               |

| 7/6/2024 User group        | Permissions                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| integrationusergroup       | Members of integrationadmingroup, integrationcreategroup, and integrationviewgroup users are all members of the integrationusergroup. As a result, all users with access to the Integration API are also members of the integrationusergroup. When dening Restrictions, select the integrationusergroup as the primary Apply on group when dening a Restriction. |
| integrationmonitoringgroup | can access /InboundIntegrationMonitoring and /OutboundIntegrationMonitoring services                                                                                                                                                                                                                                                                             |
| integrationdeletegroup     | can delete Integration Object Items by integrationKey                                                                                                                                                                                                                                                                                                            |
| integrationservicegroup    | can access /IntegrationService service                                                                                                                                                                                                                                                                                                                           |
| outboundsyncgroup          | with additional membership in the integrationadmingroup, can use all HTTP methods in the Outbound Sync Meta API                                                                                                                                                                                                                                                  |

Restrictions for employeegroup and customergroup Users SAP Commerce Cloud ships with a number of out-of-the-box restrictions on the employeegroup and customergroup. When conguring technical users intended to access Integration API
OData Web Services, restrictions might be applied depending on the user's group memberships and the Item Types associated with the Integration Objects. The out-of-the-box restrictions on employeegroup and customergroup use the session attribute catalogversions in the exible search of catalog-aware items, which is not available in Integration API. For that reason, technical users should not be members of employeegroup and customergroup to avoid unexpected exible search failures.

## Ssl

The Integration API redirects requests using only HTTP to an SSL endpoint.

HTTPS secures the odata2webservices extension, so, when providing only HTTP, the application issues a 302 error. The 302 error redirects the request to an SSL endpoint. The client is responsible for following the redirection. Direct the client by allowing the redirections or providing the HTTPS protocol.

## Creating Integration Api Users

Create a new user and assign a user group to allow Integration API permissions.

Procedure 1. In a web browser, navigate to https://localhost:9002/backoffice/ and log in to Backoffice as an administrator.

2. In Backoffice, click User Employees . 3. Click +. 4. In the window that opens, enter an ID for the new user in the ID eld. 5. Click Next until you get to the Memberships tab. 6. On the Memberships tab, leave [employeegroup] in the rst eld or, if you do not want the user to have exible search restrictions, click x to remove the employeegroup. 7. Click in the second eld and select a group from the list.

 Note Add users working with Integration Objects to the Integration Admin Group [integrationadmingroup], and, under Personalization Readable catalog version , make sure they have Powertools Classication 1.0 and Electronics Classications 1.0.

8. Click Done.

## Integration Backoffice Security

The Backoffice Integration UI Tool provides Integration Administrator and Integration Agent user roles.

 Note This page may contain information about features that were only introduced in an update release. Ensure you are always on the latest release to be able to make use of all xes, security updates, and features. For a complete list of what was introduced in each update release, see What's New.

Backoffice provides the following Integration UI Tool permissions.

| User Role                              | User name                          | Access Rights                                                                                                                                                                         |
|----------------------------------------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| backofficeintegrationadministratorrole | BackofficeIntegrationAdministrator | Full access to Modeling, Authentication, Authorization, and Monitoring features. Full access to the Backoffice Administrator role. See Backoffice Administrator Role for details.     |
| backofficeintegrationagentrole         | BackofficeIntegrationAgent         | Read-only access to Modeling, Authentication, and Monitoring features.  Note This role does not provide viewing privileges for payloads on inbound and outbound monitoring requests. |

This is   For more    the SAP Help  134

## Integration Api Meta Apis

This topic provides an overview of the Meta APIs available for Integration API scenarios. With Meta APIs, you can create and congure data replication scenarios for SAP Commerce Cloud—all in real time—that include:
Inbound and outbound channels to send and receive data

Integration Objects that contain data payloads Webhooks to receive notifcations for item changes Runtime and virtual attributes for Integration Objects Virtual attributes for Integration Objects Scripts that back virtual attributes
Filter scripts for webhook ltering Monitor inbound and outbound requests The general ow of a data replication scenario is creating a channel to send and receive data between SAP Commerce Cloud and an external system, then creating an Integration Object associated with that channel that contains payloads, which can include runtime and virtual attributes, then creating webhooks to be notied of specic changes when they occur in SAP Commerce Cloud.

The following Meta APIs enable you to replicate data between SAP Commerce Cloud and an external system:
Inbound Channel Conguration - expose an Integration Object as an API to receive data from an external system. See Exposing an Integration Object using the Meta API. Outbound Channel Conguration - congure outbound sync to send data to an external system. See Outbound Sync Meta API. Webhooks - create webhooks to allow SAP Commerce Cloud to send notications to a congured destination URL when an item is saved. See Webhook Service Meta API.

Once a channel has been established, you can use the following Meta APIs to create and congure Integration Objects to send or receive data payloads:
Integration Service - create Integration Objects to send and receive data. See Modeling using the Meta API. Rutime Attributes - create attributes to add at runtime. See Runtime Attribute Meta API. Virtual Attributes - create virtual attributes for Integration Object Items and add them at runtime. See Script Service Meta API for Virtual Attributes. Webhooks - create webhooks to receive notications in response to After Save Events in SAP Commerce Cloud. See Webhook Service Meta API.

 Note You can create Integration Objects before establishing either an outbound or inbound channel and then associate it with a congured channel.

Virtual attributes and webhook ltering are both backed by script logic. You can use the the Script Service Meta API for the following:
Virtual Attributes - create scripts for virtual attributes. See Script Service Meta API for Virtual Attributes. Webhook ltering - save lter scripts in SAP Commerce Cloud. See Item Filtering for Webhooks in Webhooks.

You can also use Meta APIs to view inbound and outbound monitoring data. Unlike the previous Meta APIs, the following ones only allow for viewing (you can't use them to create):

Inbound Integration Monitoring - view inbound monitoring data. See Inbound Monitoring.
Outbound Monitoring - view monitoring data for outbound Integration Object requests. See Outbound Monitoring.

To download the corresponding YAML les for all of the available Integration API Meta APIs, see API Documentation and YAML Files.

## Exporting Conguration Types

This feature is useful when needing to move congurations from one environment to another without having to recreate them. You can use the Backoffice Integration UI Tool to export Integration API conguration types that you can then import into a target system. You can export the following three conguration types:
Integration API (InboundChannelConguration) Outbound Sync (OutboundChannelConguration) Webhook (WebhookConguration)
For each conguration type, you can select specic instances to export or use the "Select All" feature to select all instances. When you export one ore more congurations, they are contained in a single Postman Collection JSON le that contains separate Integration API Meta API requests and payloads representing the exported conguration types. For security reasons, the JSON le does not contain credential information for consumed destinations for both outbound sync and webhook congurations. For that reason, once you've imported the collection into Postman, you must provide credentials for the collection to send requests to the target system. You must also provide the base URL for the collection. After you've imported the collection and provided the necessary information, you can add, remove, or update any of the variables for each request.

 Note To mitigate any potential security threats when exporting congurations, keep the following in mind:
Do not modify any Integration API Meta APIs.

Do not run the Postman Collection against a target system if the scripts are stored in unsecured storage (for example, a shared leserver), have been shared via an unsecured channel (for example, e-mail), or if the collection was sent by an untrusted source.

You import the congurations into the target system using Integration API Meta APIs. See Integration API Meta APIs for more information.

Exporting Conguration Types Using the Backoffice Integration UI Tool Export Integration API, outbound sync, and webhook congurations as Postman Collections to import into a target system.

Prerequisites Note To mitigate any potential security threats when exporting congurations, keep the following in mind:
Do not modify any Integration API Meta APIs. Do not run the Postman Collection against a target system if the scripts are stored in unsecured storage (for example, a shared leserver), have been shared via an unsecured channel (for example, e-mail), or if the collection was sent by an untrusted source.

Procedure 1. Log in to Backoffice.

 Note This feature is available only to users with administrator privileges.

2. From the dropdown arrow in the upper-left corner of the page, select Integration UI Tool. 3. From the leftside menu, select Export Congurations. 4. Under Conguration Type, select a conguration type.

 Note When exporting an outbound sync conguration (OutboundChannelConguration), the autoGenerate ag is set to true by default, regardless of the setting in the source system.

This enables creating the OutboundChannelConguration-related entities when importing an outbound sync conguration into the target system.

5. From the right pane, select the instances you want to export for that conguration type. To selet all available instances, checkmark the "Select All" checkbox. Repeat this step for each conguration type you want to export.

 Note You can use shift-click to select multiple instances. The number of selected instances is noted by the conguration type name, for example, "InboundChannelConguration [2/9]" where "[2/9]" = "[Amount Selected]". If no instances have been selected, nothing appears next to the conguration type name.

6. Select (Export Conguration) to create the Postman Collection JSON le.

 Note Once you import the collection into Postman, you must provide the base URL for the collection. For outbound sync and webhooks, you must also provide the credentials for the collection to send requests to the target system.

Integration API Architecture The Integration API is a set of extensions providing interfaces for data integration with SAP Commerce Cloud.

Dependencies Recommendation For a better viewing experience, right-click the diagram and select one of the available browser options, such as Open Image in New Tab.

![136_image_0.png](136_image_0.png)

Recipes For a complete list of SAP Commerce Cloud recipes that may include this module, see Installer Recipes. For a complete list of the SAP Commerce Cloud, integration extension pack recipes that may include this module, see Installer Recipe Reference.

Extensions The Integration API module consists of the following extensions:
integrationservices Extension The integrationservices extension allows you to create Integration Objects that are the building blocks for Integration APIs. The extension contains the business logic for creating services for inbound and outbound communications and dening their payloads. integrationbackoffice Extension The integrationbackoffice extension allows you to perform several Integration API tasks via the Backoffice, including creating and editing Integration Objects at runtime, monitoring inbound and outbound requests, and conguring outbound sync.

inboundservices Extension The inboundservices extension allows monitoring for inbound Integration API requests.

outboundservices Extension The outboundservices extension allows monitoring for outbound Integration API requests.

odata2services Extension The odata2services extension persists inbound posts, facilitates outbound posts, and encapsulates the services used to generate an EDMX schema from an Integration Object item.

The EDMX schema can be used with SAP Cloud Integration, for example. odata2webservices Extension The odata2webservices extension exposes the business service as a REST-based web service.

outboundsync Extension The outboundsync extension allows the publication of new and modied Integration Objects to external systems.

integrationmonitoringbackoffice Extension Use the integrationmonitoringbackoffice extension to monitor incoming and outgoing requests.

outboundsyncbackoffice Extension Use the outboundsyncbackoffice extension to view and create outbound sync congurations.

integrationbackofficetest Extension The integrationbackofficetest extension provides a service for testing integrationbackoffice.

webhookbackoffice Extension Use the webhookbackoffice extension to create and manage webhooks in Backoffice.

webhookservices Extension The webhookservices extension allows SAP Commerce Cloud to send notications to a congured destination URL when an item is saved (created or updated) or deleted.

## Integrationservices Extension

The integrationservices extension allows you to create Integration Objects that are the building blocks for Integration APIs. The extension contains the business logic for creating services for inbound and outbound communications and dening their payloads.

About the Extension The integrationservices extension can be included on its own. You can only use ImpEx to import the Integration Objects and attributes. You cannot generate the EDMX schema.

Name Directory Related Module integrationservices hybris/bin/modules/integration-apis/integrationservices Integration API Module integrationbackoffice Extension The integrationbackoffice extension allows you to perform several Integration API tasks via the Backoffice, including creating and editing Integration Objects at runtime, monitoring inbound and outbound requests, and conguring outbound sync.

About the Extension

| Name                                                                                                   | Directory   | Related Module   |
|--------------------------------------------------------------------------------------------------------|-------------|------------------|
| integrationbackoffice hybris/bin/modules/integration-apis/integrationbackoffice Integration API Module |             |                  |

inboundservices Extension The inboundservices extension allows monitoring for inbound Integration API requests.

About the Extension Name Directory Related Module inboundservices hybris/bin/modules/integration-apis/inboundservices Integration API Module outboundservices Extension The outboundservices extension allows monitoring for outbound Integration API requests.

About the Extension Name Directory Related Module outboundservices hybris/bin/modules/integration-apis/outboundservices Integration API Module odata2services Extension The odata2services extension persists inbound posts, facilitates outbound posts, and encapsulates the services used to generate an EDMX schema from an Integration Object item. The EDMX schema can be used with SAP Cloud Integration, for example.

About the Extension Name Directory Related Module odata2services hybris/bin/modules/integration-apis/odata2services Integration API Module Dependencies and Architecture This extension depends on the integrationservices Extension. When you install odata2webservices, the odata2services and integrationservices extensions are automatically available at compile and runtime.

odata2webservices Extension The odata2webservices extension exposes the business service as a REST-based web service.

About the Extension Name Directory Related Module odata2webservices hybris/bin/modules/integration-apis/odata2webservices Integration API Module Dependencies and Architecture This extension depends on the odata2services Extension. When you install odata2webservices, the odata2services and integrationservices extensions are automatically available at compile and runtime.

outboundsync Extension The outboundsync extension allows the publication of new and modied Integration Objects to external systems.

About the Extension The outboundsync extension relies on the deltadetect extension to detect changes to Integration Object items in SAP Commerce Cloud. The outboundsync extension then facilitates the publication of an Integration Object, updated with the item changes, to an external system such as SAP Cloud Integration (SCI).

This is   For more    the SAP Help  138 Name Directory Related Module outboundsync hybris/bin/modules/integration-apis/outboundsync Integration API Module Conguration

![138_image_0.png](138_image_0.png)

integrationmonitoringbackoffice Extension Use the integrationmonitoringbackoffice extension to monitor incoming and outgoing requests.

About the Extension Name Directory Related Module integrationmonitoringbackoffice hybris/bin/modules/integration-apis/integrationmonitoringbackoffice Integration API Request Monitoring Dependencies This extension depends on the integrationbackoffice extension.

outboundsyncbackoffice Extension Use the outboundsyncbackoffice extension to view and create outbound sync congurations.

About the Extension This is   For more    the SAP Help  139 Name Directory Related Module outboundsyncbackoffice hybris/bin/modules/integration-apis/outboundsyncbackoffice Outbound Sync Dependencies This extension depends on the integrationbackoffice extension.

integrationbackofficetest Extension The integrationbackofficetest extension provides a service for testing integrationbackoffice.

About the Extension Name Directory Related Module integrationbackofficetest hybris/bin/modules/integration-apis/integrationbackofficetest Integration API Module Dependencies and Architecture This extension depends on the backoffice extension, the integrationbackoffice Extension, and the commerceservices extension.

webhookbackoffice Extension Use the webhookbackoffice extension to create and manage webhooks in Backoffice.

About the Extension With this extension, you can use the Backoffice Integration UI Tool to create, update, view, and delete webhooks.

Name Directory Related Module webhookbackoffice hybris/bin/modules/integration-apis/webhookbackoffice Integration API Module Dependencies This extension depends on the webhookservices extension and the integrationbackoffice extension.

webhookservices Extension About the Extension The webhookservices extension allows you to subscribe to the ItemSavedEvent by creating a WebhookConfiguration. When an item is saved (created or updated) or deleted, SAP
Commerce Cloud sends notications to the congured destination URL.

Name Directory Related Module webhookservices hybris/bin/modules/integration-apis/webhookservices Integration API Module Integration API Implementation Integration Installation and Conguration SAP Commerce Cloud requires some changes to integrate with the Integration API.

Integration Installation and Conguration SAP Commerce Cloud requires some changes to integrate with the Integration API. An example Integration Object conguration is available to help demonstrate how to create Integration Objects. The example walks you step-by-step through the process of creating a simple inbound product Integration Object, as well as how to retrieve it. You can also monitor the requests from Backoffice and update the retention policy for these monitored requests. This section also describes how to implement outbound sync. When the conguration is complete, make sure that the endpoints have security in place to protect the exchange of data.

This is   For more    the SAP Help  140 The webhookservices extension allows SAP Commerce Cloud to send notications to a congured destination URL when an item is saved (created or updated) or deleted.

Install and congure the Integration API extensions, and congure endpoint security and user roles. Tutorials walk you through creating and managing Integration Objects and data retention for API requests.

Installing the Integration Extensions After installing the current version of SAP Commerce Cloud, you can modify the localextensions.xml le to include the Integration API extensions.

Tutorial: Creating and Managing Integration Objects and Items This tutorial guides you through creating and retrieving sample Integration Objects and Integration Items and monitoring and managing your Integration API requests.

Troubleshooting Guide Follow the steps provided for the relevant situation. Exposing an Integration Object as an API Follow the steps to expose an example Integration Object with OAuth 2.0 authentication. Outbound Sync Implementation Learn how outbound sync is implemented and congure it to publish new and updated Integration Object Items. Runtime Attribute Meta API Implementation Examples The following examples show how to make POST (create), GET (read), PATCH (update), and DELETE (remove) requests using the Runtime Attribute Meta API. Runtime Attribute Implementation Examples Script Service Meta API Implementation Examples The following examples show how to make POST (create), GET (read), PATCH (update), and DELETE (remove) requests using the Script Service Meta API. Virtual Attribute Implementation Examples This topic provides script examples to show how virtual attributes can atten, format, and enhance payloads. Webhook Service Meta API Implementation Examples The following examples show how to make POST (create), GET (read), PATCH (update), and DELETE requests using the Webhook Service Meta API. Modifying Outbound Requests Enrich your outbound Integration API requests by modifying request headers and payloads.

Tutorial: Using the Outbound Service Set up and congure the Outbound Services extensions and a test endpoint to send an outbound Integration Object back to an inbound channel. Conguring Integration API Cron Jobs Cron jobs associated with the Integration API include several monitoring data clean up cron jobs and the outbound sync cron job. Date, Time, and Time Zone Handling The Integration API, SAP Commerce Cloud Platform, and Backoffice have different methods for handling time zones.

## Installing The Integration Extensions

After installing the current version of SAP Commerce Cloud, you can modify the localextensions.xml le to include the Integration API extensions.

Prerequisites Install SapMachine JDK 11. Download the latest version of SAP Commerce Cloud and follow the conguration instructions.

Context The following extensions are necessary to work with Integration API. The procedure that follows describes how to install the extensions.

odata2webservices - The odata2webservices extension exposes the business service as a REST-based web service. The extension depends on odata2services, which depends on integrationservices. When you install odata2webservices, the odata2services and integrationservices extensions are automatically available at compile and runtime.

integrationservices - This SAP Commerce Cloud extension facilitates the creation of the Integration Object within the SAP Commerce Cloud database. The integrationservices extension can be included on its own. You can only use ImpEx to import the Integration Objects and attributes. You cannot generate the EDMX schema. odata2services - This SAP Commerce Cloud extension persists inbound posts, facilitates outbound posts, and encapsulates the services used to generate an EDMX schema from an Integration Object item. The EDMX schema can be used with SAP Cloud Integration, for example.

integrationbackoffice - This extension allows you to create and edit Integration Objects at runtime. inboundservices - This extension provides monitoring capabilities for inbound data requests. This extension depends on the integrationservices extension. outboundservices - The outboundservices extension provides services and monitoring capabilities for data ows from the SAP Commerce Cloud to external systems. The extension depends on the integrationservices extension. outboundsync - This extension allows the publication of new and modied Integration Objects to external systems. The outboundsync extension relies on the deltadetect extension.

integrationmonitoringbackoffice - This extension enables monitoring of incoming and outgoing requests. outboundsyncbackoffice - Use this extension to view and create outbound sync congurations.

 Note To see full log messages to improve error troubleshooting, update the log level to DEBUG. For more information, see Updating the Log Level to Debug.

Procedure 1. In a command line, cd to the *<HYBRIS_HOME>*/hybris/bin/platform directory.

2. Source the setantenv.sh script using the command:
. setantenv.sh 3. Run ant clean all. This creates new folders in the commerce suite installation, including the config folder in the hybris directory. 4. In the SAP Commerce Cloud repository, locate and open the*<HYBRIS_HOME>*/hybris/config/localextensions.xml le.

5. Copy the following lines to the le and save.

<extension name="integrationmonitoringbackoffice" /> <extension name="outboundsyncbackoffice" />
This is   For more    the SAP Help  141 6. In a command-line interface, use the cd command to change to the cd hybris/bin/platform directory. 7. In the command line, run ant clean all. This step builds the platform/commerce-suite directory with the extensions you added to the localextensions.xml le.

8. In the command line, run ant initialize. 9. Start SAP Commerce Cloud using the command:
./hybrisserver.sh 10. To verify that the extensions are running, open localhost:9002 in a web browser and log into the SAP Commerce Cloud Administration Console.

11. Click Platform > Extensions.

12. Look for odata2services, odata2webservices, integrationservices, integrationbackoffice, inboundservices, outboundservices, integrationmonitoringbackoffice, and outboundsyncbackoffice. Verify that the Core column for each service displays a green checkmark, indicating the extension installed successfully.

13. Verify that the integrationbackoffice extension is running. Open localhost:9002/backoffice/ in a web browser and log into Backoffice.

 Note If you do not see the integration perspective, reset the Backoffice widget. See Resetting Backoffice Conguration for more information.

14. Click Administration > . If you can open the Integration UI Tool, the extension is successfully installed. Data is not present if you have not yet created any metadata for monitoring.

Updating the Log Level to Debug When the log level is set to "debug," verbose messaging displays. You can see the most comprehensive level of log messages.

Context Use the Administration Console to change the log level. You can change the log level for a single service or for all services.

Procedure 1. Log into the Administration Console.

2. Select Platform Logging .

3. Update the log level for odata2webservices.

If the de.hybris.platform.odata2webservices package is missing, add it and set the log level to DEBUG. If the de.hybris.platform.odata2webservices package is already added, search for it and set the log level to DEBUG.

![141_image_0.png](141_image_0.png)

4. Update the log level for odata2services.
If the de.hybris.platform.odata2services package is missing, add it and set the log level to DEBUG. If the de.hybris.platform.odata2services package is already added, search for it and set the log level to DEBUG.

5. Update the log level for integrationservices.

If the de.hybris.platform.integrationservices package is missing, add it and set the log level to DEBUG. If the de.hybris.platform.integrationservices package is already added, search for it and set the log level to DEBUG.

## Tutorial: Creating And Managing Integration Objects And Items

This tutorial guides you through creating and retrieving sample Integration Objects and Integration Items and monitoring and managing your Integration API requests. Complete the tutorials in the links that follow to:
1. Create an example Product Integration Object called ExampleProduct. View the new object in Backoffice, via ImpEx, or with an Integration API request.

2. Create and retrieve an example Product Integration Item using the Integration API. 3. Monitor your inbound and outbound Integration API requests in Backoffice or with an Integration API request. 4. Manage the data retention policy for Inbound Requests and run persisted request data clean-up jobs via ImpEx and in Backoffice.

Creating and Viewing a Product Integration Object This is   For more    the SAP Help  142 Create and retrieve a simple inbound Product Integration Object.

In this tutorial, create an Integration Object to dene a manageable SAP Commerce Cloud Type System object for use in an Integration API. After creating ExampleProduct, you can view it using Backoffice or the Integration Services API.

 Note For SAP Commerce Cloud version 2011 and higher, to expose an Integration Object as an API it must be associated with an InboundChannelConguration (ICC). When upgrading to version 2011 and higher, an ICC is automatically created with Basic authentication for an Integration Object that doesn't have a corresponding ICC. Once created, to set the authentication to OAuth, update the authentication type in the ICC. For more information, see Authentication.

You need integrationadmingroup permissions to create Integration Objects.

Creating the Product Integration Object Create an Integration Object named ExampleProduct that contains the code, name, and catalogVersion attributes. You can create the object using Backoffice or ImpEx.

Create an Integration Object in Backoffice Follow these steps to create the ExampleProduct Integration Object using the Integration UI Tool in Backoffice.

1. In a web browser, navigate to https://localhost:9002/backoffice/ and log in.

2. In Backoffice, from the drop-down menu at the top, click Administration > Integration UI Tool. 3. In the menu on the left, click Modeling. 4. Click +.

5. In the Create Integration Object window, enter ExampleProduct in the Name eld. 6. From the Root Type list, select or type Product.

7. From the Integration Type list, select Inbound. 8. Click Create. Click OK to conrm.

9. In the Attribute Name column, locate and click name to add it as an attribute to the ExampleProduct Integration Object.

Some attributes are preselected and marked as Unique, such as CatalogVersion and Code.

10. Click Save. In the conrmation window, click Save Denition to conrm.

Create an Integration Object using ImpEx

As an alternative to using Backoffice, you can create the ExampleProduct using ImpEx. The ImpEx denes the IntegrationObject, IntegrationObjectItem, and IntegrationObjectItemAttribute.

![142_image_0.png](142_image_0.png)

; ExampleProduct; INBOUND
INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code)
; ExampleProduct ; Catalog ; Catalog ; ExampleProduct ; CatalogVersion ; CatalogVersion ; ExampleProduct ; Product ; Product

| INSERT_UPDATE IntegrationObjectItemAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = true] ; ExampleProduct:Catalog ; id ; Catalog:id ; ; ExampleProduct:CatalogVersion ; catalog ; CatalogVersion:catalog ; ExampleProduct:Catalog ; ExampleProduct:CatalogVersion ; version ; CatalogVersion:version ; ; ExampleProduct:Product ; code ; Product:code ; ; ExampleProduct:Product ; catalogVersion ; Product:catalogVersion ; ExampleProduct:CatalogVersion ; ExampleProduct:Product ; name ; Product:name ; A message appears to indicate that the import succeeded.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Create an Integration Object using a POST request To create an Integration Object using the Integration API, send a POST request to the IntegrationService endpoint. The following example creates an Integration Object named pcm, with a root type of Product. Within the Product item, the example species the root with "root": true.

Request URL
POST https://localhost:9002/odata2webservices/IntegrationService/IntegrationObjects Request Body
{ "code": "pcm", "integrationType": { "code": "INBOUND" }, "items": [ { "code": "Catalog", "type": { "code": "Catalog" }, "integrationObject": { "code": "pcm" }, "attributes": [ { "attributeName": "id", "attributeDescriptor": { "qualifier": "id", "enclosingType": { "code": "Catalog" } }, "integrationObjectItem": { "code": "Catalog", "type": { "code": "Catalog" }, "integrationObject": { "code": "pcm" } } }, { "attributeName": "name", "attributeDescriptor": { "qualifier": "name", "enclosingType": { "code": "Catalog" } }, "integrationObjectItem": { "code": "Catalog", "type": { "code": "Catalog" }, "integrationObject": { "code": "pcm" } } } ] }, { "code": "CatalogVersion", "type": { "code": "CatalogVersion" }, "integrationObject": { "code": "pcm" }, "attributes": [ { "attributeName": "version", "attributeDescriptor": { "qualifier": "version", "enclosingType": { "code": "CatalogVersion" } }, "integrationObjectItem": { "code": "CatalogVersion", "type": { "code": "CatalogVersion" }, "integrationObject": { "code": "pcm" } } }, {
 "attributeName": "catalog",
 "attributeDescriptor": { "qualifier": "catalog", "enclosingType": { "code": "CatalogVersion" } }, "returnIntegrationObjectItem": { "code": "Catalog", "integrationObject": { "code": "pcm" } }, "unique": true,
 "integrationObjectItem": {
 "code": "CatalogVersion", "type": { "code": "CatalogVersion" }, "integrationObject": { "code": "pcm" } } } ] }, { "code": "Unit", "type": { "code": "Unit" }, "integrationObject": { "code": "pcm" }, "attributes": [ { "attributeName": "code", "attributeDescriptor": { "qualifier": "code", "enclosingType": { "code": "Unit" } }, "integrationObjectItem": { "code": "Unit", "type": { "code": "Unit" }, "integrationObject": { "code": "pcm" } } }, { "attributeName": "unitType", "attributeDescriptor": { "qualifier": "unitType", "enclosingType": { "code": "Unit" } }, "integrationObjectItem": { "code": "Unit", "type": { "code": "Unit" }, "integrationObject": { "code": "pcm" } } } ] }, { "code": "Product", "type": { "code": "Product" }, "integrationObject": { "code": "pcm" }, "root": true, "attributes": [ { "attributeName": "code", "attributeDescriptor": { "qualifier": "code", "enclosingType": { "code": "Product" } }, "integrationObjectItem": { "code": "Product", "type": { "code": "Product"}, "integrationObject": { "code": "pcm" } } }, { "attributeName": "catalogVersion", "attributeDescriptor": { "qualifier": "catalogVersion", "enclosingType": { "code": "Product" } }, "returnIntegrationObjectItem": { "code": "CatalogVersion", "integrationObject": { "code": "pcm"} }, "integrationObjectItem": { "code": "Product", "integrationObject": { "code": "pcm" } } },

 {
 "attributeName": "name", "attributeDescriptor": { "qualifier": "name", "enclosingType": { "code": "Product" } }, "integrationObjectItem": { "code": "Product", "integrationObject": { "code": "pcm" } }
 },
 { "attributeName": "description", "attributeDescriptor": { "qualifier": "description", "enclosingType": { "code": "Product" } }, "integrationObjectItem": { "code": "Product", "integrationObject": { "code": "pcm" } } }, { "attributeName": "unit", "attributeDescriptor": { "qualifier": "unit", "enclosingType": { "code": "Product" } }, "integrationObjectItem": { "code": "Product", "integrationObject": { "code": "pcm" } }, "returnIntegrationObjectItem": { "code": "Unit", "integrationObject": { "code": "pcm"} } }, { "attributeName": "order", "attributeDescriptor": { "qualifier": "order", "enclosingType": { "code": "Product" } }, "integrationObjectItem": { "code": "Product", "integrationObject": { "code": "pcm" } } } ] } ] }
Viewing the Product Integration Object After creating the ExampleProduct Integration Object, you can view it in Backoffice or using the Integration API.

View an Integration Object in Backoffice Follow these steps to view the ExampleProduct Integration Object using the Integration UI Tool in Backoffice.

1. In Backoffice, from the drop-down menu at the top, click Administration > Integration UI Tool.

2. In the menu on the left, click Modeling > Edit Mode. 3. From the Integration Object list, select ExampleProduct.

 Note If ExampleProduct is not in the list, click Refresh.

4. Click Product to view the object attributes. To view the object and its attributes in an ImpEx script or the EDMX schema, click the Metadata Viewer button and select the Impex View or EDMX View tab.

View an Integration Object using cURL
Now that you dened the Integration Object ExampleProduct, you can get the EDMX schema using the API.

1. Run the following request to retrieve the full schema for the ExampleProduct Integration Object, replacing <USERNAME>:<PASSWORD> with your Integration API credentials.

curl -k -X GET 'https://localhost:9002/odata2webservices/ExampleProduct/$metadata' -u <USERNAME>:<PASSWORD>
A successful request returns the EDMX schema:
<?xml version='1.0' encoding='UTF-8'?> <edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" Version="1.0"> <edmx:DataServices m:DataServiceVersion="1.0" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"> <Schema Namespace="HybrisCommerceOData" xmlns="http://schemas.microsoft.com/ado/2008/09/edm"> <EntityType Name="CatalogVersion"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="version" Type="Edm.String" IsUnique="true" Nullable="false"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" Alias="CatalogVersion_version|Catalog_id"/> <NavigationProperty Name="catalog" Relationship="HybrisCommerceOData.FK_CatalogVersion_Catalog" FromRole="CatalogVersion" ToRole </EntityType> <EntityType Name="Product"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="code" Type="Edm.String" IsUnique="true" Nullable="false"/> <Property Name="name" Type="Edm.String" IsLanguageDependent="true" Nullable="true"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" Alias="CatalogVersion_version|Catalog_id|Product_code"/> <NavigationProperty Name="catalogVersion" Relationship="HybrisCommerceOData.FK_Product_CatalogVersion" FromRole="Product" ToRole </EntityType> <EntityType Name="Catalog"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="id" Type="Edm.String" IsUnique="true" Nullable="false"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" Alias="Catalog_id"/> </EntityType> <Association Name="FK_CatalogVersion_Catalog"> <End Type="HybrisCommerceOData.CatalogVersion" Multiplicity="0..1" Role="CatalogVersion"/> <End Type="HybrisCommerceOData.Catalog" Multiplicity="0..1" Role="Catalog"/> </Association> <Association Name="FK_Product_CatalogVersion"> <End Type="HybrisCommerceOData.Product" Multiplicity="0..1" Role="Product"/> <End Type="HybrisCommerceOData.CatalogVersion" Multiplicity="0..1" Role="CatalogVersion"/> </Association> <EntityContainer Name="Container" m:IsDefaultEntityContainer="true"> <EntitySet Name="CatalogVersions" EntityType="HybrisCommerceOData.CatalogVersion"/> <EntitySet Name="Products" EntityType="HybrisCommerceOData.Product"/> <EntitySet Name="Catalogs" EntityType="HybrisCommerceOData.Catalog"/> <AssociationSet Name="CatalogVersion_Catalogs" Association="HybrisCommerceOData.FK_CatalogVersion_Catalog"> <End EntitySet="CatalogVersions" Role="CatalogVersion"/> <End EntitySet="Catalogs" Role="Catalog"/> </AssociationSet> <AssociationSet Name="Product_CatalogVersions" Association="HybrisCommerceOData.FK_Product_CatalogVersion"> <End EntitySet="Products" Role="Product"/> <End EntitySet="CatalogVersions" Role="CatalogVersion"/> </AssociationSet>
 </EntityContainer>
 </Schema> </edmx:DataServices> </edmx:Edmx>
2. To request the metadata of a specic IntegrationObjectItem within the Integration Object, retrieve Catalog by running the request:
curl -k -X GET 'https://localhost:9002/odata2webservices/ExampleProduct/$metadata?Catalog' -u <USERNAME>:<PASSWORD>
A successful request returns the EDMX schema:
<?xml version='1.0' encoding='UTF-8'?> <edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" Version="1.0"> <edmx:DataServices m:DataServiceVersion="1.0" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"> <Schema Namespace="HybrisCommerceOData" xmlns="http://schemas.microsoft.com/ado/2008/09/edm"> <EntityType Name="Catalog"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="id" Type="Edm.String" IsUnique="true" Nullable="false"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" Alias="Catalog_id"/> </EntityType> <EntityContainer Name="Container" m:IsDefaultEntityContainer="true"> <EntitySet Name="Catalogs" EntityType="HybrisCommerceOData.Catalog"/> </EntityContainer> </Schema> </edmx:DataServices> </edmx:Edmx>
View an Integration Object using a GET request To view an Integration Object using the Integration API, send a GET request to the IntegrationService endpoint. The endpoint exposes all integration objects. The following example returns the metadata for the ExampleProduct integration object.

Request URL
GET https://localhost:9002/odata2webservices/IntegrationService/ExampleProduct Response Body
{
 "d" : {
"EntitySets": [
"IntegrationObjects", "IntegrationObjectItems", "ComposedTypes", "AttributeDescriptors", "IntegrationObjectItemAttributes", "IntegrationTypes"
]
}
} }

## Creating And Viewing A Product Integration Item

Create and retrieve a single Product item.

After you dene the ExampleProduct Integration Object in the system, the service is available at https://localhost:9002/odata2webservices/ExampleProduct/Products. You can then create and update a Product item. You can also use the IntegrationObjects endpoint to create and view integration object items, but the following examples use the Products endpoint. For more information about using the IntegrationObjects endpoint, see About Integration Objects.

Before you begin, complete the steps in Creating and Viewing a Product Integration Object.

Creating the Product Integration Item Use the following instructions to create a new Product Integration Item using the Integration API.

1. Create the following JSON payload and save it as product.json.

{ "@odata.context": "$metadata\#Products/$entity", "code": "camera-b52", "name": "Camera B52", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } } 
2. In the same location where you saved product.json, run the following cURL command, replacing <USERNAME>:<PASSWORD> with your Backoffice credentials.

curl -X POST -k \ -H "Content-Type:application/json" \ -H "Accept:application/json" \ -u <USERNAME>:<PASSWORD> \ -d @product.json \ https://localhost:9002/odata2webservices/ExampleProduct/Products A successful request returns an HTTP 201 response, as shown:
{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/ExampleProduct/Products('Staged%7CDefault%7Ccamera-b52')", "uri": "https://localhost:9002/odata2webservices/ExampleProduct/Products('Staged%7CDefault%7Ccamera-b52')", "type": "HybrisCommerceOData.Product" }, "code": "camera-b52", "name": "Camera B52", "integrationKey": "Staged|Default|camera-b52", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/ExampleProduct/Products('Staged%7CDefault%7Ccamera-b52')/catalogVersion" } } } }
Viewing a Product Integration Item Use the following instructions to GET the item .

Retrieve the created ExampleProduct item you created in the preceding section using the URI returned in the POST request response.

1. Run the following cURL command, replacing <USERNAME>:<PASSWORD> with your Backoffice credentials.

curl -k -u <USERNAME>:<PASSWORD> -H "Accept:application/json" "https://localhost:9002/odata2webservices/ExampleProduct/Products('Staged%7CDefaul A successful request returns the response:
{ "d": {
 "__metadata": {
 "id": "https://localhost:9002/odata2webservices/ExampleProduct/Products('Staged%7CDefault%7Ccamera-b52')", "uri": "https://localhost:9002/odata2webservices/ExampleProduct/Products('Staged%7CDefault%7Ccamera-b52')", "type": "HybrisCommerceOData.Product" }, "code": "camera-b52", "name": "Camera B52", "integrationKey": "Staged|Default|camera-b52", "catalogVersion": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/ExampleProduct/Products('Staged%7CDefault%7Ccamera-b52')/catalogVersion" } } } }

## Monitoring Integration Api Requests

Monitor your Integration API requests to view the request payloads, statuses, and any errors. Use the Integration UI Tool perspective in Backoffice to monitor inbound and outbound requests, and to enable and disable monitoring. You can also monitor inbound and outbound requests through a GET request. For more information about getting monitoring data using the Integration API, see Integration API Request Monitoring. Before you begin, complete these tutorials:
Creating and Viewing a Product Integration Object Creating and Viewing a Product Integration Item Monitoring Requests View the status, payload, and any errors you received for your inbound ExampleProduct request. If you have enabled the payload retention properties, you can download the payload in a text le or view its contents in a browser. See Conguring Payload Retention.

1. In a web browser, navigate to https://localhost:9002/backoffice/ and log in.

2. From the drop-down menu at the top, click Administration > Integration UI Tool.

3. In the menu on the left, click Monitoring > Inbound. The middle pane of the screen shows inbound requests. You can see the ExampleProduct you previously created.

 Note If you do not see your request, click Search to reload the list.

![149_image_0.png](149_image_0.png)

| ©                               |                 |                                            |                          |                |
|---------------------------------|-----------------|--------------------------------------------|--------------------------|----------------|
| Integration Key                 | Contains        | ,                                          | x                        |                |
| O                               |                 |                                            |                          |                |
| e                               |                 |                                            |                          |                |
| Message Id                      | Equals          | ,                                          | x                        |                |
| o                               |                 |                                            |                          |                |
| o                               |                 |                                            |                          |                |
| Type                            | Contains        | .                                          | x                        | >              |
| =                               |                 |                                            |                          |                |
| Integration Key                 | Message ...     | Type                                       | Status                   | Time created - |
| Staged | Default | camera · b52 | ExampleProduct  | Success                                    | Aug 28, 2018 12:26:35 PM |                |
| InboundRequest[8796158599379]   |                 |                                            |                          |                |
| Integration Key                 | Message Id      | Type                                       | Status                   |                |
| Staged | Default | camera-b52   | ExampleProduct  | Success                                    | ,                        |                |
| Time created                    | Request Payload |                                            |                          |                |
| Aug 28, 2018 12:26:35 PM        | n               | lB Payload_01559702-183f-47dd-991a-ecc1... | ✦ Create new Error       | ,              |

4. Click the Staged|Default|camera-b52 entry in the listing to populate the Inbound Request Details for the item. See Integration API Request Monitoring for a description of 5. If payload retention is enabled, double-click the Request Payload field to view the payload of the ExampleProduct. See Configuring Payload Retention for more information

| InboundRequest[8796158599379]   | »              |                                           |                     |    |
|---------------------------------|----------------|-------------------------------------------|---------------------|----|
| Integration Key                 | Message Id     | Type                                      | Status              |    |
| Staged|Default|camera-b52       | ExampleProduct | Success                                   | ,                   |    |
| Request Payload                 |                |                                           |                     |    |
| Time created                    |                |                                           |                     |    |
| Aug 28, 2018 12:26:35 PM        |                | R Payload_01559702-183f-47dd-991a-ecc1... | -+ Create new Error | ,  |

6. In the Edit item Payload window, you can view the payload in two ways:
a. In the General section of the Edit item Payload window, click Download to save a payload file to your default download folder. For JSON, the file is named Payload_<UUID>.octet-stream For XML, the file is Payload_<UUID>.xml . Open the file in a text editor to view the payload b. In the Properties section, copy the text in the URL field. In a web browser, type http://localhost:9001 and append the copied URL. The resulting URL looks like http://localhost :9001/medias/Payload-52511970-c898-4077- bbd b450abce3d677
context=byFzdGvyfHJvb3R8MJI2fHR1eHQvcGxhaw58aDk1L2hhMy84Nzk2MJU30DEyNTEwLnR4dHxmYe5YTNkYzgyNME4NwJ
Press Enter to view the item payload

![150_image_0.png](150_image_0.png)

![150_image_1.png](150_image_1.png)

![150_image_2.png](150_image_2.png)

Enabling and Disabling Monitoring

![150_image_3.png](150_image_3.png)

By default, monitoring is enabled. Use the following instructions to disable and re-enable monitoring for inbound and outbound Integration API requests.

1. In a web browser, navigate to the SAP Commerce Cloud Administration Console https://localhost:9002 and log in.

![150_image_4.png](150_image_4.png)

![150_image_6.png](150_image_6.png)

![150_image_5.png](150_image_5.png)

3. In the Search eld, enter monitoring and locate the integrationservices.monitoring.enabled property. 4. Change the value of inboundservices.monitoring.enabled and outboundservices.monitoring.enabled to false. Click the green checkmark to apply the change for each property.

5. Enable monitoring again by changing the same values to true. Click the green checkmarks to apply the changes.

## Managing Data Retention For Inbound Requests

Request data is persisted in the platform for monitoring as InboundRequest, InboundRequestError, and IntegrationApiMedia types. You can change the data retention policy for how long the data persists in the system, and for when and how often data clean-up cron jobs run. This tutorial guides you through changing the request data retention duration, the timing and intervals at which request data clean-up jobs run, and then running the data clean-up cron job manually in Backoffice. Before you begin, complete these tutorials:
Creating and Viewing a Product Integration Object Creating and Viewing a Product Integration Item Monitoring Integration API Requests Changing the Data Retention Policy and Clean-up Schedule You can change the duration of request data retention and the schedule for cleaning up request data using an ImpEx script or in Backoffice.

Change the Data Retention Policy and Clean-up Schedule using ImpEx By default, the extension creates two cron jobs, one for cleaning up InboundRequest and InboundRequestError types. You can see the default settings in the following ImpEx.

INSERT_UPDATE AfterRetentionCleanupRule creates the cleanup rules for the InboundRequest and IntegrationApiMedia cron jobs. The default retention period is 604800 seconds (7 days).

This is   For more    the SAP Help  151 INSERT_UPDATE RetentionJob denes how many items per batch get deleted at once. You can change the number of items for better performance.

INSERT_UPDATE CronJob creates the cron job and species when, and which days of the week to run each of the two cron jobs INSERT_UPDATE Trigger denes when to run each job. The expression 0 0 0 * * ? runs the jobs every day at midnight. The server must be running at the time you specify in order for it to delete the persisted request data.

INSERT_UPDATE AfterRetentionCleanupRule ; code[unique=true] ; retirementItemType(code) ; itemFilterExpression ; actionRefere ; inboundRequestCleanupRule ; InboundRequest ; ; basicRemoveCleanupAct ; inboundRequestMediaCleanupRule ; IntegrationApiMedia ; ; basicRemoveCleanupAction ; INSERT_UPDATE RetentionJob ; code[unique=true] ; retentionRule(code) ; batchSize ; inboundRequestCleanupJob ; inboundRequestCleanupRule ; 100 ; inboundRequestMediaCleanupJob ; inboundRequestMediaCleanupRule ; 100 INSERT_UPDATE CronJob ; code[unique=true] ; job(code) ; sessionLanguage(isoCode)[default=en] ; inboundRequestCleanupCronJob ; inboundRequestCleanupJob ; ; inboundRequestMediaCleanupCronJob ; inboundRequestMediaCleanupJob ; \# CronJob Triggers set to run every day at midnight INSERT_UPDATE Trigger ; cronJob(code)[unique=true] ; cronExpression ; inboundRequestCleanupCronJob ; 0 0 0 * * ? ; inboundRequestMediaCleanupCronJob ; 0 0 0 * * ?

For this tutorial, change the retention for the InboundRequest to 30 seconds.

1. In a web browser, navigate to the SAP Commerce Cloud Administration Console at https://localhost:9002/ and log in.

2. Click Console > ImpEx Import. 3. To override the default retention settings, paste the following ImpEx into the Import Content eld and click Import content.

INSERT_UPDATE AfterRetentionCleanupRule; code[unique = true]; retirementItemType(code); itemFilterExpression; actionReference; retentionTimeSeco ; inboundRequestCleanupRule ; InboundRequest ; ; basicRemoveCleanupAction ; 30 ; InboundRequest:creationtime 4. Verify that the change was made. In a web browser, navigate to https://localhost:9002/backoffice/ and log in.

5. In the Administration perspective, click System > Retention Rule. 6. Locate and click inboundRequestCleanupRule. 7. At the bottom of the screen, scroll to the Properties section and verify that the value in the Retention Time in Seconds eld is 30.

Running the Data Clean-up cron jobs Now you can run the cron job. To see the results of the cron job without waiting until the next scheduled job, change the job schedule. You can either change the schedule using ImpEx, or by triggering the job manually in Backoffice.

Changing the job schedule using ImpEx 1. To change the inboundRequestCleanupCronJob to run every 30 seconds, run the following ImpEx:
INSERT_UPDATE Trigger ; cronJob(code)[unique=true] ; cronExpression ; inboundRequestCleanupCronJob ; */30 * * * * ?

2. Wait 30 seconds and then view the log in terminal. If the job ran successfully, the log shows:
INFO [hybrisHTTP30] [PerformCronJobAction] Performing CronJob CronJobModel (8796093514229@34) from Backoffice! INFO [inboundRequestCleanupCronJob::de.hybris.platform.servicelayer.internal.jalo.RetentionJob] (inboundRequestCleanupCronJob) [AfterRetentionC INFO [inboundRequestCleanupCronJob::de.hybris.platform.servicelayer.internal.jalo.RetentionJob] (inboundRequestCleanupCronJob) [AfterRetentionC INFO [inboundRequestCleanupCronJob::de.hybris.platform.servicelayer.internal.jalo.RetentionJob] (inboundRequestCleanupCronJob) [AfterRetentionC INFO [inboundRequestCleanupCronJob::de.hybris.platform.servicelayer.internal.jalo.RetentionJob] (inboundRequestCleanupCronJob) [AfterRetentionC
Changing the job schedule and running the cron job in Backoffice To clean up a persisted InboundRequest using the Integration UI Tool view in Backoffice, perform the following steps.

1. In a web browser, navigate to https://localhost:9002/backoffice/ and log in.

2. In Backoffice, from the drop-down menu at the top, click Administration > Integration UI Tool. 3. In the navigation menu on the left, click System > Background Processes > Cronjobs. 4. In the list of jobs, click inboundRequestCleanupCronJob. The job details appear in the bottom of the screen.

![152_image_0.png](152_image_0.png)

INFO [inboundRequestCleanupCronJob::de.hybris.platform.servicelayer.internal.jalo.RetentionJob] (inboundRequestCleanupCronJob) [AfterRetentionC INFO [inboundRequestCleanupCronJob::de.hybris.platform.servicelayer.internal.jalo.RetentionJob] (inboundRequestCleanupCronJob) [AfterRetentionC INFO [inboundRequestCleanupCronJob::de.hybris.platform.servicelayer.internal.jalo.RetentionJob] (inboundRequestCleanupCronJob) [AfterRetentionC INFO [inboundRequestCleanupCronJob::de.hybris.platform.servicelayer.internal.jalo.RetentionJob] (inboundRequestCleanupCronJob) [AfterRetentionC
7. In Backoffice, click Administration > Integration UI Tool. 8. In the navaigation on the left, Monitoring > Inbound.

9. Click Search. If the cron job successfully deleted the InboundRequest, it does not appear in the list.

## Troubleshooting Guide

Follow the steps provided for the relevant situation.

How to Import Discount Value with Order Entry via API
By default, discountValue is not enabled when sending order entry to SAP Commerce Cloud. discountValue is not supported by Integration Objects because it is neither an item type nor an atomic type. discountValuesInternal should be used instead that contains discount values encoded as a string, and the encoding/decoding logic is implemented in the de.hybris.platform.util.DiscountValue class (that is, parseDiscountValueCollection and toString methods). The following two attributes are available for the InboundOMMOrderEntry Integration Object: discountValues of type Collection (de.hybris.platform.util.DiscountValue), and discountValuesInternal of type java.lang.String. To import discount value, follow the steps below only using discountValuesInternal.

1. Go to Integration UI Tool Modeling InboundOMMOrderEntry and select the discountValuesInternal attribute.

2. Check the InboundOMMOrderEntry Integration Object metadata using either the IMPEX VIEW or EDMX VIEW.

![153_image_0.png](153_image_0.png)

EDMX VIEW

## Sample Code

<edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" Version="1.0"> <edmx:DataServices xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" m:DataServiceVersion="2.0"> <Schema xmlns="http://schemas.microsoft.com/ado/2008/09/edm" xmlns:s="http://schemas.sap.com/commerce" Namespace="HybrisCommerceOData <EntityType Name="Order"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="code" Nullable="true" Type="Edm.String" s:IsUnique="true"/> <Property Name="versionID" Nullable="true" Type="Edm.String" s:IsUnique="true"/> <Property Name="integrationKey" Nullable="false" Type="Edm.String" s:Alias="Order_code|Order_versionID"/> </EntityType> <EntityType Name="OrderEntry"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="entryNumber" Nullable="true" Type="Edm.Int32" s:IsUnique="true"/> <Property Name="quantity" Nullable="false" Type="Edm.Int64"/> <Property Name="totalPrice" Nullable="true" Type="Edm.Double"/> <Property Name="discountValuesInternal" Nullable="true" Type="Edm.String"/> <Property Name="basePrice" Nullable="true" Type="Edm.Double"/> <Property Name="integrationKey" Nullable="false" Type="Edm.String" s:Alias="OrderEntry_entryNumber|Order_code|Order_versionID <NavigationProperty FromRole="OrderEntry" Name="product" Nullable="false" Relationship="HybrisCommerceOData.FK_OrderEntry_pro <NavigationProperty FromRole="OrderEntry" Name="order" Nullable="false" Relationship="HybrisCommerceOData.FK_OrderEntry_order <NavigationProperty FromRole="OrderEntry" Name="unit" Nullable="false" Relationship="HybrisCommerceOData.FK_OrderEntry_unit" </EntityType> <EntityType Name="CatalogVersion"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="version" Nullable="false" Type="Edm.String" s:IsUnique="true"/> <Property Name="integrationKey" Nullable="false" Type="Edm.String" s:Alias="CatalogVersion_version|Catalog_id"/> <NavigationProperty FromRole="CatalogVersion" Name="catalog" Nullable="false" Relationship="HybrisCommerceOData.FK_CatalogVer </EntityType> <EntityType Name="Product"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="code" Nullable="false" Type="Edm.String" s:IsUnique="true"/> <Property Name="integrationKey" Nullable="false" Type="Edm.String" s:Alias="CatalogVersion_version|Catalog_id|Product_code"/> <NavigationProperty FromRole="Product" Name="catalogVersion" Nullable="false" Relationship="HybrisCommerceOData.FK_Product_ca </EntityType> <EntityType Name="Unit"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="code" Nullable="false" Type="Edm.String" s:IsUnique="true"/> <Property Name="integrationKey" Nullable="false" Type="Edm.String" s:Alias="Unit_code"/> </EntityType>
 <EntityType Name="Catalog">
 <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="id" Nullable="false" Type="Edm.String" s:IsUnique="true"/> <Property Name="integrationKey" Nullable="false" Type="Edm.String" s:Alias="Catalog_id"/> </EntityType> <Association Name="FK_Product_catalogVersion"> <End Multiplicity="0..1" Role="Product" Type="HybrisCommerceOData.Product"/> <End Multiplicity="0..1" Role="CatalogVersion" Type="HybrisCommerceOData.CatalogVersion"/>
 </Association>
 <Association Name="FK_CatalogVersion_catalog"> <End Multiplicity="0..1" Role="CatalogVersion" Type="HybrisCommerceOData.CatalogVersion"/> <End Multiplicity="0..1" Role="Catalog" Type="HybrisCommerceOData.Catalog"/> </Association> <Association Name="FK_OrderEntry_product"> <End Multiplicity="0..1" Role="OrderEntry" Type="HybrisCommerceOData.OrderEntry"/> <End Multiplicity="0..1" Role="Product" Type="HybrisCommerceOData.Product"/> </Association> <Association Name="FK_OrderEntry_order"> <End Multiplicity="0..1" Role="OrderEntry" Type="HybrisCommerceOData.OrderEntry"/> <End Multiplicity="0..1" Role="Order" Type="HybrisCommerceOData.Order"/> </Association> <Association Name="FK_OrderEntry_unit"> <End Multiplicity="0..1" Role="OrderEntry" Type="HybrisCommerceOData.OrderEntry"/> <End Multiplicity="0..1" Role="Unit" Type="HybrisCommerceOData.Unit"/> </Association> <EntityContainer Name="Container" m:IsDefaultEntityContainer="true"> <EntitySet EntityType="HybrisCommerceOData.Order" Name="Orders"/> <EntitySet EntityType="HybrisCommerceOData.OrderEntry" Name="OrderEntries"/> <EntitySet EntityType="HybrisCommerceOData.CatalogVersion" Name="CatalogVersions"/> <EntitySet EntityType="HybrisCommerceOData.Product" Name="Products"/> <EntitySet EntityType="HybrisCommerceOData.Unit" Name="Units"/> <EntitySet EntityType="HybrisCommerceOData.Catalog" Name="Catalogs"/> <AssociationSet Association="HybrisCommerceOData.FK_Product_catalogVersion" Name="Product_CatalogVersions"> <End EntitySet="Products" Role="Product"/> <End EntitySet="CatalogVersions" Role="CatalogVersion"/> </AssociationSet> <AssociationSet Association="HybrisCommerceOData.FK_CatalogVersion_catalog" Name="CatalogVersion_Catalogs"> <End EntitySet="CatalogVersions" Role="CatalogVersion"/> <End EntitySet="Catalogs" Role="Catalog"/> </AssociationSet> <AssociationSet Association="HybrisCommerceOData.FK_OrderEntry_product" Name="OrderEntry_Products"> <End EntitySet="OrderEntries" Role="OrderEntry"/> <End EntitySet="Products" Role="Product"/> </AssociationSet> <AssociationSet Association="HybrisCommerceOData.FK_OrderEntry_order" Name="OrderEntry_Orders"> <End EntitySet="OrderEntries" Role="OrderEntry"/> <End EntitySet="Orders" Role="Order"/> </AssociationSet> <AssociationSet Association="HybrisCommerceOData.FK_OrderEntry_unit" Name="OrderEntry_Units"> <End EntitySet="OrderEntries" Role="OrderEntry"/> <End EntitySet="Units" Role="Unit"/> </AssociationSet> </EntityContainer> </Schema> </edmx:DataServices> </edmx:Edmx>
3. Send POST request https://localhost:9002/odata2webservices/InboundOMMOrderEntry/OrderEntries with the following body:
 Sample Code
{ "totalPrice": "246.0", "order": { "code": "test", "integrationKey": "TEST_KEY" }, "quantity": "2", "basePrice": "123.0", "unit": { "code": "pieces", "integrationKey": "TEST_KEY" }, "entryNumber": 0, "product": { "catalogVersion": { "version": "Online", "catalog": { "id": "powertoolsProductCatalog", "integrationKey": "TEST_KEY"
 },
 "integrationKey": "TEST_KEY" }, "code": "3756512", "integrationKey": "TEST_KEY" }, "discountValuesInternal":"<<DV<001\#10\#false>VD>>", "integrationKey": "TEST_KEY" }
 Note The discountValue string can be located by using the following GROOVY script language:
 Sample Code import de.hybris.platform.util.DiscountValue; def discountValue=new DiscountValue('001',10,false,"") println discountValue.toString(); Output: <DV<001\#10.0\#false\#0.0\#\#false>VD> "<DV<" refers to DV_HEADER. ">VD>" refers to DV_FOOTER. "\#" refers to INTERNAL_DELIMITER. 001 refers to the code of the actual discount item. 10.0 refers to the discount rate or value. First false tells whether this value is relative or absolute. 0.0 refers to the applied value of this discount. Second false tells whether the discount value can be target price.

4. Go to Backoffice to see the imported discount values.

![155_image_0.png](155_image_0.png)

![156_image_0.png](156_image_0.png)

Can't See the Backoffice Integration UI Tool After Installing integrationbackoffice Installing the integrationbackoffice extension post-initialization doesn't update the widgets.xml le, which, in turn, doesn't show the newly installed cockpit or widgets. When introducing new widgets after initialization, you must reset the global widgets.xml le. Since Integration Object monitoring adds new widgets and socket connections, this reset process is also required.

To reset the global widgets.xml le, do the following:
1. Log in to Backoffice as an administrator.

2. Press F4 to open the orchestrator. 3. Select the hamburger menu in the top-right corner. 4. Select Reset Everything. 5. Wait for the process to end and then press F4 again to close the orchestrator.

Can't See the Integration UI Tool in Backoffice Due to Limited Permission The Backoffice Integration UI Tool provides Integration Administrator and Integration Agent user roles, and members within the backofficeintegrationadministrator and backofficeintegrationagent groups can see the Integration UI Tool perspective in Backoffice.

To see the Integration UI Tool, users must be assigned to one of the two groups. For more information, see Integration Backoffice Security.

Stack Traces are not Logged Throwable stack traces are logged only when the system has DEBUG-level logging enabled. To enable debug-level logging, see Updating the Log Level to Debug.

Exposing an Integration Object as an API
Follow the steps to expose an example Integration Object with OAuth 2.0 authentication.

Context Complete each of the following procedures to congure an example Integration Object for enhanced authorization. The example uses ImpEx and species OAuth authorization. To congure an Integration Object for Basic authorization, replace the OAuth values with Basic values.

 Note For SAP Commerce Cloud version 2011 and higher, to expose an Integration Object as an API it must be associated with an InboundChannelConguration (ICC). When upgrading to version 2011 and higher, an ICC is automatically created with Basic authentication for an Integration Object that doesn't have a corresponding ICC. Once created, to set the authentication to OAuth, update the authentication type in the ICC. For more information, see Authentication.

For a complete description of enhanced authorization and authentication and other Integration API security features, see Integration API Security.

 Note If you are exposing a legacy API that has search restrictions, it is recommended that you disable those restrictions. See Legacy Authentication for more information.

## Create An Integration Object

Context Import the following ImpEx to create a sample Product Integration Object called MyOauthExampleIO.

Click the arrow to expand the code example.

INSERT_UPDATE IntegrationObject; code[unique = true];

![157_image_0.png](157_image_0.png)

![157_image_1.png](157_image_1.png)

![157_image_2.png](157_image_2.png)

![157_image_3.png](157_image_3.png) ; MyOauthExampleIO ; INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code) ; root[default = false]; ; MyOauthExampleIO ; Product ; Product ; true ; ; MyOauthExampleIO ; Catalog ; Catalog ; ; ; MyOauthExampleIO ; CatalogVersion ; CatalogVersion ; ; INSERT_UPDATE IntegrationObjectItemAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = true]; attr ; MyOauthExampleIO:Product ; code ; Prod ; MyOauthExampleIO:Product ; catalogVersion ; Prod ; MyOauthExampleIO:Product ; name ; Prod ; MyOauthExampleIO:Product ; anotherName ; Prod ; MyOauthExampleIO:Product ; onlineDate ; Prod ; MyOauthExampleIO:Catalog ; id ; Cata ; MyOauthExampleIO:CatalogVersion ; catalog ; Cata ; MyOauthExampleIO:CatalogVersion ; version ; Cata ; MyOauthExampleIO:CatalogVersion ; active ; Cata Create an InboundChannelConguration

![157_image_4.png](157_image_4.png)

Context You can create an InboundChannelConguration (ICC) by importing an ImpEx le or in Backoffice.

Import the following ImpEx example to create an InboundChannelConguration for an Integration Object called MyOauthExampleIO with an inbound channel value of OAUTH.

INSERT_UPDATE InboundChannelConfiguration; integrationObject(code)[unique = true]; authenticationType(code); ; MyOauthExampleIO ; OAUTH ;
 Note When deleting an InboundChannelConguration associated with an ExposedDestination, you must rst delete the ExposedDestination before you are able to delete the ICC. When deleting an Integration Object associated with an InboundChannelConguration, you must rst delete the ICC before you are able to delete the Integration Object.

## Congure The Client Grant Type For Oauth

Context The client grant type associates a user with a client and a client with a session. The IntegrationClientCredentialsDetailsitem type denes the user authorized to make requests in a session. The item type extends the type system's client_credentials grant type and supports only the OAuth authentication ow.

 Note This process applies only to securing Integration Objects with OAuth. If you are using Basic Auth, you do not need to congure the client grant type.

Import the following ImpEx to congure the oauthexampleClient as a user.

INSERT_UPDATE IntegrationClientCredentialsDetails; clientId[unique = true]; resourceIds; authorities ; clientSecret; registeredRedirec ; oauthexampleClient ; hybris ; ROLE_INTEGRATIONADMINGROUP ; userpassword ; https://lo INSERT_UPDATE Employee; name ; UID[unique = true]; groups(uid) ; password; loginDisabled; ; oauthexampleUser ; oauthexampleUser ; integrationadmingroup ; userpassword ; ;
Grant Access Permissions by User Group Context You can grant access permissions by ImpEx or Backoffice. The following example uses Backoffice.

Procedure 1. In the Administration Cockpit perspective, select System Types .

2. Select the type that comprises the Integration Object. In this example, one of the types is Product. 3. Select the Type Permission Action icon. 4. Locate the role associated with user created for the client grant type. Click the icons to toggle the permissions for each action type available. A checkmark grants permission and an x denies permission. For this example, grant access to Read so the user can make a GET request. Close the Permission Management window when done.

5. Repeat this process for each type included in the Integration Object to ensure the user can interact with all of the Integration Object's item types.

This is   For more    the SAP Help  158 Retrieve an OAuth Endpoint Context The following example returns the metadata for the MyOauthExampleIO Integration Object you created, authenticated, and secured with OAuth in the preceding steps. To retrieve an access token for an OAuth request, provide:
Grant Type - client credentials Access Token URL Client ID Client Secret Example Request URL
GET https://localhost:9002/odata2webservices/MyOauthExampleIO/$metadata Example Response Body A successful request returns a 200 OK response.

<?xml version='1.0' encoding='UTF-8'?> <edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" Version="1.0"> <edmx:DataServices m:DataServiceVersion="1.0" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"> <Schema Namespace="HybrisCommerceOData" xmlns="http://schemas.microsoft.com/ado/2008/09/edm" s:schema-version="1" xmlns:s="http://schemas.sap <EntityType Name="Localized___Product"> <Key> <PropertyRef Name="language"/> </Key> <Property Name="name" Type="Edm.String" s:IsLanguageDependent="true" Nullable="true"/> <Property Name="anotherName" Type="Edm.String" s:IsLanguageDependent="true" Nullable="true"/> <Property Name="language" Type="Edm.String" Nullable="false"/> </EntityType> <EntityType Name="CatalogVersion"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="active" Type="Edm.Boolean" Nullable="true"/> <Property Name="version" Type="Edm.String" Nullable="false" s:IsUnique="true"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" s:Alias="CatalogVersion_version|Catalog_id"/> <NavigationProperty Name="catalog" Relationship="HybrisCommerceOData.FK_CatalogVersion_catalog" FromRole="CatalogVersion" ToRole="Cat </EntityType> <EntityType Name="Product"> <Key> <PropertyRef Name="integrationKey"/> </Key> <Property Name="onlineDate" Type="Edm.DateTime" Nullable="true"/> <Property Name="name" Type="Edm.String" s:IsLanguageDependent="true" Nullable="true"/> <Property Name="code" Type="Edm.String" Nullable="false" s:IsUnique="true"/> <Property Name="anotherName" Type="Edm.String" s:IsLanguageDependent="true" Nullable="true"/> <Property Name="integrationKey" Type="Edm.String" Nullable="false" s:Alias="CatalogVersion_version|Catalog_id|Product_code"/> <NavigationProperty Name="catalogVersion" Relationship="HybrisCommerceOData.FK_Product_catalogVersion" FromRole="Product" ToRole="Cat <NavigationProperty Name="localizedAttributes" Relationship="HybrisCommerceOData.FK_Product_localizedAttributes" FromRole="Product" T </EntityType> <EntityType Name="Catalog"> <Key> <PropertyRef Name="integrationKey"/> </Key>
 <Property Name="id" Type="Edm.String" Nullable="false" s:IsUnique="true"/>
 <Property Name="integrationKey" Type="Edm.String" Nullable="false" s:Alias="Catalog_id"/> </EntityType> <Association Name="FK_Product_catalogVersion"> <End Type="HybrisCommerceOData.Product" Multiplicity="0..1" Role="Product"/> <End Type="HybrisCommerceOData.CatalogVersion" Multiplicity="0..1" Role="CatalogVersion"/> </Association> <Association Name="FK_CatalogVersion_catalog"> <End Type="HybrisCommerceOData.CatalogVersion" Multiplicity="0..1" Role="CatalogVersion"/> <End Type="HybrisCommerceOData.Catalog" Multiplicity="0..1" Role="Catalog"/> </Association> <Association Name="FK_Product_localizedAttributes"> <End Type="HybrisCommerceOData.Product" Multiplicity="1" Role="Product"/> <End Type="HybrisCommerceOData.Localized___Product" Multiplicity="*" Role="Localized___Product"/> </Association> <EntityContainer Name="Container" m:IsDefaultEntityContainer="true"> <EntitySet Name="Localized___Products" EntityType="HybrisCommerceOData.Localized___Product"/> <EntitySet Name="CatalogVersions" EntityType="HybrisCommerceOData.CatalogVersion"/> <EntitySet Name="Products" EntityType="HybrisCommerceOData.Product"/> <EntitySet Name="Catalogs" EntityType="HybrisCommerceOData.Catalog"/> <AssociationSet Name="Product_CatalogVersions" Association="HybrisCommerceOData.FK_Product_catalogVersion"> <End EntitySet="Products" Role="Product"/> <End EntitySet="CatalogVersions" Role="CatalogVersion"/> </AssociationSet> <AssociationSet Name="CatalogVersion_Catalogs" Association="HybrisCommerceOData.FK_CatalogVersion_catalog"> <End EntitySet="CatalogVersions" Role="CatalogVersion"/> <End EntitySet="Catalogs" Role="Catalog"/> </AssociationSet> <AssociationSet Name="Product_Localized___Products" Association="HybrisCommerceOData.FK_Product_localizedAttributes"> <End EntitySet="Products" Role="Product"/> <End EntitySet="Localized___Products" Role="Localized___Product"/> </AssociationSet> </EntityContainer> </Schema> </edmx:DataServices> </edmx:Edmx>
Exposing an Integration Object Using Backoffice Use the following instructions to expose an Integration Object as an API in Backoffice.

Context The following instructions describe only the steps to congure an InboundChannelConguration with exposed destinations. When exposing an Integration Object, you must also identify the user authorized to make requests. Additionally, you must grant access permissions for each request type based on the user group. For these instructions, as well as steps to expose an Integration Object using ImpEx, see Exposing an Integration Object as an API.

 Note For SAP Commerce Cloud version 2011 and higher, to expose an Integration Object as an API it must be associated with an InboundChannelConguration (ICC). When upgrading to version 2011 and higher, an ICC is automatically created with Basic authentication for an Integration Object that doesn't have a corresponding ICC. Once created, to set the authentication to OAuth, update the authentication type in the ICC. For more information, see Authentication.

Procedure 1. In the Backoffice Integration UI perspective, select Integration APIs Authentication .

2. Select the Add icon to create an InboundChannelConguration. 3. Select the Integration Object. 4. Select the authentication type. Choose one of the following:
Basic OAuth2 OAuth2 - OAuth2 Next , then specify the OAuth Client ID, OAuth client secret, and User.

5. Select Done.

 Note For OAuth2 authentication, if you select OAuth2 Next , once you've selected Done, an IntegrationClientCredentialsDetails and ExposedOAuthCredential are created.

 Note When deleting an Integration Object associated with an InboundChannelConguration, you must rst delete the ICC before you are able to delete the Integration Object.

## Update An Existing Conguration

Context To update an existing conguration, locate and select a conguration and change the Authentication Type in the details pane. Select Save. To update an existing inbound channel conguration, locate and select a conguration and change the Authentication Type in the details pane. Select Save. To edit any information related to an endpoint or a destination, see Endpoints and Destinations.

## Exposing An Integration Object Using The Meta Api

You can expose an Integration Object as an API with enhanced authorization using the InboundChannelConguration Meta API. The following example shows how you can congure an InboundChannelConguration as part of an existing IntegrationService API. When exposing an Integration Object, you must also identify the user authorized to make requests. Additionally, you must grant access permissions for each request type based on the user group. For these instructions, as well as steps to expose an Integration Object using ImpEx, see Exposing an Integration Object as an API.

 Note For SAP Commerce Cloud version 2011 and higher, to expose an Integration Object as an API it must be associated with an InboundChannelConguration (ICC). When upgrading to version 2011 and higher, an ICC is automatically created with Basic authentication for an Integration Object that doesn't have a corresponding ICC. Once created, to set the authentication to OAuth, update the authentication type in the ICC. For more information, see Authentication.

The IntegrationService Meta API includes two IntegrationObjectItems, InboundChannelConfiguration and AuthenticationType, that allow you to expose an Integration Object as an API using enhanced OAuth or Basic authentication.

To expose a new or existing Integration Object, send a POST request to the IntegrationService/InboundChannelConfigurations endpoint. The following example exposes an existing Integration Object, MyProduct, as an API, secured with OAuth authentication.

Request URL
https://localhost:9002/odata2webservices/IntegrationService/InboundChannelConfigurations Request Body
{ "integrationObject": { "code": "MyProduct" }, "authenticationType": { "code": "OAUTH" } }
 Note When deleting an InboundChannelConguration associated with an ExposedDestination, you must rst delete the ExposedDestination before you are able to delete the ICC. When deleting an Integration Object associated with an InboundChannelConguration, you must rst delete the ICC before you are able to delete the Integration Object.

## Adding The Integration Api To A Destination Target

Add the Integration API to a destination target with either Basic or OAuth2 credentials.

Procedure 1. Select an Integration Object.

2. Select (Add the Integration API to one or more destination targets). 3. Select one or more Destination Targets. To select multiple targets, use shift-click. 4. Select one of the following:
Basic - Choose an existing basic credential or create a new one by providing the username and password for an existing user of type "employee". Ensure that the user is assigned to the right integration group to access the API. OAuth2 - Choose an existing OAuth credential or create a new one by providing an existing user of type "employee". Please make sure the user is assigned to the right integration group to access the API.

 Note For OAuth2 authentication, when creating a new credential, the user must already be assigned to the following integration group:
integrationbackoffice.client.credentials.authorities, which is a congurable property in the integrationbackoffice extension. The default value is ROLE_INTEGRATIONADMINGROUP.

 Note When deleting an InboundChannelConguration associated with an ExposedDestination, you must rst delete the ExposedDestination before you are able to delete the ICC.

5. Select Done.

For either authentication type, an exposed destination and endpoint are created, and the active status of each exposed destination is automatically set to "true". If you chose the create option, an exposed credential (either Basic or OAuth) is also created.

## Outbound Sync Implementation

Learn how outbound sync is implemented and congure it to publish new and updated Integration Object Items.

The outboundsync extension provides the OutboundSyncJob type. The OutboundSyncJob type allows you to dene the JobPerformable Spring bean that executes when the job runs via the <springId> attribute. By default, the outboundsync extension provides the outboundSyncCronJobPerformable spring bean that collects the changes for publication to the congured destinations. The streamConfigurationContainer attribute species the container for the stream congurations that declares the item types to synchronize. The outboundsync extension provides the cron job, job, and stream conguration container congurations as essential data.

Type Code/ID
cron job outboundSyncCronJob job odataOutboundSyncJob container outboundsyncDataStreams The following types support the outbound sync feature:
OutboundSyncStreamConguration container - Congure the container to identify one or more stream congurations that belong to the container.

OutboundSyncStreamConguration - Associate each stream with an item type and channel conguration.

outboundChannelConguration - An attribute of the outboundSyncStreamConfiguration, use this conguration to identify which integration objects are sent outbound, and their destinations.

ConsumedDestination - Identify the target system to send new and modied Integration Object Items. For more information about destinations, see Endpoints and Destinations. IntegrationObject - Identify the IntegrationObject to associate with the ConsumedDestination.

OutboundSyncJob - Trigger this cron job to run the OutboundSyncJob, which uses the OutboundSyncStreamConguration(s), which calls deltadetect to search for new or updated items by itemType. The cron job sends these detected items to the ConsumedDestination(s).

Identifying a Root Item for Integration Objects The root property is a mandatory Boolean property set on the IntegrationObjectItem type. By default it is set to false. If you have existing Integration Object denitions for which a root item is not specied, you might not be able to use some of the advanced outbound sync features. Be sure to designate a root item for each Integration Object via ImpEx. See Root Items for Integration Objects for more information.

Classication Attributes Outbound sync supports Integration Objects that contain classication attributes. When you create an item that includes classication attributes, the deltadetect extension identies the item and sends it to the congured ConsumedDestination the same way that it sends items without classication attributes.

This is   For more    the SAP Help  161 Virtual Attributes Outbound sync supports Integration Objects that contain virtual attributes. When you create an item that includes virtual attributes, the virtual attributes are included in an outbound payload like any other attribute.

## Conguring Outbound Sync

Create, update, retrieve, or delete an outbound sync conguration for changes to an item type.

Outbound Sync Prerequisites The prerequisites for conguring and using outbound sync include:
Ensuring that either the outboundsync or outboundsyncbackoffice extension is included in your localextensions.xml le. If you add the outboundsyncbackoffice extension, outboundsync is added by default due to a dependency between the two extensions. The outboundsyncbackoffice is required to congure an outbound channel using the Backoffice Integration UI Tool. Creating an Integration Object denition, for example, OutboundProduct. Dene Integration Objects in Backoffice using the Integration UI Tool or using the Meta API. Creating a Consumed Destination to push data to in the Backoffice Administration perspective. For information about creating a Consumed Destination, see Destination Conguration.

Understanding Outbound Sync Conguration The outbound sync process involves the following three things:
1. Conguring the outbound channel through which the changes are sent.

2. Conguring change streams, which determine what changes should be processed and sent outbound. 3. Conguring a cron job that runs periodically and collects the changes since previous runtime and sends them out to an external system.

Conguring Outbound Sync There are two ways to create or update an outbound sync conguration. One way is through the Outbound Sync Meta API, which provides a RESTful endpoint for managing outbound sync congurations. Alternatively, you can use the outbound sync conguration tools within the Backoffice Integration UI Tool. For information on how to congure outbound sync, see Outbound Sync Meta API and Outbound Sync Backoffice Conguration respectively.

Conguring an Outbound Channel Note Before conguring an outbound channel, you must have both an Integration Object and a Consumed Destination available.

You can congure outbound channels via the Meta API or the Backoffice Integration UI Tool. For information on how to congure Outbound Channel Congurations, see Creating Outbound Sync Congurations (using the Meta API) and Creating an Outbound Sync Channel (using the Backoffice Integration UI Tool). The following example is for an OutboundOrder Integration Object:
 Note This example shows a parent-child relationship. A child Integration Object Item is dened as an Integration Object Item that has a reference to the root Integration Object Item (parent). For more information, see the section Conguring Outbound Sync for Changes to an Item and Its Child in this topic. INSERT_UPDATE IntegrationObject; code[unique = true] ; OutboundOrder

INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code) ; root[default = false]

![161_image_0.png](161_image_0.png) ; OutboundOrder ; Order ; Order ; true ; OutboundOrder ; Currency ; Currency ; ; OutboundOrder ; User ; User ; ; OutboundOrder ; OrderEntry ; OrderEntry ; ; OutboundOrder ; Product ; Product ; ; OutboundOrder ; Catalog ; Catalog ; ; OutboundOrder ; CatalogVersion ; CatalogVersion ; ; OutboundOrder ; Unit ; Unit ; $item = integrationObjectItem(integrationObject(code), code) $attributeDescriptor = attributeDescriptor(enclosingType(code), qualifier) $references = returnIntegrationObjectItem(integrationObject(code), code) INSERT_UPDATE IntegrationObjectItemAttribute; $item[unique = true] ; attributeName[unique = true]; $attributeDescriptor ; $references ; OutboundOrder:Order ; code ; Order:code ; ; OutboundOrder:Order ; currency ; Order:currency ; OutboundOrder:Cur ; OutboundOrder:Order ; user ; Order:user ; OutboundOrder:Use ; OutboundOrder:Order ; date ; Order:date ; ; OutboundOrder:Order ; entries ; Order:entries ; OutboundOrder:Ord ; OutboundOrder:Currency ; isocode ; Currency:isocode ; ; OutboundOrder:User ; uid ; User:uid ; ; OutboundOrder:OrderEntry ; order ; OrderEntry:order ; OutboundOrder:Ord ; OutboundOrder:OrderEntry ; entryNumber ; OrderEntry:entryNumber ; ; OutboundOrder:OrderEntry ; product ; OrderEntry:product ; OutboundOrder:Pro ; OutboundOrder:OrderEntry ; quantity ; OrderEntry:quantity ; ; OutboundOrder:OrderEntry ; unit ; OrderEntry:unit ; OutboundOrder:Uni ; OutboundOrder:Product ; code ; Product:code ; ; OutboundOrder:Product ; catalogVersion ; Product:catalogVersion ; OutboundOrder:Cat ; OutboundOrder:Catalog ; id ; Catalog:id ; ; OutboundOrder:CatalogVersion ; version ; CatalogVersion:version ; ; OutboundOrder:CatalogVersion ; catalog ; CatalogVersion:catalog ; OutboundOrder:Cat ; OutboundOrder:Unit ; code ; Unit:code ; 

Based on the above Integration Object example, here is a sample Outbound Channel Conguration following the required steps:
This is   For more    the SAP Help  162 1. Conguring a credential based on its type for the destination:
This sets up a Basic Credential:
INSERT_UPDATE BasicCredential; id[unique = true] ; username; password ; externalPlatformBasicCredential ; admin ; nimda This sets up Consumed OAuth Credentials:
INSERT_UPDATE OAuthClientDetails; clientId[unique = true]; oAuthUrl ; admin ; https://localhost:7002/authorizationserver/oauth/token INSERT_UPDATE ConsumedOAuthCredential; id[unique = true] ; clientId ; clientSecret; oAuthUrl; ; externalPlatformConsumedOAuthCredential ; admin ; nimda ; https://localhost:7002/authorizatio 2. Conguring an Endpoint and a Destination Target:
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# \# This sets up the endpoint for another platform instance running on the same box \# We assume it has InboundOrder integration object defined, through which changes \# will be synced into that platform \# \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# INSERT_UPDATE Endpoint; id[unique = true] ; version[unique = true]; name ; specUrl ; another-local-hybris; unknown ; local-hybris ; https://localhost:7002/odata2webservices/InboundOrder/$metadata INSERT_UPDATE DestinationTarget; id[unique = true] ; external-platform 3. Conguring a Consumed Destination based on the credential type:
This sets up a Consumed Destination called "platform-basic" that uses the Basic Credential from Step 1 and the Endpoint from Step2:
INSERT_UPDATE ConsumedDestination; id[unique = true]; url ; endpoint(id, version) ; credential(id) ; destinationTarget(id) ; platform-basic ; https://localhost:7002/odata2webservices/InboundOrder/Orders ; another-local-hybris:unknown ; externalPlatformBasicCred This sets up a Consumed Destination called "platform-basic" that uses the Consumed OAuth Credential from Step 1 and the Endpoint from Step2:
INSERT_UPDATE ConsumedDestination; id[unique = true]; url ; endpoint(id, version) ; credential(id) ; destinationTarget(id); additionalProp ; platform-basic ; https://localhost:7002/odata2webservices/InboundOrder/Orders ; another-local-hybris:unknown ; externalPlatformConsumedO
4. Conguring the Outbound Channel Conguration:
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# \# This sets up the outbound channel for sending changes to the destination created above \# and using the OutboundOrder integration object for the payload. \# \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# INSERT_UPDATE OutboundChannelConfiguration; code[unique = true]; integrationObject(code); destination(id) ; outbound-orders ; OutboundOrder ; platform-basic For information on how to congure Outbound Channel Congurations, see Creating Outbound Sync Congurations (using the Meta API) and Creating an Outbound Sync Channel (using the Backoffice Integration UI Tool).

Conguring Change Streams In addition to knowing where the changes need to be sent, you need to congure outbound sync to know what changes to send. You do this by conguring change streams. Each stream is created for a single type in the platform type system to track changes, and the stream also species the outbound channel the type item changes are sent through. The streams are then grouped together via a stream container, which denes what changes are sent for a specic use case. Based on the example above for the relation between Order and Order Entry, the following example creates streams and the container to track changes in the Order items:
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# \# Create a stream container for the order sync use case \# \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# INSERT_UPDATE OutboundSyncStreamConfigurationContainer; id[unique = true] ; order-sync-changes \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# \# Create a stream for each platform type that should trigger outbound sync \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# INSERT_UPDATE OutboundSyncStreamConfiguration; streamId[unique = true]; container(id) ; itemTypeForStream(code); outboundChannelConfiguration(co ; orderStream ; order-sync-changes ; Order ; outbound-orders ; orderEntryStream ; order-sync-changes ; OrderEntry ; outbound-orders The above conguration sends updates when an Order is changed. Because OrderEntry is a child of Order, when an OrderEntry is changed, the OrderEntry changes are aggregated and sent via the Order Integration Object. If the sync job contains a change stream for an item type that is not in the Integration Object associated with the corresponding outbound channel conguration, the changes for that type are not processed—they are ignored. For example, if the Integration Object contains only Customer and Address types, but there is also an outbound sync stream conguration for the UserProle type, any change (create, update, delete) to the UserProle item is not processed and does not affect the job results. If the changed item is not associated with the root item that has type present in the Integration Object, then that change is also not processed. For example, if the Integration Object contains Customer and Address types, and an Address item is created, updated, or deleted but the address is associated with an Employee (not a Customer), that change is ignored without affecting the job results.

## Note

In the case where the infoExpression is miscalculated and autogenerated to an incorrect value, you can use the outboundsync.disabled.info.expression.auto.generation.stream.ids property to override the infoExpression on the affected OutboundSyncStreamConguration. To do so, set the value of outboundsync.disabled.info.expression.auto.generation.stream.ids to the streamId you want to override. For example, outboundsync.disabled.info.expression.auto.generation.stream.ids = "orderStream". To override more than one stream, separate the streamIds by commas. For example, outboundsync.disabled.info.expression.auto.generation.stream.ids = "orderStream, orderEntryStream".

Conguring Outbound Sync Cron Jobs Once the outbound channel and the change streams are dened, you can congure a cron job that periodically synchronizes the existing changes automatically according to a dened trigger or schedule. You need to congure an OutboundSyncJob, which is a subtype of Job, and OutboundSyncCronJob, which is a subtype of CronJob, so that you can use all of the Job and CronJob features, for example, triggers. The following is a simple example of how you can congure the cron job without an automatic trigger:
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# \# This job refers the stream container created above \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# INSERT_UPDATE OutboundSyncJob; code[unique = true]; streamConfigurationContainer(id) ; orderSyncJob ; order-sync-changes INSERT_UPDATE OutboundSyncCronJob; code[unique = true]; job(code) ; sessionLanguage(isoCode) ; orderSyncCronJob ; orderSyncJob; en For information on running outbound sync cron jobs, see Scheduling Outbound Sync. For information on cron job data cleanup, see Monitoring Retention Policy. You can autogenerate change streams and cron jobs for outbound sync. For more information, see Autogenerate an Outbound Sync Conguration.

Conguring Outbound Sync for Changes to an Item and Its Child You can congure outbound sync to detect and send changes for an Integration Object Item and its child. The congurations described in this topic send a root Integration Object outbound when a change is detected on a "child" Integration Object Item. A child Integration Object Item is dened as an Integration Object Item that has a reference to the root Integration Object Item (parent). This feature is useful when syncing items that don't make much sense by themselves. For example, an OrderEntry is always associated with an Order. Therefore, you always want to send the whole Order, even when the only change detected is for the OrderEntry. A similar relation exists between an Address and a Customer. The address is always associated with an owner such as a Customer, Employee, or Company. So when a change is detected in an Address, you want to sync the entire Customer item. The following Outbound Customer Integration Object with the root item Customer shows the relationship between Customer and Address:
INSERT_UPDATE IntegrationObject; code[unique = true] ; OutboundCustomer INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code); root ; OutboundCustomer ; Customer ; Customer ; true ; OutboundCustomer ; Address ; Address ; false $integrationItem = integrationObjectItem(integrationObject(code), code) $attributeDescriptor = attributeDescriptor(enclosingType(code), qualifier) $returnItem = returnIntegrationObjectItem(integrationObject(code), code) INSERT_UPDATE IntegrationObjectItemAttribute; $integrationItem[unique = true]; attributeName[unique = true]; $attributeDescriptor; $returnItem ; OutboundCustomer:Customer ; uid ; Customer:uid ; ; OutboundCustomer:Customer ; addresses ; Customer:addresses ; OutboundCustomer:A ; OutboundCustomer:Address ; owner ; Address:owner ; OutboundCustomer:C ; OutboundCustomer:Address ; email ; Address:email ; 
When a Root Item is Dened When a root item is dened, as in the Outbound Customer Integration Object with the root item Customer example above, outbound sync attempts to maintain the unit of work (in this case, Customer) regardless of what item changed in the Integration Object. It is the root item payload that is sent out. The changed item is reected as nested in the root item payload. Whether or not the Customer item changes or any of its children change (for example, Address) in SAP Commerce Cloud, outbound sync attempts to send the Customer payload with nested addresses. For example, for a new customer created with the user ID "jsmith" and a new address added for that customer in SAP Commerce Cloud, outbound sync detects that both changes are related to the same root item and aggregates the changes and sends the following payload:
{ "uid": "jsmith", "addresses": [ { "owner": { "uid": "jsmith" }, "email": "jsmith@somebusiness.com", "integrationKey": "jsmith%40somebusiness.com|jsmith" } ], "integrationKey": "jsmith" }
For additional information, see Conguring Root Item Grouping Sizes and Timeouts.

When a Root Item is Not Dened When a root item is not dened, there isn't an item in the Integration Object denition for which the root attribute is set to true. That means each item in the Integration Object is the "root": equally important and independent of the each other. In this case, each change is independent, not aggregated, and sent by itself. For the scenario above, outbound sync detects changes in the customer and sends them out as a Customer payload:
{ "uid": "jsmith", "addresses": [ { "owner": { "uid": "jsmith" }, "email": "jsmith@somebusiness.com", "integrationKey": "jsmith%40somebusiness.com|jsmith" } ], "integrationKey": "jsmith" }
Then outbound sync detects changes in the customer's address and sends the Address payload independently of the Customer payload:

{ "owner": { "uid": "jsmith", "addresses": [ { "email": "jsmith@somebusiness.com" } ], "integrationKey": "jsmith" }, "email": "jsmith@somebusiness.com", "integrationKey": "jsmith%40somebusiness.com|jsmith" }
Because outbound sync sends out the current state of the item it sends same information twice. The only difference is the arrangement of the payload. This is especially important to consider when the relationship between the root item and the detail item is one-to-many: the same state but in a different arrangement is sent for every changed item. For example, if you create a customer and add three addresses to it, the change is sent four times. If a change stream isn't congured for the Address type, the change won't be recognized and no item is sent. In that case, customer changes are sent out only when the Customer item changes in SAP Commerce Cloud. Because changes are processed asynchronously and without aggregation, it's possible that Address is sent before Customer. The order depends on the order of the change/delta streams within the stream container: outbound sync processes changes from the rst change stream, then the second, et cetera, but even then race conditions are still possible.

 Note It's important to understand that the root item behavior described in the sections "When a Root Item is Dened" and "When a Root Item is Not Dened" is achievable only if the root item can be derived (navigated to) from the nested detail item, for example, Address, using the Integration Object attributes. Therefore, if the Integration Object above is dened without the Address:owner attribute, which references back to the root item, it isn't possible to derive the root item for Address. Even if Customer is marked as the root item, outbound sync does not send the payloads independent of each other, without aggregation, as described in the case above when no root item is dened.

Batch Requests for Outbound Sync Batch requests allow large amounts of data to be sent instead of multiple individual REST requests. When enabled, the changes detected when running an outbound sync cron job are aggregated and sent as a single batch request to the target system. When disabled (the default setting), requests are sent individually. The following example is of an OutboundChannelConguration with batch enabled:
 Sample Code INSERT_UPDATE OutboundChannelConfiguration; code[unique = true]; integrationObject(code); destination(id); batch[default = false]; ; outbound-orders ; OutboundOrder ; platform-basic ; true ;
When batching is enabled, each change that is usually sent as an individual request is sent as a changeset in the batch. The maximum number of changesets contained in a single batch request is determined by the following property:

| Parameter                | Description                                                                  | Default Value   |
|--------------------------|------------------------------------------------------------------------------|-----------------|
| outboundsync.batch.limit | Indicates the maximum number of changesets present in the batch 200 request. |                 |

The batch limit does not necessarily match the individual number of changes detected by delta detect when performing the outbound sync. In some cases, when the change for different types has the same root pk, those changes are all sent as one single nested request, so those would then be sent as one changeset in the batch. For example, 1 order with 2 Order Entries. When running the cronjob, 3 changes are detected (1 per individual item in the system), but only 1 changeset with all 3 is added to the batch so only 1 counts towards the batch limit set by the outboundsync.batch.limit property.

Each batch changeset in the request is associated with an auto-generated UUID to identify it. This UUID is sent as part of each batch changeset as a changeset header called Content-ID. The Content-ID is expected to be returned as part of the batch response from the destination system. The Content-ID is needed in order to match the parts of the response with the parts of the request so that when receiving a response the system knows how to process each item based on that response. When a response doesn't contain the Content-ID that was sent for a changeset in the batch, a warning is logged in the terminal, and the item is processed as if it failed to synchronize so it is retried following pre-existing outbound sync retry rules. For information on how to enable batch requests, see Enabling Batch Requests for Outbound Sync and Creating an Outbound Sync Channel.

Item Delete Synchronization By default, item deletions are ignored and therefore not part of outbound sync published data. To include deletions in outbound sync, you must set the synchronizeDelete ag in the OutboundChannelConguration. You can set the ag in the following two ways:
ImpEx Sample Code INSERT_UPDATE OutboundChannelConfiguration; code[unique = true]; integrationObject(code); destination(id); synchronizeDelete ; outbound-orders ; OutboundOrder ; platform-basic ; true Outbound Sync Meta API
Send POST request https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations with the following body:
 Sample Code Authorization: Basic {{user}} {{password}} Content-Type: application/json Accept: application/json { "code": "OutboundProductChannel",
 "integrationObject": {
 "code": "OutboundProduct" }, "destination": { "id": "platform-basic", "destinationTarget": { "id": "outboundtest" } }, "synchronizeDelete": true
}
Only Item deletes related to root items are synchronized. For example, if an Integration Object contains Customer and Address types, where Customer is the root item, deletion of a Customer item is synchronized but deletion of an Address is ignored.

 Note When updating an existing OutboundChannelConguration to synchronize deletes, item deletes are captured only for items that have been modied or newly created after you set the Enable Delete ag to true. When creating a new OutboundChannelConguration, all of the items are eligible for delete.

Outbound Sync Meta API The Outbound Sync Meta API provides a RESTful endpoint for creating, updating, retrieving, or deleting outbound sync congurations. Outbound Sync Backoffice Conguration Congure outbound sync for changes to a single Integration Object Item type using Backoffice.

## Outbound Sync Meta Api

The Outbound Sync Meta API provides a RESTful endpoint for creating, updating, retrieving, or deleting outbound sync congurations.

Access the Meta API through the OutboundChannelConfig service. Use the API to create, update, view, or delete a complete conguration using the autogenerate feature, or perform the same requests on any component of an outbound sync conguration. See the following table for components. For any of the methods, the outbound Integration Object must exist. The API exposes the following congurations:

| The API exposes the following congurations:   | Conguration                                                    | Description                                                   |
|-----------------------------------------------|----------------------------------------------------------------|---------------------------------------------------------------|
| Destination-Related Congurations              | ConsumedDestination                                            | Congurations that contain the destination URL and credentials |
| Endpoints                                     | Synchronization destination URLs                               |                                                               |
| DestinationTargets                            | Destination targets required for ConsumedDestinations          |                                                               |
| BasicCredentials                              | Basic credentials to connect to the destination                |                                                               |
| ConsumedOAuthCredentials                      | OAuth credentials to connect to the destination                |                                                               |
| Outbound Sync-Related Congurations            | IntegrationObjects                                             | The Integration Objects to synchronize                        |
| ComposedTypes                                 | The item types to synchronize                                  |                                                               |
| OutboundChannelCongurations                   | Congurations that coordinate the synchronization               |                                                               |
| OutboundSyncStreamCongurationContainers       | Container for a collection of streams                          |                                                               |
| OutboundSyncStreamCongurations                | Streams that Delta Detect uses to discover what to synchronize |                                                               |
| OutboundSyncJobs                              | Job denitions that the cron job executes                       |                                                               |
| OutboundSyncCronJobs                          | Cron jobs called to run the OutboundSyncJobs                   |                                                               |
| Triggers                                      | Triggers that initiate the cron job                            |                                                               |

The following topics describe how to retrieve, create, update, and delete outbound sync conguration data using the Meta API.

Creating Outbound Sync Congurations Create an outbound sync conguration with a POST request to the Outbound Sync Meta API. Retrieving Outbound Sync Congurations Get information about an outbound sync conguration using the Outbound Sync Meta API. Updating Outbound Sync Congurations Update an outbound sync channel conguration with a PATCH request to the Outbound Sync Meta API. Deleting Outbound Sync Congurations Delete an outbound sync channel conguration with a request to the Outbound Sync Meta API.

## Creating Outbound Sync Congurations

Create an outbound sync conguration with a POST request to the Outbound Sync Meta API.

You can create a complete conguration using the autogenerate feature, or you can individually create any of the components of the outbound sync conguration using the conguration endpoints listed in Outbound Sync Meta API. To create components of an outbound sync conguration, send a request to the associated conguration endpoint. For example, to create an outbound sync stream conguration container, send a POST request to the following URL.

POST https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundSyncStreamConfigurationContainers To create a complete conguration using the autogenerate feature, send a POST request to the OutboundChannelConfigurations endpoint. Include the Integration Object, consumed destination, destination URL, and destination targets in the request body. Because autogenerate does not create a trigger to initiate the outboundSyncCronJob, the example shows how to create the trigger as an additional step. A successful request creates the following components of an outbound sync conguration:
outbound channel conguration stream container streams outbound sync job cron job consumedDestination (if it does not exist)
You can also use an existing Consumed Destination by providing its integration key.

OutboundSyncStreamCongurations created using autogenerate have an empty where clause. To use a where clause on an autogenerated stream conguration, perform a PATCH update on the stream conguration after creating it. For more information, see Updating Outbound Sync Congurations Note For more information about the autogenerate feature, see Autogenerate an Outbound Sync Conguration.

The following example creates an OutboundChannelConguration called MyOutboundChannelConfig and assumes that the Integration Object MyProduct exists. The request autocreates all of the related channel congurations, including the Consumed Destination and its required attributes, and has batch requests enabled.

 Note For more information on batch requests, see "Batch Requests for Outbound Sync" in Conguring Outbound Sync.

Request URL
POST https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations Request Body
{ "code": "MyOutboundChannelConfig", "integrationObject":{ "code":"MyProduct" }, "destination":{ "id": "MyConsumedDestination", "url": "https://localhost:9002/odata2webservices/MyProduct/Products", "credentialBasic": { "id": "MyBasicCredential", "username": "destinationUsername", "password": "destinationPasswordValue" }, "endpoint":{ "name": "MyEndpoint", "id": "MyEndpoint", "specUrl": "https://targetSystem/urlThatDoesNotMatter", "version": "endpoint_versioin_1.0" }, "destinationTarget":{ "id": "MyDestinationTarget" } }, "autoGenerate":true, "batch": false }
To create an Outbound Channel Conguration for a new or existing Consumed Destination with OAuth authentication, replace credentialBasic with the credentialConsumedOAuth attribute in the above request body. For an example:
"credentialConsumedOAuth": { "id": "oAuthCredential", "clientId": "destinationClientId", "clientSecret": "destinationClientSecret" } 
This is   For more    the SAP Help  167 Response Code A successful request returns a 201 status code.

Response Body
{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('MyOutboundChannelConfig')",
 "uri": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('MyOutboundChannelConfig')",
 "type": "HybrisCommerceOData.OutboundChannelConfiguration" }, "code": "MyOutboundChannelConfig", "autoGenerate": true, "integrationKey": "MyOutboundChannelConfig", "integrationObject": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('MyOutboundChannelConfig')/integ } }, "destination": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('MyOutboundChannelConfig')/desti } } } }
 Note When deleting an Integration Object associated with an OutboundChannelConguration, you must rst delete the OutboundChannelConguration before you are able to delete the Integration Object.

Create the Cron Job Trigger POST to the /Triggers endpoint to congure the outboundSyncCronJob schedule. For example, the following request congures the outboundSetUpTestCronJob to run daily at 12:00 PM.

Request URL
https://localhost:9002/odata2webservices/OutboundChannelConfig/Triggers Request Body
{ "cronJob":{ "code": "outboundSetUpTestCronJob" }, "cronExpression": "0 0 12 * * ?" }
See Scheduling Outbound Sync for more information.

Retrieving Outbound Sync Congurations Get information about an outbound sync conguration using the Outbound Sync Meta API. You can use a GET request to retrieve conguration metadata or the values for a specic conguration. Metadata provides information on each of the outbound sync- and destination-related congurations. When you request a specic conguration, the API returns the values for the requested conguration. To retrieve metadata, make a GET request to the following URL.

GET https://localhost:9002/odata2webservices/OutboundChannelConfig/$metadata To retrieve any conguration, append the conguration name to the request URL. Conguration names are listed in Outbound Sync Meta API. For example, the following URL retrieves information from OutboundChannelCongurations.

GET https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations The following is an example response for an OutboundChannelCongurations GET request.

{ "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('outboundExample')",
This is   For more    the SAP Help  168
 "uri": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('outboundExample')",
 "type": "HybrisCommerceOData.OutboundChannelConfiguration" }, "code": "outboundExample", "autoGenerate": false, "integrationKey": "outboundExample", "integrationObject": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('outboundExample')/integ }
 },
 "destination": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('outboundExample')/desti } } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('MyOutboundChannelConfig')", "uri": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('MyOutboundChannelConfig')", "type": "HybrisCommerceOData.OutboundChannelConfiguration" }, "code": "MyOutboundChannelConfig", "autoGenerate": true, "integrationKey": "MyOutboundChannelConfig", "integrationObject": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('MyOutboundChannelConfig } }, "destination": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('MyOutboundChannelConfig } } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('%257B%257BoutboundChannelCod "uri": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('%257B%257BoutboundChannelCo "type": "HybrisCommerceOData.OutboundChannelConfiguration" }, "code": "{{outboundChannelCode}}", "autoGenerate": true, "integrationKey": "%7B%7BoutboundChannelCode%7D%7D", "integrationObject": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('%257B%257BoutboundChann } }, "destination": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundChannelConfigurations('%257B%257BoutboundChann } } } ] } }

## Updating Outbound Sync Congurations

Update an outbound sync channel conguration with a PATCH request to the Outbound Sync Meta API. You can update a complete conguration or you can individually update any of the components of the outbound sync conguration using the conguration endpoints listed in Outbound Sync Meta API.

Where Clause When autogenerating the OutboundChannelConguration, the generated OutboundSyncStreamConguration does not include a where clause that restricts delta detection. If you need a where clause, update the OutboundSyncStreamConguration as shown in the following example.

Request URL
PATCH https://localhost:9002/odata2webservices/OutboundChannelConfig/OutboundSyncStreamConfigurations('MyOutboundChannelConfig_Product_Stream')
Request Body

{ "whereClause": "{item.catalogVersion} IN ({{SELECT {c.pk} FROM {CatalogVersion as c} WHERE {c.version}='MyCatalogVersion'}})" }
Deleting Outbound Sync Congurations Delete an outbound sync channel conguration with a request to the Outbound Sync Meta API. You can delete a complete outbound sync conguration or individually update any component of a conguration through a DELETE request, using the endpoints listed in Outbound Sync Meta API. Provide an integration key that includes the ConsumedDestination_id and the DestinationTarget_id. For example, the following request deletes the value for the consumed destination MyConsumedDestination.

DELETE https://localhost:9002/odata2webservices/OutboundChannelConfig/ConsumedDestinations('MyConsumedDestination%7CMyDestinationTarget')
A successful response returns a 200 OK response code with no response body.

 Note When deleting an Integration Object associated with an OutboundChannelConguration, you must rst delete the OutboundChannelConguration before you are able to delete the Integration Object.

Outbound Sync Backoffice Conguration Congure outbound sync for changes to a single Integration Object Item type using Backoffice. To create or update an outbound sync conguration, follow the topics in this section in the order shown.

Autogenerate an Outbound Sync Conguration You can quickly generate the container, one or more streams, job, and cronjob for an outbound sync conguration based on a container conguration. Creating an Outbound Sync Channel Create a channel that identies where outbound sync sends updated Integration Objects. Creating a Container for Outbound Sync Integrations Create a container for the set of stream congurations that identify the item types to synchronize. Creating an Outbound Sync Stream Create a stream that species the item types to listen for, and uses the container and channel you created in the preceding tasks. Creating a Sync Job Create a sync job that congures the cron job that runs the sync. Conguring Root Item Grouping Sizes and Timeouts Congure the timeout duration and maximum number of items to collect before sending outbound sync changes for a single Integration Object. Enabling Batch Requests for Outbound Sync Enable batch requests for outbound sync cron jobs.

Autogenerate an Outbound Sync Conguration You can quickly generate the container, one or more streams, job, and cronjob for an outbound sync conguration based on a container conguration.

Context Instead of individually dening each element of an outbound sync conguration, you can dene the channel and add the autoGenerate attribute to the OutboundChannelConguration object.

If you do not autogenerate a conguration, you can congure each item manually. Additionally, if you do not autogenerate a conguration when you create a channel, you cannot autogenerate a conguration from that channel later. When you autogenerate an outbound sync conguration, the operation generates the following associated models:
1 OutboundSyncStreamCongurationContainer 1-to-many OutboundSyncStreamConguration(s) 1 OutboundSyncJob 1 OutboundSyncCronJob Note The autogenerate feature works differently depending on whether a root item is dened for the Integration Object.

If a root item is dened for the Integration Object, the operation creates an OutboundSyncStreamConguration for the dened root item, as well as for any other Integration Object Item that references the same type.

If no root item is dened for the Integration Object, the operation creates an OutboundSyncStreamConguration for each unique type derived from IOItem.getType(). Therefore, either provide a root item for your Integration Object so this does not occur, or delete the unwanted stream congurations.

For more information on root items, see Root Items for Integration Objects.

To generate all necessary outbound sync congurations for the Integration Object, create an Outbound Channel Conguration using the autogenerate ag set to true. For information on creating an Integration Object, see Creating a Simple Integration Object. The following example creates an Outbound Channel Conguration using ImpEx for an existing Integration Object with code set to MyProduct and Product as the root type, and an existing Consumed Destination with the id = MyConsumedDestination with the autogenerate attribute set to true. This automatically creates the streams for all levels of Integration Object Items that reference the root item (Product). This automatically creates the streams for all levels of Integration Object Items that reference the root item.

\# Note: BasicCredential needed if no authentication or authorization is needed for the destination system \# Included in this example because typically both would be good to have for any destination system for security. INSERT_UPDATE BasicCredential; id[unique = true] ; username ; password
 ; MyBasicCredential ; destinationUsername ; destinationPasswordValue
\#Note: name and specUrl or specData attribute values are required in order to create the Endpoint, but does not affect outboundSync functionality. INSERT_UPDATE Endpoint; id[unique = true]; version[unique = true]; name ; specUrl ; MyEndpoint ; endpoint_versioin_1.0 ; MyEndpoint ; https://targetSystem/urlThatDoesNotMatter INSERT_UPDATE DestinationTarget; id[unique = true] ; MyDestinationTarget INSERT_UPDATE ConsumedDestination; id[unique = true] ; url ; endpoint(id, version); destina ; MyConsumedDestination ; https://webhook.site/a292a1cb-dd6d-4242-84c2-5a481dcec913 ; MyEndpoint:endpoint_versioin_1 \#Then to create the OutboundChannelConfiguration, OutboundSyncStreamConfigurationContainer, OutboundSyncStreamConfiguration(s), OutboundSyncJob & Out \#1 INSERT_UPDATE OutboundChannelConfiguration; code[unique = true]; integrationObject(code); destination(id) ; autoGenerate ; MyOutboundChannelConfig ; MyProduct ; MyConsumedDestination ; true You can also create an Outbound Channel Conguration with the autogenerate ag set to true via Meta API (see Creating Outbound Sync Congurations) and Backoffice (see Creating an Outbound Sync Channel).

 Note When deleting an Integration Object associated with an OutboundChannelConguration, you must rst delete the OutboundChannelConguration before you are able to delete the Integration Object.

You can see the three levels generated in Backoffice: one for the root item (Product), the second one for the item that references the root item (CatalogVersion), and one for the third level (Catalog). The preceding example autogenerates the following Outbound Sync Conguration models:
 Note The generated Outbound Sync Stream Conguration streamId removes the enveloping tick marks (` `) from the IntegrationObjectItem.type.code before adding it to the middle of the streamId.

streamId = exChannelCode_Category_Stream = <channel ID> + '_' + < Category ComposedType code > + '_' + 'Stream' channel = exChannelCode = < OutboundChannelConfiguration created above > container = exChannelCodeContainer ** = < OutboundSyncStreamConfigurationContainer created above > itemType = Category

OutboundSyncStreamConguration 2

streamId = exChannelCode_Catalog_Stream = <channel ID> + '_' + < Catalog1 ComposedType code > + '_' + 'Stream' channel = same as channel Stream1 container = same as container as Stream1 itemType = Catalog

OutboundSyncStreamConguration 3

streamId = exChannelCode_CatalogVersion_Stream = <channel ID> + '_' + < CatalogVersion ComposedType code > + '_' + 'Stream' channel = same as channel Stream1 & 2 container = same as container Stream1 & 2 itemType = CatalogVersion

| of the streamId.Model                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Attributes   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| OutboundSyncStreamCongurationContainer id = exChannelCodeContainer = <channel ID> + 'Container' OutboundSyncStreamCongurations OutboundSyncStreamConguration 1 streamId = exChannelCode_Category_Stream = <channel ID> + '_' + < Category ComposedType code > + '_' + 'Stream' channel = exChannelCode = < OutboundChannelConfiguration created above > container = exChannelCodeContainer ** = < OutboundSyncStreamConfigurationContainer created above > itemType = Category OutboundSyncStreamConguration 2 streamId = exChannelCode_Catalog_Stream = <channel ID> + '_' + < Catalog1 ComposedType code > + '_' + 'Stream' |              |

| 7/6/2024 Model      | Attributes                                                                                                                                        |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| OutboundSyncJob     | code = exChannelCodeJob = <channel ID> + 'Job' container = exChannelCodeContainer ** = < OutboundSyncStreamConfigurationContainer created above > |
| OutboundSyncCronJob | code = exChannelCodeCronJob = <channel ID> + 'CronJob' job = exChannelCodeJob = < OutboundSyncJob created above >                                 |

## Creating An Outbound Sync Channel

Create a channel that identies where outbound sync sends updated Integration Objects.

Context Note This page may contain information about features that were only introduced in an update release. Ensure you are always on the latest release to be able to make use of all xes, security updates, and features. For a complete list of what was introduced in each update release, see What's New.

Dene an outbound sync channel using a ConsumedDestination and an IntegrationObject denition.

 Note When deleting an Integration Object associated with an OutboundChannelConguration, you must rst delete the OutboundChannelConguration before you are able to delete the Integration Object.

Procedure 1. Log in to Backoffice and select the Integration UI Tool perspective.

2. Select Outbound Sync Conguration Channels . 3. To add a channel, click +. 4. In the window that appears, dene the following details for the channel.

| Field                                                                                                                           | Description                                                                                       | Example                 |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-------------------------|
| Code                                                                                                                            | Enter a unique name for the channel conguration.                                                  | MarketingProductChannel |
| Integration Object                                                                                                              | Select an integration object to send changes for.                                                 | OutboundProduct         |
| Consumed Destination                                                                                                            | Select a Consumed Destination where outbound sync sends updated Integration Objects. platform-ecp |                         |
| (Optional) Generate Related Congurations Select to autogenerate the container, stream(s), job, and cronjob for the conguration. | N/A                                                                                               |                         |
| For more information, see Autogenerate an Outbound Sync Conguration.                                                            |                                                                                                   |                         |
| (Optional) Enable Delete Requests                                                                                               | Select to enable synchronization of deletions for this channel.                                   | N/A                     |
| (Optional) Enable Batch Requests                                                                                                | Select to enable batch requests for outbound sync cron jobs.                                      | N/A                     |

## Note

You can create a Consumed Destination using the API Registry Module.

To prevent items being sent to, and changes consumed by, an inactive consumed destination, set toggle.outboundsync.destination.active.enabled to true. The default value is false.

5. Select Done.

## Creating A Container For Outbound Sync Integrations

Create a container for the set of stream congurations that identify the item types to synchronize.

Context You can use the container that comes with SAP Commerce Cloud, but the best practice is to create a container specic to your implementation. The container holds all of your outbound integration congurations. Name the container according to the domain. For example, <OrderStreamContainer>. A container can have one or more streams. For example, a container called <OrderStreamContainer> can include the OutboundSyncStreamConguration for Order and the OutboundSyncStreamConguration for OrderEntry Integration Objects.

Procedure 1. Log in to Backoffice and select the Integration UI Tool perspective.

2. Click Outbound Sync Conguration Containers . 3. To add a container, click +. 4. In the window that appears, dene the following details for the container.

This is   For more    the SAP Help  172

Field Description Example

![172_image_0.png](172_image_0.png)

![172_image_1.png](172_image_1.png) Container ID Enter a unique identier for the container. MarketingContainer
5. Click Done.

## Creating An Outbound Sync Stream

Create a stream that species the item types to listen for, and uses the container and channel you created in the preceding tasks.

Context The stream unies all of the outbound sync-related congurations. When the cron job runs, it refers to the stream, which picks up the changes for all items of the item type specied for the stream. For example, in following ImpEx, the itemTypeForStream column contains Product, which includes all Product subtypes. In this case, outbound sync sends the changes for the Product item as well as for the Product subtypes such as ApparelProduct and VariantProduct.

 Sample Code INSERT_UPDATE OutboundSyncStreamConfiguration; streamId[unique = true]; container(id) ; itemTypeForStream(code); outboundChannelConfigura ; productStream ; outboundSyncDataStreams ; Product ; outboundExample To send changes for an exact item type only, without subtypes, restrict the item type in the stream using excludedTypes. For example, the following species the Product item type only:
 Sample Code INSERT_UPDATE OutboundSyncStreamConfiguration; streamId[unique = true]; container(id) ;itemTypeForStream(code); outboundChannelConfigurat ; productStream ; outboundSyncDataStreams ;Product ; outboundExample You can also lter by attribute using whereClause. For example, the following lters out Products that do not have Online as the CatalogVersion:
 Sample Code INSERT_UPDATE OutboundSyncStreamConfiguration; streamId[unique = true]; container(id) ; itemTypeForStream(code); outboundChannelConfigura ; productStream ; outboundSyncDataStreams ; Product ; outboundExample Procedure 1. Log in to Backoffice and select the Integration UI Tool perspective.

2. Click Outbound Sync Conguration Streams . 3. To add a stream, click +. 4. In the window that appears, dene the following details for the stream.

| Field                                                                                               | Description                                                                                          | Example                   |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|---------------------------|
| ID                                                                                                  | Enter a unique name for the stream.                                                                  | MarketingProductStream    |
| Container                                                                                           | Select the container for deltadetect to use.                                                         | MarketingProductContainer |
| Item Type                                                                                           | Select the item type to detect changes for. Subtypes of the specied item are                         | Product                   |
| included unless you restrict the type using a whereClause, as described above.                      |                                                                                                      |                           |
| Outbound                                                                                            | Select the channel where outbound sync sends updated items. The                                      | MarketingProductChannel   |
| Channel                                                                                             | OutboundChannel converts the items to Integration Objects and sends them to                          |                           |
| Conguration the dened destination. Where clause Enter any ltering criteria to specify what to sync. | Only products that are part of the Online catalog version are synchronized:                          |                           |
| (Optional)                                                                                          | `{item.catalogVersion} IN ({{SELECT {c.pk} FROM {CatalogVersion as c} WHERE {c.version}='Online'}})` |                           |
| Excluded                                                                                            | A list of type codes that are subtypes of the Item Type to exclude from delta                        | VariantProduct            |
| Subtypes                                                                                            | detection.                                                                                           |                           |
| (Optional)                                                                                          |                                                                                                      |                           |

5. Click Done. 6. To perform outbound sync, run the outboundSyncCronJob manually or congure it to run according to a dened trigger or schedule. For information about running the cron job, see Scheduling Outbound Sync.

## Creating A Sync Job

Create a sync job that congures the cron job that runs the sync.

Context The sync job associates the cron job with a stream conguration container. Use the container you created in Creating a Container for Outbound Sync Integrations.

Procedure 1. Log in to Backoffice and select the Integration UI Tool perspective.

2. Click Outbound Sync Conguration Jobs .

3. To add a job, click +. 4. In the window that appears, dene the following details for the job.

| Field                                                                                                   | Description                                      | Example                 |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------|-------------------------|
| Code                                                                                                    | Enter a unique identier for the OutboundSyncJob. | MarketingProductSyncJob |
| Stream Conguration Container Select the container you created in the preceding task. MarketingContainer |                                                  |                         |

5. Click Done.

## Conguring Root Item Grouping Sizes And Timeouts

Congure the timeout duration and maximum number of items to collect before sending outbound sync changes for a single Integration Object.

Context Even though several child Items can change for a single parent Integration Object, the outbound sync process sends the parent Integration Object only once. For example, if ve new or updated order entries are detected for a single order, the system sends the Order Integration Object only once. All changes detected for an Integration Object are aggregated into a single call, dened by a maximum item number and timeout duration. Both the number of items sent at once and the timeout duration are congurable.

When the specied value for either the size and timeout parameter is reached, the system sends changes outbound. For example, if outboundsync.item.group.size.max=50 and 50 child items change for an Integration Object, the system sends the item outbound with those changes only. Additional changes for the same parent are then collected until the maximum number of items or the specied timeout duration is reached. If fewer than 50 items are awaiting outbound sync, but the timeout duration ends, then the system sends the child items, regardless of number collected.

| Parameter                                                             | Description                                                    | Default Value   |
|-----------------------------------------------------------------------|----------------------------------------------------------------|-----------------|
| outboundsync.item.group.size.max                                      | Identies the maximum number of child items to collect before   | 50              |
| sending outbound sync changes for a single parent Integration Object. |                                                                |                 |
| outboundsync.item.grouping.timeout                                    | Identies the maximum duration, in milliseconds, to wait before | 5000 ms         |
| sending outbound sync changes for a single parent Integration Object. |                                                                |                 |

Congure the timeout duration and maximum number of items sent in one call Procedure 1. Log in to the Administration Console.

2. Click Platform Conguration . 3. Search for outboundsync.item.group.size.max. 4. In the Value eld, enter the maximum number of items to send. 5. Search for outboundsync.item.grouping.timeout. 6. In the Value eld, enter the timeout duration in milliseconds.

## Enabling Batch Requests For Outbound Sync

Enable batch requests for outbound sync cron jobs.

Context Enabling batch requests allows large amounts of data to be sent instead of multiple individual REST requests. When enabled, the changes detected when running an outbound sync cron job are aggregated and sent as a single batch request to the target system. For more information, see "Batch Requests for Outbound Sync" in Conguring Outbound Sync.

## Enable Batch Requests For Outbound Sync

Procedure 1. Log in to Backoffice.

2. From the dropdown arrow in the upper-left corner of the page, select Integration UI Tool. 3. From the leftside menu, select Conguration Channels . 4. Select an outbound channel, then go to Outbound Channel Details. 5. For Enable Batch Requests, select True.

 Note To disable batch requests, select False.

This is   For more    the SAP Help  174 6. Select Save.

## Scheduling Outbound Sync

Run the outboundSyncCronJob manually or congure it to run according to a dened trigger or schedule.

Context Use the CronJobs feature in the Integration UI Tool to create, congure, and run outbound sync cron jobs. For information about job data cleanup, see Monitoring Retention Policy. You can also run the outboundSyncCronJob from the Administration perspective in Backoffice. However, if you create a cronjob for outbound sync from the Administration perspective instead of from the Integration UI Tool, select the down arrow next to the + icon and select Outbound Sync CronJob. If you do not perform this step, the cron job you create does not appear in the Integration UI Tool's CronJobs view. Search In the top pane of CronJobs, you can search by one or more of the following criteria. In advanced search mode, the system returns results that include all of the selected or entered search criteria. Click the magnifying glass icon to switch to simple search mode, which searches by OutboundSyncCronJob code, only.

Code - Enter a unique identier for an OutboundSyncCronJob. Job denition - Enter the name of an OutboundSyncJob associated with an OutboundSyncCronJob. Current Status - Select a status. For example RUNNING or FINISHED. Last Result - Select a cronjob execution result. For example, SUCCESS or ERROR.

Search results appear in the List view, in the middle pane. List View Select a cronjob in the middle pane to view or edit its details or run the cronjob. Details appear in the third pane of the CronJobs feature.

Procedure 1. Log in to Backoffice and select the Integration UI Tool perspective.

2. Click Outbound Sync Scheduling CronJobs . 3. To add a job, click +. 4. Enter or select the following required values.

Field Value

![174_image_1.png](174_image_1.png)

Job Denition odataOutboundSyncJob

![174_image_0.png](174_image_0.png)

5. Click Done. 6. To run the cron job manually, click the Run CronJob button . To congure a schedule and a trigger, see Conguring Integration API Cron Jobs. You can follow the same instructions from the Outbound Sync CronJobs view instead of switching to the Administration perspective.

## Aborting A Running Outbound Sync Cron Job

If there are outbound sync conguration errors or other issues, you can prevent items in progress from sending to the outbound destination.

Context When an outbound sync cron job runs, its status is RUNNING. Unless you abort the running job, it continues to attempt to synchronize all items, after which, the job status changes to FINISHED. When you abort a job, it nishes the changes already in process, then skips all other changed items in the job queue. The job status changes to ABORTED. Whether the cron job nishes or aborts, one of the following job results is possible:
SUCCESS - No changes were detected or one or more changed items synchronized successfully with no errors. ERROR:
One or more item changes failed to synchronize with the destination system. (For Integration Objects containing virtual attributes) one or more items failed with an IntegrationAttributeProcessingException or any other RuntimeException besides the IntegrationAttributeException. The job continued to process other items. Only changes for the failed item(s) were not consumed and retries were created for the failed items.

FAILURE:
One or more item changes failed. (For Integration Objects containing virtual attributes) one or more item changes failed with an IntegrationAttributeException. The changes for the failed item(s) and the subsequent items were not consumed. Retries were not created or counted for failed or unprocessed items.

SYSTEM_ERROR:
The job failed due to misconguration or another error.

This is   For more    the SAP Help  175

(For Integration Objects containing virtual attributes) the retrieval script is missing.

UNKNOWN - The job aborted immediately after starting before any changes were processed.

When a cron job runs, the abort button enables. To abort an outbound sync cron job:
Procedure 1. In the Integration UI Tool view Backoffice, select Outbound Sync Scheduling CronJobs .

2. Select the running cron job and select abort.

Results When you abort a cron job, the job nishes processing changes that are in progress but skips all changed items waiting in the queue. The Current Status eld changes to Aborted.

 Note The outbound sync job ignores changes for deleted items, and instead immediately consumes deleted items without processing them. Therefore, the result status for deleted item changes in an aborted job is SUCCESS.

Troubleshooting a Cron Job Use the following information to debug and troubleshoot issues with outbound sync cron jobs. If you have access to logging, you can use DEBUG-level logs to perform a stack trace when a job state is unclear. When a job is stuck in the RUNNING state, you can reset it.

Logging When the reason for a job status or result is unclear, you can trace the issue through the logs. To do so, activate DEBUG-level logging for the following loggers:
de.hybris.platform.outboundsync.activator.impl de.hybris.platform.outboundsync.job.impl Note A large number of failures when sending changed items to an external system can cause de.hybris.platform.outboundsync.activator.impl to print an overwhelming number of stack traces. To simplify stack tracing, you can disable log output for that logger. Stack traces are logged only when DEBUG level logging is enabled.

Resetting a Job If an outbound sync job remains in the RUNNING state for unexpectedly long time, reset the job. To do so, change the job status in Backoffice to ABORTED or FINISHED. Save the change and run the job again.

## Supervisor Cron Job

The supervisor cron job supervises outbound sync cron jobs to stop any of them that are stuck in a RUNNING state.

Everytime the supervisor job (outboundSyncSupervisorJob) runs it captures the state of all running outbound sync cron jobs at that moment and compares their states with the states captured on the previous supervisor run. If the supervisor job detects that an outbound sync job has not changed its state (for example, start time, status, number of items processed, etc.) since the previous run, the supervisor denes that job as being stuck and aborts it. Otherwise, it just keeps the fresh state of that job for the next run. By default, the supervisor job runs every 10 minutes and has very light impact on the system. You can adjust the frequency of the supervisor job execution by changing its trigger conguration. Changing the frequency of the job executions affects how long an outbound sync job that is stuck in a RUNNING state remains that way. At the same time, running the supervisor job too often can cause false aborts for the jobs, which are very slow to synchronize the items with an external system. If the outbound sync job is aborted, the status is always ABORTED.

## Managing Item Processing Concurrency

Outbound sync can process items using multiple concurrent threads. You can adjust this value based on your system's processing capabilities.

Context The value of the following property denes outbound sync item concurrency. Change the property in the project.properties le in the outboundsync extension. You cannot change the property at runtime.

| Property                                                                             | Description                                                     | Default Value   |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------|-----------------|
| outboundsync.queue.polling.frequency.milliseconds                                    | Denes the frequency in polling the aggregated and delete        | 5               |
| outboundsync queue channels in milliseconds.                                         |                                                                 |                 |
| outboundsync.queue.channel.capacity                                                  | Denes the capacity of the aggregated and delete queue channels. | 10000           |
| The capacity is for each channel.                                                    |                                                                 |                 |
| outboundsync.queue.channel.max.messages.per.poll                                     | Denes the maximum number of messages to poll from the           | 10              |
| aggregated and delete channels every time.                                           |                                                                 |                 |
| This is custom documentation. For more information, please visit the SAP Help Portal | 176                                                             |                 |

| 7/6/2024 Property                                       | Description                                                      | Default Value   |
|---------------------------------------------------------|------------------------------------------------------------------|-----------------|
| outboundsync.queue.channel.receive.timeout.milliseconds | Denes the time in milliseconds the poller waits for new messages | 15000           |
| while the queue channel is empty.                       |                                                                  |                 |
| outboundsync.taskexecutor.core.pool.size                | Denes the number of core threads in the task executor's thread   | 5               |
| pool.                                                   |                                                                  |                 |
| outboundsync.taskexecutor.max.pool.size                 | Denes the maximum number of threads in the task executor's       | 5               |
| thread pool.                                            |                                                                  |                 |
| outboundsync.taskexecutor.queue.capacity                | Denes the task executor's queue capacity.                        | 10              |

Setting the Outbound Sync Retry Record Retention Period You can change the duration of the retention period for records of outbound sync publication retries.

Context The retention period for outbound sync retry records is 7 days by default, after which the outboundRetryCleanupCronJob runs to clean up all retry records that have exceeded the maximum number of retries, and passed the retention period. The value you set is compared to the modied time of the retry record. For example, using the default retention period of 7 days, the outboundRetryCleanupCronJob deletes any retry record modied 7 days or more prior to the execution of the cronjob, and has reached the maximum retry attempts.

Follow these steps to change the retention period.

Procedure 1. Log into Backoffice.

2. In the Administration perspective, click System Retention Rule outboundRetryCleanupRule . 3. Set the Retention Time in Seconds attribute as desired. 4. Click Save.

Related Information Outbound Sync Attempt Retry Setting the Outbound Sync Retry Maximum Attempts You can set the maximum number of times the outbound sync cron job attempts to publish failed jobs.

Context Any failure to publish an Integration object results in an error. The OutboundSyncJob is congured to retry publication during the next scheduled or manual run after a failed attempt. The default number of retries is 5. Use the following instructions to change the maximum number of retries. If publication continues to fail after the maximum number of attempts, make sure the ConsumedDestination is properly congured.

Procedure 1. Log in to the Administration Console (HAC).

2. Click Platform Conguration . 3. Search for outboundsync.max.retries. 4. In the Value eld for the parameter, enter the number of times the cron job should retry publication after a failure.

 Note If you delete the outboundsync.max.retries property, the maximum number of retries is set to 0 (zero).

Related Information Outbound Sync Attempt Retry Tutorial: Outbound Sync to SCI Integration Flow This tutorial describes to congure outbound sync in a local environment with a destination in SAP Cloud Integration (SCI). Follow the topics in the order shown to congure an outbound sync scenario in a local environment with a destination located in SCI.

Conguring OAuth for Outbound Sync to SCI Set up an OAuth Client for authentication in SAP Cloud Integration (SCI). Conguring the SAP Cloud Integration Flow Congure an integration ow to allow outbound sync to post to the SAP Cloud Integration ow. Conguring the Outbound Sync to SCI Endpoint Test the conguration of the OAuth Client and the integration ow. Conguring SSL for Outbound Sync This is   For more    the SAP Help  177 Import the SAP Cloud Integration (SCI) certicate to the SAP Commerce Cloud truststore. Conguring Outbound Sync to send outbound requests to SCI Run the completed outbound sync to SAP Cloud Integration (SCI) scenario.

Testing a Connection from SAP Commerce Cloud to SCI using an OAuth Token You can test a connection via the Hybris Administration Console (HAC).

## Conguring Oauth For Outbound Sync To Sci

Set up an OAuth Client for authentication in SAP Cloud Integration (SCI).

Context The rst step in establishing a connection with SCI is to set up an OAuth Client and create a secret.

Procedure 1. Navigate to your SAP BTP Cockpit Subaccount and log in.

2. In the menu on the left, click Security OAuth . 3. On the Clients tab, click Register New Client. 4. Complete the required elds. The secret you enter becomes the password for getting the Bearer token. For subscription, select the value that contains imap. This is the service that allows the publication of items in SCI. Save when done.

5. Provide the user you created in the previous step with the required authorization. Click Authorizations Users .

6. In the User eld, enter oauth_client_<name_of_client> and click Show Assignments.

7. Click Assign. Select the appropriate Subaccount. For Application, select your imap. For this example, select <c1203imap>. For Role, select <ESBMessaging.send>. 8. Click Save. The assignment appears in the list. 9. On the Branding tab, copy the Token Endpoint URL at the bottom of the OAuth URLs list. This URL is required to request the OAuth Bearer token later in the tutorial.

## Conguring The Sap Cloud Integration Flow

Congure an integration ow to allow outbound sync to post to the SAP Cloud Integration ow.

Procedure 1. In a web browser, navigate to your SAP Cloud Integration instance.

2. Click Design and select your integration package or create a new package. 3. On the Artifacts tab, Edit.

4. Click Add Integration Flow to create a new Integration Flow artifact. For this tutorial, name it OutboundSync2SCPIExample. Click OK.

5. Select the new integration ow and click Edit. 6. To create an OData adapter from Sender to Start, click Sender and drag the arrow to Start. 7. In the Adapter Type window that appears, select OData. 8. With the OData adapter arrow selected, click the Adapter Specic tab and congure the connector as described.

a. In the EDMX eld, upload your schema. b. From the Operation list, select POST so Outbound sync sends a POST request to the SAP Cloud Integration ow you are creating.

c. In the Entity Set eld, enter the value of the resource type for which to send the post. Choose one of the EntitySet values in the selected EDMX schema. For this tutorial, enter Catalogs.

d. Click Save, then click Deploy.

![177_image_0.png](177_image_0.png)

The OutboundSync2SCPIExample integration ow you created appears. The status changes to Started within a few minutes. If the status does not change after several minutes, click the Reload content icon.

10. If necessary, select the new integration ow to view the Endpoints tab. Use the link in the Endpoints view in the next sections of this tutorial to get the Schema and CSRF token, and to make a POST request for the Outbound Sync scenario.

Conguring the Outbound Sync to SCI Endpoint Test the conguration of the OAuth Client and the integration ow.

This is   For more    the SAP Help  178 Context This tutorial uses Postman to test the endpoint you created in the previous topic.

Procedure 1. Get an OAuth Bearer token using the following steps.

a. Create a POST request using the URL you congured in the OAuth conguration step. Add the parameter <grant_type : client_credentials>. b. On the Authorization tab, select Basic Auth. Enter the name of the client that you congured. For the password, enter the secret you created.

c. Send the request with the following body, which contains the OAuth token.

{ "access_token": "7b60f7416d2e9ea9b79f38a4ce25ee81", "token_type": "Bearer", "expires_in": 31536000, "scope": "" }
2. Get the CSRF token using the following steps.

a. Perform a GET request using the URL you copied from the deployed integration ow conguration in Conguring the SAP Cloud Integration Flow. For this tutorial, the URL is https://c1203-iflmap.hcisb.int.sap.hana.ondemand.com/gw/odata/SAP/OUTBOUNDSYNC2SCPIEXAMPLE;v=1.

 Note To get metadata with the token, add the /$metadata endpoint to the request. For example, https://c1203iflmap.hcisb.int.sap.hana.ondemand.com/gw/odata/SAP/OUTBOUNDSYNC2SCPIEXAMPLE;v=1/$metadata b. In the the Headers tab, add the following token values.

| Key                                                                                                                                                                                                                                                     | Value                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Authorization                                                                                                                                                                                                                                           | Bearer 7b60f7416d2e9ea9b79f38a4ce25ee81 (or the token retrieved in step 1) |
| X-CSRF-Token                                                                                                                                                                                                                                            | Fetch                                                                      |
| 3. Send the request. If you requested metadata, the response body contains the EDMX schema. In The response headers include the x-csrf-token with a value. The value of the example in this tutorial is x-csrf-token →424wzmHOl-M1bNkMRy3lUfE1diCr6BMy. |                                                                            |

4. Make a POST request to the SCI endpoint to create a new Catalog.

a. Use the URL you used to get the CSRF token and add the resource you dened in the integration ow. For example: /Catalogs.https://c1203iflmap.hcisb.int.sap.hana.ondemand.com/gw/odata/SAP/OUTBOUNDSYNC2SCPIEXAMPLE;v=1/Catalogs.

b. In the body, specify the required elds in SCI. The following example species two elds in JSON format.

{ "integrationKey":"ExampleCatalog", "id": "ExampleCatalog" }
c. In Headers, specify the following.

| Key                                                                   | Value                                   |
|-----------------------------------------------------------------------|-----------------------------------------|
| Content-Type                                                          | application/json                        |
| Authorization                                                         | Bearer 7b60f7416d2e9ea9b79f38a4ce25ee81 |
| X-CSRF-Token 424wzmHOl-M1bNkMRy3lUfE1diCr6BMy Accept application/json |                                         |

d. Send the request. A successful request returns a 201 Created response and the response body contains the new entry. For example:
 "d": { "__metadata": { "id": "https://c1203-iflmap.hcisb.int.sap.hana.ondemand.com:443/gw/odata/SAP/OUTBOUNDSYNC2SCPIEXAMPLE;v=1/Catalogs('ExampleCat "uri": "https://c1203-iflmap.hcisb.int.sap.hana.ondemand.com:443/gw/odata/SAP/OUTBOUNDSYNC2SCPIEXAMPLE;v=1/Catalogs('ExampleCa "type": "HybrisCommerceOData.Catalog" }, "id": "ExampleCatalog", "integrationKey": "ExampleCatalog" } }

## Conguring Ssl For Outbound Sync

Import the SAP Cloud Integration (SCI) certicate to the SAP Commerce Cloud truststore.

Context Complete the following instructions to download the certicate. The examples in the steps describe the procedure as performed on a Mac, in a Chrome browser. Adjust the procedure according to your OS and browser use.

Procedure This is   For more    the SAP Help  179 2. In your browser, open the certicate to view its details. Take note of the certicate name so you can import it later.

![179_image_0.png](179_image_0.png)

On a Mac, you can export a certicate from the Keychain application. Under System Roots Certicates , select the certicate and click File Export Items . On a Windows machine, you might nd certicates in Console Root, in a Certificates folder.

This example uses /Baltimore\ Cybertrust\ Root.cer to identify the certicate. If your certicate is named differently, use the name of the certicate you exported.
cp <path_to_your_download_directory>/Baltimore\ CyberTrust\ Root.cer <path_to_your_commerce_suite_directory>hybris/bin/platform/resources/devce 5. Back up the truststore using the following command.

cp ydevelopers.jks ydevelopers.jks_bak 6. Import the certicate into the truststore using the following command.

keytool -import -v -trustcacerts -alias 1 -file scpiCertificate.cer -keystore ydevelopers.jks -keypass 123456 -storepass 123456

## Conguring Outbound Sync To Send Outbound Requests To Sci

Run the completed outbound sync to SAP Cloud Integration (SCI) scenario.

Context Now that the system is congured and tested, load the ImpEx provided in this topic, then run the outbound sync scenario with a ConsumedDestination pointing to an SCI integration ow resource. The following ImpEx provides the OAuth and CSRF token generation congurations. The OAuth conguration includes the client name and secret you created as well as the OAuth token URL.

For the CSRF Token, the ImpEx uses the additionalProperties column in ConsumedDestination. The value of additional properties is a map. For CSRF conguration, provide the key csrfURL, where the value is the URL to fetch the token from. For example: "csrfURL->https://c1203-iflmap.hcisb.int.sap.hana.ondemand.com/gw/odata/SAP/OUTBOUNDSYNC2SCPIEXAMPLE;v=1" Procedure 1. Load the following ImpEx.

\#******************************************\# \#************ OAuth CredentialS **********\# \#******************************************\# INSERT_UPDATE OAuthClientDetails; clientId[unique = true]; oAuthUrl; scope ; pablo-test ; https://oauthasservices-w47eb78ee.int.sap.hana.ondemand.com/oauth2/api/v1/token INSERT_UPDATE ExposedOAuthCredential; id[unique = true]; oAuthClientDetails(clientId); password ; scpi-testOauthCredential ; pablo-test ; 
This is   For more    the SAP Help  180
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# \# This sets up the endpoint called "local-hybris." \# \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# INSERT_UPDATE Endpoint; id[unique = true]; version[unique = true]; name; specUrl ; local-hybris ; unknown ; local-hybris ; "https://c1203-iflmap.hcisb.int.sap.hana.ondemand.com/gw/odata/SAP/OUTBOUNDSYNC2SCPIEXAMPLE;v=1" \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# \# This sets up a ConsumedDestination called "outbound-sync-to-scpi." \# It uses the Endpoint and BasicCredential created above. The user calls
\# the Outbound Service with the destination ID (e.g. "outbound-sync-to-scpi").

\# The Outbound Service looks up the details of the destination by ID, \# so it knows where to send the data \# \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\# INSERT_UPDATE DestinationTarget; id[unique = true] ; stoutoutboundtest INSERT_UPDATE ConsumedDestination; id[unique = true]; url; endpoint(id, version); credential(id); destinationTarget(id)[default = stoutoutboundt ; outbound-sync-to-scpi ; "https://c1203-iflmap.hcisb.int.sap.hana.ondemand.com/gw/odata/SAP/OUTBOUNDSYNC2SCPIEXAMPLE;v=1/Catalogs" ; local-hyb \# Set up a product stream that will detect changes made to the Product type and include it in the outboundSyncDataStreams OutboundSyncStreamConf \# NOTE: The whereClause is an example of how to filter out Product changes that don't have catalogVersion.version as 'Online' INSERT_UPDATE OutboundSyncStreamConfiguration; streamId[unique = true]; container(id); itemTypeForStream(code); outboundChannelConfiguration(cod ; productStream ; outboundSyncDataStreams ; Catalog ; outboundExample ; INSERT_UPDATE OutboundChannelConfiguration; code[unique = true]; integrationObject(code); destination(id) ; outboundExample ; OutboundProduct ; outbound-sync-to-scpi 2. Execute the cronjob for outbound sync. If there are changes to the Catalog type, the Integration API takes care of authentication, fetches the CSRF token, and makes the POST
request with the Catalog in the body. If the job runs and the synchronization completes successfully, then you correctly congured outbound sync to SCI.

Testing a Connection from SAP Commerce Cloud to SCI using an OAuth Token You can test a connection via the Hybris Administration Console (HAC).

Procedure 1. Navigate to HAC Console Scripting Languages .

2. Get the integration ow endpoint URL deployed in your SCI tenant, and the token endpoint URL used to get the OAuth token from SCI. 3. In the following script, update the URL, client ID, and client secret (examples in bold below), then copy-paste it into the console and execute it:
 Sample Code import groovyx.net.http.HTTPBuilder def site = new HTTPBuilder('**https://scpi-tenant-iflmap-gw-url/odata/SAP/REPLICATE-B2C-CUSTOMER-FROM-SAP-COMMERCE-TO-SAP-CRM;v=1**') def tokenurl = new HTTPBuilder('**https://scpi-oauth-token-endpoint-url/oauth2/api/v1/token**') tokenurl.auth.basic '**client_id**', '**client_secret**'
tokenurl.post( body: [grant_type:'client_credentials'] ) { resp, reader -> System.out << "Token response: " << reader println() accessToken = reader['access_token'] } site.get( query: ["limit": 1], headers: ['Authorization': "Bearer ${accessToken}"]) { resp, reader -> System.out << "response: " << reader println() } return "Test finished!"
4. In the output, you should see the access token returned and the response XML content as well.

If the above script fails to execute due to the error below, add the following listed libraries to one of the enabled customized extension's <extension folder>/lib location and restart the server:
http-builder-0.7.1.jar json-lib-2.4-jdk13.jar xml-resolver-1.2.jar Sample Code Script compilation has failed [reason: org.codehaus.groovy.control.MultipleCompilationErrorsException: startup failed: Script1.groovy: 1: **unable to resolve class groovyx.net.http.HTTPBuilder** @ line 1, column 1. import groovyx.net.http.HTTPBuilder 1 error ]
Runtime Attribute Meta API Implementation Examples The following examples show how to make POST (create), GET (read), PATCH (update), and DELETE (remove) requests using the Runtime Attribute Meta API.

 Note The following content applies only to patch version 2011.4 and later.

POST a Runtime Primitive Attribute Send POST request https://localhost:9002/RuntimeAttributeService/AttributeDescriptors with the following body:
 Sample Code
{ "partOf": false, "attributeType": { "code": "java.lang.String" }, "qualifier": "stringRuntimeAttribute", "unique": false, "localized": false, "optional": true, "enclosingType": { "code": "Catalog" }, "generate": false }
Here is the response body that is returned:
 Sample Code
{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('stringRuntimeAttribute%7CCatalog')", "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('stringRuntimeAttribute%7CCatalog')", "type": "HybrisCommerceOData.AttributeDescriptor" }, "unique": false, "localized": false, "partOf": false, "generate": false, "qualifier": "stringRuntimeAttribute", "optional": true, "integrationKey": "stringRuntimeAttribute|Catalog", "attributeType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('stringRuntimeAttribute%7CCatalog')/a }
 },
 "enclosingType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('stringRuntimeAttribute%7CCatalog')/e } } } }
GET a Primitive Runtime Attribute Descriptor Send GET request https://localhost:9002/RuntimeAttributeService/AttributeDescriptors?$filter=qualifier eq 'stringRuntimeAttribute' with the following body: Here is the request body that is returned:
 Sample Code
 "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('stringRuntimeAttribute%7CCatalog "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('stringRuntimeAttribute%7CCatalog "type": "HybrisCommerceOData.AttributeDescriptor" }, "unique": false, "localized": false, "partOf": false, "generate": false, "qualifier": "stringRuntimeAttribute", "optional": true, "integrationKey": "stringRuntimeAttribute|Catalog", "attributeType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('stringRuntimeAttribute%7CCat } },
This is   For more    the SAP Help  182

 "enclosingType": {
 "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('stringRuntimeAttribute%7CCat } } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('stringRuntimeAttribute%7CClassifi "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('stringRuntimeAttribute%7CClassif "type": "HybrisCommerceOData.AttributeDescriptor" }, "unique": false, "localized": false,
 "partOf": false,
 "generate": false, "qualifier": "stringRuntimeAttribute", "optional": true, "integrationKey": "stringRuntimeAttribute|ClassificationSystem", "attributeType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('stringRuntimeAttribute%7CCla } }, "enclosingType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('stringRuntimeAttribute%7CCla } } } ] } }
PATCH a Runtime Primitive Attribute with a Required Attribute (Non-Optional)
Send PATCH request https://localhost:9002/RuntimeAttributeService/AttributeDescriptors('primitiveRuntimeAttribute%7CTitle') with the following body:
 Sample Code
{ "partOf": false, "attributeType": { "code": "java.lang.String" }, "qualifier": "primitiveRuntimeAttribute", "unique": false, "localized": false, "optional": false, "enclosingType": { "code": "Title" }, "generate": false }
Here is the response body that is returned:
 Sample Code
{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('primitiveRuntimeAttribute%7CTitle')", "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('primitiveRuntimeAttribute%7CTitle')", "type": "HybrisCommerceOData.AttributeDescriptor" }, "unique": false, "localized": false, "partOf": false, "generate": false, "qualifier": "primitiveRuntimeAttribute", "optional": false, "integrationKey": "primitiveRuntimeAttribute|Title", "attributeType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('primitiveRuntimeAttribute%7CTitle')/ } }, "enclosingType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('primitiveRuntimeAttribute%7CTitle')/ } } } }
DELETE a Runtime Primitive Attribute Send DELETE request https://localhost:9002/RuntimeAttributeService/AttributeDescriptors('primitiveRuntimeAttribute%7CTitle')
No response body is returned.

POST a Composed Type Runtime Attribute on Product Send POST request https://localhost:9002/RuntimeAttributeService/AttributeDescriptors with the following body:
 Sample Code

{ "partOf": false, "attributeType": { "code": "Country" }, "qualifier": "countryOfOrigin", "unique": false, "localized": false, "optional": true, "enclosingType": { "code": "Product" }, "generate": false
}
Here is the response body that is returned:
 Sample Code
{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('countryOfOrigin%7CProduct')", "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('countryOfOrigin%7CProduct')", "type": "HybrisCommerceOData.AttributeDescriptor" }, "unique": false, "localized": false, "partOf": false, "generate": false, "qualifier": "countryOfOrigin", "optional": true, "integrationKey": "countryOfOrigin|Product", "attributeType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('countryOfOrigin%7CProduct')/attribut } }, "enclosingType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('countryOfOrigin%7CProduct')/enclosin } } } }
GET a Composed Type Attribute Descriptor Send GET request https://localhost:9002/RuntimeAttributeService/AttributeDescriptors Here is the response body that is returned:
 Sample Code
{ "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('countryOfOrigin%7CProduct')",
 "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('countryOfOrigin%7CProduct')",
 "type": "HybrisCommerceOData.AttributeDescriptor" }, "unique": false, "localized": false, "partOf": false, "generate": false, "qualifier": "countryOfOrigin", "optional": true, "integrationKey": "countryOfOrigin|Product", "attributeType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('countryOfOrigin%7CProduct')/ } }, "enclosingType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('countryOfOrigin%7CProduct')/ } } }, { "__metadata": { "id": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('countryOfOrigin%7CVariantProduct "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('countryOfOrigin%7CVariantProduct "type": "HybrisCommerceOData.AttributeDescriptor" }, "unique": false, "localized": false, "partOf": false, "generate": false, "qualifier": "countryOfOrigin", "optional": true, "integrationKey": "countryOfOrigin|VariantProduct", "attributeType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('countryOfOrigin%7CVariantPro } }, "enclosingType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('countryOfOrigin%7CVariantPro } }
This is   For more    the SAP Help  184

 }
 ] } }
POST a Localized String Type Runtime Attribute on Country Note RuntimeAttributeService contains the localized attribute exposed, but this attribute is read-only so contains the correct value when making a GET request for the attribute. This means that the value specied in the payload when POSTing or PATCHing is not the value that is persisted. The persisted value for localized depends on whether or not the localized: prex is present in the attributeType.

Send POST request https://localhost:9002/RuntimeAttributeService/AttributeDescriptors with the following body:
 Sample Code
{ "partOf": false, "attributeType": { "code": "localized:java.lang.String" }, "qualifier": "localizedDescription", "unique": false, "localized": false, "optional": true, "enclosingType": { "code": "Country" }, "generate": false }
Here is the response body that is returned:
 Sample Code
{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('localizedDescription%7CCountry')", "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('localizedDescription%7CCountry')", "type": "HybrisCommerceOData.AttributeDescriptor" }, "unique": false, "localized": true, "partOf": false, "generate": false, "qualifier": "localizedDescription", "optional": true, "integrationKey": "localizedDescription|Country", "attributeType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('localizedDescription%7CCountry')/att } }, "enclosingType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('localizedDescription%7CCountry')/enc }
 }
 } }
GET a Localized Attribute Descriptor Note The attribute type contains the localized prex, but localized is set as false in the payload. As mentioned above, the localized attribute value is ignored in the POST request, and the attribute created is localized due to the prex of attributeType. When making a GET request that returns this attribute, the value of localized is true.

Send GET request https://localhost:9002/RuntimeAttributeService/AttributeDescriptors Here is the response body that is returned:
 Sample Code
{ "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('localizedDescription%7CCountry')" "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('localizedDescription%7CCountry' "type": "HybrisCommerceOData.AttributeDescriptor" }, "unique": false, "localized": true, "partOf": false, "generate": false, "qualifier": "localizedDescription", "optional": true, "integrationKey": "localizedDescription|Country", "attributeType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('localizedDescription%7CCount }
This is   For more    the SAP Help  185

 },

![185_image_0.png](185_image_0.png)

 "enclosingType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('localizedDescription%7CCount } } } ] } }
POST a Unique String Type Runtime Attribute on User Send POST request https://localhost:9002/RuntimeAttributeService/AttributeDescriptors with the following body:
 Sample Code
{ "partOf": false, "attributeType": { "code": "java.lang.String" }, "qualifier": "newUniqueAttribute", "unique": true, "localized": true, "optional": true, "enclosingType": { "code": "User" }, "generate": false }
Here is the response body that is returned:
 Sample Code
{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('newUniqueAttribute%7CUser')", "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('newUniqueAttribute%7CUser')", "type": "HybrisCommerceOData.AttributeDescriptor" }, "unique": true, "localized": false, "partOf": false, "generate": false, "qualifier": "newUniqueAttribute", "optional": true, "integrationKey": "newUniqueAttribute|User", "attributeType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('newUniqueAttribute%7CUser')/attribut } }, "enclosingType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/RuntimeAttributeService/AttributeDescriptors('newUniqueAttribute%7CUser')/enclosin } } } }
Runtime Attribute Implementation Examples The following topics contain example integration scenarios that demonstrate how to use runtime attributes. You can use runtime attributes for all integration scenarios—they are treated like any other attribute during runtime—and they are available for all Types from the Type System for Integration Objects. For more information, see Runtime Attributes. For integration scenarios, the following runtime attribute features are supported:
Primitive Composed Types Localized Primitive Types Unique Collections For information on how to create runtime attributes in Backoffice, see Setting Up Different Types of Attributes in Backoffice. Once a runtime attribute has been created for a Type, it's available to use with Integration Objects via the Backoffice Integration UI Tool. Runtime attributes are available for all integration scenarios. The topics that follow contain some example integration scenarios that demonstrate how to use runtime attributes.

Primitive Type Runtime Attribute This example shows how to POST (create) an Integration Object with a Catalog Type that contains the Primitive Type runtime attribute runtimeCatalogDescription and also PATCH (update) the value of the runtime attribute runtimeCatalogDescription.

Composed Type Runtime Attribute This example shows how to POST (create) an Integration Object with a Catalog Type that contains the Composed Type runtime attribute runtimeCatalogCountry.

Localized Type Runtime Attribute This is   For more    the SAP Help  186 This example shows how to POST (create) an Integration Object with a Catalog Type that includes the localized attribute runtimeLocalizedAttribute.

Outbound Sync with Runtime Attributes This example shows how to POST (create) an Integration Object with a Catalog Type that includes the localized attribute runtimeLocalizedAttribute.

A Missing Required Runtime Attribute (Error)
This examples shows what happens when you POST (create) an Integration Object with a Catalog Type that doesn't contain the required runtime attribute, in this case requiredRuntimeAttribute.

Unique Runtime Attribute This example shows how to POST (create) an Integration Object with a Catalog Type that contains the unique runtime attribute uniqueRuntimeAttribute.

Filter Runtime Attribute and orderBy Runtime Attribute This example shows how to GET (read) metadata for currencies ltered by the runtime attribute filterRuntimeAttribute, then metadata for currencies by the orderBy runtime attribute. Collection Runtime Attribute This example shows how to POST (create) then GET (read) a catalog and then expand it by the collectionRuntimeAttribute.

Script Service Meta API Implementation Examples The following examples show how to make POST (create), GET (read), PATCH (update), and DELETE (remove) requests using the Script Service Meta API.

 Note For more information on the Script Service Meta API, see Script Service Meta API for Virtual Attributes.

The following table shows the exposed attributes for a script:

| Attribute     | Description                                                                                                                                                       |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| code          | The script's unique identier.                                                                                                                                     |
| content       | The code that is executed.                                                                                                                                        |
| scriptType    | Species the language in which the script is written. The Script model supports BEANSHELL, JAVASCRIPT, and GROOVY.                                                 |
| description   | Describes what the script is for.                                                                                                                                 |
| disabled      | Disables a script. The default value is false. If the script throws an exception when being executed, it's marked as disabled = true if autodisabling is enabled. |
| autodisabling | Automatically disables a script that fails to execute. The default value is false.                                                                                |

 Note By default, an ItemModel is provided to the script as a variable.

POST a Script This example creates a script to format a product's online date (formatProductOnlineDate) to a readable format for customers. To create scripts for virtual attributes, send POST request https://localhost:9002/odata2webservices/ScriptService/Scripts with the following body:
 Note The mandatory elds to create scripts are code and content. scriptType defaults to GROOVY if one isn't specied in the payload.

 Sample Code
{ "code": "formatProductOnlineDate", "scriptType": { "code": "GROOVY" }, "description": "This script formats the Product's online date to a human readable format", "autodisabling": false, "disabled": false, "content": "import de.hybris.platform.core.model.product.ProductModel\r\nimport java.text.SimpleDateFormat\r\nProductModel product = (ProductMo }
 Note The content in the body of the request message must be escaped so that the code is posted as a string in the JSON. Use a Java string escape tool to format the code. The original Groovy script is listed below.

 Sample Code Original GROOVY script:
import de.hybris.platform.core.model.product.ProductModel import java.text.SimpleDateFormat ProductModel product = (ProductModel) itemModel new SimpleDateFormat('MMM dd, yyyy HH:mm:ss').format(product.onlineDate)
Here is the response body that is returned:

 Sample Code
{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')", "uri": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')", "type": "HybrisCommerceOData.Script" }, "description": "This script formats the Product's online date to a human readable format",
 "autodisabling": false,
 "disabled": false, "code": "formatProductOnlineDate", "content": "import de.hybris.platform.core.model.product.ProductModel\r\nimport java.text.SimpleDateFormat\r\nProductModel product = (Produ "integrationKey": "formatProductOnlineDate", "scriptType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')/scriptType" } }, "localizedAttributes": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')/localizedAttributes" } } } }
GET a Script Use a GET request to retrieve script metadata, persisted scripts, or a single script.

Retrieve Metadata Send GET request https://localhost:9002/odata2webservices/ScriptService/Scripts/$metadata Retrieve Persisted Scripts This example retrieves persisted scripts.

Send GET request https://localhost:9002/odata2webservices/ScriptService/Scripts A list of scripts is returned:
 Sample Code
{ "d": { "results": [
 {
 "__metadata": { "id": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')", "uri": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')", "type": "HybrisCommerceOData.Script" }, "description": "This script formats the Product's online date to a human readable format", "autodisabling": false, "disabled": false, "code": "formatProductOnlineDate", "content": "import de.hybris.platform.core.model.product.ProductModel\r\nimport java.text.SimpleDateFormat\r\nProductModel product "integrationKey": "formatProductOnlineDate", "scriptType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')/scriptType" } }, "localizedAttributes": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')/localizedAttributes" } } }
 Note Only active scripts for the specied code are returned. In the above sample code, only active scripts for formatProductOnlineDate are returned.

Retrieve a Single Script Send a GET request for a single script by providing the integration key "code" in the URL.

This example retrieves the script for formatProductOnlineDate. Send GET request https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')

## Sample Code

{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')",
 "uri": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')",
 "type": "HybrisCommerceOData.Script" }, "description": "This script formats the Product's online date to a human readable format", "autodisabling": false, "disabled": false, "code": "formatProductOnlineDate", "content": "import de.hybris.platform.core.model.product.ProductModel\r\nimport java.text.SimpleDateFormat\r\nProductModel product = (Produ "integrationKey": "formatProductOnlineDate", "scriptType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')/scriptType" } }, "localizedAttributes": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')/localizedAttributes" } } } }
PATCH a Script To update a script, provide the eld that needs to be updated in the payload for the specied script.

This example updates the code description for formatProductOnlineDate. Send PATCH request https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')
Here is the response body that is returned:
 Sample Code
{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')", "uri": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')",
 "type": "HybrisCommerceOData.Script"
 }, "description": "Returns an online date that is formatted like this Jan 01, 2020 12:42:22", "autodisabling": false, "disabled": false, "code": "formatProductOnlineDate", "content": "import de.hybris.platform.core.model.product.ProductModel\r\nimport java.text.SimpleDateFormat\r\nProductModel product = (Produ "integrationKey": "formatProductOnlineDate", "scriptType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')/scriptType" } }, "localizedAttributes": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')/localizedAttributes" } } } }
DELETE a Script Delete a script that is no longer needed or invalid.

This example deletes the script for formatProductOnlineDate. Send DELETE request https://localhost:9002/odata2webservices/ScriptService/Scripts('formatProductOnlineDate')
No response body is returned.

 Note Only active scripts for the specied code are deleted. Previous revisions are still present in SAP Commerce Cloud but marked as inactive. You must delete the inactive scripts in either the Backoffice Administration Cockpit or the SAP Commerce Cloud Administration Cockpit before creating a script with the same script code.

## Virtual Attribute Implementation Examples

This topic provides script examples to show how virtual attributes can atten, format, and enhance payloads.

The following ImpEx is for a CustomerReview Integration Object that contains the virtual attributes productRating, productName, and createdOnDate:
 Sample Code INSERT_UPDATE IntegrationObject; code[unique = true]; integrationType(code) ; CustomerReview; INBOUND INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code); root[default = false]; itemTypeMatch ; CustomerReview ; CustomerReview ; CustomerReview ; true ; ALL_SUB_AND_SUPER_TYPES ; INSERT_UPDATE IntegrationObjectItemAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = true]; at ; CustomerReview:CustomerReview ; creationtime ; CustomerReview:creationtime ; ; ; ; CustomerReview:CustomerReview ; processed ; CustomerReview:processed ; ; ; ; CustomerReview:CustomerReview ; headline ; CustomerReview:headline ; ; ; ; CustomerReview:CustomerReview ; description ; CustomerReview:comment ; ; ; ; CustomerReview:CustomerReview ; rating ; CustomerReview:rating ; ; ; ; CustomerReview:CustomerReview ; code ; CustomerReview:code ; ; true ; INSERT_UPDATE IntegrationObjectItemVirtualAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = tr ; CustomerReview:CustomerReview ; productRating ; formatProductRating ; CustomerReview:CustomerReview ; productName ; productName ; CustomerReview:CustomerReview ; createdOnDate ; createdOn INSERT_UPDATE IntegrationObjectVirtualAttributeDescriptor; code[unique = true]; logicLocation; type(code) ; formatProductRating ; model://formatStars ; java.lang.String ; productName ; model://formatProductName ; java.lang.String ; createdOn ; model://formatDate ; java.lang.String Each of the following script examples backs a specic virtual attribute referenced in the above ImpEx.

Payload Flattening This example shows a script called formatProductName that backs the virtual attribute productName that attens a payload.

 Sample Code import de.hybris.platform.customerreview.model.CustomerReviewModel; import de.hybris.platform.core.model.product.ProductModel; CustomerReviewModel review = (CustomerReviewModel)itemModel; ProductModel product = review.product; product.name Payload Formatting This example shows a script called formatStars that backs the virtual attribute ProductRating that formats a product review rating to stars.

 Sample Code import de.hybris.platform.customerreview.model.CustomerReviewModel; CustomerReviewModel review = (CustomerReviewModel)itemModel; Math.round(review.rating) + ' Stars' Payload Enhancement This example shows a script called formatDate that backs the virtual attribute createdOnDate that formats a date so that it's in human-readable format.

 Sample Code import java.text.SimpleDateFormat new SimpleDateFormat('MMM dd, yyyy HH:mm:ss').format(itemModel.creationtime)
Webhook Service Meta API Implementation Examples The following examples show how to make POST (create), GET (read), PATCH (update), and DELETE requests using the Webhook Service Meta API. The webhook examples in this topic are based on an Integration Object called EmployeeIO. To create the Integration Object, send POST request https://localhost:9002/odata2webservices/IntegrationService/InboundChannelConfigurations with the following body:
 Sample Code
{ "integrationObject": { "code": "EmployeeIO",

 "items": [

![190_image_1.png](190_image_1.png)

 { "root": false, "code": "UserGroup", "type": { "code": "UserGroup" }, "attributes": [ { ![190_image_0.png](190_image_0.png) "code": "UserGroup"
 }
 }, "unique": true } ] }, { "root": true, "code": "Employee", "type": { "code": "Employee" }, "attributes": [ { "attributeName": "name", "attributeDescriptor": { "qualifier": "name", "enclosingType": { "code": "Employee" } } }, { "attributeName": "uid", "attributeDescriptor": { "qualifier": "uid", "enclosingType": { "code": "Employee" } }, "unique": true }, { "attributeName": "password", "attributeDescriptor": { "qualifier": "password", "enclosingType": { "code": "Employee" } } }, { "attributeName": "groups", "attributeDescriptor": { "qualifier": "groups", "enclosingType": { "code": "Employee" } }, "returnIntegrationObjectItem": { "code": "UserGroup" } } ] }
 ]
 }, "authenticationType": { "code": "BASIC" } }
Here is the response body that is returned:

![190_image_2.png](190_image_2.png)

 Sample Code
 "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/IntegrationService/InboundChannelConfigurations('EmployeeIO')", "uri": "https://localhost:9002/odata2webservices/IntegrationService/InboundChannelConfigurations('EmployeeIO')", "type": "HybrisCommerceOData.InboundChannelConfiguration" }, "integrationKey": "EmployeeIO", "authenticationType": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/IntegrationService/InboundChannelConfigurations('EmployeeIO')/authenticationType" } }, "integrationObject": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/IntegrationService/InboundChannelConfigurations('EmployeeIO')/integrationObject" } } } }

POST a Webhook Send POST request https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations with the following body:
 Sample Code
{ "eventType": "de.hybris.platform.webhookservices.event.ItemSavedEvent", "integrationObject": { "code": "EmployeeIO" }, "destination": {
 "id": "ExistingWebhookDestination",
 "destinationTarget": { "id": "webhookServices" } } }
Here is the response body that is returned:
 Sample Code
{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices%7CEm "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices%7CE "type": "HybrisCommerceOData.WebhookConfiguration" }, "filterLocation": null, "eventType": "de.hybris.platform.webhookservices.event.ItemSavedEvent", "integrationKey": "ExistingWebhookDestination|webhookServices|EmployeeIO|de.hybris.platform.webhookservices.event.ItemSavedEvent", "integrationObject": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices } }, "destination": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices } } } }
POST a Webhook with Nested Destination Elements Send POST request https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations with the following body:
 Sample Code
 "eventType": "de.hybris.platform.webhookservices.event.ItemSavedEvent", "integrationObject": { "code": "EmployeeIO" }, "destination": { "id": "NewDestination", "url": "https://postman-echo.com/post", "destinationTarget": { "id": "NewTarget", "destinationChannel": { "code": "WEBHOOKSERVICES" }, "eventConfigurations": [ { "eventClass": "de.hybris.platform.webhookservices.event.ItemSavedEvent", "exportName": "does not matter but must be present" } ] }, "endpoint": { "id": "NewEndpoint", "version": "test", "name": "Postman echo", "specUrl": "https://postman-echo.com" }, "credentialBasic": { "id": "NewCredential", "username": "postman", "password": "test" } }, "filterLocation": "model://someScript" }
Here is the response body that is returned:
 Sample Code

{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('NewDestination%7CNewTarget%7CEmployeeIO%7Cde.hybr "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('NewDestination%7CNewTarget%7CEmployeeIO%7Cde.hyb "type": "HybrisCommerceOData.WebhookConfiguration" }, "filterLocation": "model://someScript", "eventType": "de.hybris.platform.webhookservices.event.ItemSavedEvent", "integrationKey": "NewDestination|NewTarget|EmployeeIO|de.hybris.platform.webhookservices.event.ItemSavedEvent", "integrationObject": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('NewDestination%7CNewTarget%7CEmployeeIO%7Cde } }, "destination": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('NewDestination%7CNewTarget%7CEmployeeIO%7Cde } } } }
GET a Webhook by Key Send PATCH request https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations ('<integrationKey>').

For example, https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices%7CEmployeeIO%7Cde Here is the response body that is returned:
 Sample Code
{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices%7CEm "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices%7CE "type": "HybrisCommerceOData.WebhookConfiguration" }, "filterLocation": null, "eventType": "de.hybris.platform.webhookservices.event.ItemSavedEvent", "integrationKey": "ExistingWebhookDestination|webhookServices|EmployeeIO|de.hybris.platform.webhookservices.event.ItemSavedEvent", "integrationObject": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices } },
 "destination": {
 "__deferred": { "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices } } } }
GET All Webhooks Send GET request: https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations Here is the response body that is returned:
 Sample Code
{ "d": { "results": [ { "__metadata": { "id": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('NewDestination%7CNewTarget%7CEmployeeIO%7 "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('NewDestination%7CNewTarget%7CEmployeeIO% "type": "HybrisCommerceOData.WebhookConfiguration" }, "filterLocation": "model://someScript", "eventType": "de.hybris.platform.webhookservices.event.ItemSavedEvent", "integrationKey": "NewDestination|NewTarget|EmployeeIO|de.hybris.platform.webhookservices.event.ItemSavedEvent", "integrationObject": { "__deferred": {
This is   For more    the SAP Help  193
 "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('NewDestination%7CNewTarget%7CEmploye
 } }, "destination": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('NewDestination%7CNewTarget%7CEmploye } } } ]
 }
}
PATCH a Webhook Send PATCH request: https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations ('<integrationKey>').

For example, https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices%7CEmployeeIO%7Cde with the following body:
 Sample Code
{ "filterLocation": "model://someScript" }
Here is the response body that is returned:
 Sample Code
{ "d": { "__metadata": { "id": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices%7CEm "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices%7CE "type": "HybrisCommerceOData.WebhookConfiguration" }, "filterLocation": "model://someScript", "eventType": "de.hybris.platform.webhookservices.event.ItemSavedEvent", "integrationKey": "ExistingWebhookDestination|webhookServices|EmployeeIO|de.hybris.platform.webhookservices.event.ItemSavedEvent", "integrationObject": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices } }, "destination": { "__deferred": { "uri": "https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices
 }
 } } }
DELETE a Webhook Send DELETE request: https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations ('<integrationKey>').

For example, https://localhost:9002/odata2webservices/WebhookService/WebhookConfigurations('ExistingWebhookDestination%7CwebhookServices%7CEmployeeIO%7Cde No response body is returned.

## Modifying Outbound Requests

Enrich your outbound Integration API requests by modifying request headers and payloads. Systems sometimes require specic header properties or parameters in incoming requests. If you send outbound requests using the Integration API, you might need to modify the requests, depending on the needs of the target system. To enrich an outbound request, register a new decorator using one of these methods:
Modify the current decorator list. All clients share the new decorator.

Dene a custom list and assign it to a custom OutboundServiceFacade object. This method allows clients to have unique congurations.

The following examples describe how to modify an existing decorator list or dene a new list, depending on your needs.

Modifying an Existing Decorator List You can modify an existing decorator list via bean wiring. Use the following code as an example.

<beans ...>
<bean id="myCustomDecorator" class="com.company.MyOutboundRequestDecorator" /> <bean id="outboundRequestDecoratorList" parent="outboundRequestDecoratorList" class="org.springframework.beans.factory.config.ListFactoryBean
<property name="sourceList">
<list merge="true">
<ref bean="myCustomDecorator" />
</list>
</property>
</bean>
</beans>
Dening a Custom List Custom lists allow clients to have unique congurations without affecting other clients. To dene a decorator for use by specied clients, dene a new OutboundRequestFacade using the following code as an example.

<beans ...>
<bean id="myCustomDecorator" class="com.company.MyOutboundRequestDecorator" /> <bean id="myOutboundServiceFacade" parent="outboundServiceFacade">
<property name="outboundRequestDecorators">
<bean parent="outboundRequestDecoratorList" class="org.springframework.beans.factory.config.ListFactoryBean">
<property name="sourceList">
<list merge="true">
<ref bean="myCustomDecorator" />
</list>
</property>
</bean>
</property>
</bean> <bean id="myService" class="com.company.service.MyServiceImpl">
<property name="outboundServiceFacade" ref="myOutboundServiceFacade" /> <!-- here we make sure we use OUR outboundServiceFacade -->
</bean>
</beans>
SAP Passport ID
When requests are sent out of SAP Commerce, they are decorated with an SAP Passport ID. The header is added to the outbound request with the name SAP-PASSPORT. The value contains a Hex-encoded string of the <DSRPassport>. You can congure the creation of the Passport with the following properties.

| Key                                                                                                                                                                                                                                                                                                                                                    | Default Value   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| integrationservices.sap.passport.systemid SAP Commerce integrationservices.sap.passport.service 39 integrationservices.sap.passport.user This value defaults to the current user's UID. You can overwrite this value, but if you override the value in the Administration Console (HAC), the new value is not guaranteed to match an existing user ID. |                 |

## Conguring Resttemplate Caching For Outbound Services

To improve performance in sending outbound, outboundservices caches the RestTemplate to enable reuse of the RestTemplate per ConsumedDestination. This reduces the number of expensive operations that occur each time the service connects to the destination. You can congure the cache with the following properties at Platform start-up time.

| Property                                                                                                                    | Description                                                                  | Default Value   |
|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------|
| outboundservices.cache.resttemplate.maxEntries                                                                              | Congure the maximum number of RestTemplate the cache stores.                 | 1000            |
| outboundservices.cache.resttemplate.eviction.policy                                                                         | Congure the eviction policy, or how to handle a full cache. The options are: | LFU             |
| <LFU> - The service evicts the Least Frequently Used item rst. <LRU> - The service evicts the Least Recently Used item rst. |                                                                              |                 |
| outboundservices.cache.resttemplate.exclusiveComputation                                                                    | Congure whether to synchronize the cache when getting and                    | false           |
| loading items.                                                                                                              |                                                                              |                 |
| This is custom documentation. For more information, please visit the SAP Help Portal                                        | 195                                                                          |                 |

Property Description Default Value outboundservices.cache.resttemplate.statsEnabled Congure whether to collect statistics. true outboundservices.cache.resttemplate.ttlSeconds Congure the duration to keep an item in the cache before purging

it.

7200 seconds (2 hours)

Caching with OAuth Authentication If connecting to the destination requires OAuth authentication, the cached RestTemplate retrieves the access token only once until the token expires or the RestTemplate is evicted from the cache. While the RestTemplate is cached, it uses the same <clientId> and <secret> as when it was created, to retrieve the access token. If the <clientId> and <secret> are updated after caching the RestTemplate, the new credentials are not applied until the current RestTemplate is evicted from the cache and a new RestTemplate created for the destination.

Caching with Basic Authentication If connecting to the destination requires basic authentication, the cached RestTemplate is reused until it is evicted from the cache. While the RestTemplate is cached, it uses the same user name and password to authenticate as when it was created. If the user name and password are updated after caching the RestTemplate, the new credentials are not applied until the current RestTemplate is evicted from the cache and a new RestTemplate created for the destination.

## Conguring Csrf Token Caching For Outbound Services

To improve outbound request performance, outbound services caches the CSRF token per ConsumedDestination. This reduces the number of expensive operations that occur each time the service connects to the destination. Congure the cache with the following properties at SAP Commerce Cloud Platform start-up time.

Monitoring and Clearing the Cache Monitor and cache Hits, Misses, Invalidations, Evictions, Fetches, and InstanceCount, or clear the cache.

| Property                                                                                                                    | Description                                                                  | Default Value   |
|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------|
| outboundservices.cache.csrf.maxEntries                                                                                      | Congure the maximum number of CSRF tokens the cache stores.                  | 1000            |
| outboundservices.cache.csrf.eviction.policy                                                                                 | Congure the eviction policy, or how to handle a full cache. The options are: | LFU             |
| <LFU> - The service evicts the Least Frequently Used item rst. <LRU> - The service evicts the Least Recently Used item rst. |                                                                              |                 |
| outboundservices.cache.csrf.exclusiveComputation                                                                            | Congure whether to synchronize the cache when getting and                    | false           |
| loading items.                                                                                                              |                                                                              |                 |
| outboundservices.cache.csrf.statsEnabled                                                                                    | Congure whether to collect statistics.                                       | true            |
| outboundservices.cache.csrf.ttlSeconds                                                                                      | Congure the duration to keep an item in the cache before purging             | 60 seconds      |
| it.                                                                                                                         |                                                                              |                 |

Monitoring the Cache Procedure 1. Log in to the Administration Console (HAC).

2. Click Monitoring Cache . 3. For RestTemplate caching, click outboundServicesRestTemplateCacheRegion to expand the cache view. For CSRF Token caching, click outboundServicesCsrfTokenCacheRegion.

Clearing the Cache Procedure 1. Log in to the Administration Console (HAC).

2. Click Monitoring Cache . 3. Click Clear Cache.

Tutorial: Using the Outbound Service Set up and congure the Outbound Services extensions and a test endpoint to send an outbound Integration Object back to an inbound channel.

Prerequisites Install the most recent version of SAP Commerce Cloud.

Context There are options for sending data outbound using the Integration API. To replicate data externally based on a precongured schedule, use Outbound Sync, or, if you prefer an event-based approach, use webhooks. However, to send data to an outbound destination based on an SAP Commerce Cloud process or custom logic, use the Outbound Service. The Outbound Service use case requires you to write custom code to integrate with an existing SAP Commerce Cloud process. The following process provides an example for setting up the communication between the Outbound Service and the OData2 endpoint and verifying that the operation was successful in Backoffice. Step 6 is an example of one way to send Integration Object Items outbound using the Outbound Service.

Procedure 1. Congure the localextensions.xml le to make the Outbound Service available to SAP Commerce Cloud.

a. To set up the environment, run the setantenv command from {commerce_installed_dir}/bin/platform. b. To prepare SAP Commerce Cloud, run the ant clean command.

c. Congure the integrationbackoffice extension to manage the Integration Object denition in Backoffice.

A localextensions.xml le is created in {commerce_installed_dir}/hybris/config.

<?xml version="1.0" encoding="UTF-8"?> <hybrisconfig xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="resources/schemas/extensions.xsd"> <extensions> <!-- All extensions located in ${HYBRIS_BIN_DIR}/platform/ext are automatically loaded. More information about how to configure available extensions can be found here : https://wiki.hybris.com/x/nZVzC --> <path dir="${HYBRIS_BIN_DIR}" /> <extension name='integrationbackoffice' /> </extensions> </hybrisconfig>
d. To initialize the platform, run ant initialize from {commerce_installed_dir}/bin/platform. e. To start SAP Commerce Cloud, run hybrisserver from {commerce_installed_dir}/bin/platform.

2. Create an Integration Object with the Category Integration Object Item as the root by sending POST request https://localhost:
<sourceSystemPort>/odata2webservices/IntegrationService/InboundChannelConfigurations with the following body:
{ "integrationObject": { "code": "InboundCategory", "items": [ { "code": "Category", "root": true, "type": { "code": "Category" }, "attributes": [ { "attributeName": "code", "attributeDescriptor": { "enclosingType": { "code": "Category" }, "qualifier": "code" }, "unique": true } ]
 }
 ] }, "authenticationType": { "code": "BASIC" } } 
3. Create an instance of a category in the source system to send out later. POST to the Integration Object that was just created for the Category Integration Object Item with an authorized users by ending POST request https://localhost:<sourceSystemPort>/odata2webservices/InboundCategory/Categories with the following payload:
{ "code": "cat1"} 
4. Dene an Integration Object that has the same root as the Integration Object dened on the source system in the destination system. For example, by sending POST request https://localhost:<destinationSystemUrlPort>/odata2webservices/IntegrationService/InboundChannelConfigurations with the following body:
{ "integrationObject": { "code": "OutboundCategory", "items": [ { "code": "Category", "root": true, "type": { "code": "Category" }, "attributes": [ { "attributeName": "code", "attributeDescriptor": { "enclosingType": { "code": "Category" }, "qualifier": "code" }, "unique": true } ] } ] },

 "authenticationType": {
 "code": "BASIC" } } 
5. Dene the Consumed Destination details on the source system by importing the following ImpEx:
 Sample Code INSERT_UPDATE BasicCredential; id[unique = true] ; username; password ; basicCredential_1 ; newUser ; newUser INSERT_UPDATE Endpoint; id[unique = true]; version[unique = true]; name ; specUrl
 ; endpoint_1 ; unknown ; requiredEndpointName ; https://targetSystem/urlThatDoesNotMatter INSERT_UPDATE DestinationTarget; id[unique = true] ; destinationTarget_1 INSERT_UPDATE ConsumedDestination; id[unique = true] ; url ; endpoint(id, vers ; consumedDestination_1 ; https://localhost/<destinationSystemUrl>/OutboundCategory/Categories ; endpoint_1:
 Note The basicCredential includes credentials that are used to authenticate and authorize the request with the destination system (endpoint) and the Consumed Destination URL
specied in the link that the outbound request is sent to.

6. To create an OutboundProduct named "Original Name", use a REST client to POST the following payload to https://localhost:9002/odata2webservices/OutboundProduct/Products:
Include the following header values in the POST request:
Basic Authentication Content-Type: application/json Accept: application/json
{ "@odata.context": "$metadata\#Product/$entity", "code": "test_article", "name": "Original Name", "catalogVersion": { "catalog": { "id": "Default" }, "version": "Staged" } }
7. Dene an InboundChannelConguration to expose the OutboundProduct Integration Object with Basic Authentication. For example:
INSERT_UPDATE InboundChannelConfiguration; integrationObject(code)[unique = true] ; OutboundProduct Note For SAP Commerce Cloud version 2011 and higher, to expose an Integration Object as an API it must be associated with an InboundChannelConguration. for more information, see Exposing an Integration Object using the Meta API.

8. One way to send Integration Object Items outbound is to trigger the Outbound Services OutboundServiceFacade. To do so, you can execute the following script from Console Scripting Languages in the Administration Console.

import de.hybris.platform.outboundservices.facade.impl.DefaultOutboundServiceFacade import de.hybris.platform.core.model.user.CustomerModel import de.hybris.platform.core.Registry import org.slf4j.Logger import org.springframework.http.ResponseEntity import de.hybris.platform.integrationservices.util.Log import rx.Observable import java.lang.reflect.Field import java.time.LocalDateTime def LOG = Log.getLogger(DefaultOutboundServiceFacade.class) def ctx = Registry.getApplicationContext() def outboundServiceFacade = ctx.getBean("outboundServiceFacade") def category = modelService.get(new de.hybris.platform.core.PK(8796093055118)) //send 1 outbound request outboundServiceFacade.send(category, "InboundCategory", "consumedDestination_1").subscribe( // onNext { responseEntityMap -> LOG.info("Successful response with status code: {}", responseEntityMap.getStatusCode()) } , // onError { error -> LOG.info("Encountered an ERROR with the following message: {}", error.getMessage()) } )
 Note Replace PK equal to 8796093055118 with the PK of the instance of a Category from the source system.

9. After running the script, log into Backoffice and verify that the product name changed to the name specied in the test.

Related Information Integration Object Outbound Services This is   For more    the SAP Help  198 Conguring Integration API Cron Jobs Cron jobs associated with the Integration API include several monitoring data clean up cron jobs and the outbound sync cron job.

Context You can congure and run these cron jobs in Backoffice. All of the cron jobs are accessible in the Administration perspective, under System Background Processes CronJobs . The outbound sync cron job is also accessible in the Integration UI Tool, under Outbound Sync CronJobs .

Procedure 1. In a browser, navigate to Backoffice.

2. In Backoffice, click System Background Processes CronJobs . 3. Select a cron job name. 4. Click Time Schedule Create new Trigger . 5. In the Create New Trigger window, set the values for Active, Next Activation Time, and Cron expression as necessary.

Intelligent Selling Services Foundation Integration The Intelligent Selling Services Foundation integration facilitates the connection between an SAP Commerce Cloud instance and Intelligent Selling Services Foundation.

![198_image_0.png](198_image_0.png)

Merchandising Module Merchandising is a part of Intelligent Selling Services for SAP Commerce Cloud. It provides a range of features related to displaying Merchandising data on your web site.

![198_image_1.png](198_image_1.png)

Congurator for Complex Products Module The Congurator for Complex Products module (configurator-complex-products) provides the user interface that is required to sell congurable products in the online store. It is a fundamental component of the Product Conguration with SAP Variant Conguration and Pricing, and SAP Product Conguration (On-Premise Edition) integrations.

Extensions SAP Variant Conguration and Pricing SAP Product Conguration (On-Premise Edition)
This is   For more    the SAP Help  199

The Congurator for Complex Products extensions provide fundamental components for product conguration

![199_image_0.png](199_image_0.png)

congurator-complex-products Architecture The Product Conguration with SAP Variant Conguration and Pricing integration is available in the optional integration

![199_image_1.png](199_image_1.png)

SAP Commerce Cloud, integration extension pack The SAP Product Conguration (On-Premise Edition)
integration is available in the optional integration

![199_image_2.png](199_image_2.png)

SAP Commerce Cloud, integration extension pack

## Sap Btp Extensions Integration Module

SAP BTP, Kyma runtime is the customization layer for SAP Commerce Cloud. Kyma runtime allows you to use microservices to customize the standard functions of SAP Commerce Cloud without compromising on upgradability.

 Note This module can only be used with SAP Commerce Cloud in the Public Cloud. To use the extension features provided by SAP BTP, Kyma runtime, you have to use SAP Business Technology Platform. For more information, see Kyma Environment.

The SAP BTP Extensions Integration module depends on the API Registry module. For more information, see API Registry Module.

![199_image_3.png](199_image_3.png)

## Sap Data Hub Adapter Module

SAP Commerce Cloud Data Hub is a powerful data integration and staging platform. It facilitates the loading of large amounts of data from one or more sources. Then it processes the data and prepares it for delivery to any number of target systems. For information on Data Hub, see Data Hub.

![199_image_4.png](199_image_4.png)

SAP Data Hub Adapter Features The SAP Data Hub Adapter provides functionality that connects SAP Commerce Cloud to Data Hub. SAP Data Hub Adapter Architecture The SAP Data Hub Adapter module is a set of extensions that connect SAP Commerce Cloud to Data Hub. SAP Data Hub Adapter Implementation This is   For more    the SAP Help  200 Make the necessary configurations in the SAP Data Hub Adapter to connect SAP Commerce Cloud to Data Hub.