function test {
konsole -e "
    nano assets/tasks.py
    read -n 1 -s -r -p 'Press Enter To Edit The Script Or Close The Window To Continue'
    nano assets/task_1.py
    "
}

test