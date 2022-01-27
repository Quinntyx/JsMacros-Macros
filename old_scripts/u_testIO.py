# test of main i/o

with open("testIO/test.txt", 'w') as f:
    f.write("Testing, Testing, 123")
    
try: 
    with open("testIO/test.txt", 'r') as f:
        Chat.log(f.read())
except Exception as e:
    Chat.log(f"Standard I/O Failed with error {e}")    
    
# secondary test
try: 
    import shelve

    shelf = shelve.open("testIO/test")

    shelf['test'] = 'test'
    shelf['True'] = True
    
    Chat.log(f"shelf['test']: {shelf['test']}")
    Chat.log(f"shelf['True']: {shelf['True']}")
    
except ImportError as e:
    Chat.log(f"Failed to import 'shelve' with error {e}")
