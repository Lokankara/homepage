# Installer Platform Plugin

The Platform Plugin is a standard Gradle plugin. It provides an API for managing Platform instances, as well as Tomcat instances in Gradle build les, in an easy, and readable way.

## Enabling The Platform Plugin

You enable the Platform plugin in a Gradle build le. Once you have enabled the plugin, you can set up and congure any existing Platform instance. To enable the Platform plugin, use the following method:
apply plugin: 'platform-plugin'

## Environment Variables

DRIVER_JAR_PATH is a path to the jdbc driver jar that must be copied into the Platform home lib/dbdrivers directory in some special cases when working with the installer.

## Gradle Project Properties

The Platform plugin may use a project property passed to the build script to determine the Platform home:
-Pplatform_home=/path/to/bin/platform This variable is useful in the development mode when testing plugin separately or if an installer project that is using the Platform plugin is outside of SAP Commerce Cloud. Please note that the installer install scripts use this property via the -P
option - the -Pplatform_home switch may be used only when using gradle directly.

## Setting Up The Platform Using The Platform Object

The following paragraph includes information about Platform Plugin variables and its methods.

## Platform Plugin Variables

The Platform plugin enriches the standard Gradle project object with the following variables:
This is   For more    the SAP Help  32

| 7/12/2024 Variable                                                                                                           | Description                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| platformHome                                                                                                                 | The absolute path to the Platform directory Type: String Examples: /Users/foo/commerce-suite5.4/hybris/bin/platform C:\foo\commerce-suite5.4\hybris\bin\platform                                                                                                                                      |
| installerHome                                                                                                                | The absolute path to the root directory of the installer project Type: String                                                        |
| installerWorkDir                                                                                                             | The work directory of the installer. Type: String                                                                                    |
| platformConfig                                                                                                               | The absolute path to the SAP Commerce Cloud cong directory Type: String Examples: /Users/foo/commerce-suite5.4/hybris/config C:\foo\commerce-suite5.4\hybris\config                                                                                                                                      |
| suiteHome                                                                                                                    | The absolute path to the SAP Commerce Cloud directory Type: String Examples: /Users/foo/commerce-suite-5.4 C:\foo\commerce-suite-5.4 |
| platformFactory                                                                                                              | The platformFactory object used to instantiate the HybrisPlatform object Type: HybrisPlatformFactory                                 |
| tomcat                                                                                                                       | The Tomcat builder object Type: HybrisTomcat                                                                                         |
| hsqldb                                                                                                                       | The HSQLDB management object that makes it possible to run the HSQLDB as a separate process. Type: HybrisHsqldb                      |
| The Platform plugin provides methods that are accessible directly from the build le so that they can be easily used with the |                                                                                                                                      |

HybrisPlatform object.

## Hybrisplatformfactory, Hybrisplatform Objects

The standard Gradle project object includes a special object, the HybrisPlatformFactory object. It sets up and creates the HybrisPlatform object.

