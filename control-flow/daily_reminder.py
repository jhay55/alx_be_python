# This script prints out a reminder or note based on task priority level and urgency 


# prompts for receiving input from user 
task = input('Enter your task: ').strip().capitalize()
priority = input('Priority (high/medium/low): ').lower().strip()
time_bound = input('Is it time-bound? (yes/no):').lower().strip()

#match and case block for priority level nested with if statements for task urgency
match priority:
    case 'high':
        if time_bound == 'yes':
            print(f'Reminder: \'{task}\' is a high priority task that requires immediate attention today!')
        else:
            print(f'Reminder: \'{task}\' is a high priority task. Try to get to it as soon as you can!')

    case 'medium':
        if time_bound == 'yes':
            print(f'Note: \'{task}\' is a medium priority task that requires attention today!')
        else:
            print(f'Note: \'{task}\' is a medium priority task.')

    case 'low':
        if time_bound == 'yes':
            print(f'Note: \'{task}\' is a low priority task that requires attention today!')
        else:
            print(f'Note: \'{task}\' is a low priority task. Consider completing it when you have free time.')
