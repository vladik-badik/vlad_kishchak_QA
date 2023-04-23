test_design_writers = [1, 3, 5]
scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

all_testers = sorted(list(set(test_design_writers + scripters + reviewers)))
script_writers_only = sorted(list(set(scripters) - set(test_design_writers) - set(reviewers)))
working_today = sorted(list(set(all_testers) - set(out_of_office_today)))
script_and_reviewers_working_today = sorted(list(set(scripters) & set(reviewers) & set(working_today)))

print("All testers:", all_testers)
print("Script writers only:", script_writers_only)
print("Testers working today:", working_today)
print("Script and reviewers working today:", script_and_reviewers_working_today)