This is   For more    the SAP Help  33 by using platformFactory:
or via the project method:
def pl = platform { // ... }

## Hybrisplatform Object

The HybrisPlatform object provides methods to congure the Platform, such as the conguration of databases, extensions, local properties, and clusters. It also provides convenient methods to write congurations to the appropriate les, compile and initialize the Platform, and run the Platform on Tomcat. To create a simple Platform object, use the following code:

## Createplatform Method

def myPlatform = platformFactory.createPlatform()
The code creates a simple Platform object called myPlatform. The object is congured with the required default settings, runs on an HSQLDB database, and has Platform extensions set only.

The following table presents the methods provided with the HybrisPlatform object:

dbSetup

def pl = platformFactory.createPlatform { // ... }

| Method             | Description               |
|--------------------|---------------------------|
| myPlatform.build() | Initializes the Platform. |

myPlatform.setup() Writes the setup to a cong folder. myPlatform.runInBackground() Runs the Platform on a Tomcat instance in background mode.

The Platform plugin also provides the platform shortcut method, accessible directly from the build le. It creates an instance of the HybrisPlatform object, and allows you to congure it. The method takes <Closure> as a parameter, as shown in the following example:
def myPlatform = platform { dbSetup { dbType 'mysql' dbUrl 'jdbc:mysql://localhost/hybris?useConfigs=maxPerformance&characterEncoding=utf8' dbUser 'dbuser' dbPassword 'passwd' } extensions { scanPath '/Users/foo/backoffice-extensions' extensionNames 'backoffice' } localProperties { property 'media.legacy.prettyURL', 'true' } }
The code example does the following:
Creates an instance of the HybrisPlatform object that is congured to use a MySQL database.

Congures the Platform to use the backoffice extension (using an additional scan path to search for the extensions in the /Users/foo/backoffice-extensions folder).

Adds the <media.legacy.prettyURL> property to the local.properties le.
You can also congure the HybrisPlatform object to be a node in a cluster. The following code excerpt shows how to do it:
def myPlatform = platform { dbSetup { dbType 'mysql' dbUrl 'jdbc:mysql://localhost/hybris?useConfigs=maxPerformance&characterEncoding=utf8' dbUser 'dbuser' dbPassword 'passwd' } extensions { scanPath '/Users/foo/backoffice-extensions' extensionNames 'hmc', 'backoffice' } clusterSettings { enableAutodiscovery() udpMulticast() } }
For more detailed information about cluster settings, see Advanced Cluster Settings API

## Hybrisplatform Api

In this paragraph you can nd detailed information about the HybrisPlatform API.

dbSetup(Closure) sets up the database connection. Note that the database must already exist. It takes <Closure>
as a parameter in which you can set the required information using the following methods:

dbType(String): The type of the database. The supported values are <mysql>, <oracle>, <sqlserver>, <sap>,
and <hsqldb>.

dbUrl(String): The URL to connect to the database.

dbUser(String): Database user name.

dbPassword(String): User database password.

dbTablePrefix(String): Prex for the database table.

dbDriverJar(String): An optional path to the custom JDBC driver jar.

## Dbsetup

dbSetup { dbType 'mysql' This is   For more    the SAP Help  35 dbUrl 'jdbc:mysql://localhost/hybris?useConfigs=maxPerformance&characterEncoding=utf8' dbUser 'myDbUser' dbPassword 'somePassword' dbTablePrefix 'foobar' dbDriverJar '/tmp/mysql-connector-java-5.1.31.jar' }
localProperties(Closure) is used to specify custom properties. It takes <Closure> as a parameter in which you can set the required information using the following methods:

property(String, String): Property key, property value.

properties(Map<String, String>): Map of properties.

customConfig(String): Name of the le used to store custom settings. All settings are merged.

## Caution

The settings specied in this le overwrite the settings specied in a recipe.

## Localproperties

localProperties { property 'foo.key', 'foo.value' properties( 'bar.key': 'bar.value', 'baz.key': 'baz.value' ) customConfig 'mySettings.properties' }
extensions(Closure) is used to add a custom set of extensions to the congured Platform. It takes <Closure> as a parameter to set the required information using the following methods:
extensionNames(String...): Extension names expressed as <varargs>.

extName(String): Extension name.

extensionDirs(String...): Extension directories expressed as <varargs>.

extDir(String): Extension directory.

scanPath(String): Directory in which the Platform looks for the extensions provided by the extensionNames method or the extName method. Note that the <autoload> option must be set to <false>,
that is, it must be disabled.

scanPath(String, Integer): Directory in which the Platform looks for extensions provided by the extensionNames method or the extName method. Note that the <autoload> option must be set to <true>,
that is, it must be enabled and the depth option set to a specied scan depth.

scanPathWithAutoLoad(String): Directory in which the Platform looks for the extensions provided by the extensionNames method or the extName method. Note that the <autoload> option must be set to <true>,
that is, it must be enabled.

scanPathWithAutoLoad(String, Integer): Directory in which the Platform looks for the extensions provided by the extensionNames method or the extName method. Note that the <autoload> option must be set to <true>, that is, it must be enabled).

disableDefaultScanPath(): It disables the default scan path (<$HYBRIS_BIN_DIR>). defaultScanPathWithAutoLoad(): It forces the default scan path (<$HYBRIS_BIN_DIR>) to have the
<autload> option set to <true>.

defaultScanPathWithAutoLoad(Integer): It forces the default scan path (<$HYBRIS_BIN_DIR>) to have the <autload> option set to <true> with a specied scan depth.

webApp(Closure): Deployment of external webapps. It takes <Closure> as a parameter to set the required information using the following methods:
context(String): Path to context.xml le.

contextRoot(String): Root context of the webapp.

customConfig(String): Name of the le used to store custom settings. All settings are merged.

## Caution

The settings specied in this le overwrite the settings specied in a recipe.

extensions extensions { scanPath '/Users/foo/additional-extensions1' scanPathWithAutoLoad '/Users/foo/load-all-extensions' extensionNames 'foo', 'bar', 'baz' extName 'one' extName 'two' extensionDirs '/Users/foo/ext1', '/Users/foo/ext2' extDir '/Users/foo/ext3' extDir '/Users/foo/ext4' webApp { context '/foo/bar/context.xml' contextRoot 'foo' path '/one/two/three.war' } customConfig 'myExtensions.xml' }

mediaStorageSettings(Closure) is used to specify the media storage conguration. By default, the Platform is congured to use local media storage out-of-the-box, therefore no special conguration is required. This method takes
<Closure> as a parameter to set the required information using the following methods:
defaultHashingDepth(Integer): Species the number of subdirectories permitted in a storage. Permitted values are 0 to 4.

disableLocalFileCache(): disables local media le cache localStorageStrategy(Closure): Sets up the local media storage. This method takes <Closure> as a parameter to set the required information using the following methods:
defaultStorageStrategy(): Species the storage strategy to be used as the default storage strategy for the entire SAP Commerce Cloud.

defaultUrlStrategy(): Sets localMediaWebURLStrategy as the default URL storage strategy.

folders(String...): Species the storage strategy to be used as the strategy for the folders. This method takes the variable argument list of folder qualiers.

foldersWithUrlStrategy(String...): Sets the storage strategy as a strategy, as well as the localMediaWebURLStrategy as the URL strategy for folders. This method takes the variable argument list of folder qualiers.

dir(String): Sets the custom directory to be used as the default storage directory.

## Mediastoragesetting

// Remaping media dir to /tmp/myMedias - useful for cluster setup mediaStorageSettings { localStorageStrategy { dir '/tmp/myMedias' } } // Setting Local Storage strategy for two folders. This make sense in case when ot mediaStorageSettings { localStorageStrategy { folders 'folderOne', 'folderTwo' } }
s3StorageStrategy: Sets up the s3 media storage. This method takes <Closure> as a parameter to set the required information using the following methods:

defaultStorageStrategy(): Sets the specied storage strategy as the default storage strategy for the entire SAP Commerce Cloud.
defaultUrlStrategy(): Sets the s3MediaURLStrategy media strategy as the default URL storage strategy. If you don't set this option, the localMediaWebURLStrategy are used by default.

folders(String...): Sets this storage strategy as the strategy for the folders. This method takes the variable argument list of folder qualiers.

foldersWithUrlStrategy(String...): Sets the storage strategy as a strategy, as well as the s3MediaURLStrategy as the URL strategy for the folders. This method takes the variable argument list of the folder qualiers.

accessKey(String): Sets the access key for the S3 account.

secretAccessKey(String): Sets the secret access key for the S3 account.

endPoint(String): Sets the end point URL for the S3 storage.

urlSigned(boolean): Species if the S3 URL strategy will produce signed URLs. This option is only applied when the defaultUrlStrategy() is used.

timeToLiveInMinutes(int): Species the length of time, in minutes, for which the signed URL is valid. This option is only applied when defaultUrlStrategy() and urlSigned(true) are used.

urlUnsignedHttps(boolean): Species if the unsigned URL uses HTTPS. This option is only applied when defaultUrlStrategy() and urlSigned(false) are used.

urlUnsignedVirtualHost(boolean): Species if the unsigned URL uses virtual hosting. This option is only applied when defaultUrlStrategy() and urlSigned(false) are used.

## S3Storagestrategy

// Setting S3 Storage Strategy as default (standard local URL strategy) mediaStorageSettings { s3StorageStrategy { defaultStorageStrategy() accessKey 'SOME-KEY' secretAccessKey 'SOME-SECRET' endPoint 'http://somewhere.com/' } } // Setting S3 Storage Strategy for two folders mediaStorageSettings {
 s3StorageStrategy {
 accessKey 'SOME-KEY' secretAccessKey 'SOME-SECRET' endPoint 'http://somewhere.com/' folders 'folderOne', 'folderTwo' } } // Setting S3 Storage Strategy as default (S3 Url strategy with default settings) mediaStorageSettings { s3StorageStrategy { defaultStorageStrategy() defaultUrlStrategy() accessKey 'SOME-KEY' secretAccessKey 'SOME-SECRET' endPoint 'http://somewhere.com/' } }
