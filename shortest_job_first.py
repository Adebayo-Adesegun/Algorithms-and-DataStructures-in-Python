from functools import reduce


def sjf(jobs: list, index: int) -> int:
    processed_jobs = list()

    job_to_track = jobs[index]

    len_of_jobs = len(jobs)
    counter = 0

    for i in range(len_of_jobs):
        current_job = jobs[i]
        if current_job < job_to_track or (current_job == job_to_track and i <= index):
            counter += 1
            processed_jobs.append(current_job)

    return reduce(lambda x, y: x + y, processed_jobs[0:counter])



print(sjf([3, 10, 20, 1, 2], 0))
