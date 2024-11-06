# Impex Api

The ImpEx API allows you to interact with the ImpEx extension. You can use the API to import and export data, and extend or adapt it to your needs. For details of the ImpEx user interface in Backoffice or SAP Commerce Cloud Administration Console, see Using ImpEx with Backoffice or SAP Commerce Cloud Administration Console.

Import API You can trigger an import using the import API in a number of ways. These include using the back end management interfaces, as well as triggering it programmatically This is   For more    the SAP Help  31 Export API
You can trigger an export using the export API in a number of ways. These include using the back end management interfaces, as well as triggering it programmatically. Validation Modes The validation mode controls validation checks on ImpEx. By default, strict mode is enabled meaning all checks are run. Customization You can extend your import or export process with custom logic. Customization allows you to addresses requirements that cannot be achieved completely with the ImpEx extension. Scripting You can use Beanshell, Groovy, or JavaScript as scripting languages within ImpEx. In addition, ImpEx has special control markers that determine simple actions such as beforeEach, afterEach, if. User Rights The ImpEx extension allows you to modify access rights for users and user groups. Translator A translator class is a converter between ImpEx-related CSV les and values of attributes of SAP Commerce Cloud items

## Import Api

You can trigger an import using the import API in a number of ways. These include using the back end management interfaces, as well as triggering it programmatically There are four basic ways of triggering an import of data for the ImpEx extension:
1. Using the Backoffice ImpEx Import Wizard. For details, see Import Wizard.

2. Creating an Import CronJob in Backoffice. For details, see Import CronJob.

3. Using ImpEx Import page in SAP Commerce Cloud Administration Console. For details, see Import Through Administration Console.

4. Using the Import API, which is described here.

To support the systems with large numbers of products, SAP Commerce Cloud has a capability of multithreaded import operations. For details, see Multithreaded Import. You have several possibilities to perform an import programmatically. The decision depends mainly on the specialized conguration needs. The basic kind of processing is the instantiation and conguration of the Importer class. For detailed information, Using an Importer Instance. Here you have the full range of conguration possibilities. The instantiation and conguration of an Importer class triggers an import cronjob too, but it additionally provides the features of a cronjob, that is, all settings, results, and logs are stored as persistent, which is strongly preferred. The third convenient alternative is the usage of the API methods of the ImpExManager method. For detailed information, see Using a Method of ImpExManager. They also use an import cronjob, but you do not have to create and congure it on your own.

## Using An Importer Instance

The Importer class is the central class for processing an import. The process for importing by directly using this class has 3 steps.

## Procedure

1. Instantiate the class.

While instantiating the Importer class, this CSV-stream is given using a CSVReader or an ImpExImportReader. If you only want to specify the input stream, use an CSVReader class, the Importer instantiates a corresponding This is   For more    the SAP Help  32 ImpExImportReader. The usage of an ImpExImportReader is only needed, if special settings while instantiation are needed (settings after instantiation can be done using the getReader() method of the Importer instance). Example:
CSVReader reader = new CSVReader( "input.csv", "utf-8" ); Importer importer = new Importer( reader );
or:
Importer importer = new Importer( new ImpExImportReader( reader, new MyImportProcessor() ) );
2. Congure the import process.

You have several possibilities for conguring the import process.

You can congure the used ImpExImportReader using the getReader method. Here you can congure several things about the reading of the input (skipValueLines, enableCodeExecution, and so on) or item processing (setRelaxedMode, and so on). You can set a DumpHandler for specifying the dump le handling. Thirdly, you can set an ErrorHandler to specify the process in case of an error. Fourthly, you can set the maximal amount of passes for resolving dumped value lines.
3. Trigger the import.

You can perform the import using the importNext, which processes the input stream until an item was processed (that means inserted, updated or removed). It returns the processed item. Another possibility is the usage of the importAll method, which calls the importNext method until nishing of the input stream. While and after the import process, you have several possibilities to get information about the state, for example: current pass, processed items, and so on. Example:
Item item = null; do { item = importer.importNext(); System.out.println( "Processed items: " + getProcessedItemsCountOverall() ); } while( item != null );
or:
importer.importAll(); System.out.println( "Processed items: " + getProcessedItemsCountOverall() );

## Using Impeximportcronjob