azureStorageStrategy(Closure): Sets up the Windows Azure Blob storage strategy. This method takes
<Closure> as a parameter to set the required information using the following methods:
defaultStorageStrategy(): Sets the specied storage strategy as the default storage strategy for the entire system.

defaultUrlStrategy(): Sets the windowsAzureBlobURLStrategy as the default URL storage strategy. If you don't set this option, the localMediaWebURLStrategy is used as the default strategy.
This is   For more    the SAP Help  38

folders(String...): Sets this storage strategy as the strategy for the folders. This method takes the variable argument list of folder qualiers.

foldersWithUrlStrategy(String...): Sets the storage strategy as a strategy, as well as windowsAzureBlobURLStrategy as the URL strategy for the folders. This method takes the variable argument list of the folder qualiers.

connection(String): Sets up the connection string for the Azure account.

publicBaseUrl(String): Sets up the public base URL for the Azure account.
containerAddress(String): Species the container address in which all media will be stored.

## Azurestoragestrategy

// Setting Windows Azure Blob storage strategy as default (standard local URL strategy) mediaStorageSettings { azureStorageStrategy { defaultStorageStrategy() connection 'CONNECTION-STRING' containerAddress 'MY-CONTAINER' publicBaseUrl 'some-account.blob.core.windows.net' } } // Setting Windows Azure Blob storage for two folders mediaStorageSettings { azureStorageStrategy { connection 'CONNECTION-STRING' containerAddress 'MY-CONTAINER' publicBaseUrl 'some-account.blob.core.windows.net' folders 'folderOne', 'folderTwo' } } // Setting Windows Azure Blob storage strategy as default (Windows Azure Url strategy wi mediaStorageSettings { azureStorageStrategy { defaultStorageStrategy() defaultUrlStrategy() connection 'CONNECTION-STRING' containerAddress 'MY-CONTAINER' publicBaseUrl 'some-account.blob.core.windows.net' } }
gridFsStorageStrategy(Closure): Species the Mongo GridFS storage strategy. This method takes
<Closure> as a parameter to set the required information using the following methods:
defaultStorageStrategy(): Sets this storage strategy as default one for entire system.

