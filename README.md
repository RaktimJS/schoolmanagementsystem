# __SCHOOL MANAGEMENT SYSTEM__

### School Management System is a CLI-based CRUD app that helps in super easy storage, retrieval, updation, and deletion of student data.

___

## About Me

Hi, my name is Raktim, and I'm a senior high school student from a Tier 3 town named Pathsala, in the state of Assam, India.

I'm very passionate about Computers and Mathematics, and I enjoy building systems that integrate Math with Computer Programming. Though this program isn’t exactly the kind of project I enjoy working on the most, building it solo was still a lot of fun!

Email: __raktimunreal4@gmail.com__ GitHub: [__https://github.com/raktimjs__](https://github.com/raktimjs)

___

This app is built completely using Python and utilizes almost every Python concept from the 11th and 12th grade CBSE Computer Science syllabus.

___

### __NOTE:__ I’ve never used macOS, so the instructions in this document (and maybe even parts of the code) might be specific to Windows. I’ve tried to keep things as generalized as possible though.

___

## Why was this needed?

I noticed that exam records of students in my school were being stored in log books. Here are the problems with that approach:

1. The whole process resulted in hundreds of log books.
2. Log books were easily damageable.
3. They were very space-consuming, and maintaining them was tedious.
4. For a private school with a decent level of infrastructure, it felt pretty primitive that data was still being stored on paper — and that too in the 2020s.

___

## What was the development pipeline?

1. This app has been made using Python from start to finish.
2. It uses JSON files for structured data storage — one for each grade (grades 1 to 12).
3. Data handling is done using Python’s `json` module. Functions like `json.dump()` for writing data and `json.load()` for retrieving data have been used.
4. For displaying stored data in a readable, tabular format, the `tabulate` module is used.
5. To make the program modular and easier to debug or scale, it’s been broken down into several modules, each doing one (or a couple of) tasks.

___

## What were the learnings?

1. Learnt to use the `json` and `tabulate` modules — these aren’t a part of the standard CBSE CS syllabus.
2. Understood the importance of software architecture and how that architecture impacts the overall user experience.
3. Explored UI enhancements for CLI programs, including error handling and ANSI escape codes to make the experience more intuitive.
4. Learned how to deliver a better user experience with clear feedback systems — and how UX is directly impacted by small UI decisions.

___

## How to run the program?

### __NOTE:__ All JSON files are already populated with placeholder data — used for testing and to help people understand the tool. Feel free to delete them if needed.

### Requirements:
- Python must be installed on your system.
- Python's path should be added to your environment variables.

The entry point of the program is the `script.py` file.

If you're running it for the first time, it will begin with a password creation step. The password is stored in `password.json`. Yes, it’s not secure at all — but my goal was to learn how to build a password-protected system, not secure authentication (yet).

Once the password is created/entered, the main menu will appear. You’ll see a list of grades; select one by typing its corresponding number.

After selecting a grade, the terminal clears and a new menu shows up — from there, you can choose the operation you want to perform on that grade's data.

When you’re done, type `quit` to go back to the main menu. From there, you can switch grades or exit by typing `quit` again.

The UI has been designed to be super self-explanatory. So, the chances of someone getting confused because of the UI or input format are minimal.

___

## What's coming in the future?

I won’t promise “when,” but I can definitely say “what.” Here's what’s planned:

1. A proper GUI for a more modern and cleaner user experience.
2. Sorting students by marks.
3. Searching students by name.
4. Searching students by roll number.

These are a few feature updates I’ve already thought about for the future.

___

## Final note

Feel free to drop a mail with your feedback.  
__I’d genuinely love it if anyone trying this app could share their thoughts.__

Any kind of suggestions — feature updates, CLI enhancements, UX tweaks — are always welcome!

Thanks in advance! 😄
