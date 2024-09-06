import os
import datetime
import re

def summarize_last_week_notes(folder_path):
    # Get today's date
    today = datetime.date.today()
    # Get the dates for the last 7 days
    last_week_dates = [(today - datetime.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
    
    # Initialize storage for summarized tasks and keywords
    tasks_summary = []
    english_summary = []
    
    # Pattern to match tasks and keywords
    task_pattern = re.compile(r'- \[( |x|-)\] (.+)\n\s+(.+)\n\s+Comment\n\s+Date: \[\[(.+)\.md\]\]')
    keyword_pattern = re.compile(r'## English\n\n((?:.+\n)+)')
    
    # Collect tasks and keywords from the last week notes
    for date in last_week_dates:
        print(f'Processing {date} ...')
        file_path = os.path.join(folder_path, f'{date}.md')
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Extract and format tasks
                tasks = re.findall(task_pattern, content)
                for task in tasks:
                    tasks_summary.append(f"- [{task[0]}] {task[1]}\n{task[2]}\nDate: [[{date}.md]]")
                # Extract and format keywords
                english_section = re.search(keyword_pattern, content)
                if english_section:
                    english_summary.append(f"- Date: [[{date}.md]]\n{english_section.group(1).strip()}")
    
    # Build the summary content
    summary_content = "## Last Week\n\n"
    
    # Add tasks summary
    if tasks_summary:
        summary_content += "## TODO\n\n" + "\n".join(tasks_summary) + "\n\n"
    
    # Add English summary
    if english_summary:
        summary_content += "## English\n\n" + "\n".join(english_summary) + "\n\n"
    
    # Save the summary to the last day's note
    last_day_note_path = os.path.join(folder_path, f'{last_week_dates[-1]}.md')
    print(f'Save to {last_day_note_path}')
    with open(last_day_note_path, 'a', encoding='utf-8') as file:
        file.write(summary_content)

# Usage example
summarize_last_week_notes('C:/Users/bi.minh.luu/Documents/Note/1_daily')