defaultUrlStrategy(): Sets localMediaWebURLStrategy as the default URL storage strategy.

The GridFS storage doesn't provide a special URL strategy, therefore this method isn't mandatory.

folders(String...): Sets this storage strategy as a strategy for folders. This method takes the variable argument list of the folder qualiers.

foldersWithUrlStrategy(String...): Sets the storage startegy as a strategy, as well as localMediaWebURLStrategy as the URL strategy for the folders. This method takes the variable argument list of the folder qualiers.
host(String): Sets the host for the MongoDB database. The default value is <localhost>.

port(String): Species the port for the MongoDB database. The default value is <27017>.

dbName(String): Species the name of the database. The default value is hybris_storage.

userName(String): Species the user name for the MongoDB database. The default value is <empty>.

password(String): Species the password for the MongoDB database. The default value is <empty>.

## Gridfsstoragestrategy

// Setting Mongo GridFS storage strategy as default mediaStorageSettings { gridFsStorageStrategy { defaultStorageStrategy() host '10.0.0.10' port '9090' userName 'some-user' password 'password' } } // Setting Mongo GridFS storage strategy for two folders mediaStorageSettings { gridFsStorageStrategy { host '10.0.0.10' port '9090' userName 'some-user' password 'password' folders 'folderOne', 'folderTwo' } }
clusterSetup(Closure): Used to specify the cluster node settings. This method takes <Closure> as a parameter to set the required information using the following methods:
id(String): ID of a node.

