---
title: "Use of the Restricted Bash Shell (rbash)"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Use_of_the_Restricted_Bash_Shell_(rbash).htm"
canonical_id: "actian-data-platform-use-of-the-restricted-bash-shell-rbash"
---

## Use of the Restricted Bash Shell (rbash)

Once you connect via SSH, you are logged into the restricted bash shell (rbash) which limits what you can do and what commands you can run. This help screen shows when you log in:

```
** This is a restricted bash shell. **
```

```
This shell has access to a limited set of Actian X tools and utilities.
```

```
To get menu in CUI tools (cbf, accessdb, isql etc) type: Esc Shift OP
```

```
(this may be mapped to NumLock in some terminal emulators e.g. putty)
```

```

```

```
Available commands:
```

```
accessdb  cbf    createdb   dircolors  grep    head        htop  iigetres   iimonitor  iiresutl  iivalres  ingcntrl  ingsetenv  isql      logger   ls       optimizedb  restart        sleep  sysmod  top
```

```
cat       ckpdb  destroydb  errhelp    groups  help_rbash  id    iiinitres  iinamu     iisetres  infodb    ingprenv  ipm        lockstat  logstat  netutil  ps          rollforwarddb  sql    tail    touch
```

```
To restart the instance after a config change use 'restart'
```

```
To see this help again, type 'help_rbash'
```

```
rbash:
```

These commands are available for use. They are a mix of Ingres and OS commands. Many of the commands have been added because they are needed for other tools not because they are necessarily intended to be used by themselves.
