# Personalization

Personalization provides an integrated, user-friendly way of building experiences that are relevant to your customers, which is key to driving engagement and conversion. Personalization capabilities work across both content and commerce in an integrated way, so that you can build customer experiences consistently across channels. The modules allow you to create customizations targeted at specic users, add personalized promotions and extend the functionality to integrate personalization with other systems.

Personalization Module The Personalization module provides an integrated, user-friendly way of building experiences that are relevant to your customers, which is key to driving engagement and conversion.

Personalization Integration Module The Personalization Integration module allows you to extend personalization functionality to integrate it with external systems.

Personalization Promotions Module The personalization promotions module allows you to customize promotions for specic user groups.

Personalization Search Module The functionality provided by the Personalization Search module along with the use of SmartEdit features gives the users personalized search experience through the search proles used in the personalization mode.

## Personalization Module

The Personalization module provides an integrated, user-friendly way of building experiences that are relevant to your customers, which is key to driving engagement and conversion.

![3_image_0.png](3_image_0.png)

## Personalization Module Features

Personalization capabilities work across both content and commerce in an integrated way, so that you can build customer experiences consistently across channels and functionality. Using SmartEdit for Customer Experience, you can see the end-customer experience as you build it, all the while working in one set of tooling.

Personalization FAQ
Our personalization FAQ will help you become more familiar with its main concepts and options. Personalization Module Concepts Get started by getting to know the main concepts and terms of the Personalization module.

Personalization Mode in SmartEdit Personalization mode is a view in SmartEdit that allows you to build and congure experiences for your customers.

Multi-Country Site Support for Personalization Multi-Country Site Support provides native support for managing and sharing content among multiple sites. Click Tracking In order to further improve the functionality of SAP Commerce Cloud to better support your business needs, click tracking is enabled in Personalization to collect the number of clicks for Personlization management.

Personalization FAQ
Our personalization FAQ will help you become more familiar with its main concepts and options.

General What is Personalization?

Personalization (based on SmartEdit) provides an integrated, user-friendly way of building experiences that are relevant to your customers, which is key to driving engagement and conversion. Personalization encompasses modules and extensions that facilitate using Personalization Mode in SmartEdit to create a fully customized user experience.

What is SmartEdit?

SAP Commerce Cloud SmartEdit allows content managers to easily create and manage their website content on-the-y in different inection points and make it available to their customers with the click of a button.

What is Personalization Mode?

Personalization Mode is a view in SmartEdit that allows you to build and congure experiences for your customers. Learn more about personalization mode features: Personalization Mode in SmartEdit.

What is a Customization?

A customization describes a set or several sets of changes. It's a way to group multiple target groups that should be mutually exclusive. Only one target group per customization can be valid at a time.

What is a Target Group?

Target groups are activated by triggers, which are dened by the segments a user should belong to.

Is a Target Group and Variation the same thing?

Yes. They both mean the same - target group is used as a label for business purposes (for example in the UI and our user guides), whereas variation is used for the technical aspects (for example in the data model).

What is a Segment?

A segment is a homogenous customer group or a cohort selected for a specic business purpose, so a group of users sharing some common characteristics such as age, gender, habits.

What is a Commerce Customization?

The term commerce customization refers to non-cms actions that are performed when a specic target group/variation is active. An example here can be a promotion available for the customer who is in a particular segment. For technical details see Commerce Customizations. You can also see an example of using commerce customizations in Activating a Personalized Promotion for a Target Group.

How to install Personalization?

You can install personalization using recipes or manually. Both ways are described in Install Personalization.

Working with Personalization in SmartEdit Where can I nd information about working with personalization mode?

You can nd all the necessary information here: Personalization Mode in SmartEdit I cannot see the personalization mode in SmartEdit Before you can see the personalization mode in SmartEdit, you must congure oAuthClient for personalization rst. For more information, see Conguring oAuthClient for Personalization. If you do not belong to the cxmanagergroup or the cxreadonly group, meaning you don't have the required permissions, you won't see the personalization mode. Make sure you have specic permissions rst. Since there are more modes available in SmartEdit, enable personalization using instructions in: Enable Personalization Mode.

I want to create a new customization featuring several target groups. Where can I nd instructions for that?

You can easily create your own customization by following the instructions in Add Customizations.

I have already congured my customizations and target groups, and I want to preview them. How can I do that?

You can preview your congurations at any time, to see how they be displayed to the customer. For details see View Customizations I want to preview more than one target group at at time. Can I do that?

Yes, you can congure the Combined View to do so: Combined View.

I would like my customers to receive a promotion if they belong to a VIP segment. How can I do that?

You can use our personalized promotions feature. Learn how to create and congure a personalized promotion: Create Personalized Promotions.

Where can I view and manage all my customizations and target groups?

You can use the Customization Library to list and modify all your existing congurations: Customization Library.

This is   For more    the SAP Help  5 Is there an alternative to working with SmartEdit?

Yes, you can also use the Backoffice Administration Cockpit as a supplementary tool. For reference check Congure Personalization.

Learning More I want to go through an end-to-end implementation of personalization. Where can I nd more information?

You can use our Personalization Trail to learn how to implement your own trigger and create a custom-made variation: Personalization Core Trail.

Personalization Module Concepts Get started by getting to know the main concepts and terms of the Personalization module.

Segments Segments group the users who share common characteristics such as age, habits, or any other traits.

Variations A variation represents a set of changes made across different channels to deliver a unique experience to a customer. Variations could include cms content, search results, promotions, and many others. Customizations Customizations group multiple variations together.

Actions and Action Results A variation is linked to actions of a CxAbstractAction type. Each action represents a changed element of the customization that makes the storefront more personalized.

Triggers Triggers are the data model objects used to activate variations for a specic user.

## Segments

Segments group the users who share common characteristics such as age, habits, or any other traits.

They are one of the foundations of the personalization module and the entry point to identify a specic user. A single user can belong to multiple segments and segments can hold multiple users. Within the segments conguration, you can:
dene segments or get them from external systems, assign segments to users, customize the segment management.

Segments are represented in the personalization module by the CxSegment type. The relation between the User and Segment is represented by the CxUserToSegment type, which is base site aware.

Technical details about segment services: Services in personalizationservices Extension Details about segments conguration: Manage Segments Variations A variation represents a set of changes made across different channels to deliver a unique experience to a customer. Variations could include cms content, search results, promotions, and many others. An example of a variation can be a SummerSaleMen variation that applies to the users belonging both to the Men and BeachEnthusiasts segments.

Technical details: personalizationservices Extension Working with variations in Backoffice Administration Cockpit: Add Customizations and Variations Managing variations using SmartEdit: Create a Customized Storefront Remember In the SmartEdit, Variation is a technical term used in the technical documentation and across the data model for the Personalization Module, instead of Target Group, used for business purposes as an UI label.

## Customizations

Customizations group multiple variations together.

Only one variation per customization can be active for a user at a given time. Variations inside of an customization are sorted by priority. Customizations also dene a priority among each other.

Technical details and information about customizations and customization priority: personalizationservices Extension Working with customizations in Backoffice Administration Cockpit: Add Customizations and Variations Managing customizations using SmartEdit: Create a Customized Storefront This is   For more    the SAP Help  6 Actions and Action Results A variation is linked to actions of a CxAbstractAction type. Each action represents a changed element of the customization that makes the storefront more personalized.

An example of such a change could be:
display a specic component, activate a specic promotion.

Technically, the CxAbstractAction type extends the AbstractAction, which is a part of the processing extension. The AbstractAction has a target attribute which in the case of personalization is a reference to an executable spring bean. As a result, when an action is activated, its executable bean is proceeded. The result of this process is an object extending the class CxAbstractActionResult. Such action results are generated beans and are persisted in the database, however they have effect only when loaded in the current session.

Technical details: Create a Personalization Action Creating actions in Backoffice Administration Cockpit: Add Actions Using actions to dene a customized storefront in SmartEdit: Combine Customizations with Storefront Components

## Triggers

Triggers are the data model objects used to activate variations for a specic user.

The following triggers are available out of the box:
The default trigger used for triggering a variation for all users, regardless of the segment they are in. The segment trigger used for enabling the variations for specic user segments. The expression trigger used to trigger the variation based on a logical expression (often complex) created from segments and joined with operators.

Triggers use the segments as an input to dene if a variation should be activated or not. Segments can be grouped under one trigger using logical operators OR, AND and NOT.

Creating Custom Triggers You can also create and congure your own custom trigger using Backoffice Administration Cockpit or impex les. For example, you can create a trigger which activates a variation for a particular user group instead of segment conguration. Extending SmartEdit functionality makes the trigger tab visible in the customization modal.

For details on creating triggers, see Create Variation Triggers. For an example of extending SmartEdit functionality to introduce a new trigger, see Extend Personalization in SmartEdit.

## Personalization Mode In Smartedit

Personalization mode is a view in SmartEdit that allows you to build and congure experiences for your customers. The Personalization mode allows you to:
manage targeting of content from within SmartEdit, create new customizations and manage how they layer and interact to build a complete user experience, see changes in the correct context as you work, preview the customizations from the context of different customers.

You can easily create your customization using the SmartEdit intuitive and user-friendly UI. Once the particular customization is ready, you can preview it to see how it works for a particular target group. Before going into practical part, let's have a closer look at the main concepts in Personalization.

How can SmartEdit Help Me Personalize the Content?

The idea behind Personalization is to give the user an ultimate, customized experience. With the help of SmartEdit, you are able to easily create a new customization by combining desired target groups and segments and connect it to the specic components of the storefront. Additionally, SmartEdit allows you to instantly see how the customization works for a particular user group.

Support Tools Although SmartEdit should be the primary tool for creating and managing customizations, you can also use the Backoffice Administration Cockpit for conguration, treating it as a complementary tool to SmartEdit. For details, see Congure Personalization.

Next Steps Once you have learned the Personalization basics, you can start creating and managing your own customizations.

Get started with the Personalization mode, learn about the core concepts and advanced options: Get to Know Personalization Mode Learn how to create new customization: Add Customizations Create a customized storefront: Create a Customized Storefront Browse through existing congurations and use SmartEdit to see how your customers see them: View Customizations Learn how to create a combined view: Combined View This is   For more    the SAP Help  7 Discover the options provided by the Customization Library: Customization Library

## Get To Know Personalization Mode

Get familiar with the Personalization Mode by grasping the main concepts and learning more about advanced features.

Main Concepts General description of the Personalization mode main elements.

Customization and Target Group Status Each customization and target group has its status depending on whether it is active or not. Personalization and Content Versioning SmartEdit users can create a version of a page in the staged catalog to keep track of the introduced changes.

Main Concepts General description of the Personalization mode main elements.

![7_image_0.png](7_image_0.png)

1. Customization: A customization refers to a collection of data that includes one or more target groups, which in turn contain particular segments the users are assigned to. In our example, the Summer Sale customization includes target groups such as VIPCustomersGoldBeachEnthusiast and VIPCustomersGoldMen. Customizations are ordered according to priority - to understand this concept better, refer to Priority in Customizations and Variations.

2. Target Group: A target group groups the data retrieved from particular customer segment. It may include one or more segments. For example, a target group called VIPCustomersGoldMen may feature segments such as Men and VIPCustomersGold. Only one target group option may be available for a customization at a given time. The target groups are sorted by priority.

 Remember The naming convention assumes that the name target group is used in the frontend only, for the business-related purposes. Across the technical documentation, you will nd the term variation meaning the same.

3. Segments: A segment is a homogenous customer group or a cohort selected for a specic business purpose, so a group of users sharing some common characteristics such as age, gender, or habits. In our example, the segments are ShortsCategoryLover, Men, and VIPCustomersGold.

One user may simultaneously belong to multiple segments and one segment can hold many users.

## Customization And Target Group Status

Each customization and target group has its status depending on whether it is active or not.

There are two possible status values:
Enabled: meaning that a customization or a target group is active and if the conditions are met, it will be displayed to the user. If it includes target groups, you can set a status separately for each of them and enable/disable them according to your needs. Disabled: meaning that a customization or a target group is inactive and it will not be displayed to the user, even if the conditions are met.

This is   For more    the SAP Help  8 Working with Statuses Let's have a look at the following example - you have created new customization called SummerSale. It includes two target groups: SummerSaleCameraLenseLoverOrWebcamLoverAndOver30Man and SummerSaleDefault. You configured this customization some time ago and wanted all three target groups to be taken into account, so you enabled the customization However, now you would like only SummerSaleCameraLenseLoverOrWebcamLoverAndOver30Man target group to be taken into account, but you don't want to delete the SummerSaleDefault target group because you might need it later. Instead of deleting a group, you can easily disable it even if the entire customization is enabled, the disabl won't be taken into consideration. As you can see in the figure below, the target group is grayed out, but the customization and the other target group are enabled.

![8_image_0.png](8_image_0.png)

Manage Customization Library
Now let's consider a scenario in which you don't want your entire customization to be active. You can disable it easily using the edit mode. This way, you won't lose your con becomes temporarily disabled until you decide to use it again. In the figure below you can see that even if the customization is disabled, the target group configuration rema grayed out. So if you want to bring it back, you simply enable it.

![8_image_1.png](8_image_1.png)

For information on setting and using statuses, see Create a Customized Storefront .

## Personalization And Content Versioning

SmartEdit users can create a version of a page in the staged catalog to keep track of the introduced changes. Working with Personalization and content versioning may affect the personalized content. When you personalize a storefront component, it is placed in a container. Because the components which have not been personalized do not have their containers, the number of versioned pages may differ depending on the Personalization settings. An example scenario looks as follows:
- Personalize some of the components on the page. - Create a new version of the page using the Versioning perspective. - In the Personalization perspective, add an action to a component which was not affected before.

Come back to the Versioning perspective and revert the version to the previous one.

The number of containers in both versions does not match so a warning is displayed.

## Enable Personalization Mode

Instructions on enabling the Personalization mode in the SmartEdit along with the description of available options.

Access SmartEdit Use the default URL: https://localhost:9002/smartedit to access SmartEdit.

Select Catalog Use the staged version of the catalog to introduce any changes in the conguration. To make your conguration visible also in the online catalog, remember to perform catalog synchronization. You can also synchronize single slots or components, but be aware that in the case of customized components, only the default version of the component is synchronized. To synchronize the full component along with its different versions, you need to synchronize the whole catalog version. For details, see Synchronizing Content Catalogs.

Enable the Personalization Mode Before you start dening your conguration, enable the personalization mode. Select Personalization from the menu on the left.

 Note If you do not belong to the cxmanagergroup or the cxreadonly group, meaning you don't have required permissions, you won't see the Personalization mode.

![9_image_0.png](9_image_0.png)

## Handling Of Cms Workow Page Status In Personalization

Depending on the CMS workow status of a page, the personalization of components can be disabled.

This is   For more    the SAP Help  10

| Item   | Description                                                                                                                                 | Learn More                        |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| 1.     | A dropdown menu you can use to access the Personalization mode. Once the Personalization mode is activated, the buttons on the left appear. | Personalization Mode in SmartEdit |
| 2.     | Using the Customize button, you can preview and customize the page you are currently viewing.                                               | Create a Customized Storefront    |
| 3.     | The Combined View allows you to preview the page in the context of multiple target groups.                                                  | Combined View                     |
| 4.     | The Library allows you to create and manage your customizations and target groups.                                                          | Customization Library             |

The current CMS workflow status of a page is also indicated in the Personalization mode. It is displayed on the top right of the Personalization toolbar:
a e
@
@

![10_image_0.png](10_image_0.png)

SAP
SmartEdit

| Apparel UK Content Catalog - Staged | English | 5/15/19 10:44 AM | Apparel .   |             |                   |             |           |
|--------------------------------------------------------------------------------|-------------|-------------------|-------------|-----------|
| Sites >                                                                        | Navigation  | Pages             | Storefront  | ']        |
| Personalization  V                                                             | @ Customize | []] Combined View | all Library | - Synched |

As a default, CMS-related personalization actions are disabled for pages that are in a workflow. This can be configured by setting the property personalizationsmartedit.editPersonalizationInworkflow.enabled to false in the SmartEdit Configuration Editor. The SmartEdit workflow configuration property can be found in the personalizationsmartedit/resources/impex/essentialdata_personalizationsmartedit.impex file:
personalizationsmartedit.editPersonalizationInWorkflow.enabled The property is set by default to false , meaning that it is not possible to edit, add or delete actions during the workflow process. The property set to true means that personalization actions on the page can be edited, added or deleted.

If Personalization is disabled during the workflow process, SmartEdit reflects the configuration by proper notifications. Click on the button to see the status of the component:
disabled as the page is in workflow, and the component is affected by some customizations:

![10_image_1.png](10_image_1.png)

Personalization Actions Unavailable No edits can be made while the page is in workflow Customizations on Component To preview customizations by target group, go to Customize or Combined View

![10_image_3.png](10_image_3.png)

![10_image_2.png](10_image_2.png)

CategoryLovers

![10_image_4.png](10_image_4.png)

![10_image_5.png](10_image_5.png)

![10_image_6.png](10_image_6.png)

canonLover

![10_image_7.png](10_image_7.png) CategoryLovers cameraLensesLover VIPCust VipGoldAndWomenNotCameraLensLov...

nalization is disabled as the page is in workflow, and there are no actions on the component:

![10_image_8.png](10_image_8.png)

![10_image_9.png](10_image_9.png)

Personalization Actions Unavailable No edits can be made while the page is in workflow Customizations on Component To preview customizations by target group, go to Customize or Combined View
- Personalization is disabled as the page is in workflow, and a customization is selected:
Sites Navigation Pages Storefront

![10_image_10.png](10_image_10.png)

Personalization  V
@ Customize

![10_image_11.png](10_image_11.png)

VIPCust

![10_image_13.png](10_image_13.png)

VipGoldAndWomenNotCameraLe.

![10_image_16.png](10_image_16.png)

![10_image_12.png](10_image_12.png)

![10_image_15.png](10_image_15.png)

![10_image_14.png](10_image_14.png)

Personalization Actions Unavailable No edits can be made while the page is in workflow This is custom documentation. For more information, please visit the SAP Help Portal

![11_image_0.png](11_image_0.png)

To learn more about the CMS workow functionality in SmartEdit, see Workows.
Create a Customized Storefront Use SmartEdit to create a personalized storefront with just a few clicks.

Components in SmartEdit Components are small blocks of content. They are based on component types, which are templates that provide specic content such as text, graphics, media, links, and so on. If you want to learn how to create and manage components, see Components. In this section, you will learn how to link the components to the target groups and customizations to create a personalized view.

Creating a Customized Storefront You can easily customize your storefront by creating new customization and target group, and then combining the components with target groups.

 Note If you want to preview your personalization conguration on the storefront while setting it up, use a different browser or an incognito mode, otherwise you won't be able to see it. If you are using tabs of the same browser, the session is shared preventing you from viewing your customized conguration.

 Tip To learn more about dening a personalized storefront and viewing the customizations, see the following topics:
Add Customizations Combine Customizations with Storefront Components View Customizations Combined View

## Add Customizations

A customization is a collection of target groups created based on the customer-specic segments.

Prerequisites Make sure the Personalization mode is enabled. If not, use the menu on the right to select Personalization.

Context SmartEdit allows you to create and manage customizations using a wizard. In this example, you will set up a SummerSale customization that includes two target groups, each of them featuring two segments as you can see in the gure:

![12_image_0.png](12_image_0.png)

## Create Customization

Create and congure a basic customization.

Procedure 1. Click the Library button and select Create New Customization from the menu.

A pop-up window appears.

2. In the Basic Information section, add the name of your customization and a brief description. 3. If you want to make your customization active, set the Status conguration toggle button to On.

4. Optional: Set the dates in which you want your customization to be active. The date settings apply only if the customization is enabled.

 Note A customization is active within the start date and end date range. If no start date is provided, the customization is automatically active until the end date. If no end date is provided, the customization becomes active at start date and is active indenitely.

The date you enter is validated against a set of constraints:
Entering a string instead of a date format results in a warning prompting you to use the proper format. You can also leave the eld blank to restore the default settings. Entering a past date results in a warning prompting you to enter a current date or a date in the future. You can also leave the eld blank to restore the default settings.

Click Next to proceed to the next step.

## Add Target Groups

Add target groups you want to create your customization for.

Context To complete the task you need the following target groups: VIPCustomersGoldBeachEnthusiast and VIPCustomersGoldMen.

Procedure 1. Click Add Target Group to activate the slider panel.

![13_image_0.png](13_image_0.png)

 Note Checking Applies to all users makes the target group displayed to all the user groups (without selecting particular segments). Any already added segment congurations are removed.

b. Create an expression using the available operators (AND, OR or NOT). Use the select segments drop down menu to add the following segments: BeachwearLover, VIPGold .

If you want to learn more about a particular segment, hover over the short description to activate the pop-up. The example shows a simple expression. For advanced expressions, see Logical Operators in Personalization.

c. Click Add to add the target group to your customization.

d. If you need to duplicate or remove a segment, hover over it and use the buttons.

If you add custom trigger type and extend SmartEdit functionality to display it, the new trigger appears as a tab in the modal. For implementation details, see Extend Personalization in SmartEdit.

2. Create a second target group called VIPCustomersGoldMen. Include the following segments: Men, VIPGold joined with OR operator.

The result should be as follows:

![14_image_0.png](14_image_0.png)

Target groups are enabled by default, but you can easily Disable them using the menu on the right. The menu allows you also to Edit or Remove a particular group. The Move Up 
Remember to click Save once you have finished editing your target group, otherwise the changes won't be saved.

Results You have created new customization that includes two target groups. The new customization is now visible among the customizations in the Customization Library and in the preview mode in SmartEdit.

Next Steps Once the customization is created, you can combine it with selected storefront components. Learn how by following the instructions in Combine Customizations with Storefront Components.

If you want to know more about managing existing customizations, refer to View Customizations and Customization Library.

Logical Operators in Personalization Using logical operators allows you to build complex expressions to dene when actions for a given target group should be executed. You can use the following logical operators to build your expression:
AND: the content becomes personalized for the target group only if the user belongs to both segments. For example: Under20 AND Women. OR: the content becomes personalized for the target group if the user belongs to one of or both segments. For example: Under20 OR Women.

NOT: the content becomes personalized for the target group only if the user does not belong to any of given segments. For example: NOT (Under20 AND Women).

 Note If a target group consists only of negated segments, the target group applies to all users not belonging to those segments. This also includes users without active consent because they are treated as rst-time visitors who are not related to any segment. If the NOT operator precedes two segments, they are always joined with AND.

Each group can contain segments or other groups. Evaluation is done by checking if the user belongs to a given segment or not. The expression is invalid if it contains an empty group. If the expression is invalid, the user can't save it.

Dening Segment Relations for a Target Group You can dene the segment relations while creating a target group in SmartEdit. Let's assume you create a target group of users who:
are between 20-29 AND 30-39 years old, are women, are BeachwearLovers OR FlipopEnthusiasts, are NOT HatsFans and NOT ShadesConnoisseurs.

The wizard allows you to create the following structure:

![16_image_0.png](16_image_0.png)

1. This button activates the fullscreen mode. Once you are in the fullscreen mode, you can always return to the minimized window.

2. The name of your target group.
3. If you want to display your target group settings to all users, use the Applies to all users option. Any existing conguration for this target group will be removed. 4. The expression created on the y while you add containers and segments. 5. A dropdown menu allowing you to select the segments.

6. The container structure. To easily build an expression, you can perform the following actions:
Drag and drop the segments to rearrange the order. Remember that a newly added segment is always placed at the top of the rst container at the top.

Use the drag and drop to move the segments within and between the containers. If the number of containers exceeds the length of the window, its content will scroll down and up automatically allowing you to drag and drop the segments at a desired position. Collapse the containers to have an overview of the structure.

Remove the container with all its segments. Change the operator using the dropdown menu.

7. The icons allow you to duplicate or remove a selected segment. You can also remove the entire group with all its segments.

 Note Your target group has to include at least one segment to be valid. If you do not want to congure your target group for all users, use the Applies to all users option.

For details and a practical example of using the operators to create segment relations, see Add Customizations.

Combine Customizations with Storefront Components You can easily link the components to a particular target group by adding the actions in SmartEdit and preview them instantly.

Prerequisites Make sure that the Personalization mode is selected. If not, use the menu on the right to select Personalization.

Context SmartEdit provides you with an easy way to assign components to a particular target group within a customization.

Procedure

![17_image_0.png](17_image_0.png)

A selected target group becomes active, and its name displayed in the top toolbar.

3. Start customizing the storefront page for your target group. Let's assume that no actions were defined for this particular storefront and that every component belongs to t i Note Notice that when you hover the mouse over components that belong to your current catalog, they become highlighted and menu options appear in the left top corner. If the component belongs to a different catalog, it can't be personalized at this moment.

![18_image_0.png](18_image_0.png)

Item Description

| 1   | The customization and target group to be affected by the action.                                 |
|-----|--------------------------------------------------------------------------------------------------|
| 2   | Information about the component. For details, see Components                                     |
| 3   | Actions include replacing a component with a new one or selecting an already existing component. |
| 4   | Component to be displayed for the target group.                                                  |

5. Dene the action for a target group of your choice.

a. Select Replace master component creating new one to create new component.

For details on creating components, see Creating Components from Component Types.

b. Select Replace master component with another saved component. A list appears allowing you to search for a particular component.

Select the component and click Save to save the conguration.

6. The modied component is now highlighted and provides you with some additional options visible once you hover over it.

This is   For more    the SAP Help  19

![19_image_0.png](19_image_0.png)

Edit Action: Opens a pop-up window in which you can create new component to replace the currently active one, or select an already existing one.

Delete Action: Reverts the component setting to a default one.

7. Use the steps above to add actions for other components.

Components affected by a certain target group become highlighted.

 Note If you want to preview your personalization conguration on the storefront while setting it up, use a different browser or an incognito mode, otherwise you won't be able to see it. If you are using tabs of the same browser, the session is shared preventing you from viewing your customized conguration.

Results You have created a personalized storefront by assigning the storefront components to a particular target group. If the user matches a given target group the conguration will be displayed.

 Note If you are working with personalization and use versioning for your pages, be aware that reverting the version may affect personalized components. For details, see Personalization and Content Versioning.

## Shared Slots

A shared content slot is a content slot that is used in different pages, such as a header or a footer content slot. Also in Personalization mode some of the page components are placed within shared content slots, however they work in the context of a chosen target group. A shared slot is marked with a border and an icon as shown in the gure:

![20_image_0.png](20_image_0.png)

Using Shared Slots in Personalization As mentioned above, the shared slots can be used in the context of a selected target group and customization. If no target group has been selected, the exclamation mark will 

![20_image_1.png](20_image_1.png)

Once a customization and target group are selected, you can change the component. The rules for changing it are the same as for any other component. For details, see Combine Customizations with Store front Components SAP
 SmartEdit Sites >
Navigation Pages Storefront Personalization  V
4 Customize

| SpringSale   |
|--------------|
| >            |

SpringSaleVipGoldWomen x
[]] Combined View an Library B2C Accelerator BRANDS
STREETWEAR
SNOW 
ACCESSORIES
YOUTH
Because it is a shared slot, the component will be changed wherever it is used within the context of a target group, so the same settings will apply for the subpages. If you different target group, you will see the default shared slot settings for this group. You can change them at any time if need be.

View Customizations SmartEdit allows you to preview the created customizations, so that you know right away how the user will see them.

If there is no specific customization selected, you will see the basic storefront.

To see the customizations affecting the component, use the
( i 

![21_image_0.png](21_image_0.png)

Apparel UK Content Catalog The list tells you which customizations are enabled for the component, but you need to select them to see the way they affect it. If there are no customizations affecting the relevant information is displayed.

## Displaying Customizations

Prerequisites Make sure that the Personalization mode is enabled. If not, use the menu on the right to select Personalization.

Context Perform the following steps to preview the existing customization.

Procedure 1. Click the Customize button to view a list of customizations and target groups that can be displayed on the page you are currently visiting. The list is governed by the pri For details, see Priority in Customizations and Variations A list of customizations and target groups appears. Their status is also displayed and you can easily filter them, using the filters provided. The standard filters are the st t the customization filter, showing all customizations or only the ones affecting the page. If you are using Personalization in the multi-country setup, an additional filter 
@ Customize
[] Combined View ap Library

![22_image_0.png](22_image_0.png)

certain target group. For more information on commerce customizations, see Use Commerce Customizations, 2. Select the customization and target group to preview the configuration. Remember that only one target group can be active for a particular customization at a given time. O
ustomization becomes active, it is visible in the top toolbar WinterSale

![22_image_1.png](22_image_1.png)

| >                                                                                                                                                                              | SummerSale     | Enabled    | 00      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|------------|---------|
| SpringSale                                                                                                                                                                     | Enabled        |            |         |
| >                                                                                                                                                                              | >              | WinterSale | Enabled |
| WinterSaleDefault                                                                                                                                                              | 3 Component(s) | Disabled   | $       |
| 3. If the configuration for this particular target group has already been defined, the storefront components become highlighted. You can modify them at any time - to learn ho |                |            |         |
| mbine Oustomizations with Storefront Co                                                                                                                                        |                |            |         |

i Note This is custom documentation. For more information, please visit the SAP Help Portal This preview displays just one target group conguration at a time - however, more than one customization may be active for the user at the storefront. If you want to congure a preview of a storefront in the context of more than one target group, refer to Combined View.

Results Your target group conguration is reected on the page.

Combined View Learn how to use the combined view to display multiple target groups on the same page.

How Does it Work?

You already know how to create a customized storefront by creating a customization (along with a target group) and combining it with the storefront components. If you need further information, see Create a Customized Storefront. Once you congure all the settings, you can see the page rendered for a user who belongs to a specic target group.

With the Combined View you can perform the following actions:
Select multiple target groups and preview the page in their context to get an idea how the storefront will look like. If the same component is affected by two or more target groups at the same time, the target group with the highest priority is displayed.

Select one target group in the combined view and directly edit the components it affects (it does not have to be the winning target group).

 Note This topic explains the options generally available in combined view used without the Multi-Country Site Support. For using combined view with the Multi-Country Site Support, see Use Combined View with Multi-Country Site Support.

Congure the Combined View Congure the combined view to display several target groups at the same time.

Prerequisites Make sure that the Personalization mode is enabled. If not, use the dropdown menu on the right to select Personalization.

Context Follow the steps to congure your combined view.

![23_image_0.png](23_image_0.png)

3. Use the dropdown list to select customizations and target groups. You can lter the customizations to access only these affecting the page you are currently conguring, or you can choose among all available customizations. A list of chosen customizations and target groups is displayed. Customizations and target groups listed in the combined view window are ordered according to their priority, and reect the order in the customization library. Changing the priority of customizations and target groups in the library, applies the changes next time you want to congure the combined view.

Remember to save your conguration.

 Note You can select only one target group from a customization. Once you select a target group, the customization is grayed out, with the selected target group displayed in bold.

4. Immediately after you save the conguration, the components assigned to the particular target groups become highlighted and marked with the corresponding letter and color.

![24_image_0.png](24_image_0.png)

You can check the priority in the main window:
5. To remove the conguration, click the Clear All button.
Results Thanks to a successfully congured combined view, you can now preview a page in the context of several target groups.

Manage Components in Combined View View and edit the components in your customizations. You can edit the page components at any time. You have the following editing options:
The combined view is on and shows components affected for several target groups, but you can edit only the ones for the winning target groups. The combined view is on but one of the target groups is selected. The view displays only the actions of that chosen target group.

Edit Components of the Winning Target Group When you hover over the corner of a chosen component, additional buttons are displayed.

![24_image_1.png](24_image_1.png)

allows to replace an already set component with a different one (it may be an already existing one or a newly created one)

![25_image_0.png](25_image_0.png)

restores the default component for the winning target group.

displays the ranking of target groups the component is affected by (including both the winning and the losing target groups).

In order to edit or remove the action for a particular component follow the steps listed in Combine Customizations with Storefront Components. As a result, the customization settings will be changed, so if you access it from the Customize menu, the new action will be visible.

Edit Components of a Selected Target Group To select a desired target group and be able to change its components, click the Combined View button, and select the target group you want to edit.

Once the target group is selected, the view is reloaded to display the page in the context of this target group. The editing options are the same as when editing a target group selected using the Customize menu.

## Customization Library

Learn more about the rules governing the customizations using the Customization Library. Let's assume that you have already created your customization using the guidelines from Add Customizations.

![25_image_1.png](25_image_1.png)

1. Search Customization: A search eld you can use to lter your customizations. You can also use the dropdown menu to show only the enabled or disabled customizations.
2. Customization: A list of available customizations along with the target groups, listed according to priority. Target groups containing a commerce customization are distinguished by a commerce customization icon. Hover over a commerce customization icon to see a tooltip with information about the type and number of commerce customizations (for example:
Promotion actions: 1).

3. Target Group: The number of target groups belonging to a given customization.

4. Components: The number of storefront components affected by a particular target group.

5. Status: Customization and target group status. 6. Start: The date indicating when a customization becomes active. 7. End: The date indicating when a customization becomes inactive.

8. Management Buttons: Management buttons allowing to perform actions affecting customizations and target groups. Follow the links to learn more about management actions:
Customizations in Customization Library, Target Groups in Customization Library.

The customizations and target groups are listed according to priority. You can rearrange their order using the drag & drop functionality. Dragging & dropping is only allowed among items of the same type, so you cannot drop a customization in-between a list of target groups. The functionality works also when ltering is enabled. If the list of customizations or target groups is too long, the scroll zones will help you to drop an item in the proper place. Simply grab the item you want to reposition and drag it to the top or bottom of the list. The scroll zone will be enabled and the list will move automatically. For more information on priority, see Priority in Customizations and Variations.

## Customizations In Customization Library

Get to know the options that will help you manage your customizations. The gure below illustrates the management options for target groups:
Manage Customization Library

| Manage Customization Library                                                | x                         |              |       |                          |
|-----------------------------------------------------------------------------|---------------------------|--------------|-------|--------------------------|
| Apparel UK Content Catalog - Staged | Customizations (5)                    | Search Customizations   Q | All Statuses | >     | Create New Customization |
| Customization                                                               | Target Groups             | Status       | Start | End                      |
| Components                                                                  |                           |              |       |                          |
| ✓ SummerSale                                                                | Enabled                   | Edit         |       |                          |
| SummerSaleDefault                                                           | Disabled                  | Move Up      |       |                          |
| Move Down                                                                   |                           |              |       |                          |
| ❯ SpringSale                                                                | Enabled                   | Remove       |       |                          |
| 1 WinterSale                                                                | Enabled                   |              |       |                          |
| - Edit: opens the customization editor and allows you to introduce changes. |                           |              |       |                          |

- Remove: removes selected customization from the library.

i Note The customization is not deleted permanently, even though you cannot see it in SmartEdit. If you need your customization again, you can retrieve it using the Backoffice Administration Cockpit. Learn how: Manage Customizations

## Target Groups In Customization Library

Get to know the options that will help you manage your target groups.

The figure below illustrates the management options for target groups:

| Manage Customization Library                                                                        | x                         |              |                  |                          |     |
|-----------------------------------------------------------------------------------------------------|---------------------------|--------------|------------------|--------------------------|-----|
| Apparel UK Content Catalog - Staged | Customizations (5)                                            | Search Customizations   Q | All Statuses | >                | Create New Customization |     |
| Customization                                                                                       | Target Groups             | Components   | Status           | Start                    | End |
| ✓ SummerSale                                                                                        | Enabled                   |              |                  |                          |     |
| SummerSaleDefault                                                                                   | Enabled                   | e            |                  |                          |     |
| Edit                                                                                                |                           |              |                  |                          |     |
|                                                                                                     | 5                         | Enabled      | Disable          |                          |     |
| Commerce Customization                                                                              |                           |              |                  |                          |     |
| > WinterSale                                                                                        | 1                         | Enabled      | Move up          |                          |     |
| ❯ CategoryLover                                                                                     | 2                         | Enabled      | 5/10/19 12:00 PM | Move down                |     |
| Remove                                                                                              |                           |              |                  |                          |     |
| l V VIP                                                                                             | Enabled                   |              |                  |                          |     |
| - Edit: opens the target group tab of the customization editor and allows you to introduce changes. |                           |              |                  |                          |     |

- Disable: Disables a selected target group. Such a target group is then marked as disabled and is not active for a particular customization.

- Commerce Customization: opens a new window in which you can configure commerce customization actions. An example here can be a personalized promotion, which becomes available for a customer fitting a particular target group.

The availablity of commerce customization depends on registered commerce actions. If there are no registered actions, the commerce customization option will not be available.

details on how to use commerce customization, see Use Commerce Customizations.

- Remove: removes selected target group from the customization. A customization must have at least one target group, so if there is only one target group present, the Remove will not be active.

Use Commerce Customizations With the functionality provided by commerce customizations, you can make sure that users belonging to a certain group receive a promotion or enjoy personalized search results. Have a look

![27_image_0.png](27_image_0.png)

at commerce customization dialog and its elements.

1. Name of the selected customization and target group along with the status.
2. An action type selector you can use to dene the commerce customization action. Currently, you can select either Promotion action or Search action (to assign a search prole to a target group).

3. Options available for a selected action type. Depending on the type you have chosen, you can select a promotion or search prole.

4. A list of selected actions for given target group.

Once you add the commerce customizations, they will appear as icons next to the names of target groups. You can see an example in View Customizations.

Commerce Customizations Use Cases To see how the commerce customizations work in practice, check the following use cases:
Creating a rules-based promotion using the Rule Builder and assigning it to a target group: Create Personalized Promotions Creating a Winter Campaign using the adaptive search perspective and activating it for a specic target group: Adaptive Search in Practice Technical Implementation For technical implementation of commerce customizations, see Commerce Customizations.

## Multi-Country Site Support For Personalization

Multi-Country Site Support provides native support for managing and sharing content among multiple sites. With Personalization now supporting the multi-country site functionality, you can view the personalized content as seen by the viewers of local and parent catalogs. You can also easily personalize the content by reusing the components from parent content catalogs in a local content catalog.

Sample Data for Multi-Country Site Support SAP Commerce Cloud provides a sample Multi-Country Site Support setup through the multicountrysampledataaddon AddOn provided in the cx installation recipe. This provides sample data for Electronics Store with multiple content catalogs as shown in the following image:

![28_image_0.png](28_image_0.png)

Personalization also provides a set of sample data dened for multi-country sites, including customizations and target groups available in catalogs at different levels. Using the sample data allows you to explore personalization functionality out of the box. The sample data is also used in the sections below to help you understand how the Multi-Country Site Support works.

How Does Multi-Country Site Support Work?

SmartEdit with Multi-Country Site Support allows you to manage the use and reuse of content from a high-level content catalog (known as a root parent content catalog), to lower-level content catalogs (known as child content catalogs). You can dene multiple levels of content catalogs.

Inheritance and Cloning Each child content catalog inherits content from a parent content catalog. If your site has multiple levels of content catalogs, the lowest-level child content catalog can inherit and display content from any of its parent content catalogs. In a real-world implementation, you could have a global content catalog where you dene pages and components that you want to make available to regional content catalogs. The regional content catalogs could then use the pages and components as they are, or they could create clones of these pages and components and modify them for their specic country or location. Local content catalogs such as country content catalog, could then further rene the content by customizing the pages and components for their markets. The sample data includes already cloned pages for Electronics EU and Electronics UK, meaning that you can dene separate congurations for each of the page (but still use the components from parent catalogs). Electronics DE, on the other hand, is not cloned, and therefore you cannot edit it. If you encounter a page which is not cloned, you will see the following warning:
If you want to edit the page in this catalog, use the instructions in Cloning Pages from Parent Content Catalog Versions to clone the page. Once the page is cloned, you can introduce the changes.

For the action (such as changing the component) to be executed properly on the page, it must be used with the CxCmsComponentContainer. This container is dened in the same way as any other CMS component and renders matching results. The container has its own sourceId, however when shared across pages, the action is executed for every instance of this container
(because it is the same sourceId).

 Note By default, the containers receive a new sourceId when the page is cloned. This means that personalization settings for the containers and components are dropped and the cloned page is not affected by personalization.

You can change the default behavior by adding the personalizationcms.containers.deepclone.keep=true property to the local.properties le. As a result, a new sourceId will not be generated for the container. However, if you choose to do so, be aware of the following aspects:
A page child catalog is cloned from the parent catalog with some components already placed in containers: personalization-related changes made to such components in the parent catalog will be reected in the child catalogs, since both containers have the same sourceId.

A page child catalog is cloned from the parent catalog with some components not placed in containers, but directly in slots: personalization-related changes made to such components in the parent catalog will not be reected in the child catalog.

Previewing and Editing Single Customizations The mechanism for previewing a single customization is similar to previewing it without the Multi-Country Site Support. Thanks to the lters, you can also include parent catalogs on your list and preview the customizations available for them. When creating new customization, you can also select the components from the parent catalogs. For details, see Manage Single Customizations with Multi-Country Site Support.

Working with Combined View You can use the Combined View to preview the page for target groups coming from both the current and the parent catalogs. For details, see Use Combined View with Multi-Country Site Support.

## Manage Single Customizations With Multi-Country Site Support

You can easily preview and edit a conguration for a single customization using the features provided by the Multi-Country Site Support.

Prerequisites A local catalog is selected, including some already dened customizations and target groups.

Procedure 1. In the personalization mode, click Customize .

![29_image_0.png](29_image_0.png)

The list includes the customizations from the local and parent catalogs. To avoid confusion, customizations from parent catalogs are marked with a globe. If you hover over the globe, you will see the parent catalog name the customization belongs to.

 Note If you are working with the top parent catalog, the catalog lter is not available since there are no parent catalogs higher in the hierarchy.

3. Select the target group from a local customization.

You can see the affected components. The globe icon indicates that the component comes from a parent catalog.

 Note If a component comes from a parent catalog, you cannot edit it, just see the catalog it belongs to. To change it, go back to site selection and switch to the parent catalog.

![30_image_0.png](30_image_0.png)

The list of available catalogs and components may vary depending on the catalog you are currently viewing. If you are working with a parent catalog at the top of the hierarchy, you will have access to components from this catalog only.

Once you select the component it is changed on the page. To see how you can display several customizations from different catalogs at the same time, see Use Combined View with Multi-Country Site Support.

Use Combined View with Multi-Country Site Support Use the Combined View with Multi-Country Site Support to preview a page in the context of several target groups.

Context The Combined View with Multi-Country Site Support behaves in a similar way to combined view for just one site, but you can combine target groups coming from parent catalogs. For example, if the component is not affected by a customization in the local catalog, but is affected by a customization selected from a parent catalog, the component from the parent catalog will be displayed.

Procedure This is   For more    the SAP Help  31 1. In the Personalization mode, select Combined View from the top menu.

2. In the combined view conguration, click Congure .

A combined view conguration modal opens.

3. Use the lters to set the context.

You have the following options:
Include only customizations affecting the page or all available customizations.

Include customizations from the current catalog, the parent catalogs or all catalogs.

4. Use the dropdown menu to select the customizations and target groups. If the list includes customizations from parent catalogs, the catalog name is provided.

Selected customizations and target groups appear on the list. The ones coming from the parent catalogs are marked with a globe icon.

5. Click Save .

6. Use the View toggle to enable the conguration.

The rendered conguration features components from the current catalog and the parent ones. If you click on the ranking icon for a particular component, an ordered list of

![31_image_0.png](31_image_0.png)

The results in the Combined View may vary depending on whether a component is placed in a container or directly in the slot. For details, see the Inheritance and Cloning section in Multi-Country Site Support for Personalization.

## Click Tracking

In order to further improve the functionality of SAP Commerce Cloud to better support your business needs, click tracking is enabled in Personalization to collect the number of clicks for Personlization management.

 Note The data is collected on company basis, which means no individual user data is collected.

To stop click tracking, administrators can set the value of smartedit.default.click.tracking.enabled to false:
smartedit.default.click.tracking.enabled=false Personalization Module Architecture The Personalization module is a set of extensions providing core personalization functionality.

Dependencies This is   For more    the SAP Help  32 The diagram presents the extensions of the Personalization module.

![32_image_0.png](32_image_0.png)

Recipes For a complete list of SAP Commerce Cloud recipes that may include this module, see Installer Recipes. For a complete list of the SAP Commerce Cloud, integration extension pack recipes that may include this module, see Installer Recipe Reference.

Extensions The Personalization module contains the following extensions:
personalizationcms Extension The personalizationcms extension contains the cms specic functionality of the Personalization Module. It provides the tools for manipulating the displayed cms components based on the evaluated user experience.

personalizationcmsbackoffice Extension The personalizationcmsbackoffice extension contains Backoffice conguration for CxCmsAction dened in the personalizationcms extension.

personalizationcmsweb Extension The personalizationcmsweb extension contains cms-specic functionality of the personalization module. It contains declaration of CxCmsActionData object, its populator and queries needed for manipulating personalized cms objects through the personalizationwebservices extension.

personalizationfacades Extension The personalizationfacades extension provides a suite of facades for the Personalization Module functionality. The facade integrates personalization services and exposes a Data Object (POJO) response adjusted to meet the front-end requirements.

personalizationintegration Extension The main purpose of the personalizationintegration extension is to provide a framework to help integrate the customer data coming from external systems inside the Personalization Module. personalizationintegrationbackoffice Extension The personalizationintegrationbackoffice extension contains the Backoffice conguration for CxConfig, which is extended with the autoCreateSegments attribute in personalizationintegration extension. personalizationsampledataaddon AddOn The personalization module comes with a personalizationsampledataaddon AddOn that adds additional personalization data to the existing electronics and apparel b2c stores as well as the b2b powertools store. personalizationservices Extension The personalizationservices extension contains the core functionality of the Personalization Module.

personalizationservicesbackoffice Extension The personalizationservicesbackoffice extension contains the Backoffice conguration for a data model dened in the personalizationservices extension.

personalizationsmartedit Extension This is   For more    the SAP Help  33 The personalizationsmartedit extension is a smartedit extension (created using the ysmarteditmodule template). It provides additional functionality of managing components of a storefront when the personalization mode is active. personalizationwebservices Extension The personalizationwebservices extension contains the personalization api which allows the introduction of changes to the customer experience data model using the rest calls. It contains the functionality for core personalization, with the possibility to extend this functionality with some other extensions.

previewpersonalizationweb Extension The previewpersonalizationwebextension extends the previewwebservices extension in the personalization context. It implements populators that deal with the extended preview ticket data model.

## Personalizationcms Extension

The personalizationcms extension contains the cms specic functionality of the Personalization Module. It provides the tools for manipulating the displayed cms components based on the evaluated user experience.

In order to properly support Personalization in OCC, the personalizationcms extension overwrites cmsSlotModelToDataRenderingPopulator. To extend this populator, extend de.hybris.platform.personalizationcms.rendering.populators.CxContentSlotModelToDataRenderingPopulator instead.

CxCmsAction and CxCmsActionResult The personalizationcms extension includes CxCmsAction, which is a new data model extending the CxAbstractAction. The purpose of the CxCmsAction is to replace a component with another one. The action denes a containerId, a componentId, and a componentCatalog. It allows the CxCmsComponentContainer with a containerId to display a component with a componentId with additional information about the catalog. During the personalization calculation process, the CxCmsAction generates a CxCmsActionResult. The CxCmsActionResult is a generated bean and contains the same information
(containerId, componentId and componentCatalog) as the CxCmsAction that generated it.

CxCmsComponentContainer The generated CxCmsActionResult has a certain effect on the site when used with the CxCmsComponentContainer. This container (which is also a CmsComponent and extending AbstractCMSComponentContainer) is dened in the same way as any other cms component. When rendered, the container reads through the various CxCmsActionResult objects linked to the current user and session and renders the component dened by the rst result matching the container.

A match happens when the sourceId of the CxCmsComponentContainer is equal to the containerId attribute of the result. If there is no match, a default component is rendered. This logic is dened in DefaultCxCmsContainerStrategy.

If a container is shared across pages or it is used in multiple places in the system, the action is executed for every instance of this container (because it is the same sourceId). Container Cleanup The CxCmsComponentContainer is required to handle the CxCmsAction related to it. If there is no related action, the container displays the default component. However, there is no possiblity of cleaning up the containers which don't have any related actions. In this case, the CxActionRemoveInterceptor replaces the container with the default component.

The CxConfig was extended to include the containerCleanupEnabled parameter so that the cleanup process can be congured in the Backoffice Administration Cockpit by setting the Container cleanup enabled attribute in the personalization conguration. For details, see Set Up a Personalization Conguration.

 Note Do not perform container cleanup in the multicountry environment. It will not work correctly if the container and action related to it are dened in different catalogs.

OCC Integration CxContentSlotModelToDataRenderingPopulator is responsible for returning components from container directly on slot level.

CxCmsComponentContainer metadata is stored in containerMetadata eld added to component.

Previewing the Content The personalizationcms extension also contains additional functionality used to render the preview in SmartEdit.

Experience Rendering Upon every request, the CxPersonalizationFilter checks if recalculation is needed, based on the global conguration and registered voters. By default, the global conguration allows triggering recalculation based on url patterns, and the personalizationcms adds a PreviewVoter, which triggers recalculation if a preview ticket is present.

While the usual experience calculation uses the current user, if the preview is activated, the experience calculation is based on the current preview data. The preview data can contain specic variations to render or specic segments to use instead of a user. The personalizationcms extension brings an additional service (CxCmsRecalculationService) to verify if the preview is active and then uses the preview data. If no preview data is present, the experience calculation is delegated to the DefaultCxRecalculationService. The preview ticket also overwrites the congured Catalog Lookup type to ALL_CATALOGS. As a result, it is possible to display all customizations in the preview mode.

PreviewData model The PreviewData data model includes additional information used to preview the storefront based on segment or variation conguration. You can nd the entire conguration in the cxcms-items.xml le.

<relations> <relation code="PreviewDataToCxVariation" autocreate="true" generate="true" localized="false"> <deployment table="PreviewToVariation" typecode="3700" /> <sourceElement qualifier="previews" type="PreviewData" cardinality="many"> <modifiers read="true" write="true" search="true" optional="true" />
This is   For more    the SAP Help  34

 </sourceElement>
 <targetElement qualifier="variations" type="CxVariation" cardinality="many">
 <modifiers read="true" write="true" search="true" optional="true" />
 </targetElement>
 </relation>
 
 <relation code="PreviewDataToCxSegment" autocreate="true" generate="true" localized="false">
 <deployment table="PreviewToSegment" typecode="3701" />
 <sourceElement qualifier="previews" type="PreviewData" cardinality="many"> <modifiers read="true" write="true" search="true" optional="true" />
 </sourceElement>
 <targetElement qualifier="segments" type="CxSegment" cardinality="many"> <modifiers read="true" write="true" search="true" optional="true" /> </targetElement>
 </relation>
</relations>
Additional Markup Additional information in the html markup is required to congure personalization in SmartEdit. Necessary attributes are added by the CxCMSDynamicAttributeService, which implements the CMSDynamicAttributeService interface provided by the Accelerator. You can also acquire additional information related to CMS component by requesting the Commerce Web Services. In this case, they are added to the properties attribute by CxCmsContainerPropertiesSupplier, which implements CMSItemPropertiesSupplier. To learn more, see Custom Properties for Rendering.

## Data Filtering For Customizations Displayed Per Page

The implementation of the personalizationsmartedit extension allows the user to view the customization panel displayed in the personalization context. This panel has to list the customizations that affect the storefront page rendered at a particular time. Below you will nd information on nding and ltering customizations per page.

Customization Endpoint Call with <pageId> Request Parameter The CustomizationController functionality (exposed by the /customization endpoint) passes a collection of request parameters through the personalizationfacades extension directly to personalizationservices extension, which implements the data ltering mechanism using the DAO strategies. For details, see Data Filtering in personalizationservices Extension.

Example:
To nd the list of customizations affecting the page, personalizationsmartedit extension executes the following request: GET/customizations?pageId=homepage. As a result the DefaultCxCustomizationDAO is looking for strategy, the required parameters collection of which contains the <pageId> parameter. If it nds it, the default query for GET /customization is replaced with the one from the found strategy. Out of the box, personalizationcms extension provides the CxCustomizationPageIdDaoStrategy query.

CxCustomizationPageIdDaoStrategy The CxCustomizationPageIdDaoStrategy implements the exible search query that can be used to retrieve customizations per page. It needs to join the content slots of the page and content slots from the page template.

SELECT DISTINCT{c.pk}, {c.groupPOS}
FROM {CxCustomization as c JOIN CxVariation as v ON {c.pk} = {v.customization}
 JOIN CxCmsAction as a ON {v.pk} = {a.variation}
 JOIN CxCmsComponentContainer as con ON {a.containerId} = {con.uid}
 JOIN ElementsForSlot as rel ON {con.pk} = {rel.target}
 JOIN ContentSlot as cont ON {rel.source} = {cont.pk} }
WHERE 
{cont.pk} IN 
(
 SELECT x.contentSlot FROM ( 
 {{ SELECT {ContentSlotForTemplate.contentSlot} as contentSlot FROM {AbstractPage}, {PageTemplate}, {ContentSlotForTemplate} WHERE {AbstractPage.masterTemplate} = {PageTemplate.pk} AND {ContentSlotForTemplate.pageTemplate} = {PageTemplate.pk} 
 AND {AbstractPage.catalogVersion} = ?catalogVersion AND {AbstractPage.uid} = ?pageId 
 }} 
 UNION ALL 
 {{ 
 SELECT {ContentSlotForPage.contentSlot} as contentSlot FROM {AbstractPage}, {ContentSlotForPage}
 WHERE 
 {ContentSlotForPage.page} = {AbstractPage.pk} 
 AND {AbstractPage.catalogVersion} = ?catalogVersion AND {AbstractPage.uid} = ?pageId }}) as x )

AND {c.catalogVersion} = ?catalogVersion ORDER BY {c.groupPOS} ASC
Where:
<?catalogVersion>: pk of the catalog version
<?pageId>: uid of page (the homepage)
Related Information Data Filtering in personalizationservices Extension personalizationsmartedit Extension

## Personalizationcmsbackoffice Extension

The personalizationcmsbackoffice extension contains Backoffice conguration for CxCmsAction dened in the personalizationcms extension.

Backoffice Conguration The personalizationcmsbackoffice extension extends the personalizationservicesbackoffice extension functionality to enable managing of CxCmsActions.

For details on how to manage actions using the Backoffice Administration Cockpit, see Add Actions.

## Personalizationcmsweb Extension

The personalizationcmsweb extension contains cms-specic functionality of the personalization module. It contains declaration of CxCmsActionData object, its populator and queries needed for manipulating personalized cms objects through the personalizationwebservices extension.

Queries The personalizationcmsweb extends the query endpoint dened in the personalizationwebservices extension (for details see Query Endpoint section in personalizationwebservices Endpoints) with the following queries:
cxReplaceComponentWithContainer - creates new container in place of a component. Takes the following parameters: catalog, catalogVersion, oldComponentId, slotId Sample request:
POST https://localhost:9002/personalizationwebservices/v1/query/cxReplaceComponentWithContainer POST Data :
{
"params": {
"entry": [{
"key": "oldComponentId",
"value": "ApparelDEHomepageShipmentBannerComponent"
}, {
"key": "slotId", "value": "Section4Slot-Homepage"
}, {
"key": "catalog", "value": "apparel-deContentCatalog"
}, {
"key": "catalogVersion", "value": "Staged"
}, {
"key": "slotCatalog",
"value": "apparel-deContentCatalog"
}, {
"key": "oldComponentCatalog",
"value": "apparel-deContentCatalog"
}]
}
}
Request Headers: Accept: application/json Content-Type: application/json Authorization: Bearer 3ac71f81-739e-41d2-9901-6f2a1a4d5fc6 cxcmscomponentsfromvariations - returns list of components related to given variations. Takes the following parameters: catalog, catalogVersion, variations.

Sample request POST https://localhost:9002/personalizationwebservices/v1/query/cxcmscomponentsfromvariations POST Data :
{
 "params":{
 "entry": [{
This is   For more    the SAP Help  36
"key": "customization",
"value": "SummerSale"
}, {
"key": "variations",
"value": "SummerSaleMen"
}, {
"key": "catalog",
"value": "apparel-deContentCatalog"
}, {
"key": "catalogVersion",
"value": "Staged"
}]
}
} Request Headers:
Accept: application/json Content-Type: application/json Authorization: Bearer 3ac71f81-739e-41d2-9901-6f2a1a4d5fc6 Sample response
{ "components" : [ "Section1SlotHomepageCxContainer", "Section2ASlotHomepageCxContainer" ] }

## Personalizationfacades Extension

The personalizationfacades extension provides a suite of facades for the Personalization Module functionality. The facade integrates personalization services and exposes a Data Object (POJO) response adjusted to meet the front-end requirements.

Data Objects The Data Objects are created only to contain values and have no business logic except for the getter and setter methods. They are populated using a subset of the data contained in the SAP
Commerce Cloud ServiceLayer Models and are not backed by a persistence layer like the Model objects. The Data Object denition can be found in the personalizationfacadesbeans.xml le. They are generated during the build process. For more information about data object generation, see Generating Beans and Enums.

Converters and Populators Data Objects are constructed from Models or other Service Layer objects using converters and populators. The following types are used during conversion:

| Type                              | Description                                                                                                                                                                               |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| populator                         | Simple classes that have sole purpose of setting values in target object using the data from the source object.                                                                           |
| populatorList                     | A grouping object that invokes a few populators in a row and is a populator itself.                                                                                                       |
| converter                         | A converter able to create instance of target or use given prototype for conversion, uses list of populators to execute conversion.                                                       |
| configurableConverter             | A custom extension of the converter principle, has an additional option parameter that is used to dene which populators should be invoked.                                                |
| configurableSubtypeConverter      | An extension of the configurableConverter, has additional properties dening what type is converted and for what parent type using dedicated marker.                                       |
| configurableSubtypeAwareConverter | An extension of configurableConverter, automatically nds configurableSubtypeConverter with a given marker and uses it for conversion of objects with type hierarchy (Actions or Triggers) |

![37_image_0.png](37_image_0.png)

Subtype Conversion Mechanism The ActionData is a DTO representing only a base abstract model (CxAbstractActionModel), not a specic implementation. TriggerData works in the same way. In case of using a standard conversion, you get only the base attributes and lose most of the necessary information from the subclasses. The mechanism, which selects a proper converter for a data class allows avoiding such a situation and creating an object with all the needed attributes.

This mechanism involves configurableSubtypeConverter and configurableSubtypeAwareConverter beans. A single bean extending the configurableSubtypeAwareConverter should be dened for conversion of a given type (in one way):
<bean id="defaultCxTriggerConfigurableConverter" parent="cxSubtypeAwareConverter"> <property name="defaultOptions" ><value type="de.hybris.platform.personalizationfacades.enums.TriggerConversionOptions">BASE</value></property>
 <property name="markerClass" value="de.hybris.platform.personalizationfacades.trigger.converters.TriggerConverter" />
</bean>
The marker class denes which instances of configurableSubtypeConverter will be used by this converter. Then you can dene as many configurableSubtypeConverter instances as you need for all subtypes.

<bean id="defaultCxSegmentTriggerConfigurableConverter" parent="cxSubtypeConverter" >
 <constructor-arg name="markerClass" value="de.hybris.platform.personalizationfacades.trigger.converters.TriggerConverter" />
 <constructor-arg name="sourceClass" value="de.hybris.platform.personalizationservices.model.CxSegmentTriggerModel" />
 <property name="targetClass" value="de.hybris.platform.personalizationfacades.data.SegmentTriggerData" />
 <property name="populators">
 <map key-type="de.hybris.platform.personalizationfacades.enums.TriggerConversionOptions">
 <entry key="BASE" value-ref="cxTriggerPopulators" />
 <entry key="FOR_SEGMENT" value-ref="cxSegmentTriggerForSegmentPopulators" />
 <entry key="FOR_VARIATION" value-ref="cxSegmentTriggerForVariationPopulators" />
 <entry key="FULL" value-ref="cxSegmentTriggerFullPopulators" /> 
 </map> </property> </bean>
All configurableSubtypeConverter with the same markerClass as in configurableSubtypeAwareConverter will be used by it. The source and target classes dene what is converted into what, which helps configurableSubtypeAwareConverter to dene which of available configurableSubtypeConverter should be used in a given conversion.

## Facades

The SegmentFacade provides the functionality for searching and managing segments. The CustomerSegmentation is an object representing a relation between the customer and segments. The CustomerSegmentationFacade provides the functionality for searching and managing this relation.

The CustomizationFacade provides the functionality for searching and managing customizations. The VariationFacade provides the functionality for searching and managing variations. The VariationSegmentation is an object representing relation between the segment and variations. The VariationSegmentationFacade provides the functionality for searching and managing this relation.

The ActionFacade provides the functionality for searching and managing actions. It uses the ActionData object not only as response data, but also as a parameter for the create and update method. Thanks to that, you are able to create specic action objects, which extend a standard action, for example the CmsActionData. A special conversion mechanism is used to ensure such functionality - for details, see the Action Conversion Mechanism section above.

The TriggerFacade provides functionality for managing Trigger objects. Triggers are used for evaluating what variation should be evaluated for users. By default, the system provides a SegmentTrigger, which links users with variations using segments and ExpressionTrigger, which works on a boolean expression based on segments (if it exists or not).

personalizationintegration Extension The main purpose of the personalizationintegration extension is to provide a framework to help integrate the customer data coming from external systems inside the Personalization Module.

The personalizationintegration extension comes with the following features:
a mapping mechanism from any type of data to CX segments, possibility of declaration of mappers through spring beans or scripts stored in database, a default update user segment strategy collecting segments from different providers, possibility of utilizing multiple integration strategies to live in parallel in the system.

Related Information Mapping Mechanism Populators Default Update User Segment Strategy Auto Creation of Segments personalizationintegrationbackoffice Extension The personalizationintegrationbackoffice extension contains the Backoffice conguration for CxConfig, which is extended with the autoCreateSegments attribute in personalizationintegration extension.

The personalizationintegrationbackoffice extension extends the functionality in the personalizationservicesbackoffice extension with the ability to manage autoCreateSegments attribute of CxConfig.

For details on the integration conguration in the Backoffice Administration Cockpit see Set Up a Personalization Conguration.

personalizationsampledataaddon AddOn The personalization module comes with a personalizationsampledataaddon AddOn that adds additional personalization data to the existing electronics and apparel b2c stores as well as the b2b powertools store.

 Caution This page refers to software that has been deprecated as part of the Accelerator UI and older OCC template extensions deprecation. For more information, see Deprecated Accelerator UIs and OCC Template Extensions - Deletion in SAP Commerce Cloud 2211.

AddOn Setup In order to activate the personalization sample data, add the personalizationsampledataaddon AddOn to your localextensions.xml le.

<extension name="personalizationsampledataaddon" />
There is no need to install the AddOn on any Accelerator template. It reacts to the SampleDataImportedEvent event triggered by the import of the data from electronicsstore and apparelstore and adds additional data to these two stores. For more information about this mechanism, refer to yaddon Extension.

Imported Data The AddOn imports the following data on top the data available in the electronics, powertools and apparel store:
cx segments and users; cx customizations and cx variations; cx triggers using the previously imported segments; personalized cms data: the CxCmsComponentContainer and additional images.

 Note To assign sample segments to the users during the update process, they need to be dened in the system with which the personalization is integrated. In case of Intelligent Selling Services integration, they should be dened in the Segment Builder in the proper tenant. For more information, see Segment Builder.

Sample Users The personalizationsampledataaddon comes with the following employee and customer sample data:
For details on user accounts and user groups dened for personalization, see User Accounts and User Groups in Personalization.

B2C Customers and Employees To manage the Backoffice Administration Cockpit and SmartEdit congurations, use the following employees:
This is   For more    the SAP Help  39 Employee cxmanager cmsmanager cxuser To log in and preview the storefront, use the following customers:
Customer vipgold@hybris.com vipsilver@hybris.com vipbronze@hybris.com women@hybris.com men@hybris.com menover30@hybris.com womenvipgold@hybris.com womenvipsilver@hybris.com menvipbronze@hybris.com menvipgold@hybris.com menshortslover@hybris.com shortslover@hybris.com burtonlover@hybris.com alistair@hybris.com canonlover@hybris.com cameralenslover@hybris.com B2B Employees and Customers To log in and preview the storefront, use the following customers:
Customer powerdrillslover@pronto-hw.com screwdriverslover@pronto-hw.com Enable Sample Users in the personalizationsampledataaddon Addon You must enable sample users in the personalization module. They are not enabled by default. For information how to enable sample users in the personalization module, see Setting Passwords for Default Users.

User Accounts and User Groups in Personalization The personalizationsampledataaddon provides user accounts and usergroups with specic access rights to work with Personalization in SmartEdit.

User groups and users are created to provide personalization users with levels of permissions. Different users have different sets of permissions to access and/or edit specied content catalog versions. Users can only view and/or edit content catalog versions if they have the required permissions.

Permission Types In the context of the Personalization mode in SmartEdit, the user can have the following rights:
read: viewing personalized content, customizations and target groups, using the combined view. write: viewing and personalizing content, creating customizations and target groups, work with promotions and search proles.

User Accounts and User Groups for Content Catalog Permissions The essentialdata_personalizationservices.impex le in the personalizationservices extension includes the denition of the following groups:
cxmanagergroup: can view and personalize content, can create promotions, and use the functionality provided by SmartEdit. cxusergroup: inherits the rights of the cxreadonlygroup (with the right to view personalized content) and also includes the access to functionality provided by SmartEdit.

The other groups and user accounts are dened in impex les in the personalizationsampledata addon.

This is   For more    the SAP Help  40

## 

Additionally, the access to personalizationwebservices is required to work with personalization features. Such access is dened in the personalizationwebservices/web/webroot/WEB-INF/config/security-spring.xml for the cxmanagergroup and cxreadonlygroup.

The following table provides information about the user accounts and user groups and their associated rights:

| The following table provides information about the user accounts and user groups and their associated rights: Usergroup Electronics Apparel DE Catalog Apparel UK Catalog   | Power Tools Catalog   | Access to personalizationwebservices   |                    |                     |                                      |        |        |      |     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------|--------------------|---------------------|--------------------------------------|--------|--------|------|-----|
| Staged                                                                                                                                                                      | Online                | Staged                                 | Online             | Staged              | Online                               | Staged | Online |      |     |
| electronicscxmanagergroup                                                                                                                                                                             | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| Write                                                                                                                                                                       |                       |                                        |                    |                     |                                      |        |        |      |     |
| electronicscxusergroup                                                                                                                                                                             | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| apparel-decxmanagergroup                                                                                                                                                                             | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| Write                                                                                                                                                                       |                       |                                        |                    |                     |                                      |        |        |      |     |
| apparel-decxusergroup                                                                                                                                                                             | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| apparel-ukcxmanagergroup                                                                                                                                                                             | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| Write                                                                                                                                                                       |                       |                                        |                    |                     |                                      |        |        |      |     |
| apparel-ukcxusergroup                                                                                                                                                                             | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| powertoolscxmanagergroup                                                                                                                                                                             | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| Write                                                                                                                                                                       |                       |                                        |                    |                     |                                      |        |        |      |     |
| powertoolscxusergroup                                                                                                                                                                             | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| Usergroup                                                                                                                                                                   | Electronics           | Apparel DE Catalog                     | Apparel UK Catalog | Power Tools Catalog | Access to personalizationwebservices |        |        |      |     |
| Staged                                                                                                                                                                      | Online                | Staged                                 | Online             | Staged              | Online                               | Staged | Online |      |     |
| cxmanager                                                                                                                                                                   | Read                  | Read                                   | Read               | Read                | Read                                 | Read   | Read   | Read | yes |
| Write                                                                                                                                                                       | Write                 | Write                                  | Write              | Write               | Write                                | Write  | Write  |      |     |
| cxuser                                                                                                                                                                      | Read                  | Read                                   | Read               | Read                | Read                                 | Read   | Read   | Read | yes |
| cxmanagerelectronics                                                                                                                                                                             | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| Write                                                                                                                                                                       |                       |                                        |                    |                     |                                      |        |        |      |     |
| cxuser-electronics Read                                                                                                                                                     | Read                  | yes                                    |                    |                     |                                      |        |        |      |     |
| cxmanagerapparel-de                                                                                                                                                                             | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| Write                                                                                                                                                                       |                       |                                        |                    |                     |                                      |        |        |      |     |
| cxuser-apparel-de                                                                                                                                                           | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| cxmanagerapparel-uk                                                                                                                                                                             | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| Write                                                                                                                                                                       |                       |                                        |                    |                     |                                      |        |        |      |     |
| cxuser-apparel-uk                                                                                                                                                           | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| cxmanagerpowertools                                                                                                                                                                             | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| Write                                                                                                                                                                       |                       |                                        |                    |                     |                                      |        |        |      |     |
| cxuser-powertools                                                                                                                                                           | Read                  | Read                                   | yes                |                     |                                      |        |        |      |     |
| User Accounts and User Groups for Multi-Country Site Support                                                                                                                |                       |                                        |                    |                     |                                      |        |        |      |     |

SmartEdit provides support for Multi-Country Site Support.

| The following tables provide information about the users and user groups and their associated content catalog permissions for Multi-Country Site Support: UserGroup Electronics Electronics EU Electronics UK Electronics DE Electronics US   | Access to personalizationwebservices   |        |        |        |        |        |        |        |        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|--------|--------|--------|--------|--------|--------|--------|--------|
| Staged                                                                                                                                                                                                                                        | Online                                 | Staged | Online | Staged | Online | Staged | Online | Staged | Online |
| electronics-eucxmanagergroup                                                                                                                                                                                                                                               | Read                                   | Read   | Read   | yes    |        |        |        |        |        |
| Write                                                                                                                                                                                                                                         |                                        |        |        |        |        |        |        |        |        |
| electronics-eucxusergroup                                                                                                                                                                                                                                               | Read                                   | Read   | Read   | yes    |        |        |        |        |        |
| electronics-ukcxmanagergroup                                                                                                                                                                                                                                               | Read                                   | Read   | Read   | Read   | yes    |        |        |        |        |
| Write                                                                                                                                                                                                                                         |                                        |        |        |        |        |        |        |        |        |
| electronics-ukcxusergroup                                                                                                                                                                                                                                               | Read                                   | Read   | Read   | Read   | yes    |        |        |        |        |
| electronics-decxmanagergroup                                                                                                                                                                                                                                               | Read                                   | Read   | Read   | Read   | yes    |        |        |        |        |
| Write                                                                                                                                                                                                                                         |                                        |        |        |        |        |        |        |        |        |
| This is custom documentation. For more information, please visit the SAP Help Portal                                                                                                                                                          | 41                                     |        |        |        |        |        |        |        |        |

| 7/12/2024 UserGroup   | Electronics   | Electronics EU   | Electronics UK   | Electronics DE   | Electronics US   | Access to personalizationwebservices   |        |        |        |
|-----------------------|---------------|------------------|------------------|------------------|------------------|----------------------------------------|--------|--------|--------|
| Staged                | Online        | Staged           | Online           | Staged           | Online           | Staged                                 | Online | Staged | Online |
| electronics-decxusergroup                       | Read          | Read             | Read             | Read             | yes              |                                        |        |        |        |
| electronics-uscxmanagergroup                       | Read          | Read             | Read             | yes              |                  |                                        |        |        |        |
| Write                 |               |                  |                  |                  |                  |                                        |        |        |        |
| electronics-uscxusergroup                       | Read          | Read             | Read             | yes              |                  |                                        |        |        |        |
| User                  | Electronics   | Electronics EU   | Electronics UK   | Electronics DE   | Electronics US   | Access to personalizationwebservices   |        |        |        |
| Staged                | Online        | Staged           | Online           | Staged           | Online           | Staged                                 | Online | Staged | Online |
| cxmanagerelectronics-eu                       | Read          | Read             | Read             | yes              |                  |                                        |        |        |        |
| Write                 |               |                  |                  |                  |                  |                                        |        |        |        |
| cxuser-electronicseu                       | Read          | Read             | Read             | yes              |                  |                                        |        |        |        |
| cxmanagerelectronics-uk                       | Read          | Read             | Read             | Read             | yes              |                                        |        |        |        |
| Write                 |               |                  |                  |                  |                  |                                        |        |        |        |
| cxuser-electronicsuk                       | Read          | Read             | Read             | Read             | yes              |                                        |        |        |        |
| cxmanagerelectronics-de                       | Read          | Read             | Read             | Read             | yes              |                                        |        |        |        |
| Write                 |               |                  |                  |                  |                  |                                        |        |        |        |
| cxuser-electronicsde                       | Read          | Read             | Read             | Read             | yes              |                                        |        |        |        |
| cxmanagerelectronics-euzone                       | Read          | Read             | Read             | Read             | Read             | Read                                   | Read   | yes    |        |
| Write                 | Write         | Write            |                  |                  |                  |                                        |        |        |        |
| cxuser-electronicseuzone                       | Read          | Read             | Read             | Read             | Read             | Read                                   | Read   | yes    |        |
| cxmanagerelectronics-us                       | Read          | Read             | Read             | yes              |                  |                                        |        |        |        |
| Write                 |               |                  |                  |                  |                  |                                        |        |        |        |
| cxuser-electronicsus                       | Read          | Read             | Read             | yes              |                  |                                        |        |        |        |

personalizationservices Extension The personalizationservices extension contains the core functionality of the Personalization Module.

Data Structure The personalizationservices extension operates in compliance with the following structure:

![42_image_0.png](42_image_0.png)

- CxAbstractAction is a main class for executing the behavior. The personalizationservices extension does not provide any concrete implementation for this class. Other extensions should provide such classes.

- CxVariation is a main grouping element from execution point of view. The variation contains all the actions required for a given segment or segments.

- CxCustomization is a main logical grouping element. It contains variations with similar purpose defined for different segments. - CxUserToSegment is the relation storing the segments assigned to a user. The user can have different segments defined for different base sites.

CxVariations and CxCustomizations can be illustrated in the following way:
- CxCustomization: a Summer Sale, which can be the personalization plan for the summer sale period.

- CxVariation: Summer Sale Young, Summer Sale Adult, representing variations within customization for desired customer groups.

Services in personalizationservices Extension The personalizationservices extension provides basic services to execute the data model operations.

Priority in Customizations and Variations This is custom documentation. For more information, please visit the SAP Help Portal Customizations contain one or multiple variations. For a specic customization, only one variation can be valid at one time, however multiple variations can be valid at a time if they belong to different customizations. Customization and variation objects can be prioritized. The priority value is important during calculating customer personalization. Variation Triggers Triggers activate different variations for a specic user. Out of the box there are three different kinds of triggers, each of them having a corresponding strategy used to evaluate them. Data Filtering in personalizationservices Extension Handling data ltering in the personalizationservices Extension.

## Services In Personalizationservices Extension

The personalizationservices extension provides basic services to execute the data model operations.

The sections below provide you with details on each service.

CX Service The CxService is the main entry point for enabling personalization for customers. This service calculates actions for a given customer and executes them by creating immutable action results related to a particular customer. The CxService is reponsible for the following functionality:
triggering of asynchronous processes to calculate user segmentation and experience synchronous calculation of user experience Segment Service The CxSegmentService provides methods for searching segments and users related to segments. The CxSegmentServices uses the CxUserSegmentService and CxUserSegmentSessionService to manage the user to segment relation. For details on these two services, see the sections below.

Additionally, the CxSegmentService handles functionality for updating segments denition and assigning segments to the customer. The update segments process is dened in the UpdateSegmentStrategy. Assigning segments to the customer is dened in the UpdateUserSegmentStrategy. A default implementation of the UpdateUserSegmentStrategy has been dened in the personalizationintegration extension. Its task is to update the user segments based on information collected from providers. For more information, see personalizationintegration Extension. To update the information about the user segments you can create a custom provider or your own implementation of this strategy. By default, the user segments are being updated in an asynchronous process when a user logs in, but it can be also congured in a different manner - for example synchronously.

Consider this fact when you create your own provider or implementation of the UpdateUserSegmentStrategy. If it uses data from external system, it should be able to handle connection problems without signicant inuence on the performance.

Update Segment Strategy The update segments process is dened in the UpdateSegmentStrategy, which provides segments denitions. It contains the updateSegments method. This method uses the CxUpdateSegmentContext parameter to control the segment update process.

The CxUpdateSegmentContext parameter contains the following elds:
segmentProviders: a set of strings that specify which providers are used for the update.

fullUpdate: a boolean ag. Setting the ag to true results in a full update, which also means removing the non-existing segments. Setting the ag to false results in adding only the new segments.

baseSites: a set of BaseSiteModel objects, controlling which base sites or tenants are used for the update.

The personalizationservices extension contains EmptyUpdateSegmentStrategy, which is an empty implementation of the UpdateSegmentStrategy.

A default implementation of the UpdateSegmentStrategy interface is dened in the personalizationintegration extension. Its task is to update segments denitions based on the information collected from providers. For more information, see Default Update Segment Strategy.

Update User Segment Strategy The process for updating customer segments is dened in the UpdateUserSegmentStrategy. It provides segments for a given customer. The strategy contains the updateUserSegments method. This method uses the CxCalculationContext parameter to control the customer segment update process. The context stores a list of providers, which should be asked for customer segments.

The personalizationservices extension contains the empty implementation of the UpdateUserSegmentStrategy. A default implementation of the UpdateUserSegmentStrategy has been dened in the personalizationintegration extension. Its task is to update the customer segments based on the information collected from providers. For more information, see Default Update User Segment Strategy.

User Segment Service The CxUserSegmentService provides the functionality used to manage the models representing the user-to-segment relations. It includes the methods for setting, adding and removing the user-to-segment relations.

User Segment Session Service The CxUserSegmentSessionService provides the functionality used to manage the data representing user to segment relations. It provides methods for setting, adding and removing the user-to-segment relations within the scope of a session. This service is used mostly for anonymous users. It can also be used for registered user segments, provided they are congured to be stored in session. You can congure this option by setting the userSegmentsStoreInSession property under Personalization Conguration Personalization conguration in the Backoffice Administration Cockpit. For details, see Set Up a This is   For more    the SAP Help  44 Personalization Conguration.

Customization Service A customization groups personalization variations intended for a common purpose. It can represent a specic campaign such as a Summer Sale. Only one variation per customization can be active for a user at a given time. The CxCustomizationService contains functionality for managing the customizations. It provides methods for searching and creating customizations.

Variation Service A variation groups actions executed to customize the user experience. The CxVariationService contains functionality for managing the variations. It provides methods for searching and creating variations.

Action Service The action object contains information about an action, which should be executed to customize the user experience. The CxActionService contains functionality for managing actions. It provides methods for searching and creating actions.

Action Result Service The action result objects store information, which is required to customize the user experience. The CxActionResultService contains functionality for managing action results. By default, the action results are stored in session. This can be changed by providing custom implementation of the CxActionResultService.

Conguration Service The default CxConfigurationService implementation provides an entry point for retrieving the global personalization conguration for a base site. To maintain the backward compatibility, a fallback mechanism for getting the conguration based on the *.property le has been implemented. For details on personalization conguration see: Congure Personalization.

Process Service The default implementation of the CxProcessService interface handles the following personalization process operations:
creating and starting personalization asynchronous process, loading and storing parameters for the process using the strategies described in the section below. The process parameters are always loaded all at once, however you can decide either to store all of them or just the selected ones. The CxProcessParameterType enumeration denes the default values.

Loading and Storing Parameters Loading and storing has been implemented with the autowired collection of CxProcessParameterStrategy. By default it includes the following strategies:
CxProcessParameterAnonymousSegmentationStrategy, which stores anonymous segmentation as a process parameter or loads it from the process and sets it using the cxSegmentService. CxProcessParameterBaseSiteStrategy, which stores the current base site as a process parameter or loads it from a process and sets it in session using the BaseSiteService.

CxProcessParameterSessionTokenStrategy, which stores the session token and the session token key as a process parameter or loads them from the process and sets both of them in session (using SessionService and CxSessionTokenStrategy).

Each of these strategies implements the load and store functions and denes (in the spring context) the supported parameters.

## Priority In Customizations And Variations

Customizations contain one or multiple variations. For a specic customization, only one variation can be valid at one time, however multiple variations can be valid at a time if they belong to different customizations. Customization and variation objects can be prioritized. The priority value is important during calculating customer personalization.

 Note For consistency purposes the technical term variation is used thoughout the document. It has the same meaning as target group, which is a business term.

The variations inside of a customization are sorted by priority. If more than one variation is assigned to a customer, the one with higher priority is selected. Customizations also dene a priority among each other. The customization with the highest priority is triggered before the ones with a lower priority.

Priority is stored in dynamic rank attribute of model objects and is handled by CxCustomizationRankAttributeHandler and CxVariationRankAttributeHandler.

Activating Customizations and Variations Customizations and variations related to them can be enabled or disabled for evaluation purposes. This allows conguring actions for a given variation and turning it on for customers when necessary. A customization has its status as well as the enabledStartDate and enabledEndDate attributes, which inuence the dynamically evaluated active attribute. A customization is active if its status is set to Enabled and the time provided by timeService is past enabledStartDate and before enabledEndDate. If the enabledStartDateattribute is empty you can assume that the current time is past this date, whereas if the enabledEndDateattribute is empty you can assume that current time is before this date.

This means that if both the enabledStartDate and enabledEndDate are empty, the customization is active based exclusively on the status eld. A variation also has the status attribute, which can be set to Enabled or Disabled for each variation. A variation has a dynamic active attribute, which takes into consideration the enabled attribute of a variation and the active attribute of a parent customization. A variation is active only if its status is set to Enabled and the parent customization is active.

This is   For more    the SAP Help  45 Examples Customizations and variations are grouped according to priority, due to the fact that it may happen that a user belongs to two or more variations at the same time, or even two or more

![45_image_0.png](45_image_0.png)

customizations. To help you understand the priority rules and priority management in SmartEdit, have a look at the following diagram:

Let's take a simple example of 2 customizations having 3 variations in total. The customizations and the variations are displayed in priority order in the diagram above.
If Variation 1.a is triggered on its own, it will be the only variation evalulated. Action 1 and Action 2 will be performed.

If Variation 1.a and Variation 1.b are triggered, only the variation with the highest priority will be evaluated (since they are in the same customization) which means Variation 1.a. As a result, Action 1 and Action 2 will be performed. If Variation 1.b and Variation 2.a are triggered, they both will be evaluated since they are in different customizations. As a result, Action 3 and Action 4 will be performed.

If Variation 1.a and Variation 2.a are triggered, they both will be evaluated since they are in different customizations. However, if actions that impact the same target item (for example the same cms component) only the action belonging to the variation with the highest priority will be performed. In this case only Action 1 and 2 will be performed.

![45_image_1.png](45_image_1.png)

You can notice the order of the customizations, marked with yellow buttons and variations (target groups), marked with blue buttons. Available customizations are listed in a descending order so the SummerSaleVariant1 takes priority over the SummerSaleVariant2. The same happens with the variations within a customization (VIPCustomers is higher in the hierarchy than VIPCustomersGoldMen. You can easily change the priority in the customization library by dragging and dropping the customizations and target groups. For details, see Customization Library.

## Variation Triggers

Triggers activate different variations for a specic user. Out of the box there are three different kinds of triggers, each of them having a corresponding strategy used to evaluate them.

The CxTriggerService executes the registered strategies (the strategies are automatically found in the global context using their type). Because strategies are automatically injected into the CxTriggerStrategy they don't have aliases. To override a strategy with a different bean, declare a bean with the same name in global context.

At any time you can implement your own trigger that suits your needs. For details, see Create a Trigger Type.

CxDefaultTriggerStrategy The CxDefaultTriggerStrategy is a simple strategy for triggering a default variation. It uses the CxDefaultTrigger models to nd variations, which should be triggered. All variations related to CxDefautlTrigger models are returned. If a default trigger is present it will always return the variations it is associated with.

This type of trigger is useful if you need a default variation activated when no other variation is returned for the current user. If this is your use case, make sure that the variation linked to a default trigger has the lowest priority in the customization. There is nothing that prevents you from having the default variation at the highest priority in which case no other variation from the customization will be evaluated.

CxDefaultTrigger has an interceptor, which prevents creating more than one trigger for a variation. The default trigger always returns a related variation and there is no point in having any other trigger for such variation. You can use the default variation trigger if you want your variation to be targeted at all users (regardless of the division to user segments). For details how to set a default variation trigger see Add Customizations.

DefaultSegmentTriggerStrategy This is a default strategy for triggering variation using related segments. It uses the CxSegmentTrigger models as information storage for evaluating what variation should be triggered.

The CxSegmentTrigger model is linked to multiple segments and also holds an attribute that denes which operation to use when the trigger is evaluated: a variation can be triggered if any of the segments is present (OR operation) or if all are present (AND operation). The strategy also lters user segments using their affinity. Only the segments which exceed a certain threshold are used in evaluation. This property can be set using the personalizationservices.segment.trigger.strategy.min.affinity property.

ExpressionTriggerStrategy This strategy handles all instances of CxExpressionTrigger model. The CxExpressionTrigger serves as a container for logical expression dening the combination of CxSegments.

The ExpressionTriggerStrategy evaluates such expressions in the context of a given user, and if an expression returns true, the strategy returns a linked variation.

Expressions are stored in JSON format in the database and can consist of:
a group of elements with an operator (AND / OR) a negation on single element segment denition A sample expression in the JSON format looks as follows:
"expression": { "type": "groupExpression", "elements": [ { "type": "segmentExpression", "code": "Men"
 },
 {
 "type": "groupExpression",
 "elements": [
 {
 "type": "segmentExpression",
 "code": "Women"
 },
 {
 "type": "negationExpression",
 "element": {
 "type": "segmentExpression", "code": "HatsFan" } } ], "operator": "AND"
 }
 ],
 "operator": "OR"
}
The above example shows the following: a user belongs to Men segment OR to (Women segment but at the same time not the HatsFan segment). The segments used to build evaluation context also need to satisfy the minimal affinity requirement.

The CxExpressionTrigger is related to segments for validation purposes, but this relation is dynamic and based on an expression. Manual modication of related segments has no effect as it is overwritten while saving it thanks to the CxExpressionTriggerInterceptor. The CxSegment can't be removed if it's related to a CxExpressionTrigger as it would alter the expected behavior of the CxExpressionTrigger.

Managing CxSegment and CxSegmentTrigger The backoffice conguration dened in the personalizationservicesbackoffice extension provides you with a CxSegment/CxSegmentTrigger management tool. The purpose of this CRUD tool is to limit the functionality and manage relations between the CxSegment and CxSegmentTrigger. To ensure smooth management, the following interceptors were introduced:
CxSegmentRemoveInterceptor: prevents removing CxSegment if it's related to any CxSegmentTrigger, because that way the relation is also removed.

This is   For more    the SAP Help  47 CxSegmentTriggerValidationInterceptor: by extending the BaseTriggerInterceptor, it prevents creating or updating the relation between the CxSegment and CxSegmentTrigger, if there is one already dened for the other trigger.

## Data Filtering In Personalizationservices Extension

Handling data ltering in the personalizationservices Extension.

DAO Strategy Approach The personalizationservices extension provides the DAO and services for accessing the following data model items used in personalization:
CxCustomization CxVariation CxAbstractAction CxActionResult CxCustomizationGroup CxPersonalizationBusinessProcess CxSegment CxTrigger CxUserToSegment The services and DAO provide a way of getting all objects or just a single object with a given ID. It also ensures the possibility to call different exible search queries based on the parameters sent to the DAO. This allows to perform ltering of the data directly in the database instead of on the returned models. The following classes/interfaces play a part in this feature:
The de.hybris.platform.personalizationservices.dao.impl.AbstractCxDao class exposes an overloaded queryList method which may override a default query with the one provided by one of available strategies (CxDaoStrategy). The de.hybris.platform.personalizationservices.dao.CxDaoStrategy is an interface which provides the information on the extra parameters required to produce different query. It is also able to produce such query if needed.

The de.hybris.platform.personalizationservices.dao.CxDaoQueryBuilder interface and its default implementation DefaultCxDaoQueryBuilder are responsible for building a FlexibleSearchQuery from a default query and additional strategies implementing CxDaoStrategy. The de.hybris.platform.personalizationservices.dao.CxDaoStrategySelector interface and its default implementation DefaultCxDaoStrategySelector are responsible for selecting the best CxDaoStrategy instance to use based on a list of strategies and a list parameters.

These parameters will be passed down to the different layers of the application (facade, service, DAO) and will be used by the DefaultCxCustomizationDAO. This DAO provides a default query that lists all the customization in the system (GET /customizations) but also a list of additional strategies that may be called instead of the default query based on the input parameters:
CxCustomizationCodeDaoStrategy which will be used of the customization code is passed as a parameter: GET /customizations?code=somecode CxCustomizationNameStatusesDaoStrategy which will lter the data based on name and status: GET /customizations?name=somename&status=ENABLED
For further examples, see Data Filtering for Customizations Displayed per Page.

An example of such data ltering would be /customizations endpoint from the CustomizationsController. This endpoint can be called with or without parameters.

GET /customizations GET /customizations?code=somecode GET /customizations?name=somename&status=ENABLED
DAO Type Approach Unlike the DAO strategy approach, which allows to dene multiple dedicated queries, the DAO type approach allows dening a class that supports a given type. This approach is supported only by de.hybris.platform.personalizationservices.action.impl.DefaultCxActionService, with the use of de.hybris.platform.personalizationservices.action.dao.CxActionTypeDao.

The ]DefaultCxActionService collects all beans that implement the CxActionTypeDao from the spring context and selects one of them using the CxActionType as a key to perform search. Currently, the CxCmsActionTypeDao supporting CxActionType.CXCMSACTION is the only implementation of this mechanism.

## Personalizationservicesbackoffice Extension

The personalizationservicesbackoffice extension contains the Backoffice conguration for a data model dened in the personalizationservices extension.

Conguration The personalizationservicesbackoffice extension contains the conguration that allows managing the entire personalization data model.

For details on how to work with Personalization using the Backoffice Administration Cockpit see: Congure Personalization.

DefaultRecalculateActionEditor To enable CxUrlVoterConfig management a custom editor was introduced. The DefaultRecalculateActionEditor extends the DefaultMultiReferenceEditor provided by Backoffice. The DefaultRecalculateActionEditorSearchFacade provides data for this editor based on RecalculateAction enum dened in the personalizationservices extension.

## Personalizationsmartedit Extension

The personalizationsmartedit extension is a smartedit extension (created using the ysmarteditmodule template). It provides additional functionality of managing components of a storefront when the personalization mode is active.

 Note Bear in mind that in technical documentation the term variation is used for a target group. Target group is a UI label used for business purposes.

The personalizationsmartedit extension contains two Angular modules:
personalizationsmarteditcontainerModule (wired with the SmartEdit Container application), personalizationsmarteditModule (wired with the SmartEdit application).

In the following sections, you will nd detailed information about the project components.

commons This directory contains the utility features, which are included to both modules: personalizationsmarteditModule and personalizationsmarteditcontainerModule. The inclusion is done by a Grunt task.

personalizationsmarteditPagination: this directory contains a directive and templates for the backend pagination mechanism. It can be used in the following way:
<personalizationsmartedit-pagination pages="pagination.pages " current-page="pagination.currentPage " page-sizes="pagination.pageSizes " curren personalizationsmarteditInfiniteScroll.js: this le contains a directive for supporting innite scroll in ui-select directive from a bootstrap. It can be used in the following way:
<ui-select-choices repeat="item in items" infinite-scroll="addMoreItems()" infinite-scroll-distance="2"> <div ng-html-bind="item.name | highlight: $select.search"></div> </ui-select-choices>
In this example, the function addMoreItems is called each time more data should be loaded to list (so when the user scrolls to end of the list). personalizationsmarteditCommons.js: this le contains validation directives, constants, and utils functions.

personalizationsmartedit This directory contains all modules used in the personalizationsmarteditModule.

combinedView: this directory contains a directive for adding a border marked with a color and a letter to storefront components selected by a user when creating a combined view. componentLightUpDecorator: this directory contains a directive for adding a lightup border to the components on the storefront, when user selects a customization or a target group.

contextMenu: this directory contains a service, which is a gateway to a corresponding service in the personaliziationsmarteditcontainerModule.

service personalizationsmarteditServicesModule.ts: this le contains a service with current context information and a gateway to communication with corresponding service in the personaliziationsmarteditcontainerModule.

personalizationsmarteditmodule.js: this le contains settings conguration for the inner application and allows, for example, enabling contextual menu buttons or enabling decorators. The module is using featureService and decoratorService from SmartEdit.

personalizationsmarteditcontainer This directory contains all modules used in the personaliziationsmarteditcontainerModule.

combinedView: this directory contains all the logic required to congure and support combined view, for example to enable or disable it, update preview ticket with selected values, and assign colors and letters to selected items.

contextMenu: this directory contains all the logic that can be executed from contextual menu buttons, for example adding an action to component, editing action for component, deleting action from component. For details on combining components with customizations see: Combine Customizations with Storefront Components.

dataFactory dataFactory.js: This le contains data factory for customizations. With this data, the factory developer can refresh the list of objects from another service or controller, so data can by synchronized.

management: for details, see Customization Library.

pageCustomizationsToolbar: for details, see View Customizations.

service personalizationsmarteditContextServiceInner.ts: this le contains a service with current context information and communication with corresponding service in the personaliziationsmarteditcontainerModule. personalizationsmarteditContextServiceOuter.ts: this le contains a service with current context information and communication with corresponding service in the personaliziationsmarteditModule.

personalizationsmarteditPreviewService.js: this le contains a service for managing preview tickets (create, update, delete).

This is   For more    the SAP Help  49 personalizationsmarteditRestService.js: this le contains a service with all functions used to manage REST data.

personalizationsmarteditcontainermodule.js: this le contains settings conguration for container application, such as adding top toolbar items, creating personalization perspective and adding all features to this perspective. The module is using featureService and perspectiveService from SmartEdit.

Styling This directory contains all custom styling used in personalizationsmartedit extension.

 Note For further information, see Overview of the SmartEdit Framework Architecture.

Personalization Mode The SmartEdit framework provides the functionality to create various modes, each of which contains a feature or other modes. When a user selects a particular mode in the SmartEdit web application, all features bound to the mode are enabled when enablingCallback functions are invoked and all features not bound to the mode are disabled when the disablingCallback functions are invoked.

The personalizationsmartedit extension includes only one mode, containing the following functionality:
top toolbar items, enable/disable personalizationsmartedit context, decorator for highlighting components, contextual menu buttons (add/edit/delete action, information),
edit component (function used from cmssmartedit extension). This function is registered to provide end user with option to edit newly created components.

The actions provided by specic modules in the personalizationsmartedit extension are as follows: personalizationsmarteditcontainerModule setting selected target groups and customizations, adding/editing/deleting customization, adding/editing/deleting target group within a customization, changing the priority of target group and customization, enabling/disabling the personalizationsmartedit context.

selecting items for the combined view.

For details, see personalizationsmarteditcontainerModule.

personalizationsmarteditModule displaying the Info, Add, Edit, Delete actions in contextual menu if the personalization mode is turned on, highlighting the containers based on selected target groups and customization, adding/editing/deleting actions to selected target group within a customization.

The state between both modules is synchronized each time the inner application is reboostrapped. For example, when the user is going to a subpage, the rebootstraping event is captured by a directive in the following way: directive is waiting until the data-smartedit-ready attribute is set on the body html element, and when its set synchronisation function is called.

 Note Each module is a separate instance of the personalizationsmartedit extension that contains a dened (current) state of the personalization context. The communication between them (using the gateway proxy) is initialized only in the case of a change in the state.

## Personalizationsmarteditcontainermodule

Personalization Toolbar Menu Items The FeatureService allows you to add additional items to the toolbar menu, contextual menu, or register any additional functionality.

Currently our extension is adding two features to the top toolbar menu that allow to perform the following actions:
displaying existing customizations and variations (target groups) on the storefront (only one target group per customization is allowed) customization/variation management For further information, see Extending the Page Tool Menu and Gateway Factory.

Displaying Existing Customizations and Variations Use the personalizationsmarteditPageCustomizationsToolbarItemTemplate.html template to:
add the customizations from the library, display the customizations and variations that affect the page that is currently being previewed, This is   For more    the SAP Help  50 lter the results according to their status (for example: ENABLED, DISABLED or ALL).

For instructions on displaying existing customizations on the storefront see: View Customizations.

Customizations and Variations Management For the purpose of creating/editing/removing existing customizations and variations, we have created a dedicated angular module (personalizationsmarteditManagerModule). The module implements a controller of a modal, which is displayed in two modes:
creating a customization with variations.

editing an existing customization.

The modal content is presented in two tabs (ui.bootstrap.tabs implementation). Depending on which tab is selected, the NEXT_BUTTON is switched to a CONFIRM_BUTTON (or the other way around).

Each tab implements its own isDirty and isValid functionality.

Based on the information from a selected tab, the proper watcher enables/disables conrm/next button accordingly.

Creating Complex Segment Expressions Segment expressions are built using multi-segment-view directive, available in the personalizationsmarteditSegmentViewModule. The multi-segment-view represents both SegmentTriggerData and ExpressionTriggerData objects from the backend system. The personalizationsmarteditTriggerService was created as part of personalizationsmarteditManagerModule to accommodate them. If an expression is simple (just one top-level group, it doesn't contain subgroups) it will be stored as SegmentTriggerData, otherwise it will be stored as ExpressionTriggerData. The personalizationsmarteditTriggerService also handles the DefaultTriggerData. It is a special case of trigger that applies to all users (may even be anonymous). Only one of DefaultTriggerData/SegmentTriggerData/ExpressionTriggerData can be related to a selected variation. Attempt to create another one will fail.

Reloading Storefront based on Selected Customization and Variations Experience Storefront Rendering Variations (or customizations which group variations) fully dene the experience using linked actions. Such actions may dene how the storefront should look (for instance by displaying different banners for a user who falls into a specic segment).

On the side of the Accelerator everything is handled by the personalizationcms extension which, with the use of DefaultCxCmsContainerStrategy, calculates the components to display for a logged user. The Personalizationcms extends also the preview ticket data model with variations, then the CxVariationPreviewStrategy based on extended data model sets action-based session attributes and the actual component calculation is being done transparently with the DefaultCxCmsContainerStrategy.

For details see: personalizationcms Extension.

Updating Preview Ticket with Selected Customizations/Variations SmartEdit uses the sharedDataService to store information about current ticket id and resource path. With this information, the existing preview ticket is updated with selected variations with extended previewwebservices /preview resource requests as presented below.

//First we call GET for existing ticket personalizationsmarteditRestService.getPreviewTicket().then(function successCallback(previewTicket) {
 //then we set selected variations for preview ticket previewTicket.variations = selectedVariationsCodes;
 //and then we call PUT for updating existing preview ticket personalizationsmarteditRestService.updatePreviewTicket(previewTicket).then(function successCallback(response) {
 return sharedDataService.get("preview").then(function successCallback(preview) {
 iFrameManager.loadPreview(preview.resourcePath, preview.previewTicketId);
 });
 }, function errorCallback(response) {
 personalizationsmarteditErrorHandler.sendError($filter('translate')('personalization.error.updatingpreviewticket'));
 });
 //...

});
Refreshing the Preview Ticket To preview a selected storefront using SmartEdit, a previewwebservices rest POST is called on the preview resource. The previewwebservices extension, on the other hand, is using the existing cms2 functionality (DefaultCMSPreviewTicketService to be precise) to create a preview ticket. The mentioned service, apart from preview ticket creation, instantiates a task runner, which after 15 minutes removes the created preview ticket.

In this case, you need a fallback mechanism to deal with the 404 response code if the preview ticket was removed. In the scenario presented below we are creating preview ticket with the same parameters that the SmartEdit iframemanager was using in the rst place.

previewService.updatePreviewTicket = function(variations) { var deferred = $q.defer(); var selectedVariationsCodes = personalizationsmarteditUtils.getVariationCodesForPreviewTicket(variations); return personalizationsmarteditRestService.getPreviewTicket().then(function successCallback(previewTicket) {
This is   For more    the SAP Help  51 previewTicket.variations = selectedVariationsCodes; return personalizationsmarteditRestService.updatePreviewTicket(previewTicket);
 }, function errorCallback(response) {
 if (response.status === 404) {
 //preview ticket not found - let's try to create a new one with the same parameters return createPreviewTicket(selectedVariationsCodes); } else {
 personalizationsmarteditErrorHandler.sendError($filter('translate')('personalization.error.gettingpreviewticket'));
 return deferred.reject(response); } });
}; var createPreviewTicket = function(variationsForPreview) {
 var experience = personalizationsmarteditContextService.seExperienceData; var configuration = personalizationsmarteditContextService.seConfigurationData; var deferred = $q.defer();
 var resourcePath = configuration.domain + experience.siteDescriptor.previewUrl; var previewTicket = {
 catalog: experience.catalogDescriptor.catalogId, catalogVersion: experience.catalogDescriptor.catalogVersion, language: experience.languageDescriptor.isocode, resourcePath: resourcePath, variations: variationsForPreview };
 return personalizationsmarteditRestService.createPreviewTicket(previewTicket).then(function successCallback(response) {
 storePreviewTicketData(response.resourcePath, response.ticketId);
 personalizationsmarteditErrorHandler.sendInformation($filter('translate')('personalization.info.newpreviewticketcreated'));
 return deferred.resolve(response);
 }, function errorCallback(response) {
 personalizationsmarteditErrorHandler.sendError($filter('translate')('personalization.error.creatingpreviewticket'));
 return deferred.reject(response);
 });
};
Useful links previewpersonalizationweb Extension Combined View The personalizationsmarteditCombinedViewModule module contains services and controllers used to support the combined view in container application. A user can select any number of target groups and customizations from the list to display them on the storefront, and the service will automatically assign the colors and letters to selected items. Once the preview ticket is updated, this information is presented on page (as borders surrounding the components). The decorator highlights the components that are customized as well as renders a preview of the current customizations for comparison. As a result, the user sees how the customizations affect the page.

## Personalizationsmarteditmodule

Contextual Menu This menu is only available when the user switches to personalization mode and selects a single customization and target group from the toolbar menu.

Adding, Editing, Deleting Actions and Information Based on the personalization context and with use of featureService you are allowed to add the Add action, Edit action, Delete action, and Information contextual menu buttons for the components.

Add action option is available only for components, which are not connected to selected target group. Edit action option is available only for components, which are connected to selected target group. Delete action option is available only for components, which are connected to selected target group Information is available if the user does not select any target group.

For further information, see Adding Contextual Menu Items to Components.

Highlighting Components The components are highlighted as a result of performing the following actions:
customizing the components, using the combined view.

In both cases it is done by directives, which take into account selected target group(s) and additional css classes to components to achieve proper styling. Additionally, when this directive is used in combined view, it assigns colors and letters to selected target group(s).

 Note The module name containing the directive must follow the pattern: directive name + Decorator To assign the directives to specic types of components, add the mapping to the decorator service and to the feature service:
decoratorService.addMappings({
 '^.*Component$': ['personalizationsmarteditComponentLightUp', 'personalizationsmarteditCombinedViewComponentLightUp']
}); featureService.addDecorator({
 key: 'personalizationsmarteditComponentLightUp',
 nameI18nKey: 'personalizationsmarteditComponentLightUp'
});
featureService.addDecorator({ key: 'personalizationsmarteditCombinedViewComponentLightUp', nameI18nKey: 'personalizationsmarteditCombinedViewComponentLightUp' });
Shared Slots A shared content slot is a content slot that is used in different pages, such as a header or a footer content slot. Since the personalization mode also assumes the use of several shared slots, the slot indicator was implemented to inform users when they are modifying shared slots. The shared slot indicator is implemented as the following angular directive which is executed on slot components:
decoratorService.addMappings( { '^.*Slot$': ['personalizationsmarteditSharedSlot'] } );
The directive is located in the personalizationsmarteditSharedSlotDecorator in personalizationsmartedit application (which is the inner application). The directive is executed on every slot in the page each time the page is reloaded (inner application is reloaded).

The onInit function directive calls the isSlotShared function in slotSharedService. You can nd the service in the cmssmartedit extension.

For more information on how to use the shared slots, see Shared Slots.

Scroll Zones The scroll zones allow for scrolling the content of the window. A good example here can be moving an item up and down on the segment list when creating a target group. The content visibility may be limited due to the size of the window, so scroll zones allow the user to easily move the item without the need to manually use the scroll bar. An example for using scroll zones when setting segment relations can be found in Logical Operators in Personalization and Add Customizations. The scroll zones are appended to the body of the page. They are created upon component initialization (for example when the slider panel is opened) and removed from the Document Object Model when the component is closed (when the slider panel is closed). In order to use the scroll zones, add the following lines in your code:
<personalizationsmartedit-scroll-zone data-scroll-zone-visible="ctrl.scrollZoneVisible" data-get-element-to-scroll="ctrl.getElementToScroll()">
</personalizationsmartedit-scroll-zone>
The following parameters need to be passed:
data-scroll-zone-visible: a boolean variable controlling if scroll zones are visible or not data-get-element-to-scroll : a function returning the element to scroll.

For more information, see the scroll zones implementation in personalizationsmartedit/web/features/personalizationcommons/personalizationsmarteditScrollZone.

Drag and Drop for Customizations and Target Groups The drag and drop functionality available in the customization library is based on the angular-ui-tree component which provides the drag and drop support. The conguration accepts moving the items of the same type only. For example, you can rearrange target groups but you cannot drop a target group in a list of customizations. The scroll zones component ensures smooth navigation through long lists of customizations and target groups. For more information on scroll zones, see the Scroll Zones section above.

personalizationwebservices Extension The personalizationwebservices extension contains the personalization api which allows the introduction of changes to the customer experience data model using the rest calls. It contains the functionality for core personalization, with the possibility to extend this functionality with some other extensions.

Extension Structure This is   For more    the SAP Help  53

## 

As you can see in the gure below, the personalizationwebservices extension depends on the personalizationservices extension (for the domain) and the webservicescommons (for web functionality). Because the personalizationservices extension provides only basic functionality for customer experience without dening any particular actions, the personalizationwebservices extension also can't provide the functionality for specic actions. However, the actions are supported by additional extensions (such as personalizationcms extension or personalizationpromotions extension) which in turn depend on personalizationservices. Therefore, the personalizationcmsweb extension was created to extend the personalization API with functionality related to CMS (for example creating a CxCmsAction).

The personalizationsearchweb extension extends the personalizationwebservices extension with information required to use the personalized search functionality through the

![53_image_0.png](53_image_0.png)

Authorization and Authentication
To call the API, you have to be authorized and authenticated and you need a proper token to use the web services. The API provided by personalizationwebservices is secured by OAuth 2.0. To get the access token, you need an OAuth client dened in the system and a user with proper rights. SAP Commerce Cloud does not provide sample OAuth clients, so you have to dene your own. For instructions, see Conguring OAuth Clients.

 Note When dening the OAuth clients remember to assign personalizationwebservices scope to them. You can also specify that scope when you request a token used to access personalizationwebservices. The user for whom you request the access token, should belong to cxmanagergroup or admingroup, since only these groups have rights to access personalizationwebservices.

Different permissions are required based on which endpoint you want to call. For the catalog-aware endpoints the requirements are as follows:
To execute a write request (POST, DELETE, UPDATE, PATCH) you need the write access to the catalog/catalogVersion on top of being included in the cxmanagergroup or the admingroup. To execute a read request (GET), you just need to have read access to a given catalog/catalogVersion, so you need to belong to cxreadonlygroup (which gives you the right to only view the combined view in personalization mode), the cxmanagergroup or the admingroup.

For non-catalog-aware endpoints such as segments/, customersegmentations/ or queries/, you just need to be in the cxmanagergroup or admingroup.

The access to the following endpoints is denied by default, in order to improve and maintain security:
v1/customersegmentations POST /v1/segments PUT /v1/segments/ {segmentCode}
DELETE /v1/segments/{segmentCode}
Using these endpoints requires changes in the security conguration. If you have insufficient rights, a 403 will be returned by the webservices.

 Note Be aware that additional checks can be performed apart from the general rules. For example, queries for the query/ endpoint usually performs checks on the catalogs as well as veries if the query returns or updates catalog-related items.

This security check is enforced by spring security conguration located in /personalizationwebservices/web/webroot/WEB-INF/config/security-spring.xml. You can overwrite the security-spring.xml le by using the personalizationwebservices.security.config property pointing to a different spring security conguration le.

Base Site Support The baseSiteHeaderFilter was added after the restSessionFilter and before the catalogVersionFilter. For every request to personalizationwebservices, the baseSiteHeaderFilter reads the header containing basesite and if the value is present, it sets the value as a current base site in the session.

This is   For more    the SAP Help  54 Overriding spring-security.xml File The personalizationwebservices extension allows overwriting its default spring-security.xml le with a custom one. The le should be placed in the resources folder of your extension. To specify the le path, you should use personalizationwebservices.security.spring property as presented below:
personalizationwebservices.security.spring=classpath:/myextension/custom-spring-security.xml Cross-Origin Resource Sharing The CORS mechanism denes a way for a browser and a server to decide which cross-origin requests to allow for restricted resources. Personalization Web Services use standard SAP Commerce sharing mechanism, which allows to congure CORS attributes as project properties or dene it in Backoffice application. Congure sample values in the personalizationwebservices/project.properties le:
corsfilter.personalizationwebservices.allowedOrigins=http://localhost:4200 https://localhost:4200 corsfilter.personalizationwebservices.allowedMethods=GET corsfilter.personalizationwebservices.allowedHeaders=origin content-type accept authorization You can override this conguration using Backoffice settings. To do so, select System CORS Filter CorsCongurationProperty . For more details, see: Cross-Origin Resource Sharing Support.

## Personalizationwebservices Endpoints

| List of personalizationwebservices Endpoints URL                              | Method Description                                                                                                     | Catalog Supports                 | Paginated Remarks   |     |                                                                                                            |                                               |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|----------------------------------|---------------------|-----|------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| aware                                                                         | Fields Parameter                                                                                                       |                                  |                     |     |                                                                                                            |                                               |
| /customizations                                                               | GET                                                                                                                    | returns all customizations yes   | yes                 | yes | for supported query parameters see the Parameters supported by the /customizations endpoint section below. |                                               |
| /customizations                                                               | POST                                                                                                                   | creates customization            | yes                 |     |                                                                                                            |                                               |
| /customizations/{customizationID}                                             | GET                                                                                                                    | returns customization            | yes                 | yes |                                                                                                            |                                               |
| with given id                                                                 |                                                                                                                        |                                  |                     |     |                                                                                                            |                                               |
| /customizations/{customizationID}                                             | PUT                                                                                                                    | updates customization            | yes                 |     |                                                                                                            |                                               |
| with given id                                                                 |                                                                                                                        |                                  |                     |     |                                                                                                            |                                               |
| /customizations/{customizationID}                                             | DELETE deletes customization with given id (also deletes all variations and actions related to this customization) yes |                                  |                     |     |                                                                                                            |                                               |
| /customizations/{customizationID}/variations                                  | GET                                                                                                                    | returns all variations for       | yes                 | yes |                                                                                                            |                                               |
| this customization                                                            |                                                                                                                        |                                  |                     |     |                                                                                                            |                                               |
| /customizations/{customizationID}/variations                                  | POST                                                                                                                   | creates variation within         | yes                 |     |                                                                                                            |                                               |
| this customization                                                            |                                                                                                                        |                                  |                     |     |                                                                                                            |                                               |
| /customizations/{customizationID}/variations/{variationId}                    | GET                                                                                                                    | returns variation with           | yes                 | yes |                                                                                                            |                                               |
| given id from this customization                                              |                                                                                                                        |                                  |                     |     |                                                                                                            |                                               |
| /customizations/{customizationID}/variations/{variationId}                    | PUT                                                                                                                    | updates variation with           | yes                 |     |                                                                                                            |                                               |
| given id from this customization                                              |                                                                                                                        |                                  |                     |     |                                                                                                            |                                               |
| /customizations/{customizationID}/variations/{variationId}                    | DELETE deletes variation with given id (also deletes all actions related to this variation)                            | yes                              |                     |     |                                                                                                            |                                               |
| /customizations/{customizationID}/variations/{variationId}/actions            | GET                                                                                                                    | returns all actions within       | yes                 | yes |                                                                                                            |                                               |
| this variation                                                                |                                                                                                                        |                                  |                     |     |                                                                                                            |                                               |
| /customizations/{customizationID}/variations/{variationId}/actions            | POST                                                                                                                   | creates action within this       | yes                 |     |                                                                                                            |                                               |
| variation                                                                     |                                                                                                                        |                                  |                     |     |                                                                                                            |                                               |
| /customizations/{customizationID}/variations/{variationId}/actions/{actionId} | GET                                                                                                                    | returns action with given        | yes                 | yes |                                                                                                            |                                               |
| id                                                                            |                                                                                                                        |                                  |                     |     |                                                                                                            |                                               |
| /customizations/{customizationID}/variations/{variationId}/actions/{actionId} | PUT                                                                                                                    | updates action with given yes id |                     |     |                                                                                                            |                                               |
| /customizations/{customizationID}/variations/{variationId}/actions/{actionId} | DELETE deletes action with given                                                                                       | yes                              |                     |     |                                                                                                            |                                               |
| id                                                                            |                                                                                                                        |                                  |                     |     |                                                                                                            |                                               |
| /actions                                                                      | GET                                                                                                                    | gets actions from                | yes                 | yes | yes                                                                                                        | currently, the type parameter is required and |
| multiple                                                                      | the only supported value is CXCMSACTION                                                                                |                                  |                     |     |                                                                                                            |                                               |
| customizations/variations                                                     |                                                                                                                        |                                  |                     |     |                                                                                                            |                                               |
| /customizations/{customizationID}/variations/{variationId}/triggers           | GET                                                                                                                    | returns all segment              | yes                 | yes |                                                                                                            |                                               |
| triggers for given variation                                                  |                                                                                                                        |                                  |                     |     |                                                                                                            |                                               |

This is   For more    the SAP Help  55

| 7/12/2024 URL                                                                                                  | Method Description                                                                  | Catalog Supports              | Paginated Remarks                           |                                        |     |                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------|---------------------------------------------|----------------------------------------|-----|-------------------------------------------|
| aware                                                                                                          | Fields Parameter                                                                    |                               |                                             |                                        |     |                                           |
| /customizations/{customizationID}/variations/{variationId}/triggers                                            | POST                                                                                | creates new segment           | yes                                         | currently only one from the following: |     |                                           |
| trigger for given variation                                                                                    | segmentTrigger/expressionTrigger/defaultTrigger can be related to a given variation |                               |                                             |                                        |     |                                           |
| /customizations/{customizationID}/variations/{variationId}/triggers/{triggerId} GET                            | gets segment trigger with                                                           | yes                           | yes                                         |                                        |     |                                           |
| given id                                                                                                       |                                                                                     |                               |                                             |                                        |     |                                           |
| /customizations/{customizationID}/variations/{variationId}/triggers/{triggerId} PUT                            | updates segment trigger                                                             | yes                           |                                             |                                        |     |                                           |
| with given id                                                                                                  |                                                                                     |                               |                                             |                                        |     |                                           |
| /customizations/{customizationID}/variations/{variationId}/triggers/{triggerId} DELETE removes segment trigger | yes                                                                                 |                               |                                             |                                        |     |                                           |
| with given id                                                                                                  |                                                                                     |                               |                                             |                                        |     |                                           |
| /segments                                                                                                      | GET                                                                                 | returns all segments          | no                                          | yes                                    | yes | supported query parameters: code          |
| /segments                                                                                                      | POST                                                                                | creates segment               | no                                          |                                        |     |                                           |
| /segments/{segmentId}                                                                                          | GET                                                                                 | returns segment with          | no                                          | yes                                    |     |                                           |
| given id                                                                                                       |                                                                                     |                               |                                             |                                        |     |                                           |
| /segments/{segmentId}                                                                                          | PUT                                                                                 | updates segment               | no                                          |                                        |     |                                           |
| /segments/{segmentId}                                                                                          | DELETE removes segment                                                              | no                            |                                             |                                        |     |                                           |
| /customersegmentations                                                                                         | GET                                                                                 | returns relations between     | no                                          | yes                                    | yes | at least one query parameter is required: |
| customer and segment                                                                                           | customerId - uid of customer segmentId - code of segment                            |                               |                                             |                                        |     |                                           |
| /customersegmentations                                                                                         | POST                                                                                | creates relation between      | no                                          |                                        |     |                                           |
| customer and segment                                                                                           |                                                                                     |                               |                                             |                                        |     |                                           |
| /customersegmentations/{customersegmentationId}                                                                | GET                                                                                 | returns relation with given   | yes                                         |                                        |     |                                           |
| id                                                                                                             |                                                                                     |                               |                                             |                                        |     |                                           |
| /customersegmentations/{customersegmentationId}                                                                | PUT                                                                                 | updates relation with         | no                                          |                                        |     |                                           |
| given id                                                                                                       |                                                                                     |                               |                                             |                                        |     |                                           |
| /customersegmentations/{customersegmentationId}                                                                | DELETE removes relation with                                                        | no                            |                                             |                                        |     |                                           |
| given id                                                                                                       |                                                                                     |                               |                                             |                                        |     |                                           |
| /query/{queryId}                                                                                               | POST                                                                                | executes query with given (?) | this is very generic endpoint for executing |                                        |     |                                           |
| id                                                                                                             | extension specic queries (e.g. cms)                                                 |                               |                                             |                                        |     |                                           |
| Parameters Supported by the /customizations Endpoint                                                           |                                                                                     |                               |                                             |                                        |     |                                           |

The following parameters are supported by the /customizations endpoint returning all customizations.

Required parameters means that the parameters necessary for the query parameter to work properly.

Works with parameters means that the query parameter can work together only with the listed ones. "-" means that the query parameter cannot be used together with other

parameters.

Required extension means that the extension that needs to be in use for the parameter to work.

| Required extension means that the extension that needs to be in use for the parameter to work.   |                                                                                                                                                                                                                                                             |                    |                                           |                             |                         |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------|-----------------------------|-------------------------|
| Query parameter                                                                                  | Description                                                                                                                                                                                                                                                 | Values             | Required parameters Works with parameters | Required extension          |                         |
| code                                                                                             | lters response by code of the customization                                                                                                                                                                                                                 | string             | -                                         | -                           | personalizationservices |
| statuses                                                                                         | lters response by status of the customization, a                                                                                                                                                                                                            | ENABLED, DISABLED, | -                                         | name, pageId                | personalizationservices |
| comma-seperated list                                                                             | DELETED                                                                                                                                                                                                                                                     |                    |                                           |                             |                         |
| name                                                                                             | lters the response by the name of customization                                                                                                                                                                                                             | string             | statuses                                  | -                           | personalizationservices |
| catalogs                                                                                         | lters response by catalog of the customization, CURRENT by default. PARENTS display customizations from parent catalogs of specied catalog. ALL displays customizations from CURRENT and PARENTS. PARENTS and ALL have meaning only in multi-country setup. | CURRENT, PARENTS,  | -                                         | All                         | personalizationcms      |
| ALL                                                                                              |                                                                                                                                                                                                                                                             |                    |                                           |                             |                         |
| pageId                                                                                           | lters response by customization that have                                                                                                                                                                                                                   | string             | statuses                                  | pageCatalogId, negatePageId | personalizationcms      |
| actions affecting the page                                                                       |                                                                                                                                                                                                                                                             |                    |                                           |                             |                         |
| pageCatalogId                                                                                    | denes catalog for page dened by pageId.                                                                                                                                                                                                                     | string             | pageId                                    | -                           | personalizationcms      |
| negatePageId                                                                                     | if set to true will search for customizations not                                                                                                                                                                                                           | true, false        | pageId                                    | -                           | personalizationcms      |
| affecting the page                                                                               |                                                                                                                                                                                                                                                             |                    |                                           |                             |                         |

Catalog Aware Endpoints

## Note

The endpoints marked as catalog aware have the /catalogs/{catalogId}/catalogVersions/{catalogVersion} prex in their path. This means that a request on /customizations should really be made on /catalogs/{catalogId}/catalogVersions/{catalogVersion}/customizations. This was removed from the table above to make it clearer.

The catalog aware functionality is handled by de.hybris.platform.webservicescommons.filter.CatalogVersionFilter declared in
/personalizationwebservices/web/webroot/WEB-INF/personalizationwebservices-web-spring.xml le. For details on the CatalogVersionFilter see: Common Filters and Controllers.

Fields Parameter All GET methods support elds query parameter which allows dening which elds of the requested object should be included in the response. The format of this parameter is described in more details in: Fields Conguration Format. The elds are supported by aspect fieldsetAspect declared in the /personalizationwebservices/web/webroot/WEBINF/springmvc-servlet.xml le.

... 

 <aop:aspectj-autoproxy /> <bean id="aopFieldsetConverter" class="de.hybris.platform.webservicescommons.mapping.aop.FieldsFilter" autowire="constructor"> <property name="disableFullMapping" value="true" /> </bean> 
 <aop:config>
 <aop:aspect id="fieldsetAspect" ref="aopFieldsetConverter">
 <aop:pointcut expression="execution(public * de.hybris.platform.personalizationwebservices.controllers.*.get*(..))" id="fieldsetPointcut
 <aop:around method="filterFields" pointcut-ref="fieldsetPointcut"/>
 </aop:aspect>
 </aop:config>
...

Response Pagination If the endpoint supports pagination, it accepts two additional parameters in the query:
pageSize: number of items on the returned page currentPage: number of the current page to return (starting from 0)
Actions Endpoint Actions can be accessed using two different endpoints:
/customizations/{customizationID}/variations/{variationId}/actions: dedicated for manipulating actions (create / update / delete). Queries are restricted to actions in a given customization/variation and supported query parameters are limited.

/actions: this endpoint supports the GET operation only, and returns a list of actions from multiple customizations or variations.

Action endpoints use dynamic response type mechanism to return data from specic action subclass. For details, see Dynamic Response Types in Web Services. For details on extending the action endpoint, see Create a Personalization Action, for details on extending action queries, see Data Filtering in personalizationservices Extension.

Trigger Endpoint The Trigger endpoint uses the dynamic response type mechanism to return data from a specic abstractTrigger subclass. For details on the mechanism, see also: Dynamic Response Types in Web Services. By default the system provides the following trigger types:
segmentTrigger, providing a simple way of triggering variation using a list of segments joined by logical operators AND or OR. A sample body in JSON format looks as follows:
{
 "type": "segmentTriggerData",
 "code": "trigger1",
 "groupBy": "AND",
 "segments": [
 {
 "code": "Men"
 },
 {
 "code": "VIPBronze" } ] }
expressionTrigger, providing support for complex logical expressions containing AND / OR / NOT operations on segments. A sample body in JSON format looks as follows:
{
 "type": "expressionTriggerData",
 "code":"exTrigger1",
 "expression": {"type":"groupExpressionData", "operator":"OR", "elements":[
 {"type":"segmentExpressionData", "code":"Men"},
 {"type":"groupExpressionData", "operator":"AND", "elements":[
 {"type":"segmentExpressionData", "code":"Women"},
 {"type":"negationExpressionData", "element":
 {"type":"segmentExpressionData", "code":"HatsFan"} } ]}

 ]}
}
 Note Only one segmentTrigger or expressionTrigger can be related to single variation. Attempt to create next one results in an error.

For more information on triggers, see: Variation Triggers.

Query Endpoint A query endpoint is a generic endpoint, which executes the logic from a bean with given ID. The bean implements the de.hybris.platform.personalizationwebservices.queries.RestQueryExecutor interface in order to be visible in the Query endpoint. Any extension may declare such a bean to extend the functionality available through this endpoint. The main purpose for adding such beans is to enable access to functionality specic for a given subtype of CxAbstractAction through web services.

For example, the CxCmsAction denes the CmsComponent, which should be displayed by the CxCmsContainer. To learn which CMS components are affected by a given variation, you need logic aware of CxCmsContainer. Such custom logic is specic for the personalizationcmsweb extension and cannot be placed in personalizationwebservices. When implementing your own RestQuery, you need the following methods from the RestQueryExecutorInterface:
Object execute(Map<String, String> params): this is where the logic of your query goes. For example, execute a exissearch, update and save the data model.

List<CatalogVersionWsDTO> getCatalogsForWriteAccess(final Map<String, String> params): this is where you declare which catalogs will be used to write data.

This is important if you want permissions check for your query.

List<CatalogVersionWsDTO> getCatalogsForReadAccess(final Map<String, String> params): this where you declare which catalogs will be used to read data from. This is important if you want permissions check for your query.

The query endpoint accepts a single parameter of de.hybris.platform.personalizationwebservices.data.QueryParamsWsDTO type, which consists of a single string - string map. The queryId is the name of bean which should be executed with given parameters. The bean can do anything it wants and should return an object representing rest response. It may be anything from a simple WsDTO object up to a ResponseEntity. For example, in the cxcmsweb extension you may dene the cxcmscomponentsfromvariations bean.

<bean id="cxcmscomponentsfromvariations" class="de.hybris.platform.personalizationcmsweb.queries.CmsComponentsQueryExecutor" parent="abstractFlexibl de.hybris.platform.personalizationcmsweb.queries.CmsComponentsQueryExecutor implements de.hybris.platform.personalizationwebservices.queries.RestQueryExecutor and executes exible search to extract information about the components affected by given variations. Such data would be unavailable in any other way trough personalization API. For details see the Queries section in personalizationcmsweb Extension.

## Personalizationwebservices Api Reference

For the API Reference for the personalizationwebservices extension, see API Documentation and YAML Files.

## Previewpersonalizationweb Extension

The previewpersonalizationwebextension extends the previewwebservices extension in the personalization context. It implements populators that deal with the extended preview ticket data model.

Extended Preview Ticket Data Model The personalizationcms extension adds variations list to the existing PreviewTicketDataModel. A CMSSiteFilter is then applied to the extended data model to achieve a storefront rendered properly in the personalization context (meaning for the provided variations).

Populating the Extended Data Model The existing previewwebservices populators handle the basic preview ticket data model. However, the data model already extended to support the variations or segments needs some additional populators. The previewpersonalizationweb extension implements two populators:
PersonalizationPreviewTicketPopulator, which retrieves segment codes from the PreviewTicketData model and puts it into a PreviewTicketWSDTO. The variation codes are wrapped along with the customization codes in the CxVariationKey.

PersonalizationPreviewTicketPopulator public class PersonalizationPreviewTicketPopulator implements Populator<CMSPreviewTicketModel, PreviewTicketWsDTO>
{
//...

 @Override public void populate(final CMSPreviewTicketModel source, final PreviewTicketWsDTO target) throws ConversionException
 {
 Assert.notNull(source, "Parameter source cannot be null.");
 Assert.notNull(target, "Parameter target cannot be null."); localViewExecutor.executeWithAllCatalogs(() -> { final PreviewDataModel previewData = source.getPreviewData(); if (previewData != null)
This is   For more    the SAP Help  58
 {
 target.setVariations(ConversionUtils.convert(source.getPreviewData().getVariations(), v -> createKey(v)));
 target.setSegments(ConversionUtils.convert(source.getPreviewData().getSegments(), s -> s.getCode()));
 }
 return null;
 });
 } protected CxVariationKey createKey(final CxVariationModel variation)
 {
 final CxVariationKey key = new CxVariationKey(); key.setVariationCode(variation.getCode()); key.setCustomizationCode(variation.getCustomization().getCode()); return key;
 } //...

}
PersonalizationPreviewTicketReversePopulator, which retrieves a list of variation codes along with the variation list wrapped into CxVariationKey and, with the use of CxVariationService provided by the personalizationservices extension, gets lists of CxSegmentModel and CxVariationModel and puts them in the PreviewTicketDataModel.

If the cxVariationService cannot nd variation for any of codes, it throws the ConversionException. The message contains a list of codes that has not been found by the cxVariationService.

public class PersonalizationPreviewTicketReversePopulator implements Populator<PreviewTicketWsDTO, PreviewDataModel>
{ //... @Override public void populate(final PreviewTicketWsDTO source, final PreviewDataModel target) throws ConversionException { Assert.notNull(source, "Parameter source cannot be null."); Assert.notNull(target, "Parameter target cannot be null."); localViewExecutor.executeWithAllCatalogs(() -> {
 setVariations(source, target);
 setSegments(source, target);
 return null;
 });
 }
 protected void setVariations(final PreviewTicketWsDTO source, final PreviewDataModel target)
 {
 if (CollectionUtils.isEmpty(source.getVariations()))
 { target.setVariations(null); } else { final CatalogVersionModel catalogVersion = catalogVersionService.getCatalogVersion(source.getCatalog(),
 source.getCatalogVersion()); final Collection<CxVariationModel> existingVariations = cxVariationService.getVariations(source.getVariations(),
 catalogVersion);
 validateVariations(source.getVariations(), existingVariations);
 target.setVariations(existingVariations);
 }
 } protected void setSegments(final PreviewTicketWsDTO source, final PreviewDataModel target)
 { if (CollectionUtils.isEmpty(source.getSegments())) { target.setSegments(null); } else
 {
 final Collection<CxSegmentModel> existingSegments = cxSegmentService.getSegmentsForCodes(source.getSegments());
 validateSegments(source.getSegments(), existingSegments);
 target.setSegments(existingSegments);
 }
 } public void validateVariations(final Collection<CxVariationKey> inputVariationCodes, final Collection<CxVariationModel> existingVariations)
 { if (CollectionUtils.isEmpty(existingVariations)) {
This is   For more    the SAP Help  59 throw new ConversionException( String.format("No variations found for provided list of codes (%s)", createErrorMessageForVariationKeys(inputVariationCodes)));
 } if (inputVariationCodes.size() != existingVariations.size())
 {
 final Collection<CxVariationKey> existingVariationKeys = existingVariations.stream().map(this::createKey) .collect(Collectors.toSet()); final Collection<CxVariationKey> wrongVariationCodes = inputVariationCodes.stream() .filter(code -> !existingVariationKeys.contains(code)).collect(Collectors.toSet()); throw new ConversionException( String.format("No variations found for provided list of codes (%s)", createErrorMessageForVariationKeys(wrongVariationCodes)));
 }
 } public void validateSegments(final Collection<String> inputSegmentsCode, final Collection<CxSegmentModel> existingSegments)
 { if (CollectionUtils.isEmpty(existingSegments))
 {
 throw new ConversionException( String.format("No segments found for provided list of codes (%s)", createErrorMessageForCodes(inputSegmentsCode)));
 } if (inputSegmentsCode.size() != existingSegments.size()) { final Collection<String> existingSegmentCodes = existingSegments.stream().map(s -> s.getCode()) .collect(Collectors.toSet());
 final Collection<String> wrongSegmentCodes = inputSegmentsCode.stream()
 .filter(code -> !existingSegmentCodes.contains(code)).collect(Collectors.toSet()); throw new ConversionException( String.format("No segments found for provided list of codes (%s)", createErrorMessageForCodes(wrongSegmentCodes)));
 }
 }
 protected CxVariationKey createKey(final CxVariationModel variation)
 {
 final CxVariationKey key = new CxVariationKey();
 key.setVariationCode(variation.getCode()); key.setCustomizationCode(variation.getCustomization().getCode()); return key; } protected String createErrorMessageForVariationKeys(final Collection<CxVariationKey> keys)
 {
 return keys.stream().map(k -> "[" + k.getCustomizationCode() + " , " + k.getVariationCode() + "]")
 .collect(Collectors.joining(","));
 } protected String createErrorMessageForCodes(final Collection<String> codes)
 {
 return codes.stream().map(c -> "[" + c + "]").collect(Collectors.joining(","));
 }
Both newly created populators are added to proper converters dened in the previewwebservices extension with the use of the modifyPopulatorList method. The conguration is located under: previewpersonalizationweb/resources/previewpersonalizationweb-spring.xml.

<bean id="personalizationPreviewTicketPopulator" class="de.hybris.platform.previewpersonalizationweb.populator.PersonalizationPreviewTicketPopulator
 <property name="localViewExecutor" ref="localViewExecutor" />
</bean> <bean parent="modifyPopulatorList"> <property name="list" ref="previewTicketConverter"/>
 <property name="add" ref="personalizationPreviewTicketPopulator"/>
</bean> <bean id="personalizationPreviewTicketReversePopulator" class="de.hybris.platform.previewpersonalizationweb.populator.PersonalizationPreviewTicketRe <property name="cxVariationService" ref="cxVariationService" />
 <property name="catalogVersionService" ref="catalogVersionService" />
 <property name="localViewExecutor" ref="localViewExecutor" /> <property name="cxSegmentService" ref="cxSegmentService" />
</bean> <bean parent="modifyPopulatorList">
 <property name="list" ref="previewTicketReverseConverter"/> <property name="add" ref="personalizationPreviewTicketReversePopulator"/>
</bean>
Extending Field Level Mapping Denition
//... }

DEFAULT and FULL elds level denition has to be extended with variation and segment list to be visible in the response without explicit denition as a request parameter. Because the level mappings for a specic class dened in spring context are merged, all you needed to do is add the required elds in your <eldset> denition (variations and segment lists in this case). You can nd the conguration under: resources/config/previewPersonalizationweb-field-mapping-spring.xml.

<bean parent="fieldSetLevelMapping" id="personalizationPreviewTicketWsDTOFieldSetLevelMapping"> <property name="dtoClass" value="de.hybris.platform.previewwebservices.dto.PreviewTicketWsDTO"/> <property name="levelMapping"> <map> <entry key="DEFAULT"
 value="variations, segments"/>
 <entry key="FULL"
 value="variations, segments"/>
 </map>
 </property>
</bean>

## Personalization Module Implementation

Use and extend the personalization features by adding your own congurations and settings. Integrate personalization with external systems to easily obtain and process data.

Personalization Calculation Process Personalization is calculated depending on the conguration dened for a base site. The default conguration for sample data (electronics, apparel-uk, apparel-de) starts the synchronous calculation and asynchronous process after the user logs in.

Multi-Country Site Support Personalization supports the multicountry setup, and can be congured to behave in a certain way when multicountry settings are enabled.

Install Personalization You can install Personalization using dedicated recipes or manually by adding a set of extensions. Congure Personalization The Backoffice Administration Cockpit provides you with an intuitive user interface, which helps you to easily manage the segments, variations and customizations within a personalization conguration. Extend Personalization The guides provide you with information on how you can extend personalization to fully use its features.

Data Annotation and Retention in Personalization Personalization segment data, when perceived as sensitive, should be included in the audit report and removed once the customer decides to close the account. Consent Templates in Personalization The consent templates used in Personalization ensure that the customer gives consent to user data processing Personalization Core Trails Personalization trails help you to get to know the functionality in details and to create your own solutions.

## Personalization Calculation Process

Personalization is calculated depending on the conguration dened for a base site. The default conguration for sample data (electronics, apparel-uk, apparel-de) starts the synchronous calculation and asynchronous process after the user logs in. The general calculation ow is as follows:
1. The congured triggers are evaluated and return active variations.

2. A subprocess for variations begins. It includes the following steps:
a. Variations are grouped based on their customization. b. Variations are then ltered out based on the one variation active per customization rule.

c. Variations are sorted based on their group priority.

3. The actions linked to the variations are retrieved.

4. The actions are executed (and generate instances of the CxAbstractActionResult class).

5. The potential results are stored in the session for the current user. 6. The personalized output is displayed to the user.

Below you can nd a detailed diagram of the customization calculation process:
 Tip For a larger image, open the gure in a separate tab.

![61_image_0.png](61_image_0.png)

![61_image_1.png](61_image_1.png)

Calculation Actions and Conguration You can dene the calculation process and schedule when it is called.

Model-based Personalization Parameters The model-based personalization conguration is dened in the personalizationservices extension.

Asynchronous Process The CxService service provides a method called startPersonalizationCalculationProcess. Out of the box, this method starts a new process to update the user segments and calculate the experience in an asynchronous way. Voters The voter mechanism allows determining when and how the recalculation is triggered. The logic of handling votes is in the CxPersonalizationFilter.

Storing Personalization Calculation Results The CxService provides the calculateAndStorePersonalization method, which in its default implementation stores the results in the database.

Congure Calculation Time Header and Cookie Name Congure custom Calculation Time header and cookie names by setting respective properties.

## Calculation Actions And Conguration

You can dene the calculation process and schedule when it is called. The way of calculating personalization is crucial, because executing calculations per each user for each request may lead to performance issues. Performing the recalculation not often enough does not ensure relevant customer experience.

Calculation Actions The following recalculation actions are dened in the RecalculateAction enum:
RECALCULATE: recalculates customization results and stores them in the session. UPDATE: updates information about the user segments.

ASYNC_PROCESS: starts an asynchronous process to update user segments and calculate customization results to be stored in the database. For more information on the process, see Asynchronous Process. LOAD: loads customization results stored in database as a result of asynchronous calculation process.

Calculation Conguration The CxConfigurationModel stores the conguration in the database. You can apply such a conguration to one or many base sites. If a current base site does not have conguration dened, the default values are used. For settings conguration, see Set Up a Personalization Conguration. The CxConfigurationModel contains:
This is   For more    the SAP Help  62

| 7/12/2024 Element           | Description                                                                                                                                                                                                |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| userChangedActions          | Denes what set of RecalculateAction should be executed when the user changes in session. These actions are executed after user the logs in. A user changed event is handled by CxAfterUserChangedListener. |
| anonymousUserDefaultActions | A set of actions executed only once when a session is created. It is handled by the NewSessionVoter.                                                                                                       |
| urlVoterConfigurations      | A list of CxUrlVoterConfigModel. This conguration is used by ConfigurableUrlVoter.                                                                                                                         |
| periodicVoterConfigs        | A list of CxPeriodicVoterConfigModel, which describes actions executed periodically (for example after 3 requests or after 20 seconds). This conguration is used by the PeriodicVoter.                     |

Use the following properties to add default values for base sites without congurations:
dening which actions are called on user changed event. Use the personalizationservices.after.user.changed.actions property to dene which actions should be called.

personalizationservices.after.user.changed.actions=RECALCULATE,ASYNC_PROCESS
actions called on storefront page requests. Example conguration:
personalizationservices.calculate.default.load.url=.*
personalizationservices.calculate.default.load.actions=LOAD
 Note This conguration is deprecated and support for it will be removed in the future. Instead, use the conguration stored in database (CxConfigModel).

## Model-Based Personalization Parameters

The model-based personalization conguration is dened in the personalizationservices extension.

 Note Use the Backoffice Administration Cockpit to dene your personalization conguration. For details, see Congure Personalization, and treat this additional information about the parameters as the fallback mechanism.

The conguration consists of the following elements:
CxConfig: the main class of personalization conguration. Thanks to the implemented one-to-many optional relation to the basesite, the conguration is basesite-aware. It allows setting one conguration for many sites. The following table lists the personalization parameters available in the Backoffice Administration Cockpit, along with their description. The Property in project.properties column lists the corresponding properties that can be dened in the project.properties le, if there is no conguration set in the Backoffice Administration Cockpit.

| Parameter Name                                                                                                                                                                                                      | Mandatory/Optional                                                  | Description                                                                                                                     | Property in project.properties                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| minAffinity                                                                                                                                                                                                         | Mandatory                                                           | A minimum affinity for the userto-segment relation. Default                                                                                                                                 | personalizationservices.segment.trigger.strategy.min.affinity |
| value: BigDecimal.valueOf(0.5)                                                                                                                                                                                      |                                                                     |                                                                                                                                 |                                                               |
| actionResultMaxRepeat                                                                                                                                                                                               | Mandatory                                                           | A number of retries in case of action result load error caused by optimistic locking failure. Default value: Integer.valueOf(1) | personalizationservices.actionResult.load.repeat.max          |
| userChangedActions                                                                                                                                                                                                  | Optional                                                            | A set of actions to be called after personalizationservices.after.user.changed.actions a user changed event takes place.        |                                                               |
| a list of CxUrlVoterConfig (a one-tomany relation to CxConfig)                                                                                                                                                                                                                     | Optional. The optional ag                                           | A list of url voter congs for                                                                                                   | N/A                                                           |
| settled for CxConfig part of                                                                                                                                                                                        | CxConfig                                                            |                                                                                                                                 |                                                               |
| relation makes it optional.                                                                                                                                                                                         |                                                                     |                                                                                                                                 |                                                               |
| calculationProcess                                                                                                                                                                                                  | Mandatory                                                           | The name of the calculation                                                                                                     | personalizationservices.calculation.process                   |
| process used.                                                                                                                                                                                                       |                                                                     |                                                                                                                                 |                                                               |
| catalogLookup                                                                                                                                                                                                       | Optional                                                            | The type of strategy used for                                                                                                   | personalizationservices.calculate.catalogLookup               |
| multicountry conguration.                                                                                                                                                                                           |                                                                     |                                                                                                                                 |                                                               |
| a list of ConsentTemplate objects (a                                                                                                                                                                                | Optional                                                            | ConsentTemplates end-user                                                                                                       |                                                               |
| one-to-many relation to CxConfig)                                                                                                                                                                                   | needs to accept to receive personalized content based on user data. | N/A                                                                                                                             |                                                               |
|  Note Pay attention to the type of consent template you add for personalization. Anonymous users can see only the consent templates marked as exposed, and the system veries only such templates for user consent. |                                                                     |                                                                                                                                 |                                                               |

| Parameter Name             | Mandatory/Optional   | Description                                                                                                                                         | Property in project.properties   |
|----------------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| userSegmentsStoreInSession | Optional             | Denes if segments for registered user should be stored in session and saved to database after session ends. The default value is: Boolean.FALSE N/A |                                  |

 Note For the list of parameters you can dene for the anonymous user see the anonymous voter section in Voters.

CxUrlVoterConfig: A ConfigurableUrlVoter conguration which contains the following parameters:

| Parameter Name                    | Mandatory/Optional   | Description                       | Property Equivalent                                  |
|-----------------------------------|----------------------|-----------------------------------|------------------------------------------------------|
| urlRegexp                         | Mandatory            | A url regular expression          | personalizationservices.calculate.<configId>.url     |
| actions                           | Mandatory            | A set of string representation of | personalizationservices.calculate.<configId>.actions |
| the RecalculateAction enum values |                      |                                   |                                                      |

## Asynchronous Process

The CxService service provides a method called startPersonalizationCalculationProcess. Out of the box, this method starts a new process to update the user segments and calculate the experience in an asynchronous way.

The conguration is dened for each base site. You can easily view and recongure it using the Backoffice Administration Cockpit. For details, see Set Up a Personalization Conguration.

## Note

If no conguration was dened for a particular base site, the process denition can be congured in the personalizationservices.calculation.process property. If you need to extend the personalization calculation process, you can write your own process denition and redene this property. By default the process is dened in the defaultPersonalizationCalculationProcess.xml le. This denition only denes the following steps:
updateUserSegments: responsible for updating which segments the user belongs to. calculateAndStorePersonalizationForUser: used to calculate customization variations for user and store them on the same user.

Using the process engine to update the user personalization gives you the following advantages:
It does not block the calls, so the user experience in the Accelerator is not affected.

It monitors various processes through the tools for the process engine.

It is easily scalable and allows you to run the process engine on different nodes.

 Note Using the ASYNC_PROCESS may cause some delay in removing the personalization results, when an anonymous user withdraws consent for personalization by manually removing the cookie.

 Caution The duration of the asynchronous process strongly depends on how the process engine and Task Service are congured. For example, the task.polling.interval.min and task.polling.interval properties affect the delay in the processing of actions. For more details on setting these properties, see Task Service Properties. For more details on the process engine, see The SAP Commerce Cloud processengine.

Cleaning Old Processes Asynchronous experience recalculation is using the process engine. Each recalculation is creating a new business process that is being stored in the database and not removed. To solve this problem with stacking enormous number of processes, we have come up with an implementation that is using the existing Maintenance Framework mechanism. For more information, see Creating Strategy to Process Instances and The Cronjob Service.

CxPersonalizationProcessCleanupCronJob The default CxPersonalizationProcessCleanupCronJob is created during the init/update process. The script with the default denition is located in personalizationservices/resources/impex/essentialdata_personalizationservices.impex.

INSERT_UPDATE CxPersonalizationProcessCleanupCronJob; code[unique=true];job(code);singleExecutable;sessionLanguage(isocode);maxProcessAge;processSta ;cleanupCxPersonalizationProcessesCronJob;cleanupCxPersonalizationProcessJobsPerformable;false;de;120;SUCCEEDED,FAILED,ERROR
Use Backoffice Administration Cockpit to congure or create a new job.

 Note Only users with administrator rights can create or edit the cron job.

CxPersonalizationProcessCleanupCronJob is dened in the personalizationservices-items.xml le. There are two attributes dening which processes should be removed:
This is   For more    the SAP Help  64 maxProcessAge: Removing processes older than a specied number of minutes.

processStates: Removing processes states that are taken into account during the cleanup process. Values which can be used are dened by ProcessState enum: CREATED, RUNNING, WAITING, SUCCEEDED, FAILED, ERROR
Trigger The default trigger for cleanupCxPersonalizationProcessesCronJob is set for every 30 minutes. The script with the default denition is located in personalizationservices/resources/impex/essentialdata_personalizationservices.impex.

INSERT_UPDATE Trigger; cronJob(code)[unique = true] ; second; minute; hour; day; month; year; relative; active; maxAcceptableDelay
\# Run the cleanupCxPersonalizationProcessesCronJob every 30 minutes
; cleanupCxPersonalizationProcessesCronJob ; 0 ; 30 ; -1 ; -1 ; -1 ; -1 ; true ; true ; -1 Use Backoffice Administration Cockpit to congure or create a new trigger for a job.

 Note Only users with administrator rights can create or edit the cron job.

CxPersonalizationProcessCleanupStrategy CxPersonalizationProcessCleanupStrategy nds processes based on the given parameters and removes them. Processes are cleanup in bundles (batches). Batch size is congured by setting personalizationservices.calculation.process.cleanup.pageSize property in local.properties le. Default value is 1000.

... <bean id="cleanupCxPersonalizationProcessJobsPerformable" parent="abstractGenericMaintenanceJobPerformable"> <property name="pageSize" value="\#{configurationService.configuration.getProperty('personalizationservices.calculation.process.cleanup.pageSize')}"/
<property name="maintenanceCleanupStrategy" ref="cxPersonalizationProcessCleanupStrategy"/>
 </bean> <alias name="defaultcxPersonalizationProcessCleanupStrategy" alias="cxPersonalizationProcessCleanupStrategy"/>
 <bean id="defaultcxPersonalizationProcessCleanupStrategy" class="de.hybris.platform.personalizationservices.strategies.impl.CxPersonalizationProce
 <property name="timeService" ref="timeService"/>
 <property name="modelService" ref="modelService"/>
 </bean>
... 

## Voters

The voter mechanism allows determining when and how the recalculation is triggered. The logic of handling votes is in the CxPersonalizationFilter. Voters have access to httpRequest and httpResponse to create a vote. Based on provided input, a voter decides if customer experience recalculation in form of a vote is required or not.

For each vote, you can set the following properties:
recalculateActions: a set of recalculation actions to be executed (the values of RecalculateAction enum). conclusive: a vote is nal, no other vote is taken into account.

The execution of CxPersonalizationFilter results in evaluating voters according to their order. For each voter, a corresponding vote is checked. If a conclusive vote is encountered, the rst vote is the only one considered. If there is no conclusive vote, the actions returned by each voter are merged into one set of actions to execute.

Actions can be ordered in DefaultCxRecalculationService. The default action order is as follows: UPDATE, RECALCULATE, LOAD, ASYNC_PROCESS. The voters are executed one after another depending on the action order.

PreviewVoter A PreviewVoter triggers recalculation if a preview ticket exists. This vote is conclusive by default.

PeriodicVoter A PeriodicVoter triggers the periodic recalculation. The conguration for the PerodicVoter is stored in the database in the CxPeriodicVoterConfigModel. The congurations for base sites are gathered in the periodicVoterConfigs attribute of the CxConfigModel. A single CxPeriodicVoterConfigModel contains the following attributes:
userType: a user type for which the conguration is valid (ALL, REGISTERED, ANONYMOUS). actions: a set of actions to be executed on subsequent requests if userMinRequestNumber and userMinTime conditions are met.

userMinRequestNumber: the minimal number of requests that need to pass between executing actions. userMinTime: minimal time (in milliseconds) that needs to pass between executing actions.

The table shows a sample PeriodicVoter conguration and its meaning:

| userMinRequestNumber                                                                 | userMinTime   | Meaning                                   |
|--------------------------------------------------------------------------------------|---------------|-------------------------------------------|
| 0                                                                                    | 0             | actions will be executed on every request |
| This is custom documentation. For more information, please visit the SAP Help Portal | 65            |                                           |

| 7/12/2024 userMinRequestNumber   | userMinTime   | Meaning                                                                                               |
|----------------------------------|---------------|-------------------------------------------------------------------------------------------------------|
| 1                                | 0             | actions will be executed on every request                                                             |
| 0                                | 1             | actions will be executed on every request if at least 1 ms passed from last execution                 |
| 10                               | 0             | actions will be executed on every tenth request                                                       |
| 0                                | 60000         | actions will be executed if one minute passed from last execution                                     |
| 10                               | 60000         | actions will be executed if one minute passed and there were at least 10 requests from last execution |

## Configurableurlvoter

ConfigurableUrlVoter triggers the recalculation if the request url contains one of congured patterns. It can be congured in the Backoffice Administration Cockpit using the CxUrlVoterConfig model.

You need to dene the following attributes:
userType: user type for which the conguration is valid (ALL, REGISTERED, ANONYMOUS). urlRegexp: regular expression to be evaluated against the HttpServletRequest.getRequestURI.

actions: a set of actions to be executed when the request's url matches the urlRegexp pattern.

If a requested url matches more than one conguration, the actions will be merged. For example, the following url:
https://electronics.local:9002/yacceleratorstorefront/electronics/en/ matches both the following congurations:
userType=ALL
URL regexp=.*
actions=RECALCULATE,LOAD
userType=ALL
URL regexp=electronics/en/$
actions=UPDATE
This is why the action set returned by the ConfigurableUrlVoter includes the following actions: RECALCULATE, LOAD, UPDATE.

UrlVoter(deprecated)
 Note UrlVoter is deprecated. Use the ConfigurableUrlVoter instead.

The UrlVoter triggers recalculation if the request url contains one of congured patterns. The UrlVoter reads conguration from properties of the following format:
personalizationservices.calculate.<configId>.url = <regex_for_url> personalizationservices.calculate.<configId>.actions=<comma_separated_actions>
where:
<regex_for_url>: regexp expression, which will be evaluated against the HttpServletRequest.getRequestURI
<comma_separated_actions>: comma separated values of RecalculateAction enum.

An example:
\#Loading recalculation result on each request personalizationservices.calculate.default.load.url=.*
personalizationservices.calculate.default.load.actions=LOAD \#Synchronous recalculation on homepage request personalizationservices.calculate.homepage.url=electronics/en/$ personalizationservices.calculate.homepage.actions=RECALCULATE
\#Synchronous update user segments and recalculation on checkout personalizationservices.calculate.checkout.url=checkout personalizationservices.calculate.checkout.actions=UPDATE,RECALCULATE \#Starting asynchronous recalculation process personalizationservices.calculate.checkout.url=.*/cart personalizationservices.calculate.checkout.actions=ASYNC_PROCESS
If a requested url matches more than one conguration, the actions will be merged. For example the following url:
https://electronics.local:9002/yacceleratorstorefront/electronics/en/ matches both the following conguration:
personalizationservices.calculate.default.load.url=.* personalizationservices.calculate.default.load.actions=RECALCULATE
and this one:

personalizationservices.calculate.homepage.url=electronics/en/$
personalizationservices.calculate.homepage.actions=ASYNC_PROCESS
That is why the action set returned by the UrlVoter will be RECALCULATE, ASYNC_PROCESS. The value of the property is a normal regexp expression, which is evaluated against HttpServletRequest.getRequestURI.

Custom Voters A custom voter can be created by performing the following actions:
creating class that implements de.hybris.platform.personalizationservices.voters.Voter, dening this class as a bean in Spring context - it is automatically used by CxPersonalizationFilter.

## Storing Personalization Calculation Results

The CxService provides the calculateAndStorePersonalization method, which in its default implementation stores the results in the database.

The method is used in the case of asynchronous calculation of results. Results can be identied by their key, which is generated based on user, catalog version and session information.

Tasks Executed after Closing the Session Once the user session is closed, there might be a need to execute additional tasks, such as cleaning the calculation result. To easily handle this need, we have provided a session close listener.

The listener can schedule a task either for anonymous or registered user. For more details on the task service refer to The Task Service.

You will nd the listener conguration in the personalizationservices-spring.xml le.

...

 <bean id="cxBeforeSessionCloseListener" class="de.hybris.platform.personalizationservices.events.CxBeforeSessionCloseListener" parent="abstractEventListener">
 <property name="taskService" ref="taskService"/>
 <property name="modelService" ref="modelService"/>
 <property name="userService" ref="userService"/>
 <property name="defaultSessionTokenService" ref="defaultSessionTokenService" />
 <property name="cxConfigurationService" ref="cxConfigurationService"/> <property name="cxUserSegmentSessionService" ref="cxUserSegmentSessionService"/> <property name="anonymousUserTaskRunnerName" value="cleanCxSessionResultsTaskRunner"/> <property name="registeredUserTaskRunnerName" value="cxRegisteredUserSessionCloseTaskRunner"/> </bean>
 <bean id="cleanCxSessionResultsTaskRunner" class="de.hybris.platform.personalizationservices.task.CleanCxSessionResultsTaskRunner" >
 <property name="actionResultDao" ref="cxActionResultDao"/>
 <property name="modelService" ref="modelService"/>
 </bean> <bean id="cxRegisteredUserSessionCloseTaskRunner" class="de.hybris.platform.personalizationservices.task.CxRegisteredUserSessionCloseTaskRunner"
 <property name="modelService" ref="modelService"/>
 <property name="userService" ref="userService"/>
 <property name="cxUserSegmentService" ref="cxUserSegmentService"/>
 <property name="cxUserSegmentConversionHelper" ref="cxUserSegmentConversionHelper"/> </bean> ...

Anonymous User Task A task for an anonymous user is dened to avoid storing large amount of results for anonymous users in the database. It cleans the already calculated personalization results, which are no longer needed once the session for anonymous user is closed.

Registered User Task The current implementation of a task triggered for registered user is responsible for storing user segments in the database. It is used when the registered user segments are set to be stored in session. You can dene this setting in your personalization conguration. For details, see Set Up a Personalization Conguration. User segments are stored for the current base site.

Cron Job Mechanism for Cleaning Results Additionally, you can use a cronJob to remove old personalization calculation results. The cronJob is using the maintenance cron job mechanism described in The Cronjob Service.

Cronjob: The CxResultsCleaningCronJob item type is dened in the personalizationservices-items.xml le.

There are two attributes dening which results should be removed:
resultMaxAge: Results older than a specied number of seconds is removed. The default value is 172800 (2 days). anonymous: Denes what type of results should be removed (anonymous or regular customer results). The default value is true.

CxResultsCleanupStrategy: Finds results based on given parameters and removes them. Results are cleanup in bundles (batches). Batch size is congured by setting personalizationservices.calculation.results.cleanup.pageSize property in local.properties le. Default value is 1000.

...

 <bean id="cleanupCxResultsJobPerformable" parent="abstractGenericMaintenanceJobPerformable">
<property name="pageSize" value="\#{configurationService.configuration.getProperty('personalizationservices.calculation.results.cleanup.pageSize This is   For more    the SAP Help  67
 <property name="maintenanceCleanupStrategy" ref="cxResultsCleanupStrategy"/>
 </bean>
 <alias name="defaultCxResultsCleanupStrategy" alias="cxResultsCleanupStrategy"/>
 <bean id="defaultCxResultsCleanupStrategy" class="de.hybris.platform.personalizationservices.strategies.impl.CxResultsCleanupStrategy">
 <property name="timeService" ref="timeService"/>
 <property name="modelService" ref="modelService"/> </bean> ... 

Trigger: The default CxResultsCleaningCronJob is created during the init/update process. The trigger is set to 4:05: AM daily. The script located in the /personalizationservices/resources/impex directory provides an example of adding a cronjob. You can congure it or create new job using the Backoffice Administration Cockpit.

INSERT_UPDATE CxResultsCleaningCronJob; code[unique=true];job(code);singleExecutable;sessionLanguage(isocode);anonymous;maxResultsAge;
;cleanupCxResultsCronJob;cleanupCxResultsJobPerformable;false;de;true;172800; INSERT_UPDATE Trigger;cronJob(code)[unique=true];second;minute;hour;day;month;year;relative;active;maxAcceptableDelay
\# Run the cleanupCxResultsCronJob at 4:05 AM every day
;cleanupCxResultsCronJob;0;5;4;-1;-1;-1;false;true;-1 Note Creating and editing these cron jobs is only possible for users with administrator rights.

Congure Calculation Time Header and Cookie Name Congure custom Calculation Time header and cookie names by setting respective properties.

 Caution Header/cookie is set only when calculation happens, in other cases no header/cookie is returned.

Default name for header is Occ-Personalization-Time. Congure custom header using the personalizationservices.personalizationTimeHeader property. You can congure the calculation time cookie only if cookies for OCC are enabled. Default name for cookie name is CxCt. Set a custom cookie name using the personalizationservices.personalizationTimeCookie property.

 Note Calculation time cookie is used only if the system cannot nd the header.

## Multi-Country Site Support

Personalization supports the multicountry setup, and can be congured to behave in a certain way when multicountry settings are enabled. By default, the system provides the following conguration options:
ALL_CATALOGS: uses all catalogs from the hierarchy. This is the default conguration. LEAF_CATALOGS: uses only the current catalog and ignores personalization from parent catalogs.

LEAF_CLOSEST_ANCESTOR_CATALOGS: uses personalization from the lowest possible catalog in the hierarchy. If the current catalog contains personalization, it will be used. If not, it will traverse the parent structure until personalization is found.

Conguring the Multi-Country Site Support You can easily congure your settings to support using the Backoffice Administration Cockpit. For details, see Set Up a Personalization Conguration.

Extending Multi-Country Site Support If you want to extend the available options, you should perform the following steps:
extend the CxCatalogLookupType in items.xml and provide a new type, dene a new spring bean that implements CxCatalogLookupStrategy.

The system will automatically pick up this strategy and use it for basesites where a corresponding lookup type is congured. When more than one catalog contains personalization, the system will evaluate all of them, giving the higher priority to the lower in the hierarchy. In other words, the local catalogs are always considered before the parent catalogs.

Working with Multi-Country Site Support in SmartEdit With the Multi-Country Site Support enabled, you can work with a hierarchy of catalogs to make your content regionally personalized. You can use the functionality provided by SmartEdit to switch between the catalogs, use the components from the parent and child catalogs and preview them using the Combined View. For details, see Multi-Country Site Support for Personalization.

Install Personalization You can install Personalization using dedicated recipes or manually by adding a set of extensions. Once you install Personalization, the system includes a set of sample data for the demonstration storefronts.

Installing Personalization Using Recipes To perform a basic installation of Personalization, follow the steps described in Installing SAP Commerce Cloud Using Installer Recipes.

Extensions to Include When Performing a Manual Installation If you are installing SAP Commerce Cloud with Personalization but are not using an installation recipe, include the extensions you need in the localextensions.xml le. To include the main Personalization functionality, use the following set of extensions:
<extension name="previewpersonalizationweb" />
<extension name="personalizationcmsweb" />
<extension name="personalizationsmartedit" />
<extension name="personalizationpromotionssmartedit" />
<extension name="personalizationsampledataaddon" />
<extension name="personalizationpromotionssampledataaddon" />
<extension name="personalizationpromotions" />
<extension name="personalizationpromotionsweb" /> <extension name="personalizationservicesbackoffice" />
<extension name="personalizationpromotionsbackoffice" />
<extension name="personalizationcmsbackoffice" /> <extension name="personalizationintegrationbackoffice" /> <extension name="personalizationsearchbackoffice" /> <extension name="personalizationsearchsmartedit" /> <extension name="personalizationsearchweb" />
<extension name="personalizationsearchsamplesaddon" />
<extension name="personalizationaddon" />
 
Depending on your project, you may need additional extensions. Use the links for reference on extensions included in a given module.

Personalization module: Personalization Module Architecture Personalization promotions: Personalization Promotions Module Architecture Personalization integration: Personalization Integration Module Architecture Personalization search: Personalization Search Module Architecture Handling Third-Party NPM-related JavaScript Libraries SAP no longer includes third-party npm-related JavaScript libraries in SAP Commerce Cloud. This impacts any extensions and addOns that use these libraries. To enable full build and test capabilities on these extensions and addOns, you must download the required libraries through npm. To download the required libraries for Personalizationdo the following:
Ensure that ant is running.

Go to the $HYBRIS_BIN_DIR/platform directory.

Execute the ant npminstall command.

You can now execute any ant targets on your extensions or addOns.

## Congure Personalization

The Backoffice Administration Cockpit provides you with an intuitive user interface, which helps you to easily manage the segments, variations and customizations within a personalization conguration. Recalculating the user experience for each user is a complex task, but you can easily dene what should be done and when by using the conguration functionality provided by personalization.

The Backoffice Administration Cockpit interface allows you to set your conguration quickly and make it error-free.

The main conguration is base site-aware meaning that you can dene separate congurations for each base site. This conguration denes high-level behavior, and the url voter denes gradient behavior of personalization.

 Caution When dening a conguration, bear in mind that some operations may cause severe performance issues. Examples of such operations include:
synchronous updating of segments coming from an external system, synchronous recalculation performed too often.

Personalization in Backoffice Administration Cockpit vs Personalization in SmartEdit Both the Backoffice Administration Cockpit and SmartEdit give you the opportunity to use the intuitive and user-friendly UI to dene and manage segments, variations and customizations to create relevant user experience.

Personalization in Backoffice Administration Cockpit, with all its options, complements the functionality provided by SmartEdit. The SmartEdit user interface, thanks to its intuitive personalization mode, allows you to build customizations and target groups using predened segments and, once they are created, bind them with storefront components to dene a complete, personalized experience. However, if you need more advanced functionality that exceeds options described above, the Backoffice Administration Cockpit gives you further options, unavailable in SmartEdit. These include for instance creating and viewing particular segments or dening and managing available triggers. For details on Personalization in SmartEdit refer to: Personalization Mode in SmartEdit.

 Recommendation It is highly recommended to use the Backoffice Administration Cockpit as a supplementary tool and to dene the customizations in SmartEdit.

Fallback Mechanism If no conguration is found for any of the basesites, the predened fallback mechanism is used to ensure the default conguration remains intact. You can dene the personalization conguration using the project.properties le.

Logging of Changes The cxmanager is able to monitor changes in personalization congurations in the Backoffice Administration Cockpit. The logged items include:
properties, calculation, integration, yprole mappers.

The details logged for each item include:
user who did the change timestamp changed attribute (name, new value, old value)
modication type (update, delete, creation)
An example of logged changes looks as follows:

![69_image_0.png](69_image_0.png)

Access Personalization in Backoffice Administration Cockpit The Personalization node in the Explorer Tree allows you to view and manage the Personalization elements such as segments, users, variations, and customizations.

Set Up a Personalization Conguration Personalization conguration includes the general personalization settings, such as the base site the conguration applies to, the actions to be performed for the user and the multicountry site support denition.

Congure Default Personalization Results Default personalization results are calculated for anonymous users and contain only action results for default variations.

This is   For more    the SAP Help  70 Personalization in Commerce Web Services Commerce web services support personalization, allowing you to personalize the request responses for specic customers. Manage Segments Segments allow you to dene different variations. Learn how to create, manage, and congure the properties of segments.

Create Variation Triggers Variation triggers are the data model objects used to activate variations for a specic user. Learn how to use the Backoffice Administration Cockpit to dene segment variation triggers.

Add Actions An action represents a changed element of the customization that makes it more personalized. Add Customizations and Variations Use the Backoffice Administration Cockpit to create and manage customizations and variations.

Conguring oAuthClient for Personalization SmartEdit uses oAuth token for authorization.

Access Personalization in Backoffice Administration Cockpit The Personalization node in the Explorer Tree allows you to view and manage the Personalization elements such as segments, users, variations, and customizations.

Context Follow the steps described below to access Personalization in the Backoffice Administration Cockpit.

Procedure 1. Log in to the Backoffice Administration Cockpit.

The main window appears.

![70_image_0.png](70_image_0.png)

2. A detailed view of options available for the element selected from the list.
Results You can now go to particular elements of the node to work with them. For details, see:
Set Up a Personalization Conguration Manage Segments Create Variation Triggers Add Actions Add Customizations and Variations Set Up a Personalization Conguration Personalization conguration includes the general personalization settings, such as the base site the conguration applies to, the actions to be performed for the user and the multi-country site support denition.

Add a Basic Personalization Conguration Dene a new personalization conguration.

Customize Personalization Conguration Customize your conguration at any time, using the dedicated editor.

Congure Personalization Calculation You can congure the customer experience calculation options while creating or editing the personalization conguration. This example shows editing an existing conguration.

Add a Basic Personalization Conguration Dene a new personalization conguration.

Procedure 1. Navigate to Personalization Conguration Personalization conguration .

On the right, you can see the list of available congurations.

2. Click the button.

A new window pops up. Provide the mandatory attributes.

| Attribute Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | A unique code of your conguration.                                                                                                                                                                                                                    |
| Set of base sites                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | A set of base sites affected by the conguration.                                                                                                                                                                                                      |
| Consent templates                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Consent templates the end user must accept to have personalized content calculated.  Note You can select only consent templates which have the ag exposed set to true. For details on available templates, see Consent Templates in Personalization. |
| Action result load max repeat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Number of retries in case of action result load error caused by optimistic locking failure. The default value for this eld is: 1.                                                                                                                     |
| Auto create segments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | If set to true, segments are automatically created during update. The segments are based on user data coming from an external system.                                                                                                                 |
| 3. Under Calculation tab, provide the following attributes. Attribute Name Description Calculation process name The default name of the calculation process to start for asynchronous calculation. This eld is automatically lled in. Minimum affinity Minimum affinity for user-to-segment relation. The default value for this eld is 0.5. New session actions Actions to be executed when a new session starts. User login actions Set of actions to be called after user logs in. Congurations of url voter List of url voter congurations. Congurations of periodic voter List of periodic voter congurations. |                                                                                                                                                                                                                                                       |

4. Click Done to nish.

Your conguration is now ready and visible on the list.

## Customize Personalization Conguration

Customize your conguration at any time, using the dedicated editor.

Use the tabs to add or edit the settings for your conguration.

Properties Edit the attributes you have already provided while creating the conguration. Besides attributes you have set in creation wizard you can also dene the following:

| Attribute                          | Description                                                                                                                                                                                            |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set of base sites                  | Base sites included in this conguration.                                                                                                                                                               |
| Consent templates                  | Consent templates the end-user must accept to have the personalized content calculated.  Note You can select only consent templates which have the ag exposed set to true.                            |
| User segments store in session     | Denes if segments for registered user should be stored in session and saved to database after session ends.Allowing the user segments to be stored in session increases the performance of the system. |
| Category hierarchy lookup strategy | The strategy used to retrieve information on which catalogs to use when evaluating personalization with the multi-country site support enabled. For details, see Multi-Country Site Support.           |
| Action result load max repeat      | Number of retries in case of action result load error caused by optimistic locking failure.                                                                                                            |
| Container cleanup enabled          | Attribute dening if the cxContainer should be removed in case there are no actions related to it. For details, see the Container Cleanup section in personalizationcms Extension.                      |

Calculation Dene details for the calculations process. For details, see Congure Personalization Calculation.

Commerce Web Services Enable and congure the support for commerce web services in personalization. For details, see Personalization in Commerce Web Services.

Integration Indicate if you want the system to automatically create segments from data coming from an external system.

Mappers Dene a segment map for the order mapper. The segment with the highest threshold is the winning one. The sample personalization data provides you with two sample segment maps.

Congure Personalization Calculation You can congure the customer experience calculation options while creating or editing the personalization conguration. This example shows editing an existing conguration.

Procedure 1. Navigate to Personalization Conguration Personalization conguration Calculation Tab and click the conguration you want to edit.

2. Go to Calculation tab.

Here you can view and congure the personalization calculation settings. The numbers represent further steps.

![72_image_0.png](72_image_0.png)

![72_image_1.png](72_image_1.png)

![72_image_2.png](72_image_2.png)

| 3. Congure General properties. Attribute Name   | Description                                                                                                                           |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Calculation process name                        | The name of the calculation process to start for asynchronous calculation. Asynchronous calculation calls the process with this name. |
| Minimum affinity                                | Minimum affinity for user-to-segment relation. Only relations with affinity >= minAffinity are used in calculation process.           |
| 4. Congure Initial Actions.                     |                                                                                                                                       |

![72_image_3.png](72_image_3.png)

| Attribute Name                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User login actions              | Set of actions to be called after user logs in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| New session actions             | Actions to be executed when new session starts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Actions when user gives consent | A set of actions to be executed once the user gives all consents required by personalization. If there are no consents required by personalization, this option has no effect. If consent is required by personalization, selected actions are executed once after the user has given the consent. If multiple consents are required by personalization, selected actions are executed once after the customer has given all required consents. In case the user withdraws the consent, the actions may be triggered again when the user gives consent once more.  Note Execution of actions is event-based so if events are sent in asynchronous way only ASYNC_PROCESS action is a valid option. If the events are synchronous then all selected actions are executed synchronously. |

For more information on the actions, see Personalization Calculation Process.

5. Congure URL Related Actions after customer has given consent. This conguration allows you to dene actions to be executed for specic URLs. The ConfigurableUrlVoter triggers the recalculation if the request url contains one of the congured patterns.

a. Click Create new Conguration of url voter .

b. In the new window, ll in the required elds.

| Attribute Name   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code             | A unique code for your url voter conguration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| User type        | User type for which cong is valid (ALL, REGISTERED, ANONYMOUS).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| URL regexp       | A regular expression. If matched, the actions entered in the Actions eld are executed by the voter.  Caution Be very careful when dening the expression because of potential ReDoS (Regular Expression Denial of Service) attack. The ReDoS attack is an algorithmic complexity attack that produces a denial of service by providing a regular expression that takes a very long time to evaluate. The attack exploits the fact that most regular expression implementations have exponential time worst case complexity, so for larger input strings (the ʻevil regex') the time taken by a regex engine to nd a match increases exponentially. |
| Actions          | A list of actions returned by voter if the regular expression matches. The value for this attribute must be between 1 and 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

 Note You can see the list of all available url voters under Personalization Conguration Personalization Conguration Conguration of url voter and assign it to the desired personalization conguration.

6. Congure Periodic Actions to dene actions which are executed periodically.

a. Click Create new Conguration of periodic voter.

b. In the new window, ll in required elds.

| Attribute Name         | Description                                                                                                                        |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Code                   | A unique code for your url voter conguration.                                                                                      |
| User type              | User type for which cong is valid (ALL, REGISTERED, ANONYMOUS).                                                                    |
| Actions                | A list of actions returned by voter if the regular expression matches. The value for this attribute must be between 1 and 255.     |
| Minimal time interval  | The minimal time (in milliseconds) that needs to pass between executing actions. The value for this attribute must be 0 or higher. |
| Minimal request number | The minimal number of requests that needs to pass between executing actions. The value for this attribute must be 0 or higher.     |

 Note You can see the list of all available periodic voters under Personalization Conguration Personalization Conguration Conguration of periodic voter .

7. Click Done to nish.

## Congure Default Personalization Results

Default personalization results are calculated for anonymous users and contain only action results for default variations.

Context These results are valid for all anonymous users, who visit the storefront for the rst time and don't belong to any segment yet. Calculating and storing default results allows you to avoid calculating them separately. Default results are used by LOAD action if there are no specic results for the customer.

Congure the CxDefaultPersonalizationCalculationCronJob to calculate default personalization results.

 Note Only users with administrator rights can manage this cron job.

Procedure 1. Go to System Background Processes CronJobs 2. Create Calculating Default Personalization Cron Job.

a. Set the job denition to cxDefaultPersonalizationCalculationJob. b. Add base sites you want to calculate the personalization results for.

Alternatively, import the cron job impex le similar as in the example.

$siteUid=<yourSiteId> INSERT_UPDATE CxDefaultPersonalizationCalculationCronJob; code[unique = true]; job(code); singleExecutable; sessionLanguage(isocode); bas
;cxDefaultPersonalizationCalculationCronJob ; cxDefaultPersonalizationCalculationJob ;false; en; $siteUid ;
3. Optional step: Use an impex le to set a trigger for this cron job if you want to run it periodically.

\# Run the CxUpdateSegmentsCronJob at 4:00 AM every day INSERT_UPDATE Trigger; cronJob(code)[unique = true]; second; minute; hour; day; month; year; relative; active; maxAcceptableDelay ; cxUpdateSegmentsCronJob ; 0 ; 0 ; 4 ; -1 ; -1 ; -1 ; false ; true ; 600 Note Pay attention to the last parameter: maxAcceptableDelay. Its default value means that the maximum delay is set as 600 seconds. For more information on the parameter, see Automatic Activation of Triggers at Startup section in The Cronjob Service.

## Personalization In Commerce Web Services

Commerce web services support personalization, allowing you to personalize the request responses for specic customers.

This is handled by CxOccPersonalizationFilter and based on the personalization identier.

If a request does not have a personalization identier, it is created for this request and returned in the response header.

If a request already contains a personalization identier, the occ voters decide what recalculation action is executed. By default the LOAD action is executed to load the previously calculated personalization results. If there are no results for a specic customer or personalization identier, the default results are loaded.

If a request contains a cmsTicketId parameter, the recalculation is done based on preview ticket data. Related documentation: previewwebservices Extension, previewpersonalizationweb Extension.

Personalization for Commerce Web Services is disabled by default, so you have to enable it: Congure Personalization for Commerce Web Services.

 Note Be aware of the possibility that the personalization identier for an anonymous user can be abused by other users. Because of that carefully consider personalization options available for anonymous users, especially when creating personalized promotions.

Personalization calculation results can inuence the following requests:

| Request Example                                                                                                      | Action Performed                                 |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| GET https://localhost:9002/rest/v2/electronics/products/search?query=camera                                          | search for products                              |
| GET https://localhost:9002/rest/v2/electronics/users/john.doe@mail.com/carts/00001002                                | cart actions (for example turn on the promotion) |
| GET https://localhost:9002/rest/v2/electronics/cms/components/Section1SlotHomepageCxContainer cms components on page |                                                  |

![75_image_0.png](75_image_0.png)

## Occ Voters

The occ voter mechanism allows you to determine when and how the personalization is recalculated for commerce web services. The logic of handling votes is dened in CxOccPersonalizationFilter. When you run the CxOccPersonalizationFilter, the system evaluates the voters (classes implementing the CxOccVoter according to their order).

For each voter, it checks the corresponding vote. If it encounters a conclusive vote, the rst vote is considered. If there is no conclusive vote, it merges the actions returned by each voter into one set of actions.

Time Voter The CxOccTimeVoter triggers the asynchronous recalculation process if the value set for personalization calculation validity time parameter is exceeded. The default value for this parameter is 60000 milliseconds, but you can change it to suit your needs.

Custom Voter You can create a custom voter to perform the following actions:
Create a class implementing de.hybris.platform.personalizationservices.occ.voters.CxOccVoter.

Dene this class as a bean in the Spring context to be automatically used by the CxOccPersonalizationFilter.

Interceptors You can inuence the personalization process for commerce web services either by implementing the CxOccInterceptor interface or extending the AbstractCxOccInterceptor.

package de.hybris.platform.personalizationservices.occ; import de.hybris.platform.personalizationservices.voters.CxOccInterceptorVote; import de.hybris.platform.personalizationservices.voters.Vote; import javax.servlet.http.HttpServletRequest; import javax.servlet.http.HttpServletResponse; import org.springframework.integration.context.Orderable;
/**
 * Interceptor for personalization process called in Commerce Web Services (OCC) */
public interface CxOccInterceptor extends Orderable
{
/** * Method to determine if personalization process should be executed for this request
 * 
 * @param request
 * Http request
 * @return true - when personalization process should be continued<br/>
 * false - when personalization process should be omitted
 * 
 * @deprecated since 1905. Please use {@link CxOccInterceptor\#shouldPersonalizeRequestVote(HttpServletRequest)} instead.

 */
@Deprecated default boolean shouldPersonalizeRequest(final HttpServletRequest request)
{
return true;
} /** * Method to determine if personalization process should be executed for this request * * @param request * Http request
 * @return CxOccInterceptorVote - vote with information if personalization process should be continued<br/>
 */
default CxOccInterceptorVote shouldPersonalizeRequestVote(final HttpServletRequest request)
{
final CxOccInterceptorVote result = new CxOccInterceptorVote();
result.setVote(true);
result.setConclusive(false);
return result;
}
/** * Method called before voters will be asked about recalculation actions * * @param request * Http request
 */
default void beforeGetVote(final HttpServletRequest request)
{
} /**
 * Method called before final vote will be executed
 * 
 * @param request
 * Http request
 * @param vote
 * Final vote which will be executed */ default void beforeVoteExecution(final HttpServletRequest request, final Vote vote) { }
/**
 * Method called after final vote execution
 * 
 * @param request
 * Http request
 * @param response
 * Http response
 * @param vote
 * final vote which was executed
 */ default void afterVoteExecution(final HttpServletRequest request, final HttpServletResponse response, final Vote vote) { }
Congure Personalization for Commerce Web Services Enable and congure personalization for commerce web services to make the request responses personalized. Congure Custom Personalization Header Congure a custom header by setting respective properties.

Congure Personalization for Commerce Web Services Enable and congure personalization for commerce web services to make the request responses personalized.

Procedure 1. Go to Personalization Conguration Personalization conguration .

![77_image_0.png](77_image_0.png)

The time in milliseconds limiting the validity for generated personalization calculation results. When this time passes, the calculation process starts to generate new personalization results.

5. Optional step: Cross-Origin Resource Sharing support To use headers, it is vital to set the Cross-Origin Resource Sharing rules accordingly. You must add occ-personalization-id and occ-personalization-time (or custom names if it was changed) properties to allowed and exposed headers in ycommercewebservices (or custom extension if it was generated from template).

Sample conguration:
corsfilter.ycommercewebservices.allowedHeaders=origin content-type accept authorization occ-personalization-id occ-personalization-time corsfilter.ycommercewebservices.exposedHeaders=occ-personalization-id occ-personalization-time Congure Custom Personalization Header Congure a custom header by setting respective properties.

Context By default, personalization for commerce web services uses the personalization identier stored in the Occ-Personalization-Id header.

Procedure 1. Go to the local.properties le.

2. Edit the le to add a custom name for the header.

\#Defines custom name for personalization id header when using personalization for Commerce Web Services \#if its empty the default value is "Occ-Personalization-Id" personalizationservices.personalizationIdHeader=

## Manage Segments

Segments allow you to dene different variations. Learn how to create, manage, and congure the properties of segments. There are two types of providers, delivering the segment data:
Segment Provider supplies segment denition to the system. To learn more, see Default Update Segment Strategy.

User Segment Provider assigns segments to users. To learn more, see Default Update User Segment Strategy.

Manual Management Dene Segments Use the Backoffice Administration Cockpit to view and congure the user segments.

To add new segment, see Add a Segment. To edit properties of the segment, see Congure a Segment.

Use the impEx import to create and manage segment data. An example of an .impex le, loading the segment data is presented below:
INSERT_UPDATE CxSegment;code[unique=true];
;VIPGold;
;VIPSilver;
;VIPBronze;
;WinterAccessoriesLover;
;BurtonBrandLover;
;ShortsCategoryLover;
;Women;
;Men; Assign Segment to Users To assign users to the selected segment, use the Backoffice Administration Cockpit: Users in Segments.

To do this using an .impex le, see the following example:
$siteUid=electronics INSERT_UPDATE CxUserToSegment;segment(code)[unique=true];user(uid)[unique=true];baseSite(uid)[unique=true,default=$siteUid];affinity[default=1]; ;VIPGold;vipgold@hybris.com;; ;VIPSilver;vipsilver@hybris.com;; ;VIPBronze;vipbronze@hybris.com;; ;Women;women@hybris.com;;
;Women;womenvipgold@hybris.com;;
;VIPGold;womenvipgold@hybris.com;;
;Women;womenvipsilver@hybris.com;;
;VIPSilver;womenvipsilver@hybris.com;;
;Men;men@hybris.com;;
;Men;menvipbronze@hybris.com;;
;VIPBronze;menvipbronze@hybris.com;;
;Men;menvipgold@hybris.com;;
;VIPGold;menvipgold@hybris.com;;
System Automatic Management There are two types of automatic segment data updates available in the system:
Update segment denition - this functionality is related to the UpdateSegmentStrategy interface. For more information, check the Update Segment Strategy section in Services in personalizationservices Extension and Default Update Segment Strategy.

Update user to segments assignment - this functionality is related to UpdateUserSegmentStrategy. For more information, check the Update User Segment Strategy section in Services in personalizationservices Extension and Default Update User Segment Strategy. Frequency of update user segments process depends on calculation conguration: Congure Personalization Calculation.

Customize Segment Denition To customize segment denition management, you can take one of the following steps:
Congure default cron job, which updates the segments denition. For details, see Cron Job for Refreshing Segments.

Create Segment Provider. For details, see the Dene Segments Provider section in Default Update Segment Strategy and Dene Simple User Segments Provider. The diagram shows where the SegmentsProvider ts in the ow:

![79_image_0.png](79_image_0.png)

Congure the frequency of the update user segments process. For details, see Congure Personalization Calculation.

Customize the UPDATE action ow: to customize the update process, create your own implementation of the UserSegmentsProvider interface. For details, see Dene Segments

![79_image_1.png](79_image_1.png)

 Caution Creating a UserSegmentsProvider interface using data from an external system, affects the performance of the storefront. Make sure that your provider is fast or that it is called in the asynchronous process. You can congure each provider separately, as they have dedicated actions such as UPDATE_<providerId> or ASYNC_PROCESS_<providerId>.

Add a Segment Add a segment to accommodate user data.

Congure a Segment Congure your segment by connecting it to user data and adding triggers.

Users in Segments Assign your segment to specic users. Cron Job for Refreshing Segments The CxUpdateSegmentsCronJob interface allows to dene segments based on the information obtained from the external systems.

## Add A Segment

Add a segment to accommodate user data.

Procedure 1. Go to Personalization Segments to see the list of already created segments (if any) along with their detailed conguration.

This is   For more    the SAP Help  80 2. Click the button in the top menu bar. 3. Once a pop-up window has appeared, enter the code and description for your segment as well as select the segment provider. The code has to be unique.

By default, the code can't be longer than 255 characters. This limit can be adjusted by modifying the PersonalizationservicesConstants.MAX_SEGMENT_NAME_LENGTH
constant. Within the internal logic, the validator reads the constant during the platform startup. In the Backoffice, the constraint reads the constant during the essential data update.

The CxSegmentNameLengthConstraint can be also modied manually in the Backoffice.

 Note To see the adjusted segment provider editor, you have to apply the personalizationintegration extension. For details, navigate to: personalizationintegration Extension.

 Caution Segment code may contain personal data. Be aware that these data are exposed in the personalized web pages. They are not presented as clear text, but they are base64 encoded.

However, this kind of encoding can be easily reverted to achieve the original text.

Click Done to save and nish.

Results A segment was successfully created and after clicking the Search button, it appears at the end of the list. You can now congure your segment to link it with specic variations and users.

## Congure A Segment

Congure your segment by connecting it to user data and adding triggers.

Procedure 1. Navigate to Personalization Segments . From the list, select the segment that you have created and click the entry.

A conguration section appears for the selected segment.

1. Code: Unique code you have chosen for your segment. 2. Description: A meaningful description, dening the purpose of the segment. The description is displayed when you select segments in SmartEdit.

3. Triggers: Triggers pointing to specic variations. By dening a list of triggers, you congure the relation between the segment and the variation.

4. Expression Triggers: Expression triggers pointing to a variation. These triggers are based on logical expressions. 5. User links: Users assigned to your segment. 6. Segment providers: Choose providers that contain the segment.

7. Auto created: Indicates if the segment has been created automatically. In our case, it is set to false by default.

 Note To see up-to-date editors for creating new user to segment relation and editing an existing one, the personalizationintegrationbackoffice extension is required. For details about the extension, see personalizationintegrationbackoffice Extension.

2. Select the triggers from the list:
 Tip If you want to learn more about a particular trigger, double-click the trigger entry. A pop-up window appears, showing the trigger details. You can also create an entirely new trigger using the Create new segment trigger button. For details on creating triggers see: Create Variation Triggers.

3. Dene the user - segment relation by clicking Create new User to Segment relation button.

A new pop-up window appears.

| Item   | Field             | Description                                                                                                                              |
|--------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| 1.     | Base site         | Determines the sites for which the relation remains valid. Select the base site from the list.                                           |
| 2.     | Provider identier | Providers which deliver this segment.                                                                                                    |
| 3.     | Affinity          | Affinity value is used to measure the strength of a relationship between the user and the segment. It can be any value from 0 through 1. |
| 4.     | Segment           | This eld has already been lled in for you in this case, because you dene the relation from the point of view of a given segment.         |
| 5.     | User              | The user to be linked with a given segment. Select the user from the list.                                                               |

Click Done to create the relation. It is now added as a new entry on the list.

## Users In Segments

Assign your segment to specic users.

Context The Users in segments section allows you to establish a user to segment relations in a similar way as for conguring a segment.

Procedure 1. Navigate to Personalization Users in segments .

You can see a list of already dened users.

2. Click the User to Segment relation button.

A new window appears. For details on the values of the elds, see: Congure a Segment, Step 3.

3. A new User to Segment relation object is added to the list. You can edit it at any time, simply by clicking the entry and editing the properties in an editor.

Next Steps Learn how SmartEdit can help you use the segments to create customizations: Create a Customized Storefront.

## Cron Job For Refreshing Segments

The CxUpdateSegmentsCronJob interface allows to dene segments based on the information obtained from the external systems. The default cron job is already available in the system, imported in the projectdata_personalizationservices.impex le:
INSERT_UPDATE CxUpdateSegmentsCronJob; code[unique = true] ; job(code) ; singleExecutable; sessionLanguage(isocode); fullUpdate; allBa
 ; cxUpdateSegmentsCronJob ; cxUpdateSegmentsJob ; false ; en ; true ; true Dened cron job runs the update process for all base sites, gets the data from all providers, and performs the full update. Cron job isn't triggered by default. You can add the trigger with the following impex:
\# Run the CxUpdateSegmentsCronJob at 4:00 AM every day INSERT_UPDATE Trigger; cronJob(code)[unique = true]; second; minute; hour; day; month; year; relative; active; maxAcceptableDelay
 ; cxUpdateSegmentsCronJob ; 0 ; 0 ; 4 ; -1 ; -1 ; -1 ; false ; true ; 600 You can also add the trigger or change other settings in the Backoffice Administration Cockpit:
1. Go to System Background Processes CronJobs .

2. Edit cxUpdateSegmentsCronJob.

| 2. Edit cxUpdateSegmentsCronJob.   |
|------------------------------------|
| Congure the following attributes:  |

Full update:
False to add new segments.

True to add new segments and also remove not used segments.

Providers - set All segment providers to True to get data from all registered providers or dene a list of providers. Don't run the update segment process without any provider. If the provider list is empty, the segments will come from all providers.

![82_image_0.png](82_image_0.png)

![82_image_1.png](82_image_1.png)

![82_image_2.png](82_image_2.png)

![82_image_3.png](82_image_3.png)

![82_image_4.png](82_image_4.png)

![82_image_5.png](82_image_5.png)

Base Sites - set All baseSites to True to run update segment process for all base sites or to dene the base site list. If your segment data do not depend on any base site, you can

![82_image_6.png](82_image_6.png)

![82_image_7.png](82_image_7.png)

![82_image_8.png](82_image_8.png)

![82_image_9.png](82_image_9.png)

![82_image_10.png](82_image_10.png)

congure an empty base site list. In such case, no base site is set in session for update segment process.

## Create Variation Triggers

![82_Image_11.Png](82_Image_11.Png)

![82_Image_12.Png](82_Image_12.Png)

![82_Image_13.Png](82_Image_13.Png)

![82_Image_14.Png](82_Image_14.Png)

![82_Image_15.Png](82_Image_15.Png)

Variation triggers are the data model objects used to activate variations for a specic user. Learn how to use the Backoffice Administration Cockpit to dene segment variation triggers.

The following triggers types are available:
The default trigger used for triggering a variation for all users, regardless of the segment they are in. The segment trigger used for enabling the variations for specic user segments.

The expression trigger used to trigger the variation based on a logical expression (often complex) created from segments and joined with operators. Custom triggers used to trigger the variation based on specied conditions, for example for a specic user group. Add a Segment Trigger Add and congure a segment trigger.

Add an Expression Trigger Add and congure an expression trigger.

Add a Default Trigger Add and congure a default trigger.

Add a Custom Trigger Create a custom trigger suited to your needs. Edit a Trigger Edit the trigger to introduce changes. Delete a Trigger Delete a trigger you no longer want to use.

Add a Segment Trigger Add and congure a segment trigger.

Procedure 1. In the Segments Trigger section click the button.

A pop-up window appears.

2. Fill the elds with appropriate values.

| Item   | Field                    | Description                                                                                                                                                                                        |
|--------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.     | Code                     | A unique code for the trigger.                                                                                                                                                                     |
| 2.     | Variation triggered      | A variation that will be triggered for the selected segments once the segment condition dened by the operator is met.                                                                              |
| 3.     | Segments used by trigger | A segment or several segments that trigger a particular variation. To add a segment, select it from the drop-down menu.                                                                            |
| 4.     | Group segments by        | An operator dening the segment conguration needed to trigger a variation. Two values are available: AND: a user needs to belong to both segments. OR: a user may belong to either of the segments. |

3. Click Done to complete the process.

Your trigger is now available on the list.

## Add An Expression Trigger

Add and congure an expression trigger.

Context Use the steps below to create and congure a new expression trigger.

Procedure 1. In the Expression Trigger section click the button.

A pop-up window appears.

2. Fill the elds with appropriate values. 3. Click Done to complete the process.

| Item   | Field               | Description                                                                                                           |
|--------|---------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1.     | Code                | A unique code for the trigger.                                                                                        |
| 2.     | Variation triggered | A variation that will be triggered for the selected segments once the segment condition dened by the operator is met. |
| 3.     | Logical expression  | A logical expression stored in a JSON format.                                                                         |

Your trigger is now available on the list.

## Add A Default Trigger

Add and congure a default trigger.

Procedure 1. In the Default Trigger section click the button.

A pop-up window appears.

2. Fill the elds with appropriate values.

This is   For more    the SAP Help  84

| Item                                   | Field               | Description                                                                                                           |
|----------------------------------------|---------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1.                                     | Code                | A unique code for the trigger.                                                                                        |
| 2.                                     | Variation triggered | A variation that will be triggered for the selected segments once the segment condition dened by the operator is met. |
| 3. Click Done to complete the process. |                     |                                                                                                                       |

Your trigger is now available on the list.

## Add A Custom Trigger

Create a custom trigger suited to your needs.

You can create a custom trigger and use it in the target group model. For example, you can create a trigger which activates a variation for a particular user group instead of segment conguration.

For instructions on creating a custom trigger, see Personalization Core Trail. For details on extending personalization in SmartEdit to add a new trigger type, see Extend Personalization in SmartEdit.

## Edit A Trigger

Edit the trigger to introduce changes.

Context The following steps show you how to edit your triggers on the example of the Segment Trigger.

Procedure 1. If you want to edit the trigger, navigate to Personalization Triggers Segment Triggers and select a trigger from the list. It can be the trigger you have created in the previous task.

2. An editor appears. You can now edit the properties of your trigger, for example change the variation, add/remove the segments or change segment grouping.

3. Once you are done with editing, remember to click Save to save your results.

## Delete A Trigger

Delete a trigger you no longer want to use.

Context You can easily delete the triggers you don't need anymore.

Procedure Navigate to Personalization Triggers Segment Triggers and select a trigger from the list. It can be the trigger you have created in the previous task. Click the bin icon at the top of the page. A conrmation dialog will appear asking you to conrm that you want to delete the trigger. Click Yes to delete.

Next Steps You can also congure the triggers and variations using SmartEdit. For details, see Create a Customized Storefront. Bear in mind that for business purposes the variations are labelled target groups in SmartEdit.

## Add Actions

An action represents a changed element of the customization that makes it more personalized.

 Recommendation It is strongly recommended to use SmartEdit to congure the relation between variations and actions, using Backoffice Administration Cockpit as an additional tool.

Currently, you have the possibility of creating and adding the following types of actions: a general CMS Action, a Promotion Action, and a Search Prole Action. Adding an action in such way works exactly the same as selecting a promotion or search prole in the Commerce Customization modal, however is not so intuitive since it requires knowledge of the ID numbers and codes of promotions or search proles. To access the actions, navigate to Personalization Actions :

![85_image_0.png](85_image_0.png)

1. Actions node: Includes general Actions node, CMS Action, Promotion Action, and Search Prole Action. Depending on the node you choose, the list of available actions will include CMS
actions, promotion actions, search prole actions or all of them. The button used to create the actions will also change.

2. A list of already created actions. 3. A button used to create actions. Clicking it invokes a new wizard window.

 Caution Action code may contain personal data. Be aware that these data are exposed in the personalized web pages. They are not presented as clear text, but they are base64 encoded. However, this kind of encoding can be easily reverted to achieve the original text.

You can create the following types of actions:
CMS Action: Add CMS Actions.

Promotion Action: Add Promotion Actions.

Search Prole Action: Add Search Prole Actions. Search Prole Action is implemented in the personalizationsearch extension. For details, see Personalization Search Module.

## Add Cms Actions

Context The steps below will instruct you on creating a CMS Action.

Procedure 1. Navigate to Personalization Actions CMS Action . Click the button in the top menu bar.

A new pop-up window appears.

2. Provide the details of your new action.

| Item   | Name                   | Description                                                                                                                                    |
|--------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.     | Component ID           | An ID of the relevant storefront component (such as a banner). You need to know the exact name of the component for the action to take effect. |
| 2.     | Code                   | A unique code for the action.                                                                                                                  |
| 3.     | Component Container ID | An ID of the container the component is placed in. You need to know the exact name of the container for the action to take effect.             |
| 4.     | Variation              | Variation the action is dened for.                                                                                                             |

3. Click Done to nish. Your action is added to the end of the list.

## Editing A Cms Action

Context You can easily edit your action at any time. Follow the steps to learn how.

Procedure 1. Navigate to Personalization Actions CMS Action . Search for your action on the list or by using the search eld at the top of the page. Click the action entry.

An editor appears.

You can now edit some of the action attributes such as variations and catalog version.

2. Click Save to save your changes.

## Deleting Actions

Context You can easily delete the action you don't need anymore. The example shows a CMS Action, because the procedure is the same for every action.

Procedure Navigate to Personalization Actions CMS Action and select a action from the list. It can be the action you have created in the previous task.

Click the bin icon at the top of the page. A conrmation dialog will appear asking you to conrm that you want to delete the action. Click Yes to delete. The action is no longer present on the list.

Related Information Create a Personalization Action Add Promotion Actions The steps below will instruct you on creating a Promotion Action and connect it to a given target group.

Prerequisites A source promotion rule is already created.

 Recommendation You can use the Backoffice Administration CockpitSmartEdit interface for the purpose. For details see: Activating a Personalized Promotion for a Target Group.

Procedure 1. Navigate to Personalization Actions Promotion Action . Click the button in the top menu bar. to create and manage a promotion action, however it is strongly recommended to use the A new pop-up window appears.

2. Provide the details of your new action.

| Item   | Name         | Description                                                                                                                                                                                                                                                                                                                   |
|--------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.     | Code         | A unique code for the action.                                                                                                                                                                                                                                                                                                 |
| 2.     | Variation    | Variation (target group) the action is dened for.                                                                                                                                                                                                                                                                             |
| 3.     | Promotion ID | An ID of the promotion action. The ID must be to create and manage a promotion action, however it is strongly recommended to identical to the code of a personalized promotion rule, otherwise the action cannot be created, because the rule is not found. You can nd the code in the table under Rule Engine Source Rules . |

3. Click Done to nish. Your action is added to the end of the list. If you click it, the editor opens so you can introduce changes if necessary. As you can see, the Catalog Version eld is lled in automatically, based on the variation details.

4. To verify if the action was added properly, go to personalization mode in SmartEdit. 5. Navigate to Library Manage Library and nd the target group you created the action for (in our example it is the VipSilver target group). 6. Use the more menu to access Commerce Customizations.

| Manage Customization Library                             | x                        |              |         |                          |     |
|----------------------------------------------------------|--------------------------|--------------|---------|--------------------------|-----|
| Apparel UK Content Catalog - Staged | Customizations (5) | Search Customizations  Q | All Statuses | >       | Create New Customization |     |
| Customization                                            | Target Groups            | Components   | Status  | Start                    | End |
| ❯ SummerSale                                             | 1                        | Enabled      |         |                          |     |
| ✦ SpringSale                                             | S                        | Enabled      |         |                          |     |
| 1 WinterSale                                             | Enabled                  |              |         |                          |     |
| ❯ CategoryLover                                          | 2                        | Enabled      | 00      |                          |     |
|                                                          | 4                        | Enabled      | ++      |                          |     |
| 1 VipGold                                                | i                        | Enabled      | 00      |                          |     |
| 1 VipSilver                                              | i                        | Enabled      | ..      |                          |     |
| Edit                                                     |                          |              |         |                          |     |
| 1 VipBronze                                              | 1                        | Enabled      | Disable |                          |     |
| Commerce Customization                                   |                          |              |         |                          |     |
| VIPDefault                                               | 1                        | Disabled     | Move up |                          |     |
| Move down                                                |                          |              |         |                          |     |
| Remove                                                   |                          |              |         |                          |     |

7. The action is added to the target group.

l you remove it at this point, it will be also removed from the Backoffice Administration Cockpit. For details on how to remove an action using the Backoffice Administration Deleting Actions Add Customizations and Variations Use the Backoffice Administration Cockpit to create and manage customizations and variations.

→ Tip It is recommended to use SmartEdit for configuring your variations and customizations. For details see: Create a Customized Storetront . However, you can also use the Backof Administration Cockpit as a supplementary tool Q Remember The term target group is used in the user documentation instead of variation, used in technical documentation. Target group is an Ul label used for business purposes.

Use the links below to navigate to sections that you want to explore:
- Add Variations
- Manage Customizations
- Manage Customization Groups Ad Variations Context The following steps will help you create and manage your variations using the Backoffice Administration Cockpit.

Procedure To access the variations, navigate to Personalization Variations . A list of already created variations (if any) appears.

## Creating Variations

Context Perform the steps below to create a variation.

Procedure 1. Navigate to Personalization Variations . Click the button in the top menu bar.

A new pop-up window appears.

2. Provide the details of your new variation.

| Item   | Name   | Description               |
|--------|--------|---------------------------|
| 3.     | Code   | A code for the variation. |

1. Status Denes if the variation is enabled, disabled, or deleted. The default value is enabled. For more on status values, see

Personalization Mode in SmartEdit.

2. Customization A customization the variation belongs to.

3. Code A code for the variation.

4. Name A name for your variation. It can be the same as the code.

 Caution Variation name or code may contain personal data. Be aware that these data are exposed in the personalized web pages. They are not presented as clear text, but they are base64 encoded. However, this kind of encoding can be easily reverted to achieve the original text.

3. Click Done to nish. Your variation is added to the end of the list.

## Editing Variations

Context You can easily edit your variation at any time. Follow the steps to learn how.

Procedure 1. Navigate to Personalization Variations . Search for your variation on the list or by using the search eld at the top of the page. Click the variation entry.

An editor appears.

![88_image_0.png](88_image_0.png) It offers you various edition options, so you can change the catalog version, name, status, or customization the particular variation belongs to. You can also disable or deactivate the variation. The editor provides you also with the following additional options (you can see them marked on the screenshot):
1. Actions: this eld allows you to create actions for the variation. For details, see Add Actions.

2. Triggers: here you can add the triggers that invoke the variation. For details, see Create Variation Triggers.

3. Priority: you can dene the priority settings for a variation. For details on priority, see Personalization Mode in SmartEdit.

2. Click Save to save your changes.

Deleting Variations This is   For more    the SAP Help  89 Context You can easily delete the variation you don't need anymore.

Procedure Navigate to Personalization Variations and select a variation from the list. It can be the variation you have created in the previous task. Click the bin icon at the top of the page. A conrmation dialog appears asking you to conrm that you want to delete the variation. Click Yes to delete. The variation is no longer present on the list.

Related Information Create a Customized Storefront Manage Customizations Context The following steps will help you create and manage your customizations using the Backoffice Administration Cockpit.

Procedure To access the customizations, navigate to Personalization Customizations . A list of already created customizations (if any) appears.

Create Customizations Context Perform the steps below to create a customization.

Procedure 1. Navigate to Personalization Customizations . Click the button in the top menu bar.

A new pop-up window appears.

2. Provide the details of your new customization.

| Item   | Name   | Description   |
|--------|--------|---------------|

1. Status Denes if the variation is enabled, disabled, or deleted. The default value is enabled. For more on status values, see

Personalization Mode in SmartEdit.

2. Name A name for your customization. It doesn't have to be unique. 3. Code A unique code for your customization. 4. Customization Group A group your customization belongs to.

 Caution Customization name or code may contain personal data. Be aware that these data are exposed in the personalized web pages. They are not presented as clear text, but they are base64 encoded. However, this kind of encoding can be easily reverted to achieve the original text.

3. Click Done to nish. Your customization is added to the end of the list.

Edit Customizations Context You can easily edit your customization at any time. Follow the steps to learn how.

Procedure 1. Navigate to Personalization Customizations . Search for your customization on the list or by using the search eld at the top of the page. Click the customization entry.

An editor appears.

![90_image_0.png](90_image_0.png)

o 1. Start and End Date: Dates determining the period within the customization is active. If no time is specified, the customization is always active.

o 2. Rank (Priority): Determines the priority of a particular customization. In the Personalization mode in SmartEdit, you simply drag and drop the customizations to define t priority, however in the Backoffice Administration Cockpit you use numbers. For details on priority, see Priority in Oustomizations and Variations, o 3. Variation: Variations belonging to this customization. For details, see Add Variations, - 4. Active: Determines if the customization is active and can be used on the storefront.

2. Click Save to save your changes.

## Delete Customizations

Context You can easily delete the customization you don't need anymore. Procedure Navigate to ] Þ Personalization ⟩ Customizations ] and select a customization from the list. It can be the customization you have created in the previous task.

Click the bin icon at the top of the page. A confirmation dialog will appear asking you to confirm that you want to delete the customization. Click Yes to delete.

## Retrieve Customizations

Context SmartEdit UI allows you to remove a customization (see: Customization Library ). However, it is not removed permanently in case you would like to use it again - for example i configuration was complex and you don't want to build it again from scratch. Use the Backoffice Administration Cockpit to retrieve your customization Procedure 1. In SmartEdit, delete one of your customizations.

Manage Customization Library x

| Apparel UK Content Catalog - Staged | Customizations (5)   | All Statuses   | Create New Customization   |         |       |     |
|------------------------------------------------------------|----------------|----------------------------|---------|-------|-----|
| Search Customizations  Q                                   | >              |                            |         |       |     |
| Customization                                              | Target Groups  | Components                 | Status  | Start | End |
| ❯ SummerSale                                               | Enabled        | Edit                       |         |       |     |
| ❯ SpringSale                                               |                | Enabled                    | Move Up |       |     |
| 1 WinterSale                                               | Enabled        | Move Down                  |         |       |     |
| Remove                                                     |                |                            |         |       |     |
| ❯ CategoryLover                                            | 2              | Enabled                    |         |       |     |
| > VIP                                                      | Enabled        |                            |         |       |     |

The customization will be removed from the list.

2. Navigate to [ ] Personalization ] Customizations ] and search for your customization.

P
SummerSale

![91_image_0.png](91_image_0.png)

a

![91_image_1.png](91_image_1.png)

e
+ -  R

| = E        5 items                   |                                        |                 |                                        |         |         |
|--------------------------------------|----------------------------------------|-----------------|----------------------------------------|---------|---------|
| e                                    | + -  R                                 | Rank (priority) |                                        |         |         |
| Code                                 | Catalog Version                        | Name            | Customization group                    | Status  |         |
| Electronics Content Catalog : Staged | electronicsCustomizationGroup : Staged | ENABLED         |                                        |         |         |
| SummerSale                           | SummerSale                             | 1               |                                        |         |         |
| SummerSale                           | Electronics Content Catalog : Online   | SummerSale      | electronicsCustomizationGroup : Online | ENABLED |         |
| 1                                    |                                        |                 |                                        |         |         |
| SummerSale                           | Apparel DE Content Catalog : Staged    | SummerSale      | appareIDECustomizationGroup : Staged   | 0       | ENABLED |
| SummerSale                           | Apparel DE Content Catalog : Online    | SummerSale      | appareIDECustomizationGroup : Online   | 0       | ENABLED |
| C00000000                            | Apparel UK Content Catalog : Staged    | SummerSale      | apparelUKCustomizationGroup : Staged   | 0       | DELETED |

As you can see, your customization is still on the list, however its status says DELETED which means that the customization is no longer visible in SmartEdit.

3. Click the customization to open the editor. In the Status field, change the value to ENABLED. Remember to click Save, otherwise your changes won't be saved.

SummerSale : Staged
- 

![91_image_3.png](91_image_3.png)

i 4

.

![91_image_2.png](91_image_2.png)

![91_image_6.png](91_image_6.png)

PROPERTIES
 ADMINISTRATION

![91_image_4.png](91_image_4.png)

| Rank (priority) ©   | Status   |         |
|---------------------|----------|---------|
| 0                   | DELETED  |         |
| n/a                 |          |         |
| ENABLED             |          |         |
| DISABLED            |          |         |
| End Date O          | n        | DELETED |

![91_image_5.png](91_image_5.png)

![91_image_7.png](91_image_7.png)

Customization group ☺
apparelUKCustomizationGroup : Sta...

![91_image_9.png](91_image_9.png)

![91_image_8.png](91_image_8.png)

The customization is again visible in SmartEdit

## Manage Customization Groups

Context A customization group may hold several customizations to create an organized structure. With the Backoffice Administration Codpit you can easily manage your customizations wi customization groups.

Create Customization Groups Procedure 1. Navigate to Personalization Customization Groups . If there have been any customization groups created, you should see a list. Click the button at the top of the page.

A new pop-up window appears.

2. Provide the details of your new customization.

![92_image_0.png](92_image_0.png)

Edit Customization Groups Context You can easily edit your customization groups at any time. Follow the steps to learn how.

Procedure

![92_image_1.png](92_image_1.png)

also add a description for the customization group. The editor provides you also with some additional options (you can see them marked on the screenshot):
Customizations: Customizations belonging to this customization group.

2. Click Save to save your changes.

Delete Customization Groups Context You can easily delete the customization group you don't need anymore.

Procedure 1. Navigate to Personalization Customization Groups and select a customization group from the list. It can be the customization group you have created in the previous task.

Click the bin icon at the top of the page. A conrmation dialog will appear asking you to conrm that you want to delete the customization group.

2. Click Yes to delete.

The customization group is no longer present on the list.

Related Information Create a Customized Storefront Conguring oAuthClient for Personalization SmartEdit uses oAuth token for authorization. To enable personalization, update oAuthClient with the following impex:
INSERT_UPDATE OAuthClientDetails;clientId[unique=true];scope[mode=append]
;smartedit;personalizationwebservices Extend Personalization The guides provide you with information on how you can extend personalization to fully use its features.

Create a Personalization Action A personalization action represents a change in customer experience, for example when displaying a specic component or activating a promotion. To show how a personalization action can be created, let's use the example of CxCmsAction used to customize the storefront components and provided out of the box.

Implement Custom Mapping Learn how to dene your own mapping.

Commerce Customizations The term commerce customization refers to non-cms actions that are performed when a user belongs to given target group.

Create a Personalization Action A personalization action represents a change in customer experience, for example when displaying a specic component or activating a promotion. To show how a personalization action can be created, let's use the example of CxCmsAction used to customize the storefront components and provided out of the box.

Currently, the Personalization module supports the actions related to cms components such as displaying a specic component or activating a particular promotion displayed to the customer on the storefront, making the editing and changing the storefront content easy and efficient. However, the module ensures extensibility in order to support further personalization actions.

There are different layers of the system that you need to extend in order to create a fully congurable new type of action :
Service layer to add the core functionality of your action and its persistence in the database.

Webservice layer to add REST endpoints for the tools used for conguring personalization (such as SmartEdit)
Extend Service Layer Context Follow the steps below to extend the service layer for the functionality related to actions in personalizationcms extension.

Procedure 1. Start with adding a new type in your items.xml le. Dene the action model by providing an item denition, which extends the AbstractCxAction in <yourextension>-
items.xml personalizationcms-items.xml
... 

 <itemtype generate="true" code="CxCmsAction" jaloclass="de.hybris.platform.personalizationcms.jalo.CxCmsAction" autocreate="true" exten abstract="false">
 <attributes>
 <attribute qualifier="componentId" type="java.lang.String"> <description>Targeted component id</description>
 <modifiers optional="false" />
 <persistence type="property" />
 </attribute>
 <attribute qualifier="containerId" type="java.lang.String"> <description>Targeted container id</description>
 <modifiers optional="false" />
 <persistence type="property" />
 </attribute>
 <attribute type="java.lang.String" qualifier="affectedObjectKey" redeclare="true"> <modifiers write="false" />
 <persistence type="dynamic" attributeHandler="cxCmsActionAffectedObjectKeyAttributeHandler" />
 </attribute> </attributes> </itemtype> ...

2. Add a new bean in your beans.xml le. Dene the action result by providing a bean denition, which extends CxAbstractActionResult in <yourextension>-beans.xml. For details, see: Generating Beans and Enums. personalizationcms-beans.xml
...

 <bean class="de.hybris.platform.personalizationcms.data.CxCmsActionResult" extends="de.hybris.platform.personalizationservices.data.CxAbstr
 <property name="componentId" type="String"/>
 <property name="containerId" type="String"/>
 </bean> ...

3. Dene the action performer. The implementation of ActionPerformable (de.hybris.platform.servicelayer.action.impl.ActionPerformable) interface is responsible for executing a new action and optionally creating the action result. The CxAbstractActionPerformable is an abstract class, which can be used as a parent class for action performers.

It is possible for ActionPerformable interface not to create any action result and instead to execute the action immediately. In such a case, the implementation of ActionPerformable should be done in a non-thread blocking way. Additionally, consider that ActionPerformable is called for a given customer each time the system recalculates the variation and custom implementations of ActionPerformable should be idempotent.

CxCmsActionPerformable.java public class CxCmsActionPerformable extends CxAbstractActionPerformable<CxCmsActionModel>
{
 @Override protected CxAbstractActionResult executeAction(final CxCmsActionModel action, final CxContext context)
 { final CxCmsActionResult actionResult = new CxCmsActionResult(); actionResult.setComponentId(action.getComponentId()); actionResult.setContainerId(action.getContainerId());
 return actionResult;
 } }
personalizationcms-spring.xml
... <bean id="cxCmsActionPerformable" class="de.hybris.platform.personalizationcms.action.CxCmsActionPerformable" /> ...

4. Dene the action target provider.

To dene default values when creating new action models, use the mechanism provided by the de.hybris.platform.personalizationservices.action.property.ActionPropertySetter. This ActionPropertySetter will use the spring beans dened in the current spring context that match the current item type created and call them to set default values for this item.

The ActionPropertySetter interface provides two methods:
supports to dene what class it supports.

provideValues to set default values on given action.

One property that needs to be set on all action types is target. The target attribute determines which bean (for example CxCmsActionPerformable dened in previous step)
executes your action. As a result, you need to dene the target attribute provider that will be used to automatically set a default target attribute during the action creation. This provider class is available out of the box:
de.hybris.platform.personalizationservices.action.property.ActionTargetProvider You just need to declare a new instance of it in your spring context.

personalizationcms-spring.xml
...

 <bean id="cxCmsActionTargetProvider" class="de.hybris.platform.personalizationservices.action.property.ActionTargetProvider"> <property name="supportedClass" value="de.hybris.platform.personalizationcms.model.CxCmsActionModel" />
 <property name="target" value="cxCmsActionPerformable" />
 </bean> ...

## Extend Action Endpoint

Context A separate web extension is recommended to extend the functionality provided by the action endpoint and allow the conguration of your new type of action by SmartEdit. The personalizationcmsweb extension can be an example of such an extension. To introduce new action data subclass for action endpoints, perform the following steps:
Procedure 1. Dene the new action data representing a new action type. You can do it in the<yourextension>-beans.xml le (See also: Generating Beans and Enums)
personalizationcmsweb-beans.xml
... 

 <bean class="de.hybris.platform.personalizationcmsweb.data.CxCmsActionData" extends="de.hybris.platform.personalizationfacades.data.ActionD <property name="componentId" type="String" />
 <property name="containerId" type="String" />
 </bean> ...

2. Dene the populator and converter for the new action data.

a. Dene the populator for new attributes.

CxCmsActionPopulator.java public class CxCmsActionPopulator implements Populator<CxCmsActionModel, CxCmsActionData>
{
 @Override public void populate(final CxCmsActionModel source, final CxCmsActionData target) throws ConversionException {
 target.setComponentId(source.getComponentId());
 target.setContainerId(source.getContainerId());
 }
}
personalizationcmsweb-spring.xml This is   For more    the SAP Help  95
...

 <alias name="defaultCxCmsActionPopulator" alias="cxCmsActionPopulator" />
 <bean id="defaultCxCmsActionPopulator" class="de.hybris.platform.personalizationcmsweb.populators.CxCmsActionPopulator" /> ...

b. Dene the converter.

The converter dened for a new action data should be compliant with the Subtype Conversion Mechanism (For details on the mechanism, see the Subtype Conversion Mechanism section in personalizationfacades Extension). You can achieve it by using the cxActionPopulatingConverter as a parent bean.

personalizationcmsweb-spring.xml
...

 <bean id="defaultCxCmsActionConverter" parent="cxActionPopulatingConverter" > <constructor-arg name="sourceClass" value="de.hybris.platform.personalizationcms.model.CxCmsActionModel" />
 <property name="targetClass" value="de.hybris.platform.personalizationcmsweb.data.CxCmsActionData" />
 <property name="populators" > <map>
 <entry key="BASE" value-ref="cxCmsActionPopulators" />
 </map>
 </property>
 </bean>
 <alias name="defaultCxCmsActionPopulators" alias="cxCmsActionPopulators" />
 <bean id="defaultCxCmsActionPopulators" parent="abstractPopulatorList" >
 <property name="populators">
 <list> <ref bean="cxCmsActionPopulator" />
 <ref bean="cxActionPopulator" />
 </list>
 </property>
 </bean> ...

3. Dene the reverse populator and converter for new action data.

a. Dene the reverse populator for new attributes.

CxCmsActionReversePopulator.java public class CxCmsActionReversePopulator implements Populator<CxCmsActionData, CxCmsActionModel>
{
 @Override public void populate(final CxCmsActionData source, final CxCmsActionModel target) throws ConversionException {
 target.setComponentId(source.getComponentId());
 target.setContainerId(source.getContainerId()); } }
personalizationcmsweb-spring.xml
... <alias name="defaultCxCmsActionReversePopulator" alias="cxCmsActionReversePopulator" />
 <bean id="defaultCxCmsActionReversePopulator" class="de.hybris.platform.personalizationcmsweb.populators.CxCmsActionReversePopulator"
...

b. Dene the reverse converter. The reverse converter dened for new action data should be compliant with the Subtype Conversion Mechanism (For details on the mechanism, see the Subtype Conversion Mechanism section in personalizationfacades Extension). You can achieve it by using cxActionReversePopulatingConverter as a parent bean.

...

 <bean id="defaultCxCmsActionReverseConverter" parent="cxActionReversePopulatingConverter" >
 <constructor-arg name="sourceClass" value="de.hybris.platform.personalizationcmsweb.data.CxCmsActionData" />
 <property name="targetClass" value="de.hybris.platform.personalizationcms.model.CxCmsActionModel" />
 <property name="populators" >
 <map> <entry key="BASE" value-ref="cxCmsActionReversePopulators" /> </map> </property> </bean>
 <alias name="defaultCxCmsActionReversePopulators" alias="cxCmsActionReversePopulators" />
 <bean id="defaultCxCmsActionReversePopulators" parent="abstractPopulatorList" >
 <property name="populators">
 <list>
 <ref bean="cxCmsActionReversePopulator" />
 <ref bean="cxActionReversePopulator" />
 </list>
 </property>
 </bean>
...

4. Congure the mapping mechanism. The action endpoint exposes a method, which declares returning a general object (ActionData), however it can also return a specic object
(subclass object). Because of that, add information in your conguration to enable subclasses mapping. For details on the mapping see: Dynamic Response Types in Web Services).

a. Dene the subclassMapping, a bean for dening what class is subclass of ActionData
<bean id="cxCmsActionDataSubclassMapping" parent="subclassMapping">
 <property name="parentClass" value="de.hybris.platform.personalizationfacades.data.ActionData" />
 <property name="subclassesSet" value="de.hybris.platform.personalizationcmsweb.data.CxCmsActionData" />
</bean>
b. Dene the fieldMapper, a bean for dening which source should be converted into which target class.

<bean id="cxCmsActionDataFieldMapper" parent="fieldMapper">
 <property name="sourceClass" value="de.hybris.platform.personalizationcmsweb.data.CxCmsActionData"/>
 <property name="destClass" value="de.hybris.platform.personalizationcmsweb.data.CxCmsActionData"/>
</bean>
c. Dene the fieldsetLevelMapping, the eldset denition for new data object.

<bean id="cxCmsActionFieldSetLevelMapping" parent="fieldSetLevelMapping"> <property name="dtoClass" value="de.hybris.platform.cxcmsweb.data.CxCmsActionWsDTO"/> <property name="levelMapping">
 <map>
 <entry key="BASIC" value="code,componentId"/> <entry key="DEFAULT" value="code,target,actionType,componentId"/> <entry key="FULL" value="code,target,targetHash,actionType,componentId"/>
 </map>
 </property>
</bean>
Implement Custom Mapping Learn how to dene your own mapping.

Context The recommended way to implement your own integration to an external system into the Personalization Module assumes the following steps.

Dene Populators Dene the populators for your mappers.

Procedure 1. There are several possibilities of creating your own mappers.

You can implement the Populator interface as presented below:
public class CxTestSuffixMapper implements Populator<List<String>, MappingData> { @Override public void populate(final List<String> data, final ProfileMappingData target) throws ConversionException
 {
 data.stream().map(s -> s + "-test").forEach(s -> {
 final SegmentMappingData segment = new SegmentMappingData();
 segment.setCode(s); target.getSegments().add(segment);
 });
 }
}
You can also simply extend one of the generic mappers provided out of the box:
public class CxTestScriptProfileMapper extends CxScriptProfileMapper<List<String>>
{
 //empty
}
2. Dene your populator in the Spring conguration
<bean id="cxTestFixedSegmentsProfileMapper" class="de.hybris.platform.personalizationintegration.mapping.mapper.impl.CxTestFixedSegmentsProfile
<bean id="cxTestScriptProfileMapper" class="de.hybris.platform.personalizationintegration.mapping.mapper.impl.CxTestScriptProfileMapper" parent
 <property name="scriptGroup" value="testGroup"/>
</bean>
<bean id="cxTestSuffixMapper" class="de.hybris.platform.personalizationintegration.mapping.mapper.impl.CxTestSuffixMapper"/>

## Dene Converters

Use the populators you have just dened to implement a new converter.

Procedure 1. Inject the newly created populators in your own converter.

<bean id="testIntegrationConverter" parent="abstractPopulatingConverter"> <property name="targetClass" value="de.hybris.platform.personalizationintegration.mapping.ProfileMappingData"/> <property name="populators">
 <list>
 <ref bean="cxTestFixedSegmentsProfileMapper"/>
 <ref bean="cxTestScriptProfileMapper"/>
 <ref bean="cxTestSuffixMapper"/>
 </list>
This is   For more    the SAP Help  97
 </property>
</bean>
2. Inject your new converter into the CxIntegrationMappingService by using the map merge directive.

<bean depends-on="cxIntegrationConvertersMap" parent="mapMergeDirective">
 <property name="key" value="testConverterName" />
 <property name="value" ref="testIntegrationConverter" />
</bean> 
3. Using the map merge directive registers your converter in DefaultCxIntegrationMappingService. In order to convert some external data using your converter through the service you just need to execute the following :
defaultCxIntegrationMappingService.mapExternalDataToSegments(testValues,"testConverterName");

## Commerce Customizations

The term commerce customization refers to non-cms actions that are performed when a user belongs to given target group. The commerce customizations functionality has been designed to allow extensibility so that any commerce customization may register itself in personalizationsmarteditCommerceCustomizationService service. This service is then used in personalizationsmarteditCommerceCustomizationView.

personalizationsmarteditCommerceCustomizationService The personalizationsmarteditCommerceCustomizationService service is a part of the personalizationsmarteditCommons module. Its main features are the following:
registerType: allows other modules to register a new commerce customization type as in the example below:
{
 type: String - type identifier, should be identical to type of action returned by web service, e.g. 'cxPromotionActionData',
 text: String - key for localized name of this type which will be displayed in 2),
 template: String - location of template which will be injected into commerce customization view when this type is selected, confProperty: String - configuration key which define if this type should be enabled or not, getName: function(action) - should return localized string describing given action. Only actions of this type will be provided as input }
getCommerceActionsCountMap(variation): returns a map of commerce customization types (as the key) and their count (as the value).

getCommerceActionsCount(variation): returns a number of commerce actions in a given variation. getNonCommerceActionsCount(variation): returns a number of non-commerce actions in a given variation.

Basing on confProperty and setConfigurationData, this service denes whether a registered type is available or not. If there is no registered type or all registered types are unavailable then the Commerce Customization view is also unavailable.

personalizationsmarteditCommerceCustomizationView The personalizationsmarteditCommerceCustomizationView view is available in the personalizationsmarteditCommerceCustomizationModule module. It uses the personalizationsmarteditCommerceCustomizationService to get available action types and it is also responsible for handling creating, editing or deleting actions. Commerce customizations registered in this view are able to add actions, which will be created when the save operation is executed. The $scope.addAction(actionBody, compareFunction) function accepts an object representing an action, which is used to create an action and compare function, which in turn determines if the two provided actions are identical or not.

Commerce Customizations Implementations Currently the commerce customizations functionality is implemented in the following way:
personalized promotions, used to assign promotions to selected target groups. For implementation details see personalizationsmarteditPromotionModule section in personalizationpromotionssmartedit Extension. personalized search proles, used to assign search proles (dened in Adaptive Search perspective in Backoffice Administration Cockpit) to selected target groups. For details, see Personalizationsearchsmartedit Extension section Personalization Search Module.

## Data Annotation And Retention In Personalization

Personalization segment data, when perceived as sensitive, should be included in the audit report and removed once the customer decides to close the account.

Data Annotation If you perceive segment data as sensitive, it is recommended to annotate it in the audit report conguration le. Follow the instructions on conguring the audit report in the creating report conguration section of Generic Data Report and Audit, and include the following conguration to make sure your data is properly annotated.

<type code="User">
...

 <virtual-attributes>
...

 <virtual-attribute expression="user" type="CxUserToSegment" many="true" displayName="cxUserToSegment"/>
...

 </virtual-attributes>
... </type> <type code="CxUserToSegment" displayName="CxUserToSegment">
 <atomic-attributes>
 <atomic-attribute qualifier="affinity" displayName="Affinity" />
 </atomic-attributes>
 <reference-attributes>
 <reference-attribute qualifier="segment" displayName="Segment" type="CxSegment" />
 </reference-attributes>
</type>
<type code="CxSegment" displayName="CxSegment"> <atomic-attributes> <atomic-attribute qualifier="code" displayName="code" /> </atomic-attributes> </type>
Data Retention When you use Personalization to collect the personal data of your customers, you may want to make sure the data is removed or anonymized after a certain period. The retention mechanisms provided by the Data Retention Framework included in the Platform help you do it.

The data removal mechanisms cover the following scenarios:
the user withdraws the consent, so the segments related to this user are no longer processed, no consent is given during segment update, so we store an empty list as user segment effectively erasing all segments related to the user, the user account is removed after retention period, so we remove all related data.

By adding a hook to the list of customerCleanupHooks we made sure that the user segment information is removed once the customerCleanupRelatedObjectsAction is executed. The action is dened in the yacceleratorcore extension and referenced by the customersWithOrdersRetentionCronJob/customersWithoutOrdersRetentionCronJob. For details on available cronJobs and Customer and Order Cleanup Hooking Mechanism, see Personal Data Erasure. For general information on the Data Retention Framework, see Data Retention.

cxCustomerSegmentRetentionJob It may happen that the user does not give consent for data processing or withdraws such a consent. Since consent management is supported, segment information is still in the system, even if the user doesn't visit the page again. To handle such situations we provide (as part of the personalization essential data) a cxCustomerSegmentRetentionJob cronjob, which is not triggered by default, but may be easily congured. The cron job is looking for all user to segment relations for users that did not give any consent or have withdrawn their consent for consent templates dened in all personalization conguration objects.

The user to segment relation is base site aware. It means that removing the data depends on personalization conguration for a specic base site.

The relation will be removed only if:
the personalization conguration for a specic base site requires consent, the user did not give any consent for required templates or has withdrawn consent for all required templates.

The relation will not be removed if:
there is no consent template dened in personalization conguration for base site the user has at least one active consent dened in the personalization congurations for a base site Removing Data for Several Base Sites Have a look at the following scenario to learn more about data removal in a situation when the user has access to several base sites.

The user dened in the system has access to many base sites.

Let's assume electronics site requires consent, and apparel-uk doesn't. The user visits apparel site, and doesn't give any consent, because it is not required. Additionally, the user visits the electronics site and gives the needed consent there.

At that moment customer have segments for electronics and apparel-uk.

Let's assume that later the user withdrew the consent for electronics. If the cronjob is executed, the system removes the user to segment relation only for electronics.

For general information on data deletion, see Deletion.

## Consent Templates In Personalization

The consent templates used in Personalization ensure that the customer gives consent to user data processing Every consent template is dened for a specic base site. You can add multiple consent templates for one CxConfig.

 Note Pay attention to the type of consent template you add for personalization. Anonymous users can see only the consent templates marked as exposed, and the system veries only such templates for user consent.

Personalized content can be evaluated only if the user gave consent to all the templates specied in your conguration that match the current basesite. Trying to add a template that doesn't match the base site (for example the apparel-de template for a personalization conguration set for apparel-uk base site) results in an exception. If no consent is set for a base site, the personalized content is calculated as if the user agreed to all the consent templates that were necessary.

 Note Withdrawing the consent for personalized content by manually removing the cookie may cause a delayed removal of personalization results. The delay depends on the calculation conguration and is especially noticeable when using ASYNC_PROCESS.

| Basesites for CxCong                                                                                                                                                          | Consent Templates in CxCong                                    | Consent Templates the user agreed too   | Is personalization content calculated?   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|-----------------------------------------|------------------------------------------|
| Electronics                                                                                                                                                                   | ElectronicsTemplate1                                           | -                                       | no                                       |
| Electronics                                                                                                                                                                   | ElectronicsTemplate1                                           | ElectronicsTemplate1                    | yes                                      |
| Electronics                                                                                                                                                                   | ElectronicsTemplate1 ElectronicsTemplate2 ElectronicsTemplate1 | no                                      |                                          |
| Electronics, Apparel                                                                                                                                                          | ElectronicsTemplate1, ApparelTemplate1                         | ApparelTemplate1                        | Apparel - yes, Electronics - no          |
| Electronics, Apparel                                                                                                                                                          | ApparelTemplate1                                               | ApparelTemplate1                        | yes (both)                               |
| You can easily dene the consent templates in the Backoffice Administration Cockpit under personalization conguration. For details, see Customize Personalization Conguration. |                                                                |                                         |                                          |

Disabling Personalized Content if no Consent Template was Selected As mentioned above, if no consent template is selected for a given base site, the personalized content for that basesite will be automatically calculated for every user. If you wish to disable personalized content when there is no consent template specied, set the following property to false:
personalizationservices.consent.ignoreConsentCheckWhenNoConsentTemplate=false For general information on consent management in accelerators, see User Consent.

## Personalization Core Trails

Personalization trails help you to get to know the functionality in details and to create your own solutions.

Personalization Core Trail Create a custom variation with a new trigger that is not available by default, using a custom scenario for an end-to-end implementation.

Extend Personalization in SmartEdit This trail demonstrates how to extend personalization functionality in the SmartEdit application.

## Personalization Core Trail

Create a custom variation with a new trigger that is not available by default, using a custom scenario for an end-to-end implementation. The personalization core trail covers the following aspects:
Exploring personalization installation. Implementing a new trigger for a variation to enable the variation based on a user group.

Making the new trigger type work with personalizationwebservices extension.

Scenario If customers belong to specic target group, they are able to see a specic homepage banner. To make this scenario work, you need to trigger a variation based on group which the customer belongs to.

Prerequisites For this trail, use a standard B2C Accelerator storefront with electronics store sample data. You can easily set up a local installation using the cx recipe. For details on installation procedure, refer to: Installing SAP Commerce Cloud Using Installer Recipes.

Recommended Reading For details on personalization concepts, refer to Personalization Module Concepts.

Procedure Navigate through the documentation to complete the trail:
Get to Know the Personalization Add personalizationtrail Extension Create a Trigger Type This is   For more    the SAP Help  100 Congure the User Group Trigger Retrieve Trigger Data Create Trigger Data using personalizationwebservices Extension Next Steps When you complete the personalization core trail you can move to Extend Personalization in SmartEdit, which shows you how to extend personalization functionality available in SmartEdit.

## Get To Know The Personalization

At this point you will get familiar with SAP Commerce Cloud and the Personalization. You can skip this step if you already have such knowledge.

Context The cx recipe contains all extensions required to successfully set up and congure the Personalization Module. In this trail you will be working with the electronics storefront.

Procedure 1. Set up the hosts. If you have administrator rights you should add the entries mentioned below to your hosts le. Modifying the hosts le allows the Accelerator to identify the sites
(the CMSSites) from the url.

Navigate to the le:
on Windows: c:\Windows\System32\drivers\etc\hosts; on a unix-based system: /etc/hosts.

and add the 127.0.0.1 electronics.local entry to the le.

2. Start the SAP Commerce Cloud server by executing the following commands a. For Windows: install.bat -r cx start from the installer directory or hybrisserver.bat from hybris/bin/platform directory b. For a unix-based system: ./install.sh -r cx start from the installer directory or ./hybrisserver.shfrom hybris/bin/platform directory.

3. Open your browser and provide the address to access the electronics store.

http://electronics.local:9001/yacceleratorstorefront http://localhost:9001/yacceleratorstorefront?site=electronics You can see the default electronics storefont.

![100_image_0.png](100_image_0.png)

 Note If you don't know the password, contact your system administrator.

This is   For more    the SAP Help  101 The main banner has changed. It is because the user canonlover@hybris.com belongs to Category Canon segment, which triggers canonlovervariation. The action defined for

![101_image_0.png](101_image_0.png)

The Personalization node is visible in the Explorer Tree on the left. You can now access all the sample data loaded in Personalization Module. For more details on Personaliza

Backoffice Administration Cockpit see: Configure Personalization .

![101_image_1.png](101_image_1.png)

Next Steps Proceed to: Add personalizationtrail Extension.

Add personalizationtrail Extension In this step you will create a custom extension using the the yempty template.

Context For the purpose of this trail, name your new extension the personalizationtrail extension. All customized code will be included in this extension.

Procedure 1. Create the new personalizationtrail extension using the yempty template. The package name should be de.hybris.personalizationtrail. For details on how to create a new extension, refer to Creating a New Extension.

2. Create a workspace using the IDE of your choice and import the personalizationtrail extension along with other required extensions. 3. Add your newly created extension to /config/localextensions.xml le.

<extension name="personalizationtrail"/>
This extension has to depend on the personalizationservices, personalizationfacades and personalizationwebservices extensions. Add these to extensioninfo.xml in your new extension and congure relation in your IDE.

<requires-extension name="personalizationservices"/> 
<requires-extension name="personalizationfacades"/> 
<requires-extension name="personalizationwebservices"/>
4. Build the SAP platform:
a. Go to hybris/plaftorm directory. b. Execute setantenv.bat (for Windows) or . ./setantenv.sh (for unix-based systems).

c. Run ant all command.

The platform is built.

Create a Trigger Type Dene the UserGroupTrigger type to dene actions for user groups.

Procedure 1. Add the following item denition to personalizationtrail-items.xml le:
<itemtype generate="true" code="UserGroupTrigger" jaloclass="de.hybris.personalizationtrail.jalo.UserGroupTrigger" extends="CxAbstractTrigger" <attributes>
 <attribute qualifier="userGroup" type="UserGroup" >
 <description>User group</description>
 <modifiers read="true" write="true" optional="false" initial="true" unique="false" />
 <persistence type="property" />
 </attribute>
 </attributes>
</itemtype>
2. When dening new types, you should also provide their localizations. To do this, add key=localized string entries in the type system localization le:
personalizationtrail/resources/localization/personalizationtrail-locales_en.properties.

type.UserGroupTrigger.name = User Group Trigger type.UserGroupTrigger.description = Variation trigger using UserGroup type.UserGroupTrigger.userGroup.name = UserGroup used by trigger type.UserGroupTrigger.userGroup.description = UserGroup used by trigger 3. Build your platform by running ant all command. 4. You should be able to nd UserGroupTriggerModel.java model that has just been generated.

5. Since you have modied the SAP Commerce Cloud Data Model (by modifying the items.xml le), you must update the system.

You have two possibilities of doing that:
run the ant updatesystem command, or start the SAP Commerce Cloud server and go to Platform Update in the Administration Console (https://localhost:9002/platform/update). Select only the following values: Update running system and Localize types. Then, click the Update button to start the process.

## Add Backoffice Conguration

Add the conguration for your new trigger type to view and manage it in Backoffice.

Procedure 1. Create the personalizationtrail-backoffice-config.xml le under /personalizationtrail/resources/ and copy the following backoffice conguration:
<config xmlns="http://www.hybris.com/cockpit/config" xmlns:y="http://www.hybris.com/cockpit/config/hybris" xmlns:wz="http://www.hybris.com/cockpitng/config/wizard-config" xmlns:explorer-tree="http://www.hybris.com/cockpitng/config/explorertree" xmlns:editorArea="http://www.hybris.com/cockpitng/component/editorArea" xmlns:list-view="http://www.hybris.com/cockpitng/component/listView" xmlns:advanced-search="http://www.hybris.com/cockpitng/config/advancedsearch" xmlns:simple-search="http://www.hybris.com/cockpitng/config/simplesearch"> <!-- Explorer tree configuration --> <context component="explorer-tree" merge-by="module" parent="auto" module="personalizationtrail"> <explorer-tree:explorer-tree> <explorer-tree:navigation-node id="cxnode">
 <explorer-tree:navigation-node id="cxtriggers">
 <explorer-tree:type-node code="UserGroupTrigger" id="usergrouptrigger" />
 </explorer-tree:navigation-node>
 </explorer-tree:navigation-node>
 </explorer-tree:explorer-tree>
 </context>
 
 <!-- UserGroupTrigger configuration -->
 <!-- Base configuration -->
 <context type="UserGroupTrigger" component="base" merge-by="type" parent="CxAbstractTrigger"> <y:base> <y:labels> <y:label>code + " (" + variation.code+","+userGroup.uid +")" + " : " + catalogVersion.version</y:label> </y:labels> </y:base>
 </context>
 <!-- Editor area configuration -->
 <context type="UserGroupTrigger" component="editor-area" merge-by="type" parent="CxAbstractTrigger" >
 <editorArea:editorArea>
 <editorArea:tab name="backoffice.personalizationservices.properties">
 <editorArea:section name="backoffice.personalizationservices.section.attributes">
 <editorArea:attribute qualifier="userGroup" />
 </editorArea:section>
 </editorArea:tab>
 </editorArea:editorArea>
 </context>
 <!-- List view configuration -->
 <context type="UserGroupTrigger" component="listview" merge-by="type" parent="CxAbstractTrigger" > <list-view:list-view> <list-view:column qualifier="userGroup" /> </list-view:list-view> </context> <!-- Advanced search configuration -->
 <context type="UserGroupTrigger" component="advanced-search" merge-by="type" parent="CxAbstractTrigger" >
 <advanced-search:advanced-search>
 <advanced-search:field-list>
 <advanced-search:field name="userGroup" selected="true" />
 </advanced-search:field-list>
 </advanced-search:advanced-search>
 </context>
 <!-- Simple search configuration -->
 <context type="UserGroupTrigger" component="simple-search" merge-by="type" parent="CxAbstractTrigger" >
 <simple-search:simple-search> <simple-search:field name="code" /> </simple-search:simple-search> </context> </config>
2. Add localization to the congured type node.

Create the personalizationtrail-backoffice-spring.xml le under /personalizationtrail/resources/ and add the following backoffice spring conguration:
<?xml version="1.0" encoding="UTF-8"?> <beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
 <bean id="personalizationtrailbackofficeLabelLocator" class="com.hybris.cockpitng.util.labels.ResourcesLabelLocator" scope="singleton" init
 <property name="location" value="/personalizationtrail-backoffice-labels/"/>
 <property name="name" value="labels"/>
 </bean>
This is   For more    the SAP Help  104
</beans>
3. Mark the personalizationtrail extension as the backoffice module by adding <meta key="backoffice-module" value="true"/> line to extensioninfo.xml le as shown below.

<extensioninfo xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="extensioninfo.xsd">
 <extension abstractclassprefix="Generated" classprefix="Personalizationtrail" managername="PersonalizationtrailManager" managersuperclass="
 ... 

 <meta key="backoffice-module" value="true"/>
 </extension> 
</extensioninfo>
4. Create the /personalizationtrail/resources/personalizationtrail-backoffice-labels/labels_en.properties le and add the following line:
usergrouptrigger=User Group Triggers 5. Build the SAP Commerce Cloud platform by running ant all command. 6. Start the SAP Commerce Cloud server and go to Backoffice Administration Cockpit by entering the following address: https://localhost:9002/backoffice. You should see a new node under Personalization Triggers called the User Group Triggers. If you cannot see the node, perform the following steps a. Click F4. b. Click the SAP Commerce Cloud icon in the right upper corner.

c. Select Reset Everything option from menu.

d. Go back to the standard view by pressing F4.

Next Steps Proceed to the next step: Congure the User Group Trigger.

Congure the User Group Trigger Integrate your trigger with personalization functionality. Learn how to implement a trigger strategy and dene a trigger DAO, which helps the trigger strategy to nd the required data.

Dene Trigger DAO
Procedure 1. Create a UserGroupTriggerDao.java le in the /personalizationtrail/src/de/hybris/personalizationtrail/trigger/dao/ directory.

package de.hybris.personalizationtrail.trigger.dao; import de.hybris.platform.catalog.model.CatalogVersionModel; import de.hybris.platform.core.model.user.UserGroupModel; import de.hybris.platform.personalizationservices.model.CxVariationModel; import de.hybris.platform.servicelayer.internal.dao.Dao; import java.util.Collection; import java.util.Set; public interface UserGroupTriggerDao extends Dao
{
 /**
 * Selects variations which can be triggered for given user groups. Should respect given catalog version.

 *
 * @param userGroups * groups for which variations should be selected * @param catalogVersion * from which variation will be returned * @return collection of valid variations */
 Collection<CxVariationModel> findApplicableVariations(Set<UserGroupModel> userGroups, CatalogVersionModel catalogVersion);
}
2. Create a default implementation for UserGroupTriggerDao by creating a DefaultUserGroupTriggerDao.java le and placing it in
/personalizationtrail/src/de/hybris/personalizationtrail/trigger/dao/impl/ directory.

package de.hybris.personalizationtrail.trigger.dao.impl; import de.hybris.personalizationtrail.model.UserGroupTriggerModel; import de.hybris.personalizationtrail.trigger.dao.UserGroupTriggerDao; import de.hybris.platform.catalog.model.CatalogVersionModel; import de.hybris.platform.core.model.user.UserGroupModel; import de.hybris.platform.personalizationservices.dao.impl.AbstractCxDao; import de.hybris.platform.personalizationservices.model.CxVariationModel; import de.hybris.platform.servicelayer.util.ServicesUtil; import java.util.Collection; import java.util.HashMap; import java.util.Map; import java.util.Set; public class DefaultUserGroupTriggerDao extends AbstractCxDao<UserGroupTriggerModel> implements UserGroupTriggerDao
{ public static final String FIND_VARIATIONS_QUERY = " SELECT {v." + CxVariationModel.PK + "} " + " FROM { "
This is   For more    the SAP Help  105
 + CxVariationModel._TYPECODE + " as v " + " JOIN " + UserGroupTriggerModel._TYPECODE + " as t on {t."
 + UserGroupTriggerModel.VARIATION + "} = {v." + CxVariationModel.PK + "} " + " } " + " WHERE {v."
 + CxVariationModel.CATALOGVERSION + "} = ?catalogVersion " + " AND {t." + UserGroupTriggerModel.CATALOGVERSION
 + "} = ?catalogVersion " + " AND {t." + UserGroupTriggerModel.USERGROUP + "} IN (?usergroups) ";
 public DefaultUserGroupTriggerDao()
 {
 super(UserGroupTriggerModel._TYPECODE);
 }
 @Override public Collection<CxVariationModel> findApplicableVariations(final Set<UserGroupModel> userGroups, final CatalogVersionModel catalogVersion)
 { ServicesUtil.validateParameterNotNull(userGroups, "userGroups must not be null"); ServicesUtil.validateParameterNotNull(catalogVersion, "catalogVersion must not be null");
 final Map<String, Object> params = new HashMap<String, Object>();
 params.put("usergroups", userGroups);
 params.put("catalogVersion", catalogVersion);
 return queryList(FIND_VARIATIONS_QUERY, params);
 }
}
3. Add the following bean denition in /personalizationtrail/resources/personalizationtrail-spring.xml le.

<alias name="defaultUserGroupTriggerDao" alias="userGroupTriggerDao"/>
<bean id="defaultUserGroupTriggerDao" parent="baseCxDao" class="de.hybris.personalizationtrail.trigger.dao.impl.DefaultUserGroupTriggerDao" />
4. Execute the ant all command to build the SAP Commerce Cloud platform.

## Implement Trigger Strategy

Procedure 1. Create the DefaultUserGroupTriggerStrategy.java le, which includes the trigger strategy implementation. Place the le in the
/personalizationtrail/src/de/hybris/personalizationtrail/trigger/strategy/impl/ directory.

package de.hybris.personalizationtrail.trigger.strategy.impl; import de.hybris.personalizationtrail.trigger.dao.UserGroupTriggerDao; import de.hybris.platform.catalog.model.CatalogVersionModel; import de.hybris.platform.core.model.user.UserGroupModel; import de.hybris.platform.core.model.user.UserModel; import de.hybris.platform.personalizationservices.model.CxVariationModel; import de.hybris.platform.personalizationservices.trigger.strategy.CxTriggerStrategy; import de.hybris.platform.servicelayer.user.UserService; import java.util.Collection; import java.util.Set; import org.springframework.beans.factory.annotation.Required; public class DefaultUserGroupTriggerStrategy implements CxTriggerStrategy
{
 private UserService userService; private UserGroupTriggerDao userGroupTriggerDao;
 @Override public Collection<CxVariationModel> getVariations(final UserModel user, final CatalogVersionModel catalogVersion)
 {
 final Set<UserGroupModel> usersGroup = userService.getAllUserGroupsForUser(user);
 return userGroupTriggerDao.findApplicableVariations(usersGroup, catalogVersion);
 }
 @Required public void setUserService(final UserService userService) { this.userService = userService; } @Required public void setUserGroupTriggerDao(final UserGroupTriggerDao userGroupTriggerDao)
 {
 this.userGroupTriggerDao = userGroupTriggerDao;
 }
}
2. Add the bean denition to the /personalizationtrail/resources/personalizationtrail-spring.xml le.

<bean id="userGroupTriggerStrategy" class="de.hybris.personalizationtrail.trigger.strategy.impl.DefaultUserGroupTriggerStrategy">
 <property name="userService" ref="userService" />
 <property name="userGroupTriggerDao" ref="userGroupTriggerDao" />
</bean>
3. Run the ant all command to build the SAP Commerce Cloud platform.

Test the UserGroupTrigger Context At this point you should have implemented all things needed to make your new trigger work. To verify it we need to import some sample data to the system. In this trail part, you will use the impex import but you can also dene the sample data in the Backoffice Administration Cockpit.

Procedure 1. Download the Banners ZIP le, which includes: userGroupBanner_1400W.jpg, userGroupBanner_960W.jpg, userGroupBanner_770W.jpg, and userGroupBanner_480W.jpg. Unzip the le and copy the four banners to /personalizationtrail/resources/personalizationtrail/import/images/banners directory.

2. Start the SAP Commerce Cloud server and go to Console/ImpEx Import in the SAP Commerce Cloud Administration Console
(https://localhost:9002/console/impex/import). Paste the following code in the Import content tab and click Import content button.

ImpEx File
$contentCatalog=electronicsContentCatalog
$contentCV=catalogVersion(CatalogVersion.catalog(Catalog.id[default=$contentCatalog]),CatalogVersion.version[default=Staged])[default=$contentC
$siteResource=jar:de.hybris.personalizationtrail.constants.PersonalizationtrailConstants&/personalizationtrail/import
$medias=medias(code, $contentCV); $mediaContainer=media(qualifier, $contentCV); INSERT_UPDATE UserGroup;uid[unique=true];groups(uid);members(uid);
;personalizedUserGroup1;;;
;personalizedUserGroup2;;;
INSERT_UPDATE Customer;uid[unique=true];groups(uid);password[default=$defaultPassword];name;
;customer1@hybris.com;customergroup,personalizedUserGroup1;;John Doe;
;customer2@hybris.com;customergroup,personalizedUserGroup2;;John Doe; INSERT_UPDATE CxCustomization;code[unique=true];name;$contentCV[unique=true];group(code,$contentCV)[default='electronicsCustomizationGroup'];st
;Banner;Banner;;
INSERT_UPDATE CxVariation;code[unique=true];name;$contentCV[unique=true];enabled[default=true];customization(code,$contentCV)[unique=true];&var
;variationForUserGroup;variationForUserGroup;;;Banner;variationForUserGroup INSERT_UPDATE UserGroupTrigger;code[unique=true];variation(code,$contentCV)[unique=true];$contentCV[unique=true];userGroup(uid);
;userGroupTrigger;variationForUserGroup;;personalizedUserGroup1; INSERT_UPDATE Media;mediaFormat(qualifier);code[unique=true];@media[translator=de.hybris.platform.impex.jalo.media.MediaDataTranslator][forceWr
;mobile;userGroupBanner_480W.jpg;$siteResource/images/banners/userGroupBanner_480W.jpg;userGroupBanner_480W.jpg;"Save Big On Select SLR & DSLR 
;tablet;userGroupBanner_770W.jpg;$siteResource/images/banners/userGroupBanner_770W.jpg;userGroupBanner_770W.jpg;"Save Big On Select SLR & DSLR 
;desktop;userGroupBanner_960W.jpg;$siteResource/images/banners/userGroupBanner_960W.jpg;userGroupBanner_960W.jpg;"Save Big On Select SLR & DSLR ;widescreen;userGroupBanner_1400W.jpg;$siteResource/images/banners/userGroupBanner_1400W.jpg;userGroupBanner_1400W.jpg;"Save Big On Select SLR INSERT_UPDATE MediaContainer;qualifier[unique=true];$medias;$contentCV[unique=true]
;variationForUserGroupMediaContainer;userGroupBanner_480W.jpg,userGroupBanner_770W.jpg,userGroupBanner_960W.jpg,userGroupBanner_1400W.jpg INSERT_UPDATE SimpleResponsiveBannerComponent;$contentCV[unique=true];uid[unique=true];$mediaContainer;name;urlLink;&componentRef
;;variationForUserGroupComponent;variationForUserGroupMediaContainer;Electronics Homepage Splash Banner Component;/OpenCatalogue/Cameras/Digita UPDATE CxCmsComponentContainer;$contentCV[unique=true];uid[unique=true];simpleCMSComponents(&componentRef)[mode=append] ;;Section1SlotHomepageCxContainer;variationForUserGroupComponent INSERT_UPDATE CxCmsAction;containerId;componentId;code[unique=true];type(code);target;variation(&variationRef);$contentCV[unique=true]
;Section1SlotHomepageCxContainer;variationForUserGroupComponent;userGroupAction;PLAIN;cxCmsActionPerformable;variationForUserGroup; 3. Verify if the data was loaded in the Backoffice Administration Cockpit. Navigate to Personalization Triggers User Group Triggers to see your new trigger.

4. You have loaded the personalization data for the Staged version of Content Catalog. So if you now log in to the electronics storefront as customer1@hybris.com and the password dened for that user, the changes will not be visible because you need to sychronize the catalog version rst. Perform the following steps:
a. Navigate to the Backoffice Administration Cockpit.

b. Select Catalog/Catalog Versions.

c. Edit Electronics Content Catalog - Staged.

d. Run Catalog Synchronization from the action toolbar.

5. Verify that user group trigger is working by logging in as customer1@hybris.com You should see that the banner has changed

![107_image_0.png](107_image_0.png)

Next Steps Proceed to the next step: Retrieve Trigger Data.

## Retrieve Trigger Data

The personalizationwebservices extension contains the personalization api which allows the introduction of changes to the customer experience data model using the REST calls. You will need to add some changes to make the API endpoint work also for your new trigger type.

 Note For more information on personalizationwebservices Extension, refer to: personalizationwebservices Extension.

## Create Data Transferring Objects

Procedure 1. Create the UserGroupTriggerData data transfer objects. You should create the Data objects in a declarative way in an xml le used as input for code generating. Extend the standard TriggerData with an additional userGroupUid attribute.

Add the following denition to personalizationtrail/resources/personalizationtrail-beans.xml le.

<bean class="de.hybris.personalizationtrail.data.UserGroupTriggerData" extends="de.hybris.platform.personalizationfacades.data.TriggerData"> <property name="userGroupUid" type="String" /> </bean>
2. Run ant all command and refresh the workspace. Have a look at the UserGroupTriggerData data object class that was created.

## Dene Converters And Populators

Procedure 1. Create a UserGroupTriggerPopulator.java le that holds a populator for the new attributes. Place the le under the following directory:
/personalizationtrail/src/de/hybris/personalizationtrail/trigger/converters/populator/.

package de.hybris.personalizationtrail.trigger.converters.populator; import de.hybris.personalizationtrail.data.UserGroupTriggerData; import de.hybris.personalizationtrail.model.UserGroupTriggerModel; import de.hybris.platform.converters.Populator; import de.hybris.platform.servicelayer.dto.converter.ConversionException; import org.springframework.util.Assert; public class UserGroupTriggerPopulator implements Populator<UserGroupTriggerModel, UserGroupTriggerData>
{
 @Override This is   For more    the SAP Help  108 public void populate(final UserGroupTriggerModel source, final UserGroupTriggerData target) throws ConversionException
 {
 Assert.notNull(source, "Parameter source cannot be null.");
 Assert.notNull(target, "Parameter target cannot be null.");
 target.setUserGroupUid(source.getUserGroup().getUid());
 }
}
2. Dene the converter and populator in the Spring context using the following le: /personalizationtrail/resources/personalizationtrail-spring.xml The converter dened below is a special type of converter, allowing you to choose the convertion option. It is very useful because sometimes you do not need all the trigger information - for example when you convert the trigger as part of the variation object. Thanks to that you can use the same converter in various situations. This converter supports also the subtype conversion used in facades. For details on this conversion mechanism see: personalizationfacades Extension.

<!-- UserGroupTrigger converter and populators -->
<bean id="userGroupTriggerPopulator" class="de.hybris.personalizationtrail.trigger.converters.populator.UserGroupTriggerPopulator" /> <bean id="userGroupTriggerForVariationPopulators" parent="abstractPopulatorList" >
 <property name="populators">
 <list>
 <ref bean="cxTriggerPopulator" />
 <ref bean="userGroupTriggerPopulator" />
 </list>
 </property>
</bean> <bean id="userGroupTriggerFullPopulators" parent="abstractPopulatorList" >
 <property name="populators">
 <list> <ref bean="cxTriggerPopulator" /> <ref bean="cxTriggerWithVariationPopulator" /> <ref bean="userGroupTriggerPopulator" /> </list> </property>
</bean> <bean id="userGroupTriggerConfigurableConverter" parent="cxSubtypeConverter" >
 <constructor-arg name="markerClass" value="de.hybris.platform.personalizationfacades.trigger.converters.TriggerConverter" />
 <constructor-arg name="sourceClass" value="de.hybris.personalizationtrail.model.UserGroupTriggerModel" />
 <property name="targetClass" value="de.hybris.personalizationtrail.data.UserGroupTriggerData" />
 <property name="populators">
 <map key-type="de.hybris.platform.personalizationfacades.enums.TriggerConversionOptions">
 <entry key="BASE" value-ref="cxTriggerPopulators" />
 <entry key="FOR_VARIATION" value-ref="userGroupTriggerForVariationPopulators" /> <entry key="FULL" value-ref="userGroupTriggerFullPopulators" /> </map> </property> </bean>
3. Run ant allcommand to build the platform.

## Congure The Mapping Mechanism

Context The trigger endpoint exposes a method which declares returning a general object (TriggerData object), however it can also return specic object (a subclass object). Because of that you need to add some information in yout conguration to enable the subclass mapping. For details on mapping see: Dynamic Response Types in Web Services.

Procedure 1. Dene subclassMapping, a bean used for dening which class is the subclass of the TriggerData class.

Add the following denition to the personalizationtrail/resources/personalizationtrail-spring.xml le.

<bean id="userGroupTriggerSubclassMapping" parent="subclassMapping">
 <property name="parentClass" value="de.hybris.platform.personalizationfacades.data.TriggerData" />
 <property name="subclassesSet" value="de.hybris.personalizationtrail.data.UserGroupTriggerData" /> </bean>
2. Dene the fieldMapper, a bean for dening which source should be converted into which target class.

Add the following denition to the personalizationtrail/resources/personalizationtrail-spring.xml le.

<bean id="userGroupTriggerDataFieldMapper" parent="fieldMapper">
 <property name="sourceClass" value="de.hybris.personalizationtrail.data.UserGroupTriggerData"/>
 <property name="destClass" value="de.hybris.personalizationtrail.data.UserGroupTriggerData"/> </bean>
3. Dene the fieldsetLevelMapping, a eldset denition for the new data object.

Add the following denition to personalizationtrail/resources/personalizationtrail-spring.xml le.

<bean id="userGroupTriggerDataFieldSetLevelMapping" parent="fieldSetLevelMapping" >
 <property name="dtoClass" value="de.hybris.personalizationtrail.data.UserGroupTriggerData"/>
 <property name="levelMapping"> <map>
This is   For more    the SAP Help  109
 <entry key="BASIC" value="code"/>
 <entry key="DEFAULT" value="code,userGroupUid,variation(DEFAULT)"/>
 <entry key="FULL" value="code,userGroupUid,variation(FULL)"/>
 </map>
 </property>
</bean>
4. Start the SAP Commerce Cloud server.

## Test Personalizationwebservices Extension

Context Follow the steps to verify if the personalizationwebservices extension works properly.

Procedure 1. The personalizationwebservices extension uses the OAuth2 authorization mechanism. You need the OAuth token to be able call web services API. Because the OAuth client is not dened in the system by default, you need to dene it. Start SAP Commerce Cloud and go to Console/ImpEx Import in theSAP Commerce Cloud Administration Cockpit. You can use the following link: https://localhost:9002/console/impex/export.

Paste following code in the Import content tab and click the Import content button.

INSERT_UPDATE OAuthClientDetails;clientId[unique=true] ;resourceIds ;scope ;authorizedGrantTypes ;oauth_client ;hybris ;basic,personalizationwebservices ;refresh_token,password,cli 2. Retrieve the OAuth token using your favorite REST client or cURL.

curl --insecure --verbose https://localhost:9002/authorizationserver/oauth/token --request POST --data "client_id=oauth_client&client_secret=se The response should be as follows:
{ "access_token":"32f0d12f-296a-427b-a958-f7b63b7aa926", "token_type":"bearer", "refresh_token":"2cbe91b7-0f33-4f33-bde0-427b95c81da1", "expires_in":42990,
 "scope":"basic"
}
 Note The generated access token may differ from the one used an example above. Once the access token is generated for you, you can use it in further calls.

3. Try to send sample requests to make sure that the personalizationwebservices works correctly. For details about available requests, see the Endpoints section of personalizationwebservices Extension.

a. Get information about the sample variation. If you use cURL to do so, enter the following command:
curl --insecure --verbose --header "Authorization: Bearer *<ACCESS_TOKEN_FROM_PREVIOUS_STEP>*" https://localhost:9002/personalizationwebser The response should look as follows:
{ "actions" : [ { "type" : "cxCmsActionData", "code" : "userGroupAction" } ], "active" : true,
 "code" : "variationForUserGroup",
 "enabled" : true,
 "name" : "variationForUserGroup",
 "rank" : 4,
 "triggers" : [ {
 "type" : "userGroupTriggerData",
 "code" : "userGroupTrigger"
 } ]
}
b. Get the trigger information.

If you use cURL, enter the following information:
curl --insecure --verbose --header "Authorization: Bearer *<ACCESS_TOKEN_FROM_PREVIOUS_STEP>*" https://localhost:9002/personalizationwebse The response should look as follows:
{
 "type" : "userGroupTriggerData",
 "code" : "userGroupTrigger",
 "userGroupUid" : "personalizedUserGroup1" }
c. Get the selected information about the trigger.

If you use cURL, use the following command:
curl --insecure --verbose --header "Authorization: Bearer *<ACCESS_TOKEN_FROM_PREVIOUS_STEP>*" https://localhost:9002/personalizationwebser You should receive the following response:
{
 "type" : "userGroupTriggerData",
 "userGroupUid" : "personalizedUserGroup1" }
Next Steps Proceed to the next step: Create Trigger Data using personalizationwebservices Extension Related Information OAuth 2.0 Create Trigger Data using personalizationwebservices Extension Follow the steps described below to create Trigger Data with the help of personalizationwebservices extension.

Dene Reverse Converter and Populator Procedure 1. Create the UserGroupTriggerReversePopulator.java to dene the reverse populator for new attributes.

Place your conguration in the following directory: /personalizationtrail/src/de/hybris/personalizationtrail/trigger/converters/populator/
package de.hybris.personalizationtrail.trigger.converters.populator; import de.hybris.personalizationtrail.data.UserGroupTriggerData; import de.hybris.personalizationtrail.model.UserGroupTriggerModel; import de.hybris.platform.converters.Populator; import de.hybris.platform.core.model.user.UserGroupModel; import de.hybris.platform.servicelayer.dto.converter.ConversionException; import de.hybris.platform.servicelayer.user.UserService; import org.springframework.beans.factory.annotation.Required; import org.springframework.util.Assert; public class UserGroupTriggerReversePopulator implements Populator<UserGroupTriggerData, UserGroupTriggerModel>
{
 private UserService userService;
 @Override public void populate(final UserGroupTriggerData source, final UserGroupTriggerModel target) throws ConversionException { Assert.notNull(source, "Parameter source cannot be null."); Assert.notNull(target, "Parameter target cannot be null."); final UserGroupModel userGroup = userService.getUserGroupForUID(source.getUserGroupUid()); target.setUserGroup(userGroup);
 }
 public UserService getUserService()
 {
 return userService;
 }
 @Required public void setUserService(final UserService userService)
 {
 this.userService = userService;
 }
}
2. Dene the reverse converter and populator in the Spring context: /personalizationtrail/resources/personalizationtrail-spring.xml.

The reverse converter dened below supports subtype conversion used in facades. For detailed information on the conversion mechanism see: personalizationfacades Extension.

<bean id="userGroupTriggerReversePopulator" class="de.hybris.personalizationtrail.trigger.converters.populator.UserGroupTriggerReversePopulator <property name="userService" ref="userService" /> </bean> <bean id="userGroupTriggerReversePopulators" parent="abstractPopulatorList" > <property name="populators"> <list>
 <ref bean="cxTriggerReversePopulators" />
 <ref bean="userGroupTriggerReversePopulator" />
 </list>
 </property>
</bean>
<bean id="userGroupTriggerReverseConverter" parent="cxSubtypeConverter">
This is   For more    the SAP Help  111

 <constructor-arg name="markerClass" value="de.hybris.platform.personalizationfacades.trigger.converters.TriggerReverseConverter" />
 <constructor-arg name="sourceClass" value="de.hybris.personalizationtrail.data.UserGroupTriggerData" />
 <property name="targetClass" value="de.hybris.personalizationtrail.model.UserGroupTriggerModel" />
 <property name="populators">
 <map>
 <entry key="BASE" value-ref="userGroupTriggerReversePopulators"/>
 </map>
 </property>
</bean>

## Dene The Validator

Context The input data for created object should be validated. The trigger endpoint dened in personalizationwebservices is able to support subtype validation. For detailed information on subtype validation see the Validation section in: Dynamic Response Types in Web Services.

Procedure 1. Create /personalizationtrail/src/de/hybris/personalizationtrail/trigger/validator/UserGroupTriggerDataValidator.java class which implements the TriggerValidator inteface.

package de.hybris.personalizationtrail.trigger.validator; import de.hybris.personalizationtrail.data.UserGroupTriggerData; import de.hybris.platform.personalizationwebservices.validator.TriggerValidator; import org.springframework.validation.Errors; import org.springframework.validation.ValidationUtils; public class UserGroupTriggerDataValidator implements TriggerValidator
{
 @Override public boolean supports(final Class<?> arg0)
 {
 return UserGroupTriggerData.class.isAssignableFrom(arg0);
 }
 @Override public void validate(final Object target, final Errors errors)
 {
 ValidationUtils.rejectIfEmpty(errors, "userGroupUid", "field.required");
 } }
2. Dene the trigger validator bean by adding the following denition to personalizationtrail/resources/personalizationtrail-spring.xml le.

<bean id="userGrouptTriggerValidator" class="de.hybris.personalizationtrail.trigger.validator.UserGroupTriggerDataValidator" />
3. Run the ant all command to build the SAP Commerce Cloud platform.

Create a New Trigger Procedure 1. Try to create a new trigger without the userGroupUid to verify that the validator works properly.

If you use cURL, execute the following command:
curl --insecure --verbose --header "Authorization: Bearer *<ACCESS_TOKEN>*" --header "Content-Type: application/json" https://localhost:9002/pers You should get the following error info:
{
 "errors" : [ {
 "message" : "This field is required.",
 "reason" : "missing",
 "subject" : "userGroupUid",
 "subjectType" : "parameter",
 "type" : "ValidationError"
 } ]
}
2. Create a trigger for personalizedUserGroup2.

If you use cURL, execute the following command:
curl --insecure --verbose --header "Authorization: Bearer *<ACCESS_TOKEN>*" --header "Content-Type: application/json" https://localhost:9002/pers 3. Verify if the trigger was created.

If you use cURL, execute the following command:
curl --insecure --verbose --header "Authorization: Bearer *<ACCESS_TOKEN>*" https://localhost:9002/personalizationwebservices/v1/catalogs/electro 4. Verify if the new trigger is working.

a. Because you have created the trigger for the Staged version of the Content Catalog, you need to synchronize the catalog version.

Navigate to the Backoffice Administration Cockpit Select Catalog/Catalog Versions node Edit the Electronics Content Catalog - Staged Run the Catalog Synchronization from the action toolbar b. Verify if the user group trigger is working.

Go to electronics storefront and login as customer2@hybris.com. You should see that the banner on the Homepage has changed (customer2@hybris.com belongs to personalizedUserGroup2).

Next Steps Congratulations! You have sucessfully completed the trail.

Extend Personalization in SmartEdit This trail demonstrates how to extend personalization functionality in the SmartEdit application.

Scenario After the trail is completed, you can use an additional tab in the Target Group modal in SmartEdit to add triggers of a new type.

Prerequisites You have completed Personalization Core Trail, because you need to use the User Group Trigger in this scenario.

Recommended Reading Get to Know Personalization Mode Create a Customized Storefront Procedure Navigate through the documentation to complete the trail:
Introduction Create personalizationsmartedittrail Extension Create the Component For Customer Group Trigger Denition Add the ITriggerTab Verify the Conguration Introduction Familiarize yourself with the personalization functionality before you start extending it.

Create personalizationsmartedittrail Extension Create a custom extension using the the ysmarteditmodule template.

Create the Component For Customer Group Trigger Denition Create an angular component which allows you to create a customer group trigger from the SmartEdit application. Add the ITriggerTab Add an additional tab to the Target Group modal so that you can congure the customer group trigger.

Verify the Conguration Verify if the tab for the new trigger type is displayed.

## Introduction

Familiarize yourself with the personalization functionality before you start extending it.

Prerequisites You have created the variationForUserGroup trigger by performing steps in Congure the User Group Trigger.

Procedure 1. Go to https://localhost:9002/smartedit 2. Display the homepage for the Electronics Staged catalog 3. Select Personalization for the top right menu.

4. Go to Library Manage Library 5. On the list, go to CategoryLovers canonLover and edit it.

This is   For more    the SAP Help  113

![113_image_0.png](113_image_0.png)

Next Steps
In the next steps of the trail, you will extend the personalization configuration to enable Target Group for customers belonging to the selected customer group.

Create personalizationsmartedittrail Extension Create a custom extension using the the ysmarteditmodule template. Procedure 1. Use the instructions in Creating a New Extension to create personalizationsmarted it trail extension using the ysmarted it module template. Use the
e complete and the cont 2. Add your new extension to /config/localextensions.xml file.

This is custom documentation. For more information, please visit the SAP Help Portal
<extension name="personalizationsmartedittrail"/>
3. Add the dependency to personalizationsmartedit extension to the extensioninfo.xml le in your new extension and congure the relation in your IDE.

<requires-extension name="personalizationsmartedit"/>
4. Install the npm modules in order to enable full build and test capabilities.

ant npminstall 5. Clean up the sample code:
Delete the personalizationsmartedittrail/web/features/personalizationsmartedittrail/abAnalyticsDecorator directory. Delete the personalizationsmartedittrail/web/features/personalizationsmartedittrailContainer/abAnalyticsToolbarItem directory.

Delete the personalizationsmartedittrail/jsTests/tests/personalizationsmartedittrail/unit/features/abAnalyticsDecoratorControllerTest.js file. Delete the personalizationsmartedittrail/jsTests/tests/personalizationsmartedittrailcommons/unit/features/abAnalyticsServiceTest.js le.

Replace the code in personalizationsmartedittrail/web/features/personalizationsmartedittrail/personalizationsmartedittrailModule.ts with the following:
import {doImport} from './forcedImports';
doImport();
import {SeModule} from 'smarteditcommons';
/** * @ngdoc overview * @name personalizationsmartedittrail * @description * Placeholder for documentation
 */
@SeModule({
 imports: [
 ],
 initialize: () => { // Parameters are injected factory methods
 'ngInject';
 }
})
export class Personalizationsmartedittrail {}
Replace the code in personalizationsmartedittrail/web/features/personalizationsmartedittrailContainer/personalizationsmartedittrailcontainerModule.ts with the following code:
import {doImport} from './forcedImports';
doImport();
import {SeModule} from 'smarteditcommons'; /**
 * @ngdoc overview
 * @name personalizationsmartedittrailContainer
 * @description
 * Placeholder for documentation
 */
@SeModule({ imports: [ ], initialize: () => { 'ngInject'; }
})
export class PersonalizationsmartedittrailContainer {}
6. Uncomment the content of personalizationsmartedittrail/resources/impex/essentialdata_personalizationsmartedittrail.impex for the module to be loaded to SmartEdit.

INSERT_UPDATE SmartEditConfiguration;key[unique=true];value
;applications.personalizationsmartedittrail;{"smartEditLocation":"/personalizationsmartedittrail/personalizationsmartedittrail/js/personalizati
;applications.personalizationsmartedittrailContainer;{"smartEditContainerLocation":"/personalizationsmartedittrail/personalizationsmartedittrai 7. Stop the SAP server. 8. Build the SAP platform.

ant clean build 9. Update the system.

ant updatesystem 10. Start the SAP server.

This is   For more    the SAP Help  115

## Create The Component For Customer Group Trigger Denition

Create an angular component which allows you to create a customer group trigger from the SmartEdit application.

Procedure 1. Create the personalizationsmartedittrail/customerGroupTriggerTemplate.html le in the web/features/personalizationsmartedittrailContainer/customerGroupTriggerComponent directory.

<div>
 <label class="personalization-modal__label" data-translate="personalizationsmartedittrail.customergroup.label"></label>
 <y-select data-ng-model="$ctrl.selectedId" data-on-select="$ctrl.ySelectOnSelect" data-fetch-strategy="$ctrl.ySelectFetchStrategy" data-search-enabled="false" /> </div>
2. Create the CustomerGroupTriggerComponent.ts le in personalizationsmartedittrail/web/features/personalizationsmartedittrailContainer/customerGroupTriggerComponent.

/*
 * [y] hybris Platform
 *
 * Copyright (c) 2018 SAP SE or an SAP affiliate company. All rights reserved. * * This software is the confidential and proprietary information of SAP * ("Confidential Information"). You shall not disclose such Confidential * Information and shall use it only in accordance with the terms of the * license agreement you entered into with SAP.

 */ import {SeComponent} from 'smarteditcommons';
@SeComponent({
 templateUrl: 'customerGroupTriggerTemplate.html'
})
export class CustomerGroupTriggerComponent {
 public selectedId: string; public ySelectFetchStrategy = { fetchAll: this.fetchAll.bind(this) }; public ySelectOnSelect = this.onSelect.bind(this); private customerGroups: any; private triggerDataState: any; private initialTriggerData: any = null; private triggerData: any = null; constructor( public $q: angular.IQService, private triggerTabService: any) {
 this.triggerDataState = this.triggerTabService.getTriggerDataState();
 for (const trigger of this.triggerDataState.selectedVariation.triggers) {
 if (trigger.type === 'userGroupTriggerData') { this.initialTriggerData = trigger; this.triggerData = trigger; } } } public fetchAll(): any {
 return this.$q.when(this.customerGroups);
 } public $onInit(): void {
 this.customerGroups = [
 {
 id: "undefined",
 label: "\u200C" }, { id: "regulargroup", label: "regulargroup" },
 {
 id: "customergroup",
This is   For more    the SAP Help  116 The html template for the component contains the label and a simple ySelect component for selecting the customer group.

 label: "customergroup"
 }, {
 id: "personalizedUserGroup1",
 label: "personalizedUserGroup1"
 }
 ];
 if (this.triggerData === null) {
 this.selectedId = 'undefined';
 } else {
 this.selectedId = this.triggerData.userGroupUid;
 }
 } public onSelect(selectedItem: any, selectedId: string): void { if (selectedId === 'undefined') { this.removeTrigger();
 } else {
 if (this.triggerData === null) {
 this.createTriggerData(selectedId);
 } else {
 this.triggerData.userGroupUid = selectedId;
 }
 }
 } private removeTrigger(): void { this.triggerData = null; if (this.initialTriggerData !== null) { this.removeElement(this.triggerDataState.selectedVariation.triggers, this.initialTriggerData); } } private createTriggerData(selectedId: string): void {
 if (this.initialTriggerData !== null) {
 this.triggerData = this.initialTriggerData; this.triggerData.userGroupUid = selectedId; this.addIfNotPresent(this.triggerDataState.selectedVariation.triggers, this.triggerData);
 } else {
 this.triggerData = {
 catalog: this.triggerDataState.selectedVariation.catalog, catalogVersion: this.triggerDataState.selectedVariation.catalogVersion, type: 'userGroupTriggerData',
 userGroupUid: selectedId
 };
 this.triggerDataState.selectedVariation.triggers.push(this.triggerData); this.initialTriggerData = this.triggerData; } } private removeElement(array: any[], value: any): void {
 const idx = array.indexOf(value);
 if (idx !== -1) {
 array.splice(idx, 1);
 }
 }
 private addIfNotPresent(array: any[], value: any): void {
 const idx = array.indexOf(value);
 if (idx === -1) {
 array.push(value); } } }
3. Add localization used in the html template. Put the conguration in the personalizationsmartedittrail/resources/localization/personalizationsmartedittrail-locales_en.properties le.

personalizationsmartedittrail.customergroup.label=Customer group personalizationsmartedittrail.customergroup.placeholder=Customer group 4. Add the CustomerGroupTriggerComponent declaration to the personalizationsmartedittrail/web/features/personalizationsmartedittrailContainer/personalizationsmartedittrailcontainerModule.ts le.

import {doImport} from './forcedImports'; doImport();
import {SeModule} from 'smarteditcommons';
import {CustomerGroupTriggerComponent} from "personalizationsmartedittrailcontainer/customerGroupTriggerComponent/CustomerGroupTriggerComponent /**
 * @ngdoc overview
 * @name personalizationsmartedittrailContainer This is   For more    the SAP Help  117

 * @description
 * Placeholder for documentation
 */
@SeModule({
 imports: [ ], initialize: () => { 'ngInject'; }, declarations: [CustomerGroupTriggerComponent]
 })
export class PersonalizationsmartedittrailContainer {}

## Add The Itriggertab

Add an additional tab to the Target Group modal so that you can congure the customer group trigger.

Procedure 1. Create the customerGroupTriggerWrapperTemplate.html le in the personalizationmodule/personalizationsmartedittrail/web/features/personalizationsmartedittrailContainer/customerGroupTriggerComponent directory. This is a html wrapper template which displays the new component in the trigger tab.

<customer-group-trigger></customer-group-trigger>
2. Create an object implementing the ITriggerTab interface to create the additional tab. Keep in mind that the interface already exists in personalizationsmartedit extension so you don't need to create it.

export interface ITriggerTab { id: string; title: string; templateUrl: string; isTriggerDefined(): boolean; // Function returns 'true' if trigger is created and correct, otherwise 'false' isValidOrEmpty(): boolean; // Function returns 'true' if trigger is correct or is empty, otherwise 'false'
 // In multiple trigger environment all trigger tabs must be valid or empty, and at least one must have defined trigger
}
3. Create the customerGroupTriggerTab object in the initialize method personalizationsmartedittrail/web/features/personalizationsmartedittrailContainer/personalizationsmartedittrailcontainerModule.ts le.

import {doImport} from './forcedImports';
doImport();
import {SeModule} from 'smarteditcommons';
import {CustomerGroupTriggerComponent} from "personalizationsmartedittrailcontainer/customerGroupTriggerComponent/CustomerGroupTriggerComponent // ITriggerTab from personalizationsmarteditcontainer/management/manageCustomizationView/multipleTriggersComponent/ITriggerTab export interface ITriggerTab { id: string; title: string; templateUrl: string; isTriggerDefined(): boolean; isValidOrEmpty(): boolean;
}
@SeModule({
 imports: [
 'personalizationsmarteditManagementModule',
 'personalizationsmartedittrailContainerTemplates'
 ],
 initialize: (triggerTabService: any) => { 'ngInject'; // ITriggerTab from personalizationsmarteditcontainer/management/manageCustomizationView/multipleTriggersComponent/ITriggerTab const customerGroupTriggerTab: ITriggerTab = { id: "customerGroupTrigger",
 title: 'customerGroup',
 templateUrl: 'customerGroupTriggerWrapperTemplate.html',
 isTriggerDefined: () => {
 const data = triggerTabService.getTriggerDataState();
 data.selectedVariation = data.selectedVariation || {triggers: []};
 const userGroupTrigger = data.selectedVariation.triggers.filter((elem: any) => {
 return elem.type === 'userGroupTriggerData';
 });
 return userGroupTrigger.length === 1;
 }, isValidOrEmpty: () => { return true; } }; triggerTabService.addTriggerTab(customerGroupTriggerTab);

 },
 declarations: [CustomerGroupTriggerComponent]
})
export class PersonalizationsmartedittrailContainer {}
4. Stop and then build the SAP platform.

ant build

## Verify The Conguration

Verify if the tab for the new trigger type is displayed.

Procedure 1. Start the SAP server.

2. Go to https://localhost:9002/smartedit.

3. Display the homepage for the Electronics Staged catalog.

4. Select Personalization for the top right menu.

5. Go to Library Manage Library .

6. On the list, go to Banner variationForUserGroup and Edit it.

![118_image_0.png](118_image_0.png)

Personalization Integration Module

![118_image_1.png](118_image_1.png)

Personalization Integration Module Features The personalization integration module provides you with a range of features related to integrating personalization features with other systems. .

Integrate Personalization Functionality Extend personalization functionality to integrate with external systems.

Integrate Personalization Functionality Extend personalization functionality to integrate with external systems.

This is   For more    the SAP Help  119 Use Case A marketing executive wants to import user data and affinities from external systems to further dene segments. With these segments, the marketing executive can create a personalized storefront to target visitor preferences.

Dependencies There are no specic dependencies for using personalization integration.

Personalization Integration Module Architecture The personalization integration module is a set of extensions allowing for integration with external systems.

Dependencies

![119_image_0.png](119_image_0.png)

For a complete list of the SAP Commerce Cloud, integration extension pack recipes that may include this module, see Installer Recipe Reference.

Extensions The personalization integration module contains the following extensions:
Personalization Integration Module Implementation You can easily extend personalization functionality to integrate it with an external system. Use the guides and trails to view and try out possible examples.

Mapping Mechanism Out of the box, the system does not provide any concrete integration to any external system but it gives the opportunity for the custom implementations to do so.

Populators Populators are used to return and interpret the data coming from the prole.

Default Update Segment Strategy The DefaultCxUpdateSegmentStrategy is the default implementation of the UpdateSegmentStrategy, dened in the personalizationintegration extension.

Default Update User Segment Strategy The DefaultCxUpdateUserSegmentStrategy is the default implementation of the UpdateUserSegmentStrategy, dened in the personalizationintegration extension.

Segments Provider Trail This is   For more    the SAP Help  120

## Mapping Mechanism

Out of the box, the system does not provide any concrete integration to any external system but it gives the opportunity for the custom implementations to do so.

If you want to implement a particular integration type, use the CxIntegrationMappingService interface to do so. The DefaultCxIntegrationMappingService class registers different instances of the Converter<Object, MappingData> class.

Internally, these strategies are being stored in a map and require you to provide the strategy key (the bean name by default) when calling the service. These converters can hold multiple populators. For more information on Converters and Populators pattern refer to: Converters and Populators.

The data returned by the mapping service is a MappingData object, which contains information related to the user and the segments it belongs to.

Below you can see an example of calling a mapping:
Optional<MappingData> mapExternalData(Object externalData, String mappersGroupId)

## Populators

Populators are used to return and interpret the data coming from the prole. The following two types of populators are provided out of the box:
CxFixedSegmentsProfileMapper: a mapper that uses a property to return xed segments names.

CxScriptProfileMapper: a mapper that uses predened groovy scripts to interpret the prole data.

CxFixedSegmentsProleMapper This populator returns all the segments dened in the following property: personalizationintegration.mappers.cxfixedsegmentsprofilemapper.segments To set the segments to return you need to list the segment names separated by a comma as presented below:
personalizationintegration.mappers.cxfixedsegmentsprofilemapper.segments=segmentA, segmentB
CxScriptProleMapper This populator retrieves a set of scripts from the database and runs them.

 Note If one of the script fails or does not respect the condition stating that the return type must be a list of SegmentMappingData objects, the script fails and an error is logged but the mapper keeps going through the next scripts.

To dene a script to be picked up by this mapper, you need to dene a CxMapperScript in the database. The CxScript just extends the Script data model with one additional attribute:
group. An example of CxMapperScript denition:
INSERT_UPDATE CxMapperScript;scriptType(code);active;code[unique=true];version[unique=true];content;group;
;GROOVY;true;testcxmapperscript;0;"result = new de.hybris.platform.personalizationintegration.mapping.SegmentMappingData(); result.setCode('segment2 A CxScriptProfileMapper expects its scriptGroup property to be dened. This property is used to select which CxMapperScript will be picked up. For more information regarding Scripting engine in hybris, see: Scripting Engine.

## Default Update Segment Strategy

The DefaultCxUpdateSegmentStrategy is the default implementation of the UpdateSegmentStrategy, dened in the personalizationintegration extension.

It allows to update segments from many external systems at the same time. The DefaultCxUpdateSegmentStrategy collects the segments from the implementations of the SegmentsProvider dened in the Spring context, and saves them in the system. You can check the list of dened segments in the Backoffice Administration Cockpit under the Personalization Segments node.

Segment Validation The DefaultCxUpdateSegmentStrategy implementation allows segment validation before updating them in SAP Commerce Cloud. Default validator checks if the segment code length does not exceed the specied one. You can customize the validator list by extending cxSegmentValidators in the Spring conguration, as presented below:
<bean id="addNewValidatorExample" depends-on="cxSegmentValidators" parent="listMergeDirective">
 <property name="add" value="newValidatorBean"/>
</bean>
After the segment validation, the update proceeds. There are two possible scenarios:
A segment with a given code already exists in the system. In this case, the segment with data from an external provider is updated in the system.

This is   For more    the SAP Help  121 A segment does not exist in the system. In this case, a new segment is created and stored in the system.

Segment Removal Setting the fullUpdate ag to true means that the segments can also be removed. There are several conditions that must be fullled to remove a segment from SAP Commerce Cloud:
A segment is no longer assigned to any other provider, A segment is created automatically. This requires the autoCreated ag to be set to true for that segment.

A segment is not used by any triggers.

Segments Provider The SegmentsProvider is an interface, which should be implemented when connecting another source of segments. The SegmentsProvider interface contains two base methods:
getUserSegments - returning segments, getProviderId - returning provider identier. This method has a default implementation which classies provider as one of the DEFAULT providers.

Provider identier allows to:
congure the prex for segments returned by provider. For details, see Dene Simple User Segments Provider. select specic provider in update segment cron job. For details, see Cron Job for Refreshing Segments.

/**
 * Interface returning segments assigned to user
 */ public interface UserSegmentsProvider
{
 String DEFAULT_PROVIDER_ID = "DEFAULT"; /** * Method returning segments assigned to user
 *
 * @param user
 * User model
 * @return segments assigned to user or null if segments should not be updated */
 List<SegmentMappingData> getUserSegments(final UserModel user);
 /** * Method returns provider identifier *
 * @return - provider identifier
 * @since 1811 */
 default String getProviderId()
 {
 return DEFAULT_PROVIDER_ID;
 } }
Provider Prex The segment returned by the provider can be automatically prexed. To congure the prex for segments returned by the provider, or for the already existing ones, use the personalizationintegration.provider.<PROVIDER_ID>.prefix property:
personalizationintegration.provider.SAMPLEID.prefix=PREF
Provider Separator By default, the separator between prex and segment code is set as space. To set a different separator, use the personalizationintegration.provider.

<PROVIDER_ID>.separator property.

## Dene Segments Provider

You can create your own provider, which will be used by the DefaultCxUpdateSegmentStrategy.

Context The DefaultCxUpdateSegmentStrategy interface assumes that providers can obtain segments at any moment. However, since the process of retrieving segments from external sources may be both time- and transfer-consuming, you should minimize the number of calls.

Procedure 1. Create an implementation of the UserSegmentsProvider interface.

public class SampleSegmentsProvider implements SegmentsProvider
{
 private static final String PROVIDER_ID = "SAMPLEID";
 @Override public Optional<List<BaseSegmentData>> getSegments()
 { 
 //get segments data from external system This is   For more    the SAP Help  122 final List<BaseSegmentData> segments = ...

 
 ... //return segment list return Optional.of(segments);
 } @Override public String getProviderId()
 {
 return PROVIDER_ID;
 }
}
The getSegments method of the interface should return:
a list of segments from given providers, an Optional.empty if there is no segment null if the segment provider can't provide new data, and doesn't want the existing data to be changed.

The getProviderId method of the interface should return provider identier. There is a default implementation of this method, which returns the DEFAULT identier. This method should be implemented when:
you want be able to set separate conguration for your provider, you want to have specic prex for segments returned by provider.

2. Dene your provider in the Spring context:
<bean id="sampleSegmentProvider" class="de.hybris.platform.extensionname.segment.SampleSegmentsProvider">
</bean>
3. Congure prex for your provider.

 Note This step is required only if you have overridden the getPropertyId method and you want to have a specic prex for segments returned by the provider.

To congure prex for segments returned by your provider set the personalizationintegration.provider.<PROVIDER_ID>.prefix property:
personalizationintegration.provider.SAMPLEID.prefix=PREF

## Default Update User Segment Strategy

The DefaultCxUpdateUserSegmentStrategy is the default implementation of the UpdateUserSegmentStrategy, dened in the personalizationintegration extension. The strategy allows to update segments from several external systems at the same time. The DefaultCxUpdateUserSegmentStrategy collects the segments from the implementations of the UserSegmentsProvider dened in the Spring context and assigns the segments to the user. If there are no segments in the system, they can be created if the Auto Create Segments ag is set to true. If it's set to false, the strategy does not set any user to segment relation.

You can change this behavior in the Backoffice Administration Cockpit under Personalization Personalization Conguration . For details on how to manage the conguration, see Set Up a Personalization Conguration.

As a fallback, you can also set the personalizationintegration.updateUserSegment.createSegment property as presented below:
personalizationintegration.updateUserSegment.createSegment=true User Segments Provider The UserSegmentsProvider is an interface which should be implemented when connecting another source of user segments. The UserSegmentsProvider interface contains two base methods:
getUserSegments - returning segments for user, getProviderId - returning provider identier. This method has a default implementation which classies provider as one of the DEFAULT providers.

Provider identier allows to:
congure how often provider is called on update user segment process. For details, see Congure a Segment.

congure the prex for segments returned by provider. For details, see Dene Simple User Segments Provider.

/**
 * Interface returning segments assigned to user
 */ public interface UserSegmentsProvider
{
 String DEFAULT_PROVIDER_ID = "DEFAULT"; /** * Method returning segments assigned to user
 *
 * @param user * User model
 * @return segments assigned to user or null if segments should not be updated
 */
 List<SegmentMappingData> getUserSegments(final UserModel user);
This is   For more    the SAP Help  123

 /**
 * Method returns provider identifier * * @return - provider identifier
 * @since 1811
 */
 default String getProviderId()
 {
 return DEFAULT_PROVIDER_ID;
 }
}
Out of the box, the Personalization module contains two implementations:
UserTypeSegmentsProvider - providing segments to distinguish anonymous and registered users. ConsumptionLayerUserSegmentsProvider - providing segments from Intelligent Selling Services Foundation.

Provider Prex The segment returned by the provider can be automatically prexed. To congure the prex for segments returned by the provider, or for the already existing ones, use the personalizationintegration.provider.<PROVIDER_ID>.prefix property.

personalizationintegration.provider.SAMPLEID.prefix=PREF
Provider Separator By default, the separator between prex and segment code is set as space. To set a different separator, use the personalizationintegration.provider.

<PROVIDER_ID>.separator property.

UserTypeSegmentsProvider USER_ANONYMOUS
USER_REGISTERED
The UserTypeSegmentsProvider has a DEFAULT provider identier. This means it uses the segment prex congured for DEFAULT providers
(personalizationintegration.provider.DEFAULT.prefix) and it is called during the update, update_default, or async process actions. This means that depending on the personalization conguration, USER_ANONYMOUS and USER_REGISTERED may not be updated right away when user starts the session or logs in.

To take full advantage of the segments, perform the following:
when dening the calculation settings in the Backoffice Administration Cockpit, set the update action to be executed at the beginning of the session and during logon. For details, see the Initial Actions section in Congure Personalization Calculation. when dening the target group expression in SmartEdit, use only USER_REGISTERED or NOT (USER_REGISTERED) options. For details, see Add Customizations.

This behavior reduces instances when the given target group is not triggered.

Dene Segments Provider Context You can create your own provider used by the DefaultCxUpdateUserSegmentStrategy.

 Note Remember that if the provider uses data from the external system, it should be able to handle connection problems without signicant inuence on the performance.

Procedure 1. Create an implementation of the UserSegmentsProvider interface:
public class SampleUserSegmentsProvider implements UserSegmentsProvider { private static final String PROVIDER_ID = "SAMPLEID"; private CxIntegrationMappingService cxIntegrationMappingService;
 @Override public List<SegmentMappingData> getUserSegments(final UserModel user)
 {
 //get segment data from external system final Object segmentData = ...; //map external data to segments final Optional<MappingData> mappingData = cxIntegrationMappingService.mapExternalData(segmentData,
 "YOUR_INTEGRATION_CONVERTER_NAME");
 //return segment list return mappingData.map(MappingData::getSegments).orElseGet(() -> Collections.emptyList()); } @Override This is   For more    the SAP Help  124 public String getProviderId()
 {
 return PROVIDER_ID;
 }
 protected CxIntegrationMappingService getCxIntegrationMappingService()
 {
 return cxIntegrationMappingService;
 }
 @Required public void setCxIntegrationMappingService(final CxIntegrationMappingService cxIntegrationMappingService) { this.cxIntegrationMappingService = cxIntegrationMappingService; } }
The getUserSegments method of the interface returns:
a list of segments to be assigned to the user (the segments that are currently assigned to the user and are not on the list, will be removed), an empty list if all the segments assigned to the user should be removed, null if the segment provider can't provide new data, and doesn't want the existing data to be changed.

The getProviderId method of the interface returns the provider identier. There is a default implementation of this method, which returns the DEFAULT identier. This method should be implemented when:
you want to be able to set a separate conguration for your provider, you want to have a specic prex for segments returned by the provider.

2. Dene your provider in the Spring context:
<bean id="sampleUserSegmentProvider" class="de.hybris.platform.extensionname.segment.SampleUserSegmentsProvider">
 <property name="cxIntegrationMappingService" ref="cxIntegrationMappingService"/>
</bean>
3. Add the update actions for your provider:
 Note This step is required only if you have overridden the getProviderId method and want to be able to set a separate conguration for your provider.

To add the update actions for your provider, extend the RecalculationAction enum with the following values: UPDATE_<PROVIDER_ID> and ASYNC_PROCESS_<PROVIDERID>.

... <enum class="de.hybris.platform.personalizationservices.RecalculateAction">
 <value>UPDATE_SAMPLEID</value>
 <value>ASYNC_PROCESS_SAMPLEID</value>
</enum>
...

4. Congure the prex for your provider.

 Note This step is required only if you have overridden the getProviderId method and want to have specic prex for segments returned by the provider.

To congure the prex for segments returned by your provider, set the personalizationintegration.provider.<PROVIDER_ID>.prefix:
personalizationintegration.provider.SAMPLEID.prefix=PREF

## Auto Creation Of Segments

In the personalizationintegration extension, the CxConfig was extended to include the autoCreateSegments parameter.

If it is set to true in the Backoffice Administration Cockpit, the segments are automatically created from the external data during update. To allow enabling the auto creation of segments in the Backoffice Administration Cockpit, the personalizationintegration extension was extended with the backoffice conguration.

## Segments Provider Trail

Create a Segments Provider and a User Segments Provider for the Personalization module. The trail covers the following aspects:
Creating a simple Segments Provider. Creating a simple User Segments Provider.

Merging two simple providers into one. Creating a complex User Segments Provider, which uses the mapper mechanism to convert data to user segments. Creating a script mapper.

This is   For more    the SAP Help  125 Scenario Segments Providers add new segments to the system. Usually, they fetch needed information from external services, but in this scenario you create a simple provider, which uses customer groups from SAP Commerce Cloud. User Segments Providers assign users to specic segments. Typically, the providers communicate with external services to fetch the required information, but in this scenario you create providers which assign a customer to segments based on customer data.

Prerequisites For this trail, use a standard B2C Accelerator storefront with electronics store sample data. You can easily set up a local installation using the cx recipe. For details on the installation procedure, see Installing SAP Commerce Cloud Using Installer Recipes.

Procedure Navigate through the documentation to complete the trail:
Create personalizationsegmenttrail Extension Dene Simple Segments Provider Test Simple Segments Provider Dene Simple User Segments Provider Merge Simple Providers Dene Complex User Segments Provider Test User Segments Providers Dene the Mapper Script Create personalizationsegmenttrail Extension Create a custom extension using the yempty template to accommodate the customized code.

Context For the purpose of this trail, name your new extension as personalizationsegmenttrail extension. All customized code will be included in this extension.

Procedure 1. Create the new personalizationsegmenttrail extension using the yempty template with a de.hybris.personalizationsegmenttrail base package. For details on how to create a new extension, see Creating a New Extension.

2. Create a workspace using the IDE of your choice and import the personalizationsegmenttrail extension along with other required extensions.

The extension is added to the workspace.

3. Add your newly created extension to the /config/localextensions.xml le.

<extension name="personalizationsegmenttrail"/>
4. This extension has to depend on the personalizationintegration extension. Your sample providers also need the commercefacades extension. Add them to the extensioninfo.xml le in your new extension and congure relations in your IDE.

<requires-extension name="personalizationintegration"/>
<requires-extension name="personalizationintegrationbackoffice"/>
<requires-extension name="commercefacades"/>
5. Build and update the platform:
a. Go to hybris/platform directory. b. Execute setantenv.bat (for Windows) or . ./setantenv.sh (for unix-based systems).

c. Run ant all command.

d. Run ant updatesystem command.

The platform is built.

## Dene Simple Segments Provider

Create a simple Segments Provider to create segments based on existing customer groups.

Procedure 1. Create the SimpleSegmentsProvider.java class in the personalizationsegmenttrail/src/de/hybris/personalizationsegmenttrail/segment directory. It should implement the SegmentsProvider interface. This provider provide segments based on customer groups unique identiers fetched from the CustomerGroupFacade. See the implementation of the SimpleSegmentsProvider.java class below:
package de.hybris.personalizationsegmenttrail.segment; import de.hybris.platform.commercefacades.catalog.PageOption; This is   For more    the SAP Help  126 import de.hybris.platform.commercefacades.customergroups.CustomerGroupFacade; import de.hybris.platform.commercefacades.user.data.PrincipalData; import de.hybris.platform.personalizationintegration.segment.SegmentsProvider; import de.hybris.platform.personalizationservices.data.BaseSegmentData; import java.util.List; import java.util.Optional; import java.util.stream.Collectors; import org.springframework.beans.factory.annotation.Required; final public class SimpleSegmentsProvider implements SegmentsProvider
{
 private static final String PROVIDER_ID = "SIMPLE";
 private CustomerGroupFacade customerGroupFacade;
 @Override public Optional<List<BaseSegmentData>> getSegments() {
 final List<BaseSegmentData> segments = getCustomerGroupsUids().stream()
 .map(this::convertStringToBaseSegmentData)
 .collect(Collectors.toList());
 return Optional.of(segments);
 }
 @Override public String getProviderId() {
 return PROVIDER_ID;
 }
 private BaseSegmentData convertStringToBaseSegmentData(final String uid)
 {
 final BaseSegmentData segmentData = new BaseSegmentData();
 segmentData.setCode(uid); segmentData.setDescription("Customer group: " + uid);
 segmentData.setProvider(PROVIDER_ID);
 return segmentData;
 }
 private List<String> getCustomerGroupsUids()
 {
 final List<String> uniqueIdentifiers = customerGroupFacade.getAllCustomerGroups(PageOption.createWithoutLimits())
 .getUserGroups().stream() .map(PrincipalData::getUid)
 .collect(Collectors.toList());
 return uniqueIdentifiers; }
 @Required public void setCustomerGroupFacade(final CustomerGroupFacade customerGroupFacade) {
 this.customerGroupFacade = customerGroupFacade;
 }
}
2. Dene your provider in the Spring context. Add the bean denition to the personalizationsegmenttrail/resources/personalizationsegmenttrail-spring.xml le.

The denition should look as follows:
... <bean id="simpleSegmentsProvider" class="de.hybris.personalizationsegmenttrail.segment.SimpleSegmentsProvider">
 <property name="customerGroupFacade" ref="customerGroupFacade"/>
</bean>
...

3. Congure prex for your provider.

There is a possibility to automatically add prex to segment names returned by this provider. It can be done by setting property: personalizationintegration.provider. <PROVIDER_ID>.prefix in the personalizationsegmenttrail/project.properties le.

The S prex is added as an example.

personalizationintegration.provider.SIMPLE.prefix=S
Test Simple Segments Provider Procedure 1. Build and run Hybris platform.

2. Go to backoffice as an admin. Navigate to System Background Processes Cronjobs and run the cxUpdateSegmentsCronJob job (make sure that the All Segments Providers ag is set to true).

3. Navigate to Personalization Segments .

4. Search for "S". 5. You should see segments with S prex added by your provider.

## Dene Simple User Segments Provider

Create a simple User Segments Provider to assign segments to a customer based on the customer groups.

Procedure 1. Create the SimpleUserSegmentProvider.java class in the personalizationsegmenttrail/src/de/hybris/personalizationsegmenttrail/segment directory. Make sure the class implements the UserSegmentsProvider interface. For details on method implementation, see Dene Segments Provider.

package de.hybris.personalizationsegmenttrail.segment; import de.hybris.platform.commercefacades.customergroups.CustomerGroupFacade; import de.hybris.platform.commercefacades.user.data.UserGroupData; import de.hybris.platform.core.model.user.CustomerModel; import de.hybris.platform.core.model.user.UserModel; import de.hybris.platform.personalizationintegration.mapping.SegmentMappingData; import de.hybris.platform.personalizationintegration.segment.UserSegmentsProvider; import de.hybris.platform.personalizationservices.configuration.CxConfigurationService; import java.math.BigDecimal; import java.util.Collections; import java.util.List; import java.util.stream.Collectors; import org.springframework.beans.factory.annotation.Required; final public class SimpleUserSegmentProvider implements UserSegmentsProvider
{
 private static final String PROVIDER_ID = "SIMPLE"; private CxConfigurationService cxConfigurationService; private CustomerGroupFacade customerGroupFacade; @Override public List<SegmentMappingData> getUserSegments(final UserModel user)
 {
 if (user instanceof CustomerModel)
 {
 final List<UserGroupData> customerGroups = customerGroupFacade.getCustomerGroupsForUser(user.getUid()); final List<SegmentMappingData> userSegments = customerGroups.stream()
 .map(this::getSegmentMapping)
 .collect(Collectors.toList()); return userSegments;
 }
 return Collections.emptyList(); } private SegmentMappingData getSegmentMapping(final UserGroupData userGroupData) {
 final SegmentMappingData data = new SegmentMappingData();
 data.setCode(userGroupData.getUid());
 data.setAffinity(getAffinity()); return data;
 } private BigDecimal getAffinity()
 {
 return cxConfigurationService.getMinAffinity().add(BigDecimal.ONE);
 }
 @Override public String getProviderId() { return PROVIDER_ID; } @Required public void setCxConfigurationService(final CxConfigurationService cxConfigurationService)

 {
 this.cxConfigurationService = cxConfigurationService;
 } @Required public void setCustomerGroupFacade(final CustomerGroupFacade customerGroupFacade)
 {
 this.customerGroupFacade = customerGroupFacade;
 } }
2. Dene your provider in the Spring context. Add the bean denition to the personalizationsegmenttrail/resources/personalizationsegmenttrail-spring.xml le.

... <bean id="simpleUserSegmentProvider" class="de.hybris.personalizationsegmenttrail.segment.SimpleUserSegmentProvider"> <property name="cxConfigurationService" ref="cxConfigurationService"/> <property name="customerGroupFacade" ref="customerGroupFacade"/>
</bean>
...

3. Add update actions for your provider. To congure update actions separately for this provider, extend RecalculationAction enum in personalizationsegmenttrail/resources/personalizationsegmenttrail-beans.xml with the follwing values: UPDATE_SIMPLE and ASYNC_PROCESS_SIMPLE (where SIMPLE is the provider identier returned by the getProviderId method). You can extend RecalculationAction enum in the personalizationsegmenttrail/resources/personalizationsegmenttrail-beans.xml le:
...

<enum class="de.hybris.platform.personalizationservices.RecalculateAction"> <value>UPDATE_SIMPLE</value>
 <value>ASYNC_PROCESS_SIMPLE</value>
</enum>
...

4. In case you haven't done so in the Dene Simple Segments Provider scenario, set the personalizationintegration.provider.<PROVIDER_ID>.prefix property for the system to automatically add prex to segment names returned by this provider. The S prex is added as an example.

personalizationintegration.provider.SIMPLE.prefix=S
Merge Simple Providers Merge Simple Segments Provider and Simple User Segments Provider into a single class.

Context Both Simple Segments Provider and Simple User Segments Provider operate on customer group segments and they have the same provider ID. We can merge them into a single class which implements both SegmentsProvider and UserSegmentsProvider interfaces.

Procedure 1. Create the CustomerGroupSegmentsProvider.java class in the personalizationsegmenttrail/src/de/hybris/personalizationsegmenttrail/segment directory. It should implement the SegmentsProvider and UserSegmentsProvider interfaces.

package de.hybris.personalizationsegmenttrail.segment; import de.hybris.platform.commercefacades.catalog.PageOption; import de.hybris.platform.commercefacades.customergroups.CustomerGroupFacade; import de.hybris.platform.commercefacades.user.data.PrincipalData; import de.hybris.platform.commercefacades.user.data.UserGroupData; import de.hybris.platform.core.model.user.CustomerModel; import de.hybris.platform.core.model.user.UserModel; import de.hybris.platform.personalizationintegration.mapping.SegmentMappingData; import de.hybris.platform.personalizationintegration.segment.SegmentsProvider; import de.hybris.platform.personalizationintegration.segment.UserSegmentsProvider; import de.hybris.platform.personalizationservices.configuration.CxConfigurationService; import de.hybris.platform.personalizationservices.data.BaseSegmentData; import java.math.BigDecimal; import java.util.Collections; import java.util.List; import java.util.Optional; import java.util.stream.Collectors; import org.springframework.beans.factory.annotation.Required; final public class CustomerGroupSegmentsProvider implements SegmentsProvider, UserSegmentsProvider
{
 private static final String PROVIDER_ID = "CGSP";
 private CxConfigurationService cxConfigurationService; private CustomerGroupFacade customerGroupFacade;
 @Override public Optional<List<BaseSegmentData>> getSegments() { final List<BaseSegmentData> segments = getCustomerGroupsUids().stream() .map(this::convertStringToBaseSegmentData)
 .collect(Collectors.toList());
 return Optional.of(segments);
 } @Override public List<SegmentMappingData> getUserSegments(final UserModel user)
This is   For more    the SAP Help  129
 {
 if (user instanceof CustomerModel)
 {
 final List<UserGroupData> customerGroups = customerGroupFacade.getCustomerGroupsForUser(user.getUid());
 final List<SegmentMappingData> userSegments = customerGroups.stream()
 .map(this::getSegmentMapping)
 .collect(Collectors.toList()); return userSegments;
 }
 return Collections.emptyList();
 } @Override public String getProviderId()
 {
 return PROVIDER_ID; } private BaseSegmentData convertStringToBaseSegmentData(final String uid)
 {
 final BaseSegmentData segmentData = new BaseSegmentData(); segmentData.setCode(uid);
 segmentData.setDescription("Customer group: " + uid);
 segmentData.setProvider(PROVIDER_ID); return segmentData; } private List<String> getCustomerGroupsUids()
 {
 final List<String> uniqueIdentifiers = customerGroupFacade.getAllCustomerGroups(PageOption.createWithoutLimits()) // .getUserGroups().stream()
 .map(PrincipalData::getUid)
 .collect(Collectors.toList()); return uniqueIdentifiers; } private SegmentMappingData getSegmentMapping(final UserGroupData userGroupData) {
 final SegmentMappingData data = new SegmentMappingData();
 data.setCode(userGroupData.getUid());
 data.setAffinity(getAffinity());
 return data;
 }
 private BigDecimal getAffinity()
 { return cxConfigurationService.getMinAffinity().add(BigDecimal.ONE);
 }
 @Required public void setCxConfigurationService(final CxConfigurationService cxConfigurationService) {
 this.cxConfigurationService = cxConfigurationService;
 }
 @Required public void setCustomerGroupFacade(final CustomerGroupFacade customerGroupFacade)
 {
 this.customerGroupFacade = customerGroupFacade; }
}
2. Dene your provider in the Spring context.

Add the bean denition to the personalizationsegmenttrail/resources/personalizationsegmenttrail-spring.xml le.

...

<bean id="customerGroupSegmentsProvider" class="de.hybris.personalizationsegmenttrail.segment.CustomerGroupSegmentsProvider">
 <property name="cxConfigurationService" ref="cxConfigurationService"/>
 <property name="customerGroupFacade" ref="customerGroupFacade"/> </bean> ...

3. Add update actions for your provider.

To be able congure update actions separately for this provider, you need to extend RecalculationAction enum with values: UPDATE_CGSP and ASYNC_PROCESS_CGSP (where CGSP is your provider identier returned by getProviderId method).

We can extend RecalculationAction enum in the personalizationsegmenttrail/resources/personalizationsegmenttrail-beans.xml directory.

... <enum class="de.hybris.platform.personalizationservices.RecalculateAction">
 <value>UPDATE_SIMPLE</value>
 <value>ASYNC_PROCESS_SIMPLE</value>
 <value>UPDATE_CGSP</value>
 <value>ASYNC_PROCESS_CGSP</value> </enum>
...

4. Congure the prex for your provider.

There is possibility to automatically add prex to segment names returned by this provider. It can be done by setting property : personalizationintegration.provider. <PROVIDER_ID>.prex.

The CG prex is added as an example.

personalizationintegration.provider.CGSP.prefix=CG

Create a complex user Segments Provider, using the mapper mechanism to convert data to user segments.

Procedure 1. Create the ComplexUserSegmentProvider.java class in the personalizationsegmenttrail/src/de/hybris/personalizationsegmenttrail/segment directory. Make sure the class implements the UserSegmentsProvider interface. This provider uses CustomerModel as data based on which the mappers assign segments to customer.

Usually such data comes from an external system.

package de.hybris.personalizationsegmenttrail.segment; import de.hybris.platform.core.model.user.CustomerModel; import de.hybris.platform.core.model.user.UserModel; import de.hybris.platform.personalizationintegration.mapping.MappingData; import de.hybris.platform.personalizationintegration.mapping.SegmentMappingData; import de.hybris.platform.personalizationintegration.segment.UserSegmentsProvider; import de.hybris.platform.personalizationintegration.service.CxIntegrationMappingService; import java.util.Collections; import java.util.List; import java.util.Optional; import org.springframework.beans.factory.annotation.Required; public class ComplexUserSegmentProvider implements UserSegmentsProvider
{
 private static final String PROVIDER_ID = "COMPLEX";
 public static final String CONVERTER_NAME = "CSC"; private CxIntegrationMappingService cxIntegrationMappingService;
 @Override public List<SegmentMappingData> getUserSegments(final UserModel user)
 { if (user instanceof CustomerModel) { //get segment data (usually from external system)
 final CustomerModel segmentData = getSegmentData(user);
 //map data to segment final Optional<MappingData> mappingData = cxIntegrationMappingService.mapExternalData(segmentData, CONVERTER_NAME); //return segment list return mappingData.map(MappingData::getSegments).orElseGet(() -> Collections.emptyList()); }
 return null;
 } private CustomerModel getSegmentData(final UserModel user) {
 return (CustomerModel) user;
 } @Override public String getProviderId()
 {
 return PROVIDER_ID; } protected CxIntegrationMappingService getCxIntegrationMappingService()
 {
 return cxIntegrationMappingService; } @Required public void setCxIntegrationMappingService(final CxIntegrationMappingService cxIntegrationMappingService)
 { this.cxIntegrationMappingService = cxIntegrationMappingService;
 }
}
2. Create Mapper for CITY segments.

In this example, the segments are assigned to user based on CustomerModel, so you need to create a mapper, which maps the CustomerModel to a desired segment. In this case it is the CITY segment, assigned to the customer based on the address. Create the CitySegmentMapper.java class in the personalizationsegmenttrail/src/de/hybris/personalizationsegmenttrail/segment/mapper directory. Make sure the class implements Populator <CustomerModel, MappingData> inteface.

package de.hybris.personalizationsegmenttrail.segment.mapper; import de.hybris.platform.converters.Populator; import de.hybris.platform.core.model.user.AddressModel; import de.hybris.platform.core.model.user.CustomerModel; import de.hybris.platform.personalizationintegration.mapping.MappingData; import de.hybris.platform.personalizationintegration.mapping.SegmentMappingData; import de.hybris.platform.servicelayer.dto.converter.ConversionException; import java.math.BigDecimal; public class CitySegmentMapper implements Populator<CustomerModel, MappingData> { @Override public void populate(final CustomerModel customer, final MappingData mappingData) throws ConversionException
 {
 if (customer.getAddresses() != null)
This is   For more    the SAP Help  131
 {
 customer.getAddresses().stream()//
 .map(this::createMapping)//
 .forEach(mappingData.getSegments()::add);
 }
 } private SegmentMappingData createMapping(final AddressModel address)
 { final SegmentMappingData data = new SegmentMappingData();
 data.setCode("CITY_" + address.getTown());
 data.setAffinity(BigDecimal.ONE); return data;
 }
}
3. Dene your provider and mappers in the Spring context.

Add the beans denition to the personalizationsegmenttrail/resources/personalizationsegmenttrail-spring.xml le.

The beans denition includes the provider, converter, and the following mappers:
city mapper: a class for this mapper was dened in previous step it simply map customer address to CITY segment.

xed mapper: one of the mappers provided out of the box. It returns segment names dened in the personalizationintegration.mappers.cxfixedsegmentsprofilemapper.segments property.

script mapper: one of the mappers provided out of the box. It uses scripts to interpret the segment data.

More information about standard mappers: Implement Custom Mapping.

...

<bean id="complexUserSegmentProvider" class="de.hybris.personalizationsegmenttrail.segment.ComplexUserSegmentProvider"> <property name="cxIntegrationMappingService" ref="cxIntegrationMappingService"/>
</bean>
<!-- Converter gathering segment data mappers -->
<bean id="customerSegmentConverter" parent="faultTolerantConverter"> <property name="targetClass" value="de.hybris.platform.personalizationintegration.mapping.MappingData"/>
 <property name="populators">
 <list>
 <ref bean="fixedSegmentMapper"/>
 <ref bean="scriptSegmentMapper"/> <ref bean="citySegmentMapper" />
 </list>
 </property>
</bean>
<!-- Adding converter to map used by CxIntegrationMappingService -->
<!-- Pay attention that key is the same value which we use in ComplexUserSegmentProvider when calling cxIntegrationMappingService.mapExternalData --> <bean depends-on="cxIntegrationConvertersMap" parent="mapMergeDirective"> <property name="key" value="CSC" />
 <property name="value" ref="customerSegmentConverter" />
</bean> <!-- Mappers --> <bean id="fixedSegmentMapper" parent="cxFixedSegmentsProfileMapper"/>
<bean id="scriptSegmentMapper" parent="cxScriptProfileMapper">
 <property name="scriptGroup" value="complexProviderGroup"/> </bean>
<bean id="citySegmentMapper" class="de.hybris.personalizationsegmenttrail.segment.mapper.CitySegmentMapper"/>
...

4. Add update actions for your provider.

To congure update actions separately for this provider, extend RecalculationAction enum in personalizationsegmenttrail/resources/personalizationsegmenttrail-beans.xml with the follwing values: UPDATE_COMPLEX and ASYNC_PROCESS_COMPLEX
(where COMPLEX is the provider identier returned by the getProviderId method).

You can extend RecalculationAction enum in the personalizationsegmenttrail/resources/personalizationsegmenttrail-beans.xml le:
...

<enum class="de.hybris.platform.personalizationservices.RecalculateAction">
 <value>UPDATE_SIMPLE</value>
 <value>ASYNC_PROCESS_SIMPLE</value> <value>UPDATE_CGSP</value>
 <value>ASYNC_PROCESS_CGSP</value>
 <value>UPDATE_COMPLEX</value>
 <value>ASYNC_PROCESS_COMPLEX</value>
</enum> ...

5. Congure prex for your provider.

To automatically add prex to segment names returned by this provider, set the personalizationintegration.provider.<PROVIDER_ID>.prefix property for the system.

The C prex is added as an example.

personalizationintegration.provider.COMPLEX.prefix=C

## Test User Segments Providers

Verify if your providers are working properly.

Procedure 1. Build and run the platform.

2. In Backoffice Administration Cockpit, go to [] Personalization ⟩ Personalization Configuration [] and edit the configuration for the electronics storefront.

3. Configure UPDATE_SIMPLE and RECALCULATE as User login actions (there should not be other update or async_process actions configured in the Calculation tab).

This configuration results in assigning the customer after login to proper customer group segment by the simple Segments Provider. Because you configured only update for the provider, customer does not belong to any other segment.

PROPERTIES  CALCULATION  COMMERCE WEB SERVICES  INTEGRATION  YPROFILE MAPPERS  ADMINISTRATION
A
INITIAL ACTIONS

![132_image_0.png](132_image_0.png)

Configurations of url voter 😊

![132_image_1.png](132_image_1.png)

![132_image_2.png](132_image_2.png)

![132_image_5.png](132_image_5.png)

![132_image_3.png](132_image_3.png)

![132_image_4.png](132_image_4.png)

»
Configuration of periodic voter ©
-)- Create new Configuration of periodic voter

![132_image_6.png](132_image_6.png)

4. Go to electronics storefront and register new customer: trail@hybris.com. Make sure that you select the title. 5. Go to |}Navigate to User } Customers }} Find the created customer and check Segmentation tab. Customer should be assigned to proper customer group segment.

i Note Pay attention that:
- there is only one segment from simple provider, because we configure update action only for this provider.

- this segment has S prefix, which was configured for simple provider.

Name trail@hybris.com trail@hybris.com ATTRIBUTES
Personalization Segments links  ©
S customergroup to trail@hybris.com (electronics, S... → Create new User to Segment relation
-
6. Navigate to [] My Account → Address Book 
()  B2C Accelerator

| o                          | !!!!!           |                 |                      |         |                |             |                               |
|----------------------------|-----------------|-----------------|----------------------|---------|----------------|-------------|-------------------------------|
| I'm looking for            | a               | (o items) $0.00 |                      |         |                |             |                               |
| BRANDS                     | DIGITAL CAMERAS | FILM CAMERAS    | HAND HELD CAMCORDERS | WEBCAMS | POWER SUPPLIES | FLASH MEMOR | CAMERA ACCESSORIES & SUPPLIES |
| HOME  /  ADDRESS BOOK      |                 |                 |                      |         |                |             |                               |
| Address Book               | Add Address     |                 |                      |         |                |             |                               |
| MR. TRAIL HYBRIS (DEFAULT) |                 |                 |                      |         |                |             |                               |
| u. Zwyciestwa              | x               |                 |                      |         |                |             |                               |
| Gliwice                    |                 |                 |                      |         |                |             |                               |
| Poland 44-100              |                 |                 |                      |         |                |             |                               |

7. Change configuration for personalization. In Personalization configuration node, configure UPDATE and RECALCULATE as User login actions.

8. Re-login as new customer trail@hybris.com.

i Note There is only one segment from simple provider, because you configured the update action only for this provider. This segment has S prefix, which you configured for the simpl provider 9. Go back to Backoffice Administration Cockpit. Go to |}User } Customers } Find the created customer and check Segmentation tab.

A Caution The customer is assigned to the following segments:
- S customergroup - assigned by simple provider. - CG customergroup - assigned by our merged provider. . C CITY - assigned by complex provider.

- USER_REGISTERED - assigned by DEFAULT provider, which is present out of the box.

The standard UPDATE action calls all providers defined in the platform.

Name trail@hybris.com trail@hybris.com ATTRIBUTES
Personalization Segments links USER_REGISTERED to trail@hybris.com (electronics, ... CG customergroup to trail@hybris.com (electronics, ...

C CITY_Gliwice to trail@hybris.com (electronics, COM...

S customergroup to trail@hybris.com (electronics, SI...

- Create new User to Segment relation

![133_image_0.png](133_image_0.png)

![133_image_1.png](133_image_1.png)

## Define The Mapper Script

Use the mapper script to define a script to be executed during the update user segments process.

Procedure 1. In Backoffice Administration Cockpit, go to [] System > Scripting > Scripting 2. Choose the Cx Mapper Script type from the top menu. You can do so by clicking the arrow button and then clicking the arrow next to the Script label.

![134_image_0.png](134_image_0.png)

3. Use the wizard to create a new mapper script.

![134_image_1.png](134_image_1.png)

![134_image_2.png](134_image_2.png)

| Field              | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Script code        | titleMapperScript                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Script engine type | GROOVY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Script group       | complexProviderGroup  Note Script group has to be the same as dene in script mapper denition. <bean id="scriptSegmentMapper" parent="cxScriptProfileMapper"> <property name="scriptGroup" value="complexProviderGroup"/> </bean>                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Content            | import de.hybris.platform.core.model.user.CustomerModel; import de.hybris.platform.core.model.user.TitleModel; import de.hybris.platform.personalizationintegration.mapping.SegmentMappingData; CustomerModel customer = externalData; TitleModel title = customer.getTitle(); if (title != null) { SegmentMappingData segment = new SegmentMappingData(); segment.setAffinity(java.math.BigDecimal.ONE); segment.setCode("TITLE_" + title.getCode()); return [segment] } else { return []}  Note The externalData parameter contains data which the provider passes as a parameter in the cxIntegrationMappingService.mapExternalData method. The sample provider uses CustomerModel data type. |

4. Go to the storefront and log in as trail@hybris.com.

5. Go to the Backoffice Administration Cockpit and verify TITLE segment with a C prex was assigned to the user.

Personalization Promotions Module The personalization promotions module allows you to customize promotions for specic user groups.

![135_image_0.png](135_image_0.png)

Personalization Promotions Module Features By combining the fuctionality provided by the Rule Builder with its own features, the Personalization Promotions module allows you to create promotions targeted at specic users.

Create Personalized Promotions Add, congure, and apply personalized promotions using the Personalization mode and the Rule Builder.

Create Personalized Promotions Add, congure, and apply personalized promotions using the Personalization mode and the Rule Builder.

Use Case The administrator of the storefront needs to apply a 10% discount on the cart for the VIP Gold Customers. To make the promotion visible on the storefront, the administrator adds the conditions in the Rule Builder and assigns the promotion to a particular target group using SmartEdit.

Features Use Rule Builder to Create Promotions Use the Rule Builder to easily create promotions based on specic conditions.

Make Promotions Personalized Assign created promotions to particular user groups, so that your users receive customized promotions.

Dependencies Personalized promotions functionality depends on the Promotion Engine module and Personalization module.

Creating a Personalized Promotion Rule Learn how to create a personalized promotion rule using the actions and conditions available in the Rule Builder.

Context To assign a promotion to a particular target group, you must create it rst. The Rule Builder provides you with an intuitive user interface so you can easily select conditions and actions to create a rule. To learn more about managing source rules using the Rule Builder, refer to: Rule Builder. To learn how to create a promotion rule, see: Creating a Promotion Rule.

Procedure 1. In the Backoffice Administration Cockpit explorer tree, navigate to Marketing Promotion Rules . You can also use the search eld to narrow down the selection.

You can see a list of congured promotions (if any).

2. Click the button to open the editor for a promotion rule.

The editor appears in the section below the rule list.

3. Dene the properties of your rule in the Rule Properties tab. For more information, see: Creating a Promotion Rule.

Under the Conditions & Actions tab, you can easily dene the conditions of your promotion rule and actions to be executed if the conditions are met. For details on available conditions and actions, refer to: Conditions and Actions.

4. To make the rule personalized and available for use, add the Personalized condition. Drag and drop the condition to the Conditions area. You can also add more conditions if needed. For the description of all the conditions, see: Conditions.

This is   For more    the SAP Help  136
[personalized_de_vip_gold_customer_percentage_discount_cart]
I 
v 1 REFRESH
rule properties CONDITIONS & ACTIONS
 ADMINISTRATION
Conditions

![136_image_0.png](136_image_0.png)

 New Promotion Rule

![136_image_1.png](136_image_1.png)

~
w rule properties ACTIONS Actions Apply 10% discount on the cart total

![136_image_3.png](136_image_3.png)

![136_image_4.png](136_image_4.png)

|  Percentage discount on products   |
|------------------------------------|
| Fixed discount on products         |
| Target fixed price on products     |
| Target bundle price                |

6. Click Save to apply the promotion rule.

Your promotion rule is now available on the list of rules. You can edit it at any time, but remember to save it, otherwise your changes will be lost.

i Note Your promotion rule is created but not yet published. It means that you can assign it to a particular target group in SmartEdit, but it won't appear on the storefront. To mak visible on the storefront, follow the guidelines below.

## Publishing A Promotion Rule

Context Learn how to publish your personalized promotion rule and make it visible on the storefront here: Publishing a Promotion Rule .

![136_image_2.png](136_image_2.png)

Activating a Personalized Promotion for a Target Group To make the promotion available to a customer tting a particular target group, you can easily add a personalized promotion to a chosen target group.

Prerequisites The Personalization mode is active. If not, activate it by following the steps in: Enable Personalization Mode.

A customization with one or more target groups is available. A personalized promotion rule has already been created.

 Note To make the rule visible on the storefront, you should publish it rst.

Procedure

![137_image_0.png](137_image_0.png)

Open this video in a new window 1. In the Personalization mode, go to Library Manage Library .

The Customization Library window shows up.

2. Select a customization and open it.

A list of target groups becomes available.

3. Select a target group you want to add a personalized promotion to and select Commerce Customizations from the more menu.

| Manage Customization Library                                                                                                                                                   | x                         |              |           |                          |     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------|-----------|--------------------------|-----|
| Apparel UK Content Catalog - Staged | Customizations (S)                                                                                                                       | Search Customizations   Q | All Statuses | >         | Create New Customization |     |
| Customization                                                                                                                                                                  | Target Groups             | Components   | Status    | Start                    | End |
| 1 SummerSale                                                                                                                                                                   | 1                         | Enabled      | ..        |                          |     |
| ✓ SpringSale                                                                                                                                                                   | 5                         | Enabled      | ...       |                          |     |
| SpringSaleVipBronzeMen                                                                                                                                                         | 2                         | Enabled      | 00        |                          |     |
| SpringSaleVipGoldWomen                                                                                                                                                         | 3                         | Enabled      | 00        |                          |     |
| Edit                                                                                                                                                                           |                           |              |           |                          |     |
| SpringSaleVipSilverWomen                                                                                                                                                       | 2                         | Enabled      | Disable   |                          |     |
| SpringSaleOver30AndShortsLoverAndNotVipGold                                                                                                                                    | Commerce Customization    |              |           |                          |     |
| 2                                                                                                                                                                              | Enabled                   | Move up      |           |                          |     |
| SpringSaleDefault                                                                                                                                                              | 1                         | Disabled     | Move down |                          |     |
| Remove                                                                                                                                                                         |                           |              |           |                          |     |
| 1 WinterSale                                                                                                                                                                   | 1                         | Enabled      | ...       |                          |     |
| ❯ CategoryLover                                                                                                                                                                | 2                         | Enabled      | 00        |                          |     |
| > VIP                                                                                                                                                                          | 4                         | Enabled      | 000       |                          |     |
| A new window appears. In the Promotion field, you can see a list of available promotions. The list includes only the promotion rules, which have the Personalized condition as |                           |              |           |                          |     |

Since the list includes all personalized promotions created for various catalogs, an additional list of catalogs is displayed next to the promotion list to make it easier for the right promotion.

4. Select the personalized promotion you have created in Creating a Personalized Promotion Rule . You can add more promotions if needed.

5. Click Save to finish.

6. The promotion is added to the target group. If the customer is a VIP Gold Customer, the promotion is automatically activated if you add in the cart items over 75 GBP.

![139_image_0.png](139_image_0.png)

Results As a result of defining a promotion for a particular target group, a promotion action is created. It is recommended to use the SmartEdit therface to drectly create and assign Personalization Promotions Module Architecture The Personalization Promotions module is a set of extensions providing additional promotion functionality.

Dependencies The diagram presents the extensions of the Personalization Promotions module.

![140_image_0.png](140_image_0.png)

Recipes For a complete list of SAP Commerce Cloud recipes that may include this module, see Installer Recipes. For a complete list of the SAP Commerce Cloud, integration extension pack recipes that may include this module, see Installer Recipe Reference.

Extensions The Personalization Promotions module contains the following extensions:
personalizationpromotions Extension The personalizationpromotions extension contains the promotions-related functionality of the Personalization Module.

personalizationpromotionsbackoffice Extension The personalizationpromotionsbackoffice extension contains the Backoffice conguration for CxPromotionAction dened in the personalizationpromotions extension. personalizationpromotionssmartedit Extension The personalizationpromotionssmartedit extension extends the functionality provided in personalizationsmartedit extension with personalized promotions.

personalizationpromotionsweb Extension The personalizationpromotionsweb extension contains promotions-specic functionality of the Personalization Module.

personalizationpromotionssampledataaddon AddOn personalizationpromotionssampledataaddon AddOn provides the personalization-related promotion sample data for the storefronts.

## Personalizationpromotions Extension

The personalizationpromotions extension contains the promotions-related functionality of the Personalization Module.

Rule-Based Promotion The personalizationpromotions extension cooperates with the new rule engine-based promotions. It creates its own rule, which can be used with any promotion to make it personalized. A personalized condition can be used with any combination of other conditions. The condition does not accept any parameter. It is triggered if a logged in user generates a CxPromotionActionResult with this promotion.

personalizationpromotionsbackoffice Extension The personalizationpromotionsbackoffice extension contains the Backoffice conguration for CxPromotionAction dened in the personalizationpromotions extension.

Conguration The personalizationpromotionsbackoffice extension extends the personalizationservicesbackoffice extension functionality to enable managing CxPromotionActions.

personalizationpromotionssmartedit Extension This is   For more    the SAP Help  141 The personalizationpromotionssmartedit extension extends the functionality provided in personalizationsmartedit extension with personalized promotions.

## Personalizationpromotionsweb Extension

The personalizationpromotionsweb extension contains promotions-specic functionality of the Personalization Module. It extends the personalizationwebservices extension with information required to use personalizationpromotions through provided web services. The personalizationpromotionsweb contains denition of data objects representing CxPromotionAction and allows creation / editing / removing of such actions using personalizationwebservices action endpoint.

personalizationpromotionssampledataaddon AddOn personalizationpromotionssampledataaddon AddOn provides the personalization-related promotion sample data for the storefronts.

 Caution This page refers to software that has been deprecated as part of the Accelerator UI and older OCC template extensions deprecation. For more information, see Deprecated Accelerator UIs and OCC Template Extensions - Deletion in SAP Commerce Cloud 2211.

The AddOn adds the promotion actions and promotion source rules data to the existing electronics and apparel b2c stores as well as the b2b powertools store. It also provides personalization-specic Rule Groups.

Personalization Promotions Module Implementation Extend personalization functionality by adding promotion actions and conguring the settings in SmartEdit.

Personalization Promotions Get to know the technical details of personalization promotion functionality.

CxPromotionAction You can easily extend the promotion functionality by extending CxAbstractAction with CxPromotionAction and CxAbstractActionResult with CxPromotionActionResult.

cxpromotionsforcatalog Query The cxpromotionsforcatalog query endpoint returns a list of promotions for a given catalog.

Personalization Promotions Get to know the technical details of personalization promotion functionality.

The personalization promotions functionality is included in the following Angular modules:
personalizationpromotionssmarteditContainer (wired with the SmartEdit container application).

personalizationpromotionssmartedit (wired with the SmartEdit application).

Project Components The functionality provided by the modules can be found in the following directories of the project:
personalizationpromotionssmarteditcommons This directory contains the utility features, which are included in personalizationpromotionssmarteditModule and personalizationpromotionssmarteditcontainerModule. It also contains the personalizationpromotionssmarteditRestService.ts: including a service used to collect the data from web services. personalizationpromotionssmarteditcontainer This directory contains all modules used in personalizationsmarteditcontainerModule.

Additionally it includes the management/commerceCustomizationView subdirectory, which contains functionality registering promotions as commerce actions. As a result, promotions can be turned on for customers who belong to a particular target group.

personalizationpromotionssmarteditPromotionsModule The personalizationpromotionssmarteditPromotionsModule module is a part of personalizationpromotionssmartedit and is responsible for the following actions:
Registering cxPromotionActionData type in the personalizationsmarteditCommerceCustomizationService.

Retrieving available promotions.

Creating an object representing a new promotion action and storing it in personalizationsmarteditCommerceCustomizationView.

 Note The personalizationsmartedit.commercecustomization.promotions.enabled conguration key available in SmartEdit may be set to false to disable the possibility of personalizing promotions.

This is   For more    the SAP Help  142 To see how to manage the commerce customizations using the personalization module, see Customization Library.

## Cxpromotionaction

You can easily extend the promotion functionality by extending CxAbstractAction with CxPromotionAction and CxAbstractActionResult with CxPromotionActionResult. The CxPromotionAction can only be created for an existing promotion. That's why the cxPromotionActionPrepareInterceptor was implemented to validate whether a promotion has already been published. By default, a CxPromotionAction may be created for any promotion, even the one without a personalized condition. However, it is recommended to add such a condition when the action is created.

You can add a personalized condition by setting the personalizationpromotions.promotions.modifyByAction.enabled to true.

This will change the behavior of the interceptor to not only validate if a target promotion exists but to also check if such a target promotion is personalized. If it is not, then the interceptor will add a personalized condition to the rule. If the rule was published before the modication it will be published again.

cxpromotionsforcatalog Query The cxpromotionsforcatalog query endpoint returns a list of promotions for a given catalog. The personalizationpromotionsweb extension extends the query endpoint dened in the personalizationwebservices with the cxpromotionsforcatalog which returns a list of PromotionRuleWsDTO - returns list of PromotionRuleWsDTO for a given catalog parameters: catalog, status (optional)
A sample request looks as follows:
POST https://localhost:9002/personalizationwebservices/v1/query/cxpromotionsforcatalog POST Data :
{
 "params": {
 "entry" : [
 { "key" : "catalog", "value" : "electronicsContentCatalog" }
 ]
 }
 } Request Headers: Accept: application/json Content-Type: application/json Authorization: Bearer 3ac71f81-739e-41d2-9901-6f2a1a4d5fc6 The behavior of cxpromotionsforcatalog query depends on personalizationpromotions.promotions.modifyByAction.enabled property. If it is set to false, only personalized promotions are returned. If it is set to true, all promotions in a given catalog are returned.

## Personalization Search Module

The functionality provided by the Personalization Search module along with the use of SmartEdit features gives the users personalized search experience through the search proles used in the personalization mode.

![142_image_0.png](142_image_0.png)

Personalization Search Module Features The Personalization Search module provides a range of features related to combining search proles with personalized content. For example, you can assign search prole to a selected target groups to make the search results personalized for the user.

Search Proles in Personalization Search proles created in Adaptive Search can be used in personalization mode in SmartEdit.

Search Proles in Personalization Search proles created in Adaptive Search can be used in personalization mode in SmartEdit.

Use Case A marketing manager wants to display different search prole settings for particular groups of customers. When conguring the target group in the personalization mode in SmartEdit, the user assigns a specic search prole to the target group. As a result, the customers belonging to the target group can view a search conguration targeted specically at them. For example, fans of a certain brand see the brand-related products rst, as a result of boosting them in the search prole.

Features Using Search Proles in Adaptive Search Provides a smooth integration between search proles available in Adaptive Search with the commerce customizations functionality in Personalization (based on SmartEdit).

Personalization Search Module Architecture Personalization search module is a set of extensions enabling the use of search proles in personalization.

Dependencies The following UML displays the dependencies between all extensions providing the functionality:
Click on an extension to view detailed information about it.

This image is interactive. Hover over each area for a description. Click highlighted areas for more information.

![143_image_0.png](143_image_0.png)

![143_image_1.png](143_image_1.png)

Recipes For a complete list of SAP Commerce Cloud recipes that may include this module, see Installer Recipes.

For a complete list of the SAP Commerce Cloud, integration extension pack recipes that may include this module, see Installer Recipe Reference.

Extensions The personalization search module contains the following extensions:
personalizationsearch Extension The personalizationsearch extension provides the core implementation for using search proles in personalization mode.

personalizationsearchsmartedit Extension The personalizationsearchsmartedit extension extends the personalizationsmartedit extension by adding search functionality to commerce customizations.

personalizationsearchsamplesaddon Extension The personalizationsearchsamplesaddon extension provides the sample data for the storefronts. It includes several customizations and search proles already assigned to the groups.

personalizationsearchbackoffice Extension The personalizationsearchbackoffice extension provides the Backoffice conguration for adding the search proles to target groups in personalization mode, as well as the possibility of adding a search action using the Backoffice Administration Cockpit.

personalizationsearchweb Extension The personalizationsearchweb extends the personalizationwebservices extension with information required to use the personalized search functionality through provided web services.

personalizationsearch Extension The personalizationsearch extension provides the core implementation for using search proles in personalization mode.

Dependencies This image is interactive. Hover over each area for a description. Click highlighted areas for more information.

![144_image_0.png](144_image_0.png)

The personalizationsearchsmartedit extension extends the personalizationsmartedit extension by adding search functionality to commerce customizations.

The extension provides the following functionality:
The personalizationsearchsmartedit extension registers a new CxSearchProfileActionData action type along with an html template.

The personalization commerce customization mechanism adds the registered item (a search action type) to the top drop-down menu in the commerce customization modal (1).

Once the search action is selected from the menu, the search prole commerce customization template is added to commerce customization modal. This template contains a table of search proles with reordering options and a drag&drop mechanism, implemented based on angular ui tree drag&drop functionality (2).

![145_image_0.png](145_image_0.png)

![145_image_1.png](145_image_1.png)

![145_image_2.png](145_image_2.png)

This is custom documentation. For more information, please visit the SAP Help Portal personalizationsearchsamplesaddon Extension The personalizationsearchsamplesaddon extension provides the sample data for the storefronts. It includes several customizations and search proles already assigned to the groups.

 Caution This page refers to software that has been deprecated as part of the Accelerator UI and older OCC template extensions deprecation. For more information, see Deprecated Accelerator UIs and OCC Template Extensions - Deletion in SAP Commerce Cloud 2211.

The extension includes several customizations and search proles already assigned to the groups. Along with the sample data we provide a searchmanager account for managing the search proles using the adaptive search perspective and the Backoffice Administration Cockpit.

Dependencies This image is interactive. Hover over each area for a description. Click highlighted areas for more information.

![146_image_0.png](146_image_0.png)

![146_image_1.png](146_image_1.png)

personalizationsearchbackoffice Extension The personalizationsearchbackoffice extension provides the Backoffice conguration for adding the search proles to target groups in personalization mode, as well as the possibility of adding a search action using the Backoffice Administration Cockpit.

Dependencies This image is interactive. Hover over each area for a description. Click highlighted areas for more information.

![147_image_0.png](147_image_0.png)

![147_image_1.png](147_image_1.png)

personalizationsearchweb Extension The personalizationsearchweb extends the personalizationwebservices extension with information required to use the personalized search functionality through provided web serv Dependencies This image is interactive. Hover over each area for a description. Click highlighted areas for more information.

![148_image_0.png](148_image_0.png)