maxId(String): Max ID for the entire cluster.

enableAutodiscovery():
jGroups(Closure): Setting for the jGroups communication. This method takes a Closure as a parameter to set all necessary information by using the following methods:
channelName(String): allows you to set up a JGroups channel name. Default is hybris-broadcast.

configFile(String): the name of the conguration le.
udpPing(Closure): allows you to set up JGroups UDP/PING communication. This method takes a Closure as a parameter to set all necessary information by using the following methods:
mcastPort(int): allows you to set Multicast port for UDP/PING communication. Default is 45588.

udpPing(): allows you to set JGroups UDP/PING communication with default settings.

tcpMping(Closure): allows you to set up JGroups TCP/MPING communication. This method takes a Closure as a parameter to set all necessary information by using the following methods:

tcpAddress(String): allows you to set up a tcp bind address for TCP communication.

tcpPort(int): allows you to set up a tcp bind port for TCP communication.

multicastAddress(String): allows you to set up a multicast address for MPING
communication.
multicastPort(int): allows you to set up multicast port for MPING communication.

tcpMping(): allows you to set up JGroups TCP/MPING communication with default settings.
tcpJdbcPing(Closure): allows to set up JGroups TCP/JDBC_PING communication. This method takes a Closure as a parameter to set all necessary information by using the following methods:

tcpAddress(String): allows you to set up a tcp bind addres for TCP communication.

tcpPort(int): allows you to set up a tcp bind port for TCP communication.

clearTableOnViewChange(): enabling this can help with removing crashed members that are still in the table. Default value is false tcpJdbcPing(): allows you to set up JGroups TCP/JDBC_PING communication with default settings.

tcpKubePing(Closure): allows you to set up JGroups TCP/KUBE_PING communication. This method takes a Closure as a parameter to set all necessary information by using the following methods:
This is   For more    the SAP Help  40

tcpPort(int): allows you to set up a tcp bind port for TCP communication.

jGroups(): Default settings for the jGroups.

udpMulticast(Closure): Settings for the UDP multicast communication.

udpMulticast(): Default settings for the UDP multicast.

udpUnicast(Closure): Settings for the UDP unicast communication.

clusterSettings(Closure): the same usage as clusterSetup(Closure). This method is deprecated.

setup(): Stores the properties and extensions settings in proper les, as well as optionally copies custom JDBC driver jar to the Platform lib/dbdriver/ directory.

build(): Executes the ant clean all command on the underlying Platform.

initialize(): Executes the ant initialize command on the underlying Platform.

initialize(File): Executes ant initialize on underlying Platform and stores logs in a given le.

initializeTestSystem(): Executes the ant yunitinit command on the underlying Platform.

update(): Executes ant updatesystem on underlying Platform.

update(File): Executes ant updatesystem on underlying Platform and stores log in a given le executeAntTarget(String): Enables the execution of any ant target supported by underlying build.xml le in the Platform.

executeAntTarget(String, String): Enables the execution of any ant target supported by underlying build.xml le in the Platform with additional ant options.

## Ant Targets

executeAntTarget 'clean all initialize' executeAntTarget 'alltests -Dtestclasses.extensions=core' executeAntTarget 'initialize', '-Xmx2048m -XX:MaxPermSize=756M'

executeAntTarget(File, String): Allows you to execute any ant target and stores output in a given le.

executeAntTarget(File, String, String): Allows you to execute ant target with additional options and stores output in a given le.

start(): Starts the congured Platform on a Tomcat in interactive mode.

startInDebug(): Starts the congured Platform on a Tomcat in interactive and debug modes.

startInBackground(): Starts the congured Platform on a Tomcat in background mode.

stopInBackground(): Stops the Platform running on a Tomcat in background mode.

