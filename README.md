# JsMacros-Macros
[![License](https://img.shields.io/badge/License-GPLv3-blue.svg?style=flat-square)](https://github.com/FlareStormGaming/JsMacros-Macros/LICENSE)
A collection of Macros for Minecraft. 

***These macros are for WagYourTail's JsMacros mod!*** 
(JsMacros-Jython also, to use Jython for macro scripting)

See dependencies below. 

#

*Disclaimer: This is a collection of Minecraft Macros designed to make your life easier. However, many servers may consider these macros as conferring an "unfair advantage," or they may be seen as "cheating," "exploiting," or "hacking." Use at your own risk. You may be kicked/banned from these servers.*


## To-Do
- Write a basic command parser library which navigates a folder command tree to enable management of subcommands. 
  - Use a service for this, as JsMacros onSendMessage events can cause stutter for computationally expensive events. 
- Scrap everything in here because it's pointless and terrible and the exisitng synthetic command parser is not good
- Rewrite many of the macros to rely on Jython instead of JEP
  - Avoid libraries that can't be run on Jython
- Come up with a JsMacros library that provides solutions, extension of WIP ios (improved OS) library for linux which adds support for things like `ls` parsing
  - Command to install a library to within a local `lib` package, so that it can be imported as `lib.libraryname` or `lib.packagename.modulename`
  - Method of executing scripts that extends/circumvents `JsMacros.runScript` to allow specification of a custom, preprepared environment to execute the other script in (also bypasses the globalvars issues caused)
  - Add a manager to register global methods for accessing services from scripts, and make it importable to python scripts in order to allow accessing these methods
  - Add a method to use `@JsMacros.on` above functions as a prettified frontend to `JsMacros.on()`

## Dependencies
### [JsMacros](https://www.github.com/wagyourtail/jsmacros)
  [![Download](https://img.shields.io/badge/Download-release-%2393c54b?style=flat-square)](https://www.curseforge.com/minecraft/mc-mods/jsmacros)
  
  JsMacros is a minecraft macro mod that provides an API for scripting behavior in Minecraft. 
# 
### [JsMacros-Jython](https://www.github.com/wagyourtail/jsmacros-jython)
  [![Download](https://img.shields.io/badge/Download-release-%2393c54b?style=flat-square)](https://www.curseforge.com/minecraft/mc-mods/jsmacros-jython)
#
  An extension mod which provides Jython as an extension language for JsMacros. Extensively used for macros by yours truly, as Jython plays very well with Java (importing, etc.) and has comparable performance to JavaScript. 
## License
This is licensed under GPL 3.0. 
