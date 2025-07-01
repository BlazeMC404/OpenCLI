from opencli import setup, addcmd, newcmd, shell, colors

# 1. Setup a new terminal named 'myterminal' with the default 'opencli' shell
setup("OpenCLI", "bash")

# 2. Add built-in commands (e.g., echo, ls)
addcmd("OpenCLI", "echo")
addcmd("OpenCLI", "ls")

# 3. Create a custom command
custom_code = '''
def run():
    print(Colors.GREEN+ "Hello from OpenCLI!" + Colors.RESET)
    
run()
'''
newcmd("OpenCLI", "hello", custom_code)

# 4. Launch the shell
shell("OpenCLI", shell_name="opencli")
