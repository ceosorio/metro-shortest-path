import unittest
from graph_pkg import tests as graph_tests
import main_tests

graph_pkg_suite = unittest.TestSuite(
    [
        unittest.TestLoader().loadTestsFromTestCase(graph_tests.TestMapBuild),
        unittest.TestLoader().loadTestsFromTestCase(graph_tests.TestColapseNode),
    ]
)

main_suite = unittest.TestSuite(
    [unittest.TestLoader().loadTestsFromTestCase(main_tests.TestGetPath)]
)


complete_suite = unittest.TestSuite([graph_pkg_suite, main_suite])


def run_suites():
    result = unittest.TestResult()
    runner = unittest.TextTestRunner()
    print(runner.run(complete_suite))


if __name__ == "__main__":
    run_suites()
