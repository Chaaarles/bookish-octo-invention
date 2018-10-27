const taskInput = document.getElementById("taskInput");
const taskButton = document.getElementById("taskButton");
const tasks = document.getElementById("tasks");
const output = document.getElementById("output");

let taskList = [];

function addTask(){
    taskList.push({check: false, text: taskInput.value});
    taskInput.value = ""
    renderTasks()
    console.table(taskList);
}

function checked(i){
    e = taskList[i];
    e.check = !e.check;
    renderTasks();
}

function renderTasks(){
    tasks.innerHTML = "";
    
    const taskMarkup = taskList.map((task, i) => (
        `<li>
            <input type="checkbox" id="task-${i}" ${task.check ? "checked" : ""} />
            <label for="task-${i}" style="${task.check ? 'text-decoration: line-through' : ''}">${task.text}</label>
        </li>`
    ));

    tasks.innerHTML = taskMarkup.reverse().join("\n");

    taskList.forEach((task, i) => document.querySelector(`#task-${i}`).addEventListener("change", () => checked(i)))

    
    // output
    const len = taskList.length;
    const comp = taskList.reduce((count, t) => ((t.check ? 1 : 0) + count), 0);
    output.innerText = `${comp}/${len} completed!`
}


taskButton.addEventListener("click", addTask);