createProductionArtifacts(): Creates production artifacts that are stored in a temp directory of the Platform.

createProductionArtifact(String args): Creates production artifacts that are stored in a temp directory of Platform; it allows you to pass additional command line arguments importImpexFromContent(String content): Imports impex content kept in a string variable.
def importContent = ''' INSERT_UPDATE MediaFormat;qualifier[unique=true] ;foo; ;bar; ;baz; ''' importImpexFromContent(importContent)
importImpexFromResource(String resourcePath): Imports impex content kept in a resource.

def resource = '/tmp/myImport.impex' importImpexFromResource(resource)
This is   For more    the SAP Help  41 executeScriptFromContent(String content, String scriptType) : Executes the content of the script.

Valid script types are groovy, js, bsh.

def script = ''' flexibleSearchService.search("SELECT {PK} FROM {MediaFormat}").getResult().forEach { 
println it.qualifier 
} ''' executeScriptFromContent(content, 'groovy')
executeScriptFromResource(String resourcePath): Executes a script from the existing resource. Keep in mind that the resource le must have proper le extension (groovy, js or bsh).

def resource = '/tmp/myScript.groovy' executeScriptFromResource(resource'

## Before And After Setup/Build Hooks

You can schedule certain logic to be executed before and after the setup and build phases. There are four methods that allow you to do that:
beforeSetup(Closure)

afterSetup(Closure)
beforeBuild(Closure)
afterBuild(Closure)
The following example shows how to provide logic to be executed after setup is done:
pl.afterSetup { println 'Called after setup' } pl.setup()

## Testing Capabilities

The HybrisPlatform object includes an API for easy test execution.

Simply, inside your recipe, specify which tests and from which set of extensions you want to run:
def pl = platform { tests { extensions 'foo', 'bar' annotations 'UnitTest', 'IntegrationTest' packages 'foo.bar.baz.*' reportDir '/tmp/junit' } } pl.runTests()
The API includes the following methods:

tests(Closure): It allows you to congure test execution. This method takes <Closure> as a parameter to set the required information using the following methods:
extensions(String...): Narrows test execution only to the names of provided extension.

annotations(String...): Narrows test execution only to tests annotated with annotations. The options allowed are <UnitTest>, <IntegrationTest>, <PerformanceTest>, <DemoTest>
packages(String...): Narrows test execution only to provided packages.

excludedPackages(String...): Allows you to exclude packages from test execution.

reportDir(String): Allows you to set different report directory. The default directory is log/junit/ in the Platform main directory.

webTests(Closure): It allows you to congure execution of web tests. This method takes <Closure> as a parameter to set the required information using the following methods:
extensions(String...): Narrows test execution only to the names of provided extension.

annotations(String...): Narrows test execution only to tests annotated with annotations. The options allowed are <UnitTest>, <IntegrationTest>, <PerformanceTest>, <DemoTest>
packages(String...): Narrows test execution only to provided packages.

excludedPackages(String...): Allows you to exclude packages from test execution.

reportDir(String): Allows you to set a different report directory. The default directory is a log/junit/ in the Platform main directory.

## Advanced Cluster Settings Api

Setting up a cluster can be complicated, especially on a single-developer machine. The Platform Plugin API facilitates setting up a cluster.

To congure a cluster node, use the cluster(Closure) method; it is available in the HybrisPlatform and PlatformInstance objects.

Before conguring a cluster node, select the communication mechanism you want to use:
jGroups

UDP Multicast
UDP Unicast

## Jgroups Conguration

To congure a jGroups-enabled node, use the following code:
clusterSettings { id '0' maxId '2' jGroups() }
The code congures a cluster node with ID=0, max ID=2, and the following default jGroups communication settings:

TCP address: 127.0.0.1

TCP port : 7800
Channel name: hybris-broadcast Conguration le: jgroups-udp.xml You can congure the same cluster node, using a more verbose code:
clusterSettings { id '0' maxId '2' jGroups { defaultSettings() } }
You can also create the cluster node by specifying each setting individually:
clusterSettings { id '0' maxId '2' jGroups { tcpAddress '10.0.0.1' tcpPort 6677 channelName 'my-custom-channel' configFile '/Users/foo/my-custom-config.xml' } }

## Udp Multicast Conguration

To congure UDP multicast enabled-node, use the following code:
clusterSettings { id '0' maxId '2' udpMulticast() }
The code congures a cluster node with ID=0, max ID=2, and the following default UDP multicast communication settings:
address: 224.0.0.0 port: 9997 You can congure the cluster node, using a more verbose code:
clusterSettings { id '0' maxId '2' udpMulticast { standardSettings()
This is   For more    the SAP Help  44

 } }
You can also create the cluster node by specifying each setting individually:
clusterSettings { id '0' maxId '2' udpMulticast { address '224.0.0.1' port 9999 networkInterface 'en0' debug true } }

## Udp Unicast Conguration

To congure UDP unicast-enabled node, use the following code:
clusterSettings { id '0' maxId '2' udpUnicast { address '10.0.0.55' port 9999 clusterNodes '10.0.0.56:9999', '10.0.0.57:9999' syncNodesInterval 1 debug true } }

## Conguring Database Connections

To provide database connection parameters, use the dbSetup method. For more information, see the dbSetup Method section in HybrisPlatform API.

## Conguring The Media Storage Setup

To congure media storage settings, use the mediaStorageSettings method. For more information, see the mediaStorageSettings Method section in HybrisPlatform API.

You can also set up local le media storage for all cluster nodes using the sysTempMediaStorage() method. It stores all media in the medias subfolder of the system temp directory.

## Managing Tomcat

The Platform Plugin provides a simple API to manage Tomcat. The following code excerpt shows how to deploy the DataHub Tomcat instance:
This is   For more    the SAP Help  45 def CATALINA_OPTS = "-Xms4096m -Xmx4096m ........ " tomcat.instance('dataHub').setup { ports { http 9033 ssl 9034
 }
 webApps { webApp 'datahub-webapp.war', file(suiteHome + '/hybris/bin/ext-integration/datahub/web-app/ } libraries { lib file("/Volumes/Data/projects/hybris_git/y/bin/platform/lib/dbdriver/mysql-connector-jav propertyFile "local.properties", { property 'dataSource.driverClass', 'com.mysql.jdbc.Driver' property 'dataSource.jdbcUrl', "jdbc:mysql://localhost/integration?useConfigs=maxPerfor property 'dataSource.username', 'root' property 'dataSource.password', '' } } }.start(CATALINA_OPTS)
The code example does the following:
Creates a directory named dataHub in the INSTALLER_HOME/work/ directory.

Creates the required Tomcat conguration les, such as conguring the ports, in the dataHub/conf directory.

Copies the specied war le to dataHub/webapps/datahub-webapp.war le.

Copies the MySQL driver from the specied absolute path to the dataHub/libs directory.

Creates the local.properties le, which contains the default properties, in the dataHub/lib directory.

Starts the Tomcat with the provided <CATALINA_OPTS>. All log les are stored in the dataHub/logs directory.

## Description Of The Deploy Datahub Code

Below you can nd detailed information about the Deploy DataHub Code.

## Instance Name

Many Tomcat instances can be created and run using this API. To distinguish between the Tomcat instances, use the name of the instance as shown in the following example:
tomcat.instance('dataHub')
Each Tomcat instance must use a different port. If you have more than one Tomcat instance, make sure that the instances don't collide.

## Tomcat Ports

This is   For more    the SAP Help  46 The ports elements is used to specify which port a Tomcat instance is to use. The ports element has two parameters:
<http>
<ssl>

## Certicates

If you need to provide a custom ssl certicate to handle https traffic, you can use the certificates element.

certificates { keyStore Paths.get("/my/custom/keystore"), "123456" }
The certificates element also allows you to congure the trust store used by the jvm:
certificates { trustStore Paths.get("/my/custom/truststore"), "123456" }
You can change the trust store and the key store in a single certificates element:
certificates { keyStore Paths.get("/my/custom/keystore"), "123456" trustStore Paths.get("/my/custom/truststore"), "123456" }

## Web Applications

You can deploy multiple web applications on one Tomcat instance. Use thewebApps element to list the web applications. Dene each web application using the following syntax:

## Specifying Web Applications

webApp targetWarName, warFile where:

<targetWarName> is a string that species the target le name of the web application in the tomcat/webapps directory.

<warFile> points to the war le. Note that you can compose the path to the le using variables exposed by the Platform Plugin, such as <suiteHome>.

## Libraries

You use the libraries element to specify the content of the tomcat/lib folder. You can add les to the tomcat/lib folder using the following syntax:

## Tomcat/Lib Folder

lib file("/some/absolute/path/to/mysql-connector-java-5.1.26.jar")
You can also create property les in tomcat/lib using the following syntax:
This is   For more    the SAP Help  47 propertyFile "local.properties", { property 'key', 'value' }

## Starting And Stopping Tomcat

The Tomcat object has the following methods:
start(String tomcatOpts): Starts the Tomcat instance with the options provided.

stop: Stops the Tomcat instance.

## Managing The Hsqldb

The HybrisHsqldb object provides methods to congure the HSQLDB and run it as a standalone process. Unlike the SAP
Commerce Cloud default database, the embedded HSQLDB, which accepts only one connection, the HybrisHsqldb object accepts many connections. It can therefore be used in a cluster environment.

## Hsqldb Port

By default, the HSQLDB runs on port 9009. You can use the optional port method to change default values, as follows:
hsqldb.port 49302 ... hsqldb.startInBackground()

This is an optional step. If you want to change the port on which the HSQLDB runs, you must do it before starting or stopping the database.

## Conguring The Database

HSQLDB supports a maximum of nine (9) separate databases running on a single process. Use the <dbNames> property in the HybrisHsqldb object to congure the names of the databases as shown in the following example:

## Conguring Database Names

hsqldb.dbNames = ['foo', 'bar'] ... hsqldb.startInBackground()
The following code shows how to congure the HSQLDB to host two databases: foo and bar. The detailed conguration is displayed during startup.

Hsqldb successfully started:
foo jdbc:hsqldb:hsql://localhost:9009/foo bar jdbc:hsqldb:hsql://localhost:9009/bar

This is   For more    the SAP Help  48

## Conguring The Database Using The Hybrisplatform Object

You can congure the HSQLDB using the HybrisPlatform API. You can use the createDb method to automatically congure the database as a Platform object. The following code shows how to do it:

## Conguring Database Using The Hybrisplatform Object

def hsqldbPlatform = platform { dbSetup hsqldb.createDb("hybris") // or simply dbSetup hsqldb.createDb() }
In the provided example:
createDb(): Adds new database named <db_N> (where <N> is a number of the currently created database) and returns the conguration for <dbSetup> parameter. Note that this throws a runtime exception when the database limit of nine (9) is exceeded.

createDb(String databaseName): Adds a new database with the specied name and returns the conguration for the <dbSetup> parameter.

Note that this throws a runtime exception when the database limit of nine (9) is exceeded or when a database with the specied name already exists.

## Starting And Stopping The Hsqldb

The HSQLDB object has the following methods:
startInBackground: Starts an HSQLDB server instance on a congured port.

stopInBackground: Stops a currently running HSQLDB server instance.
kill: Kills a currently running HSQLDB process and clears the database work directory.

 Note Use the kill method cautiously because it kills processes abruptly and deletes all persisted and temporary data.

## Detailed Information About Starting And Stopping The Hsqldb

During startup, the HSQLDB looks for a conguration le in its work directory. If a pid.txt le is present, the HSQLDB tries to connect to the URLs specied in the le and has the possible results:

If successful, the HSQLDB assumes that the database was created previously; it stores some persistent data and becomes operational again. If not successful: if the HSQLDB cannot connect, it assumes that the database was stopped in an unsafe way and may be corrupted. The HybrisHsqldb object will try to kill the HSQLDBprocess that is currently running, clear the database work directory, and start the HSQLDB in a clean state.
This is   For more    the SAP Help  49

## Related Information

Installing SAP Commerce Cloud Manually Environment Variables