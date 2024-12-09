This is the starter code for the SE3150 Final Exam, Fall Semester 2024.

The instructions for the exam are here:

Details and instructions:

■	Do not start the exam prior to the start time indicated above. To receive credit, you must pass off and submit your final solution prior to the end time indicated above.

■	During the exam, you may reference any resources published prior to the start of the exam. Any material made available following the start of the exam is prohibited.

■	During the exam, do not discuss the exam or its contents with any individual other than the course instructor.

■	You may not use third-party software libraries as part of your submitted solution, with the exception of libraries explicitly specified by the exam.

■	Your score for the exam will be calculated out of 100 total points, and will represent 25% of your overall grade for the course.

■	Your solution will be evaluated according to the quality, variety, coverage, and intentional design of your test cases and scenarios. You will be graded according to your methodical and correct usage of test doubles, and according to the completeness and correctness of your test suites.

■	To receive credit, pass off your final solution with the instructor prior to leaving, and also submit your final solution using the designated private GitHub repository provided by the instructor.
 
For this exam, you will write two test suites, a unit test suite and a functional test suite, and implement a CI workflow for both. Begin by using the code provided at the start of the exam.

■	[40%]  Create a unit test suite using Python, pytest, pytest-describe, pytest-spec, and pytest-mock. The program under test is the Brute class (brute.py), a brute-force cracker.

Design and implement unit test cases in test_brute.py that thoroughly verify the functionality of the bruteOnce and bruteMany methods.

For the bruteOnce method, do not use test doubles.

For the bruteMany method, implement test doubles for the hash and/or randomGuess methods as you deem appropriate. For simplicity, avoid patching the hashlib module directly. Use stubs to force the desired test outcomes, and use mocks to verify correct implementation details.

Be sure to verify both success and failure outcomes for the methods under test.

■	[40%]  Create a functional test suite using Python, behave, behave-webdriver, and ChromeDriver. The application under test is a Caesar Cipher Encoder/Decoder.

Design and implement the two scenarios outlined in spy_messages.feature. You may use built-in step definitions, custom step definitions, or a combination of both.

Hints: manually experiment with the application before testing to understand its intended function and behavior; choose any caesar shift greater than 0 to encode or decode; and pause for 200ms between clicking the button and verifying the encoded/decoded result to allow sufficient time for event processing.

■	[20%]  Configure a continuous integration workflow that automates test runners for the two test suites above using GitHub Actions.

Create a single workflow that includes one job for each of the two test runners.

When finished, demonstrate your exam progress to the instructor via the GitHub Actions web interface. Show the test runner output for each of the two jobs.