When using ImpExImportCronjob, you have the advantage of persistent logging, as well as persistent result and settings holding. The possible settings you can nd in the API of the cron job class. The following sample shows an example conguration:
try { // Creating import media ImpExMedia jobMedia = createImpExMedia( "myImportScript", "UTF-8" );
This is   For more    the SAP Help  33 jobMedia.setFieldSeparator( ';' ); jobMedia.setQuoteCharacter( "\"" ); jobMedia.setData( new DataInputStream( ImpExManager.class.getResourceAsStream("myScript.impex")), jobMedia.getCode() + "." + ImpExConstants.File.EXTENSION_CSV, ImpExConstants.File.M // create cronjob ImpExImportCronJob cronJob = ImpExManager.getInstance().createDefaultImpExImportCronJob(); cronJob.setEnableCodeExecution( codeexecution ); cronJob.setJobMedia( jobMedia ); // process import cronJob.getJob().perform( cronJob, true ); } catch( UnsupportedEncodingException e ) { log.error( "Given encoding is not supported", e ); }

## Using A Method Of Impexmanager

The ImpExManager class provides methods with the qualier importData. These methods all use a cron job for performing an import from a given source and help you to simplify the import call. Important parameters for the import methods are as follows:
synchronous - sets the created cronjob to be performed synchronous or asynchronous. removeOnSuccess - sets the cronJob and created medias to be removed if nished successfully. codeExecution - sets the execution of BeanShell code to be enabled.

If the removeOnSuccess ag is set, the resulting cronjob may not be valid anymore after import, because it is already removed.

InputStream is = ImpExManager.class.getResourceAsStream( csv ); ImpExManager.getInstance().importData( is, "windows-1252", CSVConstants.HYBRIS_FIELD_SEPARATOR, CSVConstants.HYBRIS_QUOTE_CHARACTER, true );
Another set of methods for import are the importDataLight methods. These are lightweight methods, note that they have prex light, using no cronjob, and so no persistent and logging offset.

InputStream is = ImpExManager.class.getResourceAsStream( csv ); ImpExManager.getInstance().importDataLight( is, "windows-1252", true );

## Data Inclusion

Often you want to separate your ImpEx script logic from the data for example if the data is provided by a foreign system, and you do not want to touch this le by adding a ImpEx header. This is possible by using the include methods of the ImpExReader instance registered at the BeanShell context.

Storing both header denitions and data in one single le is a possible approach for smaller les. However, if you want to separate your ImpEx script logic from the data, for example, if you need to process externally supplied data (from a customer or supplier), or if your le exceeds several hundred lines of data, you probably want to split it. The ImpEx extension allows you to include other les within the parse process using the include methods of the ImpExReader class.

This is   For more    the SAP Help  34 Basically there are three possibilities for inclusion, rst the reference of input streams outside of the platform like les from le system, second the referencing of medias from the platform, and the third alternative is the direct inclusion of data from a database.

## Inclusion Of Data Using Input Streams

The inclusion of input streams within the parse process can be achieved by using the includeExternalData methods (marked with the BeanShell annotation) of the ImpExReader instance registered as ImpEx variable at the BeanShell context. Just add such a call to the script and the stream is included directly at the position of the call within the parse process. So be sure that there is a header written at the main script before calling an include containing only raw data.

INSERT_UPDATE Product;code[unique=true];...

"\#% impex.includeExternalData(ImpExManager.class.getResourc

| Name         | Type   | Default value   | Description                                                                                   |
|--------------|--------|-----------------|-----------------------------------------------------------------------------------------------|
| linesToSkip  | int    | 0               | Amount of lines that are skipped when start reading from external data.                       |
| columnOffset | int    | -1              | The column offset compared to ImpEx standard: if the rst column already contains data use -1. |
| encoding     | string | UTF-8           | The encoding of the external CSV data.                                                        |
| delimiter    | char   | ;               | Field separator used in external data.                                                        |

The common parameters used at most method signatures are: An other method signature alternative allows to set a CSVReader instance instead of an input stream where you can congure some additional parameters like the maximal buffer size for reading a cell, which is spread over many lines (By default a ImpEx CSV cell can only consist of 10000 lines).

$$\operatorname*{\mathsf{x B u f f e r i c i n e}}_{\mathsf{e E x t e r n a l D a}}$$

INSERT_UPDATE Product;code[unique=true];...

"\#% CSVReader reader = new CSVReader( ImpExManager.class.ge "\#% reader.setMaxBufferLines(100000l);" "\#% impex.includeExternalData( reader, 1, -1 );"

You can chain includes of data, so you can include data within an already included data. Please do not use the ImpExManager.importData() methods within BeanShell code, because it starts a completely separate import and with that a completely different context as for example the BeanShell interpreter and the resolving of dumped lines.

## Inclusion Of Data Using Media

If you already have your data le added to the platform as an instance of a ImpExMedia type, you can simply include the media using the following BeanShell call:
INSERT_UPDATE Product;code[unique=true];...

"\#% impex.includeExternalDataMedia( ""MyDataMediaCode"" );"

The advantage of using the media type is you can do the conguration using the properties of the media instance, so you just give the code of the media as parameter. Unfortunately there can be medias with the same code, so it is necessary to provide the import process with a collection of all possibly included medias. You can only do it by using an import procedure where an import cronjob takes part, because the collection of medias is stored at the cronjob instance. Summarized, to include data using a media, you have to use an import proceeding with cronjob, and you have to set the collection of all included medias at this cronjob (the attribute is called externalDataCollection).

## Inclusion Of Data Through Database Statements

Using the BeanShell, you can also include external data directly from a database connection. Therefore you rst have to open a JDBC connection using the initDatabase method. Secondly, you can include the data giving a SQL-query whose result set ts the dened header line.

\# Initialization INSERT_UPDATE XYType; $code[unique=true]; $mandant; $typ; b \#% impex.initDatabase( <dburl>, <user>, <password>, <driver "\#% impex.includeSQLData( "" SELECT ""+ "" myProduct.ProductID, myProduct.Tenant, Variant.myVaria myProduct.ProductID + '-base::' + CAST( myProduct.Tenant AS "" FROM DB.SpecialProduct as Product JOIN DB.SpecialProduct "" ON myProduct.ProductID = Variant.ID and myProduct.Tena "" WHERE ""+ "" Variant.myVariantID > 0 AND Product.variant ='xytype'" ); "
Both methods and their signatures can be accessed by using the registered ImpEx variable of type ImpExReader.

## Resolving

In contrast to export, ImpEx import provides a resolving mechanism to deal with value lines that cannot be imported by the time the parser runs across them. These lines are imported as far as possible, the unresolved lines are dumped into a temporary le and read in again when the current le has completed parsing. The following code snippet gives an example of a case where a line may remain unresolved:
INSERT Address; appartment; owner(Principal.uid) ;testApp; testUser INSERT Customer;uid[unique=true] ;testUser Lines 1 and 2 try to create an address using the user testUser as owner. However, testUser is dened in lines 3 and 4. Therefore, testUser does not exist when the attempt to create the address is attempted, and testUser cannot be assigned to the address at this point of time. The parser then writes the address denition into a temporary le. When the main le has completed, that temporary le is read in again. Now testUser exists, and the address can be nished. Such a further run is called pass and an execution of the sample script can result in the following log:
Starting import synchronous using cronjob with PK=141025265286919088 and name=00000014-ImpEx-Import INFO - Starting import with pass 1 INFO - Starting pass 2 INFO - Import finished successfully within 00:00:00:328 (hh:mm:ss:ms)

The dump le is stored by default at the used cronjob (attribute unresolvedDataStore at Log tab) and contains in the above example the following lines:
insert Address;appartment;owner(Principal.uid) ,,cannot create due to unresolved mandatory/initial columns;test;testUser If all mandatory columns in the value line were given and successfully translated, an item is created despite the fact that maybe other non-mandatory attributes are not resolved. After creation, an update of the resting columns is made. The second line of the dumped line example shows the value line, which was not completed successfully. The rst column of the value line holds three pieces of important information separated by commas. The rst eld contains the type of the item already created when mandatory attributes were resolved, but not all non-mandatory ones. The second holds the PK of this created item. The third contains an error message, which explains the reason not all attributes were resolved successfully. If the item is already created but not all attributes were resolved, the already set attributes are ignored with the <ignore> ag. So just search for attributes not marked with that ag. The following content of such a dump le shows that a value line representing a Product could not be imported completely because the detail attribute was not resolved. You can see that the rst and second attribute of the value line contain an <ignore> marker, which means that the product was created setting these two attributes. The third attribute was not resolved so there is no <ignore> marker.

INSERT Product;code;catalogVersion[allowNull=true];detail(code) Product,288342436307920,, column 3: cannot resolve value 'testDetail' for attribute 'detail';<ignor If a dump le cannot be imported completely, again, another dump le is written, and the next pass starts. If a dump le has the same size as a dump le of its following pass the import is aborted with following log:
ERROR (master) [ImpExImportJob] Can not resolve lines any more ... aborting further passes (at pass Finally could not import 1 lines!

In this case, you have to evaluate (as described above) the last dump le stored at the used cronjob. Please be aware that only header and value lines are dumped, no BeanShell. So there is no chance to execute BeanShell code at a second pass.

## Using Header Abbreviations

ImpEx provides a way to shorten length column declarations by using regexp patterns and replacements. Although the ImpEx header denition language provides a most exible way of using custom column translators, their declaration can grow long. You can shorten them using the ImpEx alias syntax. The following example shows how to use this syntax to shorten classication columns declaration by giving them a new syntax:
Put this into your SAP Commerce Cloud platform local.properties le:
impex.header.replacement.1 = C@(\\w+) ... @$1[ system='\\$systemName', version='\\$systemVersion', translator='de...ClassificationAttributeTranslator']
Note that the line has been wrapped to make it more readable - you have to leave it on one line, of course. Also note the Java string notation has to be used, that's why there are double '\'s. All parameters starting with impex.header.replacement are parsed as ImpEx column replacement rules. The parameter has to end with a number that denes the priority of the rule. This way ambiguous rules can be sorted.

This is   For more    the SAP Help  37 So what's this for? The rst part of the property C@(\w+) denes the new abbreviation pattern to be used to declare classication attribute columns with. The second part is the replacement text including the attribute qualifer match group $1. In fact, it contains the original special column declaration. Both parts are to be separated by '...'. So all that is needed now to declare classication attribute column is this:
$systemName=MySys $systemVersion=1.0 INSERT_UPDATE Product; code[unique=true]; C@attr1; C@attr2 ; ...

Now the whole translator denition is hidden and you do not need to declare any helper alias for that. Nevertheless both alias denitions are mandatory to tell the classication column which system and version it should take its attribute from.

## Export Api

You can trigger an export using the export API in a number of ways. These include using the back end management interfaces, as well as triggering it programmatically. You can trigger an export of data for the ImpEx extension in the following ways:
1. In Backoffice using the ImpEx Export Wizard. See Export Wizard.

2. In Backoffice, using an ImpExExportCronjob. See Export Using an ImpexExportCronJob.

3. In SAP Commerce Cloud Administration Console, using the ImpEx extension page. See Export Through Administration Console.

4. Using the export API which is described here.

While at an import script, the data to be imported is specied via value lines, an export script has a different structure to dene the set of items to be exported, as well as the export le format. Find more information on the structure of an export script, see Structure of an Export Script. The available validation modes for an export script are described in Validation Modes. You have several possibilities to perform an export programmatically. The decision depends mainly on the specialized conguration needs.

The basic kind of processing is the instantiation and conguration of the Exporter class. Here you have the full range of conguration possibilities. The instantiation and conguration of an Exporter does an export cronjob too, but it additionally provides the features of a cronjob, that is: all settings, results, and logs are stored as persistent, which is strongly preferred. The third convenient alternative is the usage of the API methods of the ImpExManager. They also use an export cron job, but you do not have to create and congure it on your own.

## Export Using An Exporter Instance

The Exporter class is the central class for processing an export. You can use this class directly for exporting data in three steps.

## Procedure

1. Dene your export conguration.

All conguration is done by instantiation of an ExportConfiguration. This is a container for all conguration you can set for the exporter and is passed at instantiation of the Exporter. The constructor needs an ImpExMedia where the export script is managed by and the validation mode given as EnumerationValue.

ExportConfiguration config = new ExportConfiguration( impexscript, ImpExManager.getExportOnlyM
Conguration of additional settings can then be done via the setter methods of the object, for example for setting the result medias to use explicitly. Note that otherwise they are created automatically.

config.setDataExportTarget(datatarget); config.setMediasExportTarget(mediastarget);
2. Create an instance of the class.

With the created ExportConfiguration you can now create an instance of the Exporter class using:
Exporter exporter = new Exporter( config );
3. Start the export.

You can start the export process using a simple call of the export method:
Export export = exporter.export();
The returned Result item contains all result medias accessible via getter methods.

## Export Using An Impexexportcronjob

You can generate an export using the ImpEx export cron job.

When using the ImpExExportCronjob, you have the advantage of persistent logging, as well as persistent result and settings holding. You can create a cron job using the createDefaultImpExExportCronJob method of the ImpExManager class.

Possible settings are provided in the API of the cron job class. For further details, see Using the ImpExImportCronJob. A sample conguration looks like this:
// Creating export media ImpExMedia jobMedia = createImpExMedia( "myExportScript", "UTF-8" ); jobMedia.setFieldSeparator( ';' ); jobMedia.setQuoteCharacter( "\"" ); jobMedia.setData( new DataInputStream( ImpExManager.class.getResourceAsStream("myScript.impex")), jobMedia.getCode() + "." + ImpExConstants.File.EXTENSION_CSV, ImpExConstants.File.MIME_TYPE // Creating an ExportConfiguration ExportConfiguration config = new ExportConfiguration( impexscript, ImpExManager.getExportOnlyMode() // Creating export cronjob ImpExExportCronJob cronJob=createDefaultExportCronJob( config ); // export cronJob.getJob().perform( cronJob ); // Get result Export export=cronJob.getExport();

## Using An Export Method Of The Impex Manager

You can export data using dedicated methods provided by the ImpExManager class.

This is   For more    the SAP Help  39

## 

The ImpExManager class has different methods with the qualier exportData. These methods all use a cronjob for performing an export with given ExportConfiguration and help you to simplify the import call. The only important additional parameter for this methods is synchronous. This parameter denes if the created cronjob is performed synchronous or asynchronous.

// Creating an ExportConfiguration with an media containing the script ExportConfiguration config = new ExportConfiguration( impexscript, ImpExManager.getExportOnlyMode()
// Export Export export = ImpExManager.getInstance().exportData( config, true );
Another set of methods for export are the exportDataLight methods. These are lightweight methods using no cronjob and so no persistent and logging offset.

// Creating an ExportConfiguration with an media containing the script ExportConfiguration config = new ExportConfiguration( impexscript, ImpExManager.getExportOnlyMode() // Export Export export = ImpExManager.getInstance().exportData( config );

## Structure Of An Export Script

An export script needs to specify the target le to export items to, a header line for dening how to export the items, and a statement specifying which items to export. The structure of a typical export script using the export of all languages is shown in the following example.

"\#% impex.setTargetFile( ""language.csv"", true, 1, -1 );" // 1. where to export insert_update Language;active;fallbackLanguages(isocode);isocode[unique=tru "\#% impex.exportItems( ""Language"" , true );" // 3. what to export The sample shows a typical script. Here all languages of the system are to be exported to a le called language.csv using the given header. The order of the three statements is important.

1. The rst line is used to specify where to export the items followed by the next header. Using the given le name, a le is created at the resulting archive where all items are written to and which are exported using the next header line. The setTargetFile method is located at the Exporter class and comes in different signatures all covering a different combination of the parameters. The signature using all parameters is:
public void setTargetFile( final String filename, boolean writeHeader, int linesToSkip, int of where the parameters are:

| Name         | Type                                                              | Default                    | Description                                                                       |
|--------------|-------------------------------------------------------------------|----------------------------|-----------------------------------------------------------------------------------|
| lename       | String                                                            | Type code congured at next | Name for target le within                                                         |
| header line. | resulting archive where the items of the next header are written. |                            |                                                                                   |
| writeHeader  | boolean                                                           | true                       | If set, the header is written as a comment to the rst line at the target data le. |

| Name         | Type   | Default   | Description                                                                                                                                                                                    |
|--------------|--------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| linesToSkip  | int    | 0         | Parameter is used at generated include statement at the generated import script. In the import case, it means the amount of lines that are skipped when start reading from external data.      |
| columnOffset | int    | -1        | Species the column offset of the target data le compared to ImpEx standard: if the rst column already contains data use -1 - is set at generated include statement at generated import script. |

If you use a signature with less parameters, the default values are used for the missing ones. Be aware that you do not have to give such a statement, it is optional. In that case, all default values are used (a le is created using the name of the type congured at the header line).

2. The second line is a header line describing how to export items. This is analogous to the import case except for the header mode (INSERT, UPDATE, and so on), which is ignored at the export. However a header mode has to be given, furthermore the header is copied to the generated import script, and so it is useful to give a correct one.

3. The exportItems call gathers the set of items to export and exports them using the set header and target le. The method is located at the Exporter class and comes in different signatures of different nature.

exportItems by item set:
public void exportItems( Collection<Item> items )
public void exportItems( String[
These methods export given items where the items can be passed either as a list of PK's (String) or directly using a Collection of items. exportItems by type code:
public void exportItems( String typecode )
public void exportItems( String public void exportItems( String public void exportItems( String It gathers items by selecting all items of a given type code and exports them. The parameters are:

| Name         | Type    | Default   | Description                                                                                                                       |
|--------------|---------|-----------|-----------------------------------------------------------------------------------------------------------------------------------|
| typecode     | String  | -         | The typecode where all items are gathered and exported.                                                                           |
| count        | int     | 1000      | A range parameter - many FlexibleSearches are performed each covering count items of the type - does not limit the overall count. |
| inclSubTypes | boolean | false     | If true, subtypes of given type are considered.                                                                                   |

This is   For more    the SAP Help  41

## Note Paging Of Search Result

Exporter API by default uses pagination of search results, therefore, to have accurate results, your FlexibleSearch queries must contain the ORDER BY clause, for example ORDER BY {pk}. If you disable pagination or you use some method that cares also for ordering of results, then the ORDER BY clause is not needed. For more details read FlexibleSearch, section Paging of Search Result. // since 3.1-RC
public void exportItemsFlexibleS public void exportItemsFlexibleS final boolean dontNeedTotal, int // since 3.1-u6 public void exportItemsFlexibleS
It gathers items using a given FlexibleSearch query. Be aware that the resulting items have to be compatible with the current header.

You can generate a script for all types of your platform by using the ScriptGenerator in Backoffice. For details, see Script Generator.

## Validation Modes

The validation mode controls validation checks on ImpEx. By default, strict mode is enabled meaning all checks are run. There are ve different modes available, where two are only applicable for import and three for export.

Import Strict - Mode for import where all checks relevant for import are enabled. This is the preferred one for an import.

Import Relaxed - Mode for import where several checks are disabled. Use this mode for modifying data not allowed by the data model like writing non-writable attributes. Please be aware of the fact that this mode only disables the checks by ImpEx, if there is any busines logic that prevents the modication, the import fails anyway.

Export Strict (Re)Import - Mode for export where all checks relevant for a re-import of the exported data are enabled.

This is the preferred mode for export if you want to re-import the data as in migration case. Export Relaxed (Re)Import - Mode for export where several checks relevant for a re-import of the exported data are disabled. Export Only - Mode for export where the exported data are not designated for a re-import. There are no checks enabled, so you can write for example a column twice, which cannot be re-imported in that way. Preferred export mode for an export without re-import capabilities.
The following table gives an overview of which checks can be disabled by using a different mode than the strict one.

| Check                                                               | Thrown Exception   | Import                    | Import   | Export   | Export   | Export   | Check location (for developers)   |
|---------------------------------------------------------------------|--------------------|---------------------------|----------|----------|----------|----------|-----------------------------------|
| Description                                                         | Strict             | Relaxed                   | Only     | Relaxed  | Strict   |          |                                   |
| Clashing of columns (columns referencing same attribute descriptor) | Ambiguous columns columnsrelated code.                    | HeaderDescriptor.validate |          |          |          |          |                                   |

| 7/12/2024 Check                                                                      | Thrown Exception                                                                                                                                | Import                                      | Import   | Export   | Export   | Export   | Check location (for developers)   |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------|----------|----------|----------|-----------------------------------|
| Description                                                                          | Strict                                                                                                                                          | Relaxed                                     | Only     | Relaxed  | Strict   |          |                                   |
| Missing unique modier                                                                | Missing unique modier inside header-related code - at least one attribute has to be declared as unique (attributename[ internal:unique=true ]). | HeaderDescriptor.validate                   |          |          |          |          |                                   |
| No abstract                                                                          | Type type-related                                                                                                                               | HeaderDescriptor.calculatePermittedType     |          |          |          |          |                                   |
| type                                                                                 | code is abstract.                                                                                                                               |                                             |          |          |          |          |                                   |
| No jalo only                                                                         | Type type-related                                                                                                                               | HeaderDescriptor.calculatePermittedType     |          |          |          |          |                                   |
| type                                                                                 | code is jaloOnly.                                                                                                                               |                                             |          |          |          |          |                                   |
| Missing mandatory columns                                                            | Type type-related                                                                                                                               | HeaderDescriptor.calculatePermittedType     |          |          |          |          |                                   |
| code requires missing column(s) column-related code.                                 |                                                                                                                                                 |                                             |          |          |          |          |                                   |
| Missing                                                                              | Type type-related                                                                                                                               |                                             |          |          |          |          |                                   |
| unique column                                                                        | code has no unique columns.                                                                                                                     | HeaderDescriptor.calculatePermittedType     |          |          |          |          |                                   |
| Read-only (write=false, initial=false) column with unique modier.                    | Unique attribute                                                                                                                                | StandardColumnDescriptor.validate           |          |          |          |          |                                   |
| attribute-related code is read-only which is not allowed.                            |                                                                                                                                                 |                                             |          |          |          |          |                                   |
| Mandatory columns without value (no default value, no allowNull modier)              | Value is NULL for mandatory attribute attribute-related code.                                                                                   | DefaultValueLineTranslator.translateColumnV |          |          |          |          |                                   |
| Dumping is disabled and a line has to be dumped                                      | Line line-related                                                                                                                               | ImpExImportReader.readLine                  |          |          |          |          |                                   |
| code could not be imported completely                                                |                                                                                                                                                 |                                             |          |          |          |          |                                   |
| Empty column                                                                         | No attributes                                                                                                                                   |                                             |          |          |          |          |                                   |
| expression                                                                           | specied for header with type type-related code.                                                                                                 | AbstractTypeTranslator.translateColumnDesc  |          |          |          |          |                                   |
| Column within item expression not searchable or has no persistence representation    | Attribute attribute                                                                                                                                                 | ItemExpressionTranslator.checkResolvableAt  |          |          |          |          |                                   |
| related code is not searchable - cannot use to resolve item reference via pattern.   |                                                                                                                                                 |                                             |          |          |          |          |                                   |
| This is custom documentation. For more information, please visit the SAP Help Portal | 43                                                                                                                                              |                                             |          |          |          |          |                                   |

| 7/12/2024 Check                                                   | Thrown Exception   | Import                                     | Import   | Export   | Export   | Export   | Check location (for developers)   |
|-------------------------------------------------------------------|--------------------|--------------------------------------------|----------|----------|----------|----------|-----------------------------------|
| Description                                                       | Strict             | Relaxed                                    | Only     | Relaxed  | Strict   |          |                                   |
| Column type within item expression is jalo-only.                  | Attribute attribute                    | ItemExpressionTranslator.checkResolvableAt |          |          |          |          |                                   |
| related code is jalo-only - cannot use to resolve item reference. |                    |                                            |          |          |          |          |                                   |

## Customization

You can extend your import or export process with custom logic. Customization allows you to addresses requirements that cannot be achieved completely with the ImpEx extension.

## Writing A Custom Cell Decorator

Using a cell decorator you can intercept the interpreting of a specic cell of a value line between parsing and translating of it. It means the cell value is parsed, then the cell decorator is called, which can manipulate the parsed string and then the translation of the string starts. You can congure the usage of a cell decorator by adding the modier cellDecorator to a header attribute specifying your decorator class.

INSERT MyType;...;myAttribute[cellDecorator=de.hybris.platform.catalog.jalo.classification.eclass.E
The specied class has to implement the CSVCellDecorator interface, which species a method:
String decorate( int position, Map<Integer, String> srcLine )
Here the whole parsed value line is passed (srcLine) where the line is a mapping of column position (Integer) to the parsed String. Furthermore the position of the column which has to be decorated is passed. As a result, the method estimates the decorated String, a decoration of the String inside the map has no effect. So a typical implementation is:
public class MyDecorator implements CSVCellDecorator
{ public String decorate( int position, Map<Integer, { String parsedValue=srcLine.get(position); return parsedValue+"modified"; // some decoration s } }
For more convenience, the ImpEx extension provides the AbstractImpExCSVCellDecorator implementation that additionally adds a member to the decorator holding a reference to the column descriptor where the decorator instance is applied. This descriptor is set via an additional init-method, so it is not available at the constructor calling phase. With that member you have access to the whole column specication especially all congured modiers and the whole related header descriptor.

## Writing A Custom Translator

If you have to change the translation logic for a value, then a decorator is not enough for your needs. In such cases you can write your own translator and congure it for the translation of specic attributes. You can do the conguration by simply adding the translator modier to the desired header attribute like:
This is   For more    the SAP Help  44 INSERT MyType;...;myAttribute[translator=de.hybris.platform.impex.jalo.translators.ItemPKTranslator In case the attribute is a real type attribute, the congured class has to extend the AbstractValueTranslator class in some way. This abstract class denes two methods:
1.

public abstract Object importValue( final String valueExpr, final Item toItem )
Implement the translation logic for the import case here. The given String is the parsed cell value (possible decorators already applied) and the passed item instance is the resolved item for example in case of an update or an insert where the current attribute is not mandatory. The result object represents the translated value and must be an instance of the expected attribute type. In case of an error (like a referenced item can not be resolved), you can call the protected setError method, which marks the cell as unresolved.

2.

public abstract String exportValue( final Object value )
Implement the translation logic for the export case here. The given object has to be translated to a String that has to be returned.

In most cases you want to use translation logic that already partly exists because ImpEx already provides a collection of translators. So please check rst to see if you can extend an existing one.

## Writing A Custom Special Translator

A special translator has to be written and congured in case you want to change the translation logic for special attributes, for example header attributes that have no counterpart at the type system. They are congured as normal translators:
INSERT MyType;...;@myAttribute[translator=de.hybris.platform.impex.jalo.media.MediaDataTranslator]
The congured translator has to implement the SpecialValueTranslator that species different methods. Thereby two methods are responsible for the real translation (import and export case), if you want to have default implementations for the other methods, just extend the AbstractSpecialValueTranslator. The two methods are:
1.

public void performImport( final String cellValue, final Item processedItem )
where you have to implement the translation logic for import. As for normal translators, you get the parsed cell value and the already resolved item instance. You have to return the translated value.

2.

public String performExport( final Item item )
where you have to implement the logic for export, which means you have to translate given object to a String

## Writing A Custom Script Modier For Script Generator

The ScriptGenerator generates a default export script for all types of systems. Often you want to change the script generation for special cases where the ScriptModier comes in play. The congured ScriptModier instance of a ScriptGenerator instance is asked in several cases, for example which root types have to be considered for traversing the type system tree. You can congure your ScriptModier by adding an instance to the ScriptModierEnum enumeration where the code of the new value has to represent your class name where dots are replaced by underscores, like:
de_hybris_platform_impex_jalo_exp_generator_MigrationScriptModifier With that you can choose ScriptModier at the ScriptGenerator wizard. The class specied at the enumeration has to implement the ScriptModier interface. The following methods are dened by this interface:
1.

void init( ScriptGenerator generator )
Add logic here that congures the related generator instance to your needs for example by calling generator.addIgnoreColumn( "Item", "allDocuments" );
for excluding the allDocuments attribute in general. See the APIDoc of the ScriptGenerator interface for conguration possibilities.

2.

boolean filterTypeCompletely( ComposedType type )
Here you have the chance to lter a type completely from script generation. A static default implementation that lters jaloonly types and views can be found at .lterTypeCompletely 3.

Set<ComposedType> getExportableRootTypes( ScriptGenerator callback )
Here you can specify the root set of types for which an entry at the generated export script is created. In case you do not want to implement the method, you can use a call to ExportUtils.getExportableRootTypes.

## Scripting

You can use Beanshell, Groovy, or JavaScript as scripting languages within ImpEx. In addition, ImpEx has special control markers that determine simple actions such as beforeEach, afterEach, if. The following is an example of a simple ImpEx import script using Beanshell:
INSERT_UPDATE Title;code[unique=true]
\#% beforeEach: line.clear(); ;foo With the scripting engine support in SAP Commerce Cloud, you can set the value of the ag impex.legacy.scripting to false to benet from new scripting features in ImpEx. You can then use not only Beanshell, but also Groovy and JavaScript.

The same example, but rewritten in Groovy, now looks like the following:
INSERT_UPDATE Title;code[unique=true]
\#%groovy% beforeEach: line.clear(); ;foo All you need to do is tell the console what language you use, for example %groovy%.

## Standard Imports

By default, a number of standard imports are always provided to you by default in ImpEx scripting, so you do not need to call them yourself. Here is a list of those imports:
import de.hybris.platform.core.*
import de.hybris.platform.core.model.user.* import de.hybris.platform.core.HybrisEnumValue import de.hybris.platform.util.* 
This is   For more    the SAP Help  46 import de.hybris.platform.impex.jalo.* import de.hybris.platform.jalo.* import de.hybris.platform.jalo.c2l.Currency import de.hybris.platform.jalo.c2l.* import de.hybris.platform.jalo.user.* import de.hybris.platform.jalo.flexiblesearch.* import de.hybris.platform.jalo.product.ProductManag Keep in mind that these imports are available only for Groovy and Beanshell languages. Javascript has a completely different concept of importing les so you need to use them in each script line.

## Limitations

The previous Beanshell scripting implementation provided possibilites to write scripts like that:
\#% import de.hybris.foo.bar.MyClass; INSERT_UPDATE Title;code[unique=true] \#% beforeEach: MyClass.callStaticMethod(); ;foo In the provided example, we rst import some class and in another line we refer to that class. In the new implementation this is not possible, because each line of the script is treated as a separate entity that does not know about others. So currently, we need to do it like this:
INSERT_UPDATE Title;code[unique=true]
"\#%groovy% beforeEach: import de.hybris.foo.bar.MyClass MyClass.callStaticMethod() "; ;foo

## Enabling Impex Scripting

To distinguish between the two modes of scripting in ImpEx, you can also use the property impex.legacy.scripting. This property is true by default, which means that the legacy behavior is the default. If you need new scripting capabilities, set the value of the property to false.

## User Rights

The ImpEx extension allows you to modify access rights for users and user groups. You can easily dene user rights in ImpEx using the syntax demonstrated in the following example.

$START_USERRIGHTS
Type;UID;MemberOfGroups;Password;Target;read;change;create;delete;change_pe UserGroup;impexgroup;employeegroup; ;;;;Product;+;+;+;+;- Customer;impex-demo;impexgroup;1234; $END_USERRIGHTS
The following describes each line of the syntax:
The $START_USERRIGHTS statement in line 1 indicates that every line until the $END_USERRIGHTS statement in line 6 isn't an ImpEx specic one, instead all lines between the two statements are redirected to the user rights management This is   For more    the SAP Help  47
(accessManager).

The second line is the header and denes the attributes that are to be set. This header is specic for the user rights management and doesn't support any features of ImpEx-like modiers.
The third line sets the usergroup with the name impexgroup that is a MemberOfGroups (subgroup) of employeegroup as an item where you modify given access rights. The item is the current one until the next item denition. If you forget to set a type (here UserGroup), the action will have no effect.

The fourth line sets the permissions for impexgroup: + allows, - denies the respective access right. A skipped value species no override, that is, use the inherited setting.

| Access right   | Comment / Description                                    |
|----------------|----------------------------------------------------------|
| read           | The user is allowed to read the value.                   |
| change         | The user is allowed to change the value.                 |
| create         | The user is allowed to create instances of this type.    |
| delete         | The user is allowed to delete instances of this type.    |
| change_perm    | The user is allowed to grant permissions to other users. |

If you need to dene additional user rights for impexgroup, just add the respective lines after line four. Being a header, the impexgroup user right creation is active until the next user or group creation, and all permission denitions apply to it.

The fth line creates a user of type Customer named impex-demo. This user is a member of impexgroup, and their account password is 1234. The sixth and last line ends the user right denitions section.
You must specify the columns Type, UID, MemberOfGroups, and Target in the header even if you don't want to specify their values. Not specifying one of these columns in the header results in an error message like This is not a CSV le with principal permissions! Aborting..., and the import fails.

To set access rights to an attribute of a type, add the attribute identier to the type identier, separated by a full stop (.), as follows:
$START_USERRIGHTS
Type;UID;MemberOfGroups;Password;Target;read;change;create;delete;change_pe UserGroup;impexgroup;employeegroup; ;;;;Product.code;-;-;;;; ;;;;Product.ean;-;-;;;; $END_USERRIGHTS
You have to use all of the columns Type, UID, MemberOfGroups, and Target even if you don't want to specify their values. The permission columns at the header line don't matter in any case, but you can write them down to remember the meaning of the permission values but they aren't parsed. So if you change the permission columns at the header line, this has no effect. In addition, you need to specify values for each of the potential access rights at the value line in exactly the order as in the example. The ImpEx framework implicitly expects an access rights line to contain values for all potential access rights in xed order - even for attribute access rights, where only Read and Change are available. Skipping one of these columns results in an error message like This is not a CSV le with principal permissions! Aborting..., and the import fails. For example, the following ImpEx statements work, because they specify values for all the potential access rights:
$START_USERRIGHTS 
Type;UID;MemberOfGroups;Password;Target;read;c UserGroup;impexgroup;employeegroup; ;;;;Product.code;-;-;;;; ;;;;Product.ean;-;-;;;; $END_USERRIGHTS
$START_USERRIGHTS
Type;UID;MemberOfGroups;Password;Target; UserGroup;impexgroup;employeegroup; ;;;;Product.code;-;-;;;; ;;;;Product.ean;-;-;;;; $END_USERRIGHTS
The following ImpEx statements don't work, however, because they don't specify values for all the potential access rights:
$START_USERRIGHTS
Type;UID;MemberOfGroups;Password;Target;read;c UserGroup;impexgroup;employeegroup; ;;;;Product.code;-;- ;;;;Product.ean;-;- $END_USERRIGHTS
$START_USERRIGHTS
Type;UID;MemberOfGroups;Password;Target; UserGroup;impexgroup;employeegroup; ;;;;Product.code;-;- ;;;;Product.ean;-;- $END_USERRIGHTS

## Translator

A translator class is a converter between ImpEx-related CSV les and values of attributes of SAP Commerce Cloud items A translator is one of the two ways SAP Commerce Cloud offers for using business logic when importing or exporting items. On import, a translator converts an entry of a value line into a value of an SAP Commerce Cloud item. It writes the value from the CSV le into SAP Commerce Cloud. On export, a translator converts a value of an attribute of a SAP Commerce Cloud item into a value line. It writes the value from SAP Commerce Cloud into a CSV le. SAP Commerce Cloud comes with settings for translator classes for all default types. For all out-of-the-box types, there is a preset translator class. For custom type denitions, you can code a translator to handle custom attributes. To call a custom translator in ImpEx, you make a reference to its full classpath in the translator modier in the header line of the ImpEx le, as follows:
INSERT_UPDATE myProduct;code;myAttribute[translator=my.company.org.translators.myCustomTranslator]
A translator is referenced for all value lines within a header. You cannot switch between translators within the scope of a header. SAP Commerce Cloud comes with two kinds of translator classes: standard value translators, and special value translators. Each of these is dealt with separately in the following sections.

## Standard Value Translators

Standard value translators are used for values that are mapped to standard type attributes, in contrast to special header attributes. If you do not specify a translator for a standard attribute, a xed translator is chosen by default depending on the specied attribute type. Be aware that with the exception of the default translators, Standard Value Translators are not all part of the ImpEx extension itself. They can also be part of other modules as well, such as the europe1 extension. As a consequence, a translator is not available if it is part of an extension that is not included in your installation. The table below gives an overview on Standard Value Translators and their respective extensions.

| The table below gives an overview on Standard Value Translators and their respective extensions. Class Applicable for Attribute Type New Modiers Introduced   | Part of Extension         |                           |         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------------|---------|
| CollectionValueTranslator                                                                                                                                     | Collection                | -                         | impex   |
| (used for Collections by default) Europe1ProductDiscountTranslator                                                                                            | Collection                | price-format, date-format | europe1 |
| Europe1UserDiscountsTranslator                                                                                                                                | Collection                | price-format, date-format | europe1 |
| Europe1PricesTranslator                                                                                                                                       | Collection                | price-format, date-format | europe1 |
| ActiveDirectoryGroupCollectionTranslator                                                                                                                      | Collection                | groupid                   | ldap    |
| TaxValuesTranslator                                                                                                                                           | Collection                | -                         | impex   |
| MapValueTranslator                                                                                                                                            | Map                       | -                         | impex   |
| (used for Maps by default) AtomicValueTranslator                                                                                                              | Atomic                    | -                         | impex   |
| (used for AtomicTypes by default) EClassAttributeTypeTranslator                                                                                               | ClassicationAttribute     | -                         | catalog |
| EClassUnitTranslator                                                                                                                                          | ClassicationAttributeUnit | systemName,               | catalog |
| systemVersion                                                                                                                                                 |                           |                           |         |
| ETIMAttributeTypeTranslator                                                                                                                                   | ETIMAttribute             | -                         | catalog |
| ItemExpressionTranslator                                                                                                                                      | ComposedType              | -                         | impex   |
| (used for ComposedTypes by default) AlternativeExpressionTranslator                                                                                           | ComposedType              | -                         | impex   |
| (used for Alternative Patterns by default) ItemPKTranslator                                                                                                   | PK                        | -                         | impex   |
| (used for PKs by default) ProClassAttributeTypeTranslator                                                                                                     | ProClassAttribute         | -                         | catalog |
| TaxValueTranslator                                                                                                                                            | TaxValue                  | -                         | impex   |

## Special Value Translators

Special Value Translators are used for values that have no exact attribute match, or for values that require complex business logic to resolve. Unlike Standard Value Translators, you have to explicitly enable Special Value Translators via the translator modier. The following is a list of all Special Value Translators in an out-of-the-box SAP Commerce Cloud installation.

## Mediadatatranslator

A media consists of several attributes, especially a URL where the described data can be found. Thereby the data is held locally at the **mediaweb** folder of the platform.

When inserting a media item, you can proceed like inserting a product by simply writing a header and dening the value lines. Problem is that there is no attribute that can be used for setting the real media data. This means you need a special column descriptor introduced by @ for dening a column without a mapped attribute. You have to specify the de.hybris.platform.impex.jalo.media.MediaDataTranslator as a translator. This translator holds an MediaDataHandler, which by default is the DefaultMediaDataHandler, when using a cronjob the DefaultCronjobMediaDataHandler.

The MediaDataTranslator translates the column values by calling the handler, which set the data to the already created/found media. The DefaultMediaDataHandler API offers support for importing medias from different sources (ZIP les, classpath, URL, lesystem). An example of using the DefaultMediaDataHandler is shown in the following ImpEx sample.

$catalogVersion=catalogVersion(catalog(id),version)[unique=true,default='mycatalog:Staged'] INSERT_UPDATE Media;code[unique=true];$catalogVersion; mime;realfilename;@media[translator=de.hybri \# ZIP Sample Syntax: zip-prefix:path-to-zip&path-within-zip ; demo1; ; image/jpeg; demo1.jpg; zip:c:\demo.zip&demo1.jpg \# 1. CLASSPATH Sample Syntax: jar-prefix:path-within-classpath ; demo2; ; image/jpeg; demo2.jpg; jar:/media/jeans/demo2.jpg \# 2. CLASSPATH Sample Syntax: jar-prefix:any-class-within-classpath-for-getting-classloader&path-w ; demo2; ; image/jpeg; demo2.jpg; jar:de.hybris.platform.sampledata.jalo.SampleDataManager&/media/j \# URL Sample Syntax: url-prefix:url ; demo3; ; image/jpeg; demo3.jpg; http:http://www.company.com/pictures/logo.gif \# FILE Sample Syntax: file-prefix:full-path ; demo4; ; image/jpeg; demo4.jpg; file:c:\demo4.jpg \# Exploded JAR Syntax: /medias/fromjar/file-name ; demo5; ; image/jpeg; demo5.jpg; /medias/fromjar/demo5.jpg The DefaultCronjobMediaDataHandler extends the DefaultMediaDataHandler by additionally allowing you to specify a path without prex and searches at the resource media attached at the cron job item. In that case, see Scripting. Furthermore, you can set any MediaDataHandler at run-time by using the static method setMediaDataHandler() of the MediaDataTranslator.

## Userpasswordtranslator

A special translator for importing/exporting user passwords. It stores passwords directly by specifying the desired encoding together with the encoded password separated by a colon (:). Refer to Password Storage Strategies to learn how to congure available password encodings. Use as follows:
INSERT Employee; uid[unique=true]; @password[translator=de.hybris.platform.impex.jalo.translators.U ; fritz ; md5:a7c15c415c37626de8fa648127ba1ae5 ; max ; *:plainPassword

## Velocitytranslator

The VelocityTranslator is used only for export. It can be used for exporting a value for an item using a velocity expression. With that, you can export a constant value or can aggregate different attributes. Using the following header at an export of an iorder item, the code of the order is exported as well as the id and name of the user owning the order and its payment address, street name, and country.

INSERT_UPDATE Order; code[unique=true]; \ @template1[translator=de.hybris.jakarta.ext.impex.jalo.translators.VelocityTranslator, expr='$it @template2[translator=de.hybris.jakarta.ext.impex.jalo.translators.VelocityTranslator, expr='$it "@template3[translator=de.hybris.jakarta.ext.impex.jalo.translators.VelocityTranslator, expr='$i @template4[translator=de.hybris.jakarta.ext.impex.jalo.translators.VelocityTranslator, expr='$it

## Classicationattributetranslator

Instead of importing each product feature one by one you can assign all features of a product with one value line using this translator. Therefore you have to declare a special attribute for each feature to import. Assuming you want to set a value for feature type at your product a suitable header could be as follows:
UPDATE Product; code[unique=true]; @type[system='SampleClassification',version='1.0',translator=de.

In this example, the modiers system and version, which are both mandatory, specify the classication system version of the product feature.

## Related Information

ImpEx Importing LDAP Data Using ImpEx JavaDocs