import os, subprocess, unittest

DIRECTORY = subprocess.check_output('git rev-parse --show-toplevel'.split()).strip()
print(DIRECTORY)

CPP = 'cpp'
CSHARP = 'csharp'
JAVA = 'java'
PYTHON = 'py'
LANGUAGES = [CPP, CSHARP, JAVA, PYTHON]

# Utility Functions ############################################################
def generate_files(language):
    # No need to cd back to original directory.
    # Each os.system() call starts clean.
    return 'cd %s/thrift && thrift -r --gen %s src/Service.thrift' % (DIRECTORY, language)

def remove_generated_files(language):
    return 'rm -r %s/thrift/gen-%s' % (DIRECTORY, language)

# Functions not used by the tests ##############################################
def generate_all():
    for language in LANGUAGES:
        os.system(generate_files(language))

def remove_all_generated():
    os.system('rm -r %s/thrift/gen-*' % DIRECTORY)
    #for language in LANGUAGES:
    #    os.system(remove_generated_files(language))

# Test that Thrift builds properly #############################################
class BuildTester(unittest.TestCase):
    def test_cpp(self):
        self.assertEqual(os.system(generate_files(CPP)), 0)
        self.assertEqual(os.system('c++ -std=c++11 %s/tests/languages/cpp_server.cpp' % DIRECTORY), 0)
        self.assertEqual(os.system(remove_generated_files(CPP)), 0)
        self.assertEqual(os.system('rm a.out'), 0)

    def test_csharp(self):
        self.assertEqual(os.system(generate_files(CSHARP)), 0)
        self.assertEqual(os.system('mcs /warnaserror /t:library /out:generated.dll /reference:thrift.dll %s/thrift/gen-csharp/example/*.cs' % DIRECTORY), 0)
        self.assertEqual(os.system('mcs /warnaserror /reference:generated.dll /reference:thrift.dll %s/tests/languages/CsharpServer/CsharpServer.cs' % DIRECTORY), 0)
        self.assertEqual(os.system(remove_generated_files(CSHARP)), 0)
        self.assertEqual(os.system('rm %s/tests/languages/CsharpServer/CsharpServer.exe' % DIRECTORY), 0)
        self.assertEqual(os.system('rm thrift.dll'), 0)
        self.assertEqual(os.system('rm generated.dll'), 0)

    def test_java(self):
        self.assertEqual(os.system(generate_files(JAVA)), 0)
        self.assertEqual(os.system('javac %s/languages/JavaServer.java' % DIRECTORY), 0)
        self.assertEqual(os.system(remove_generated_files(JAVA)), 0)
        self.assertEqual(os.system('rm %s/languages/JavaServer.class' % DIRECTORY), 0)

    def test_python(self):
        self.assertEqual(os.system(generate_files(PYTHON)), 0)
        self.assertEqual(os.system('python3 %s/languages/python_server.py' % DIRECTORY), 0)
        self.assertEqual(os.system(remove_generated_files(PYTHON)), 0)

if __name__ == '__main__':
    unittest.main()
