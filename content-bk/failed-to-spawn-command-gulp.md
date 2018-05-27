Title: Failed to spawn command gulp
Date: 2015-10-20 21:00
Author: Andrew Elkins
Category: Linux, Software
Slug: failed-to-spawn-command-gulp
Status: published

I ran in to the error with Atom, Failed to spawn command gulp. The
solution for me was to install the module globally.

``` {.lang-js .prettyprint .prettyprinted}
$ sudo npm install -g gulp
/usr/bin/gulp -> /usr/lib/node_modules/gulp/bin/gulp.js
gulp@3.9.0 /usr/lib/node_modules/gulp
├── interpret@0.6.6
├── pretty-hrtime@1.0.1
├── deprecated@0.0.1
├── archy@1.0.0
├── minimist@1.2.0
├── tildify@1.1.2 (os-homedir@1.0.1)
├── v8flags@2.0.10 (user-home@1.1.1)
├── semver@4.3.6
├── chalk@1.1.1 (escape-string-regexp@1.0.3, supports-color@2.0.0, ansi-styles@2.1.0, has-ansi@2.0.0, strip-ansi@3.0.0)
├── orchestrator@0.3.7 (sequencify@0.0.7, stream-consume@0.1.0, end-of-stream@0.1.5)
├── liftoff@2.2.0 (extend@2.0.1, rechoir@0.6.2, flagged-respawn@0.3.1, resolve@1.1.6, findup-sync@0.3.0)
├── vinyl-fs@0.3.14 (graceful-fs@3.0.8, strip-bom@1.0.0, vinyl@0.4.6, defaults@1.0.3, mkdirp@0.5.1, through2@0.6.5, glob-stream@3.1.18, glob-watcher@0.0.6)
└── gulp-util@3.0.7 (object-assign@3.0.0, array-differ@1.0.0, array-uniq@1.0.2, lodash._reinterpolate@3.0.0, lodash._reescape@3.0.0, lodash._reevaluate@3.0.0, beeper@1.1.0, fancy-log@1.1.0, replace-ext@0.0.1, has-gulplog@0.1.0, vinyl@0.5.3, gulplog@1.0.0, lodash.template@3.6.2, multipipe@0.1.2, through2@2.0.0, dateformat@1.0.11)
```

Easy and done.
