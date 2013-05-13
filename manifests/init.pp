node default {
    class { "aptupdate": stage => "aptupdate" }
    class { "python": stage => "py" }
    class { "application": }
}

stage { "aptupdate": before => Stage["py"] }
class aptupdate {
    exec { 'apt-get update':
        command => '/usr/bin/apt-get update'
    }
}

stage { "py": before => Stage["main"] }
class python {
    package {
        "python-dev": ensure => "installed";
        "python": ensure => "installed";
        "python-setuptools": ensure => installed;
        "python-virtualenv": ensure => installed;
        "virtualenvwrapper": ensure => installed;
    }
}

class application {
    package {
        'git-core': ensure => installed;
        'mercurial': ensure => installed;
        'libmysqlclient-dev': ensure => installed;
    }
    class { 'mysql::server':
        config_hash => { 'root_password' => '' }
    }
}
