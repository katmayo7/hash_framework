import hash_framework as hf
import json

def __main__():
    manager_uri = 'http://127.0.0.1:8000'
    scheduler_uri = 'http://127.0.0.1:8001'
    c = hf.manager.api.Client(manager_uri, scheduler_uri)
    #tid = c.create_task('md4-families-r8-12-16-20-24', 'md4')
    tid = 78
    print("Task ID: " + str(tid))

    kernel_name = "families"
    kernel = hf.kernels.lookup(kernel_name)
    algo = "md4"
    work = kernel.gen_work([8, 12, 16, 20, 24], list(range(0, 20)))

    start_state = ""
    start_block = ""

    # Default start state
    # start_state = "FTTFFTTTFTFFFTFTFFTFFFTTFFFFFFFTTTTFTTTTTTFFTTFTTFTFTFTTTFFFTFFTTFFTTFFFTFTTTFTFTTFTTTFFTTTTTTTFFFFTFFFFFFTTFFTFFTFTFTFFFTTTFTTF"

    jobs = []
    for w in work:
        oargs = kernel.work_to_args(algo, start_state, start_block, w)
        args = json.dumps(oargs)

        obj = {'task': tid, 'algo': algo, 'kernel': kernel_name, 'args': args,
               'result_table': "c_" + algo}
        jobs.append(obj)
        if len(jobs) > 10000:
            c.create_jobs(tid, jobs)
            jobs = []

    if len(jobs) > 0:
        c.create_jobs(tid, jobs)
        jobs = []


__main__()
