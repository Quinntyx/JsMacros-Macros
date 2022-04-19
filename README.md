# JsMacros-Macros
A collection of Macros for Minecraft. 
***These macros rely on WagYourTail's JsMacros mod!*** 
(JsMacros-Jython also, to use Jython for macro scripting)

See here. 

- https://www.curseforge.com/minecraft/mc-mods/jsmacros
- https://www.curseforge.com/minecraft/mc-mods/jsmacros-jython
- https://www.github.com/wagyourtail/JsMacros

***This is a collection of Minecraft Macros designed to make your life easier.***

*Disclaimer: Many servers may consider these macros as conferring an "unfair advantage," or they may be seen as "cheating," "exploiting," or "hacking." Use at your
own risk; be warned, many public servers ban for things like this.*


To-Do
---
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

License
---
This is licensed under MPL 2.0, just like JsMacros is. 
