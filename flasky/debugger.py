from os import getenv

def initializeFlaskServiceDebuggerIfNeeded():
    if getenv('DEBUGGER') == 'True':
        import multiprocessing
        
        if multiprocessing.current_process().pid > 1:
            import debugpy

            debugpy.listen(('0.0.0.0', 10001))    # start debugger listening for client connection
            print("⏳ VS Code debugger can now be attached, press F5 in VS Code ⏳", flush=True)
            debugpy.wait_for_client()           # block until the client - vscode debugger - is attached
            print("🎉 VS Code debugger attached. 🎉", flush=True)
