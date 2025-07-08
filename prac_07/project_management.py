from datetime import datetime
from project import Project


def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, "r") as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split("\t")
            project = Project(*parts)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save the current projects to a file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(complete):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects that start after a given date."""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format.")
        return
    filtered = [p for p in projects if p.start_date > filter_date]
    for project in sorted(filtered, key=lambda p: p.start_date):
        print(project)


def add_new_project():
    """Prompt user to add a new project and return it."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion = input("Percent complete: ")
    return Project(name, start_date, priority, cost_estimate, completion)


def update_project(projects):
    """Allow user to update completion and priority of a project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)
        new_completion = input("New Percentage: ")
        new_priority = input("New Priority: ")

        if new_completion:
            project.completion_percentage = int(new_completion)
        if new_priority:
            project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid selection.")


def main():
    FILENAME = "projects.txt"
    projects = load_projects(FILENAME)
    print("Welcome to Pythonic Project Management")

    menu = "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date" \
           "\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"

    print(menu)
    choice = input(">>> ").lower()

    while choice != 'q':
        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid menu option.")

        print(menu)
        choice = input(">>> ").lower()

    print("Thank you for using custom-built project management software.")


if __name__ == '__main__':
    main()
