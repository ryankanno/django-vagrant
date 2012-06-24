node default {
    class {'nginx': }
    class {'mysql::python': }
    class { 'mysql::server':
        config_hash => { 'root_password' => '' }
    }
}
