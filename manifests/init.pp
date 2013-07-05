node default {
    class { "aptupdate": stage => "aptupdate" }
    class { "users": stage => "pre" }
    class { "python": stage => "py" }
    class { "application": }
}

stage { "aptupdate": before => Stage["pre"] }
class aptupdate {
    exec { 'apt-get update':
        command => '/usr/bin/apt-get update'
    }
}

stage { "pre": before => Stage["py"] }
class users {
    package { 
        'build-essential': ensure => latest;
        'libshadow': ensure => latest, provider => 'gem', require => Package["build-essential"];
    }
    
    group { "app":
        ensure => present,
        gid => 2000 
    }

    user { "django":
        ensure => present,
        gid => "app",
        groups => ["adm", "root"],
        managehome => true,
        password => '$6$QgrFgGzO$jrmISp8T9vIcKq.DumvXVJcAvcEth7lmLY1EcG.ljkbc3KpU3NEwH8TkQzs4rmUJvsBw5zcUNpWGU4.X84AwB/',
        shell => "/bin/bash",
        require => [Group["app"], Package["libshadow"]]
    }

    file { "/var/www":
        ensure => "directory",
        owner  => "vagrant",
        group  => "app",
        mode   => 755,
        require => Group["app"]
    }

    file { "/var/www/apps":
        ensure => "directory",
        owner  => "django",
        group  => "app",
        mode   => 755,
        require => [ Group["app"], User["django"] ] 
    }
}

stage { "py": before => Stage["main"] }
class python {
    package {
        "python-dev": ensure => "2.7.3-0ubuntu2";
        "python": ensure => "2.7.3-0ubuntu2";
        "python-setuptools": ensure => installed;
        "python-virtualenv": ensure => installed;
        "virtualenvwrapper": ensure => installed;
    }
}

class application {
    package {
        'git-core': ensure => installed;
        'mercurial': ensure => installed;
        'uwsgi': ensure => installed;
        'uwsgi-plugin-python': ensure => installed, require => Package["uwsgi"];
        'libmysqlclient-dev': ensure => installed;
    }
    class { 'nginx': }
    class { 'mysql::server':
        config_hash => { 'root_password' => '' }
    }

    sudoers::user { django:
      ensure => present,
      nopasswd => true,
      commands => "ALL",
      require => [User["django"]]
    }
}
