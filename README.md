# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions
    - a function where the input is data (usually a string) and the output is a number. Must be deterministic (consistent). Every time it receives the same input, it must return the same output.
    - different input data must return different numbers to avoid collisions
    - must return numbers that are within a specific range (limit)
    - the hash function: hashes each key's input data into a number, then we use mod % to get the range of the length of the table (how many slots). returns value % len(table), and that is going to be the index of that key (the position in the hash table).
2. Collision resolution
    - when collisions happen (same output integers occur for different inputs), we need to move the keys around so that the new keys can fit into the array, hash table.
    - we can use chaining: allows each slot to hold a reference to a collection of items. In every slot, there will be a Linked List. Add to the head of the list. Then the others make room and move down.
3. Performance of basic hash table operations
    - provide key/value storage with O(1) time, constant time
    - in Python, hash tables are known as dictionaries
    - insertion (put), deletion (delete), and search (get) are basic operations
4. Load factor
    - the # of items stored in hash table / total # of slots. In other words, the occupied slots divided by the length of the array.
    - we want to maintain a low load factor to avoid collisions.
5. Automatic resizing
    - when load factor gets too high (usually 0.7 or 70% full) then we want to resize the hash table. 
    - Usually double the size of hash table, making room for more data.
    - If load factor is too low (usually 0.2), you can downsize to save memory, but this isnt usually too big of a worry.
6. Various use cases for hash tables
    - hash tables allow us to access key-value pairs quickly. they store values under a specific key.
    - quickly lookup every person in a certain department in a big list of data. You could use the hash table to find the department and print the names of everyone in that department.


We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request
