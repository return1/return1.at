Integration of Doctrine2 and Zend Framework
###########################################
:date: 2010-09-30 11:54
:category: PHP
:tags: autoloader, doctrine, zend framework
:slug: integration-doctrine2-zend-framework

*Update*: Meanwhile, Doctrine2 is stable, integration into Zend
Framework has slightly changed. I have incorporated the changes into the
article.

Integrating Doctrine2 into Zend Framwork (1.11) has
cost me some time. Enough to write about it, and maybe make it easier
for others. 

The procedure is actually easy:

#. download Zend Framework and Doctrine2
#. create project e.g. via Zend\_Tool :

   ::

       zf create project quickstart

#. link Zend Framework and Doctrine libraries with the newly created
   project, either via symlink in the library folder, or just copy and
   paste
#. configure web server

In case of problems with the above steps, Zend Framework's `quickstart
guide`_ is recommendable. `Doctrin's install guide`_ helps with
installing Doctrine2. My problem was with integrating the Doctrine2
autoloader into the Zend Framework autoloader.I was able to make it work
with support from the web. First the relevant excerpt from
bootstrap.php, in this context it is important that the application
namespace is configured before the doctrine namespace, sources are
inserted in the comments:

.. sourcecode:: php

    /**
    * Register namespace Application_
    * @return Zend_Application_Module_Autoloader
    */
    protected function _initAutoload()
    {
        $autoloader = new Zend_Application_Module_Autoloader(array(
        'namespace' => 'Application',
        'basePath'  => dirname(__FILE__),
        ));

        return $autoloader;
    }

    /**
    * Initialize auto loader of Doctrine
    *
    * @return Doctrine_Manager
    */
    protected function _initDoctrine() {
        // Fetch the global Zend Autoloader
        $autoloader = Zend_Loader_Autoloader::getInstance();

        $lib = '/path/to/Doctrine'; //path to git repository of Doctrine2 on filesystem
        require_once($lib.'/vendor/doctrine-common/lib/Doctrine/Common/ClassLoader.php');

        //doctrine autoloader
        $classLoader = new \Doctrine\Common\ClassLoader('Doctrine\Common', $lib.'/vendor/doctrine-common/lib');
        $classLoader->register();
        $classLoader = new \Doctrine\Common\ClassLoader('Doctrine\DBAL', $lib.'/vendor/doctrine-dbal/lib');
        $classLoader->register();
        $classLoader = new \Doctrine\Common\ClassLoader('Doctrine\ORM', $lib);
        $classLoader->register();

        //Push the doctrine autoloader to load for the Doctrine\ namespace
        $autoloader->pushAutoloader($classLoader, 'Doctrine\\');

        //init arraycache
        $cache = new \Doctrine\Common\Cache\ArrayCache;

        //setup configuration as seen from the sandbox application from the doctrine2 docs
        //http://www.doctrine-project.org/documentation/manual/2_0/en/configuration
        $config = new \Doctrine\ORM\Configuration();
        $config->setMetadataCacheImpl($cache);
        $driverImpl = $config->newDefaultAnnotationDriver(APPLICATION_PATH . '/../doctrine/entities');
        $config->setMetadataDriverImpl($driverImpl);
        $config->setQueryCacheImpl($cache);
        $config->setProxyDir(APPLICATION_PATH . '/../doctrine/proxies');
        $config->setProxyNamespace('Application\Proxies');
        $config->setAutoGenerateProxyClasses(true);

        //therefore you need some entries in your config:
        //doctrine.conn.host = 'localhost'
        //doctrine.conn.user = 'someuser'
        //doctrine.conn.pass = 'somepwd'
        //doctrine.conn.driv = 'pdo_pgsql' //i use postgres
        //doctrine.conn.dbname = 'somedbname'
        $doctrineConfig = $this->getOption('doctrine');
        $connectionOptions = array(
        'driver'    => $doctrineConfig['conn']['driv'],
        'user'      => $doctrineConfig['conn']['user'],
        'password'  => $doctrineConfig['conn']['pass'],
        'dbname'    => $doctrineConfig['conn']['dbname'],
        'host'      => $doctrineConfig['conn']['host']
        );

        $em = \Doctrine\ORM\EntityManager::create($connectionOptions, $config);

        Zend_Registry::set('entitymanager', $em);

        return $em;
    }

then you simply build a model:

.. sourcecode:: php

    /**
     * @Entity
     * @Table(name="test")
     */
    class Application_Model_Test {
        /**
         * @Id @Column(type="integer")
         * @GeneratedValue(strategy="AUTO")
         */
        private $id;

        /** @Column(type="string") */
        public $name;
    }

and use it in an action, voila! (first create the table in the database
;) )

.. sourcecode:: php

    class IndexController extends Zend_Controller_Action {

        public function init() {
            $this->_em = Zend_Registry::get('entitymanager');
        }

        public function indexAction() {
            $test = new Application_Model_Test();
            $test->name = 'Test';
            $this->_em->persist($test);
            $this->_em->flush();
        }
    }

.. _quickstart guide: http://framework.zend.com/manual/en/learning.quickstart.create-project.html
.. _Doctrin's install guide: http://www.doctrine-project.org/docs/orm/2.0/en/reference/introduction.html#github
