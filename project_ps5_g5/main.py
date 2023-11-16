import subprocess

def open_cmd_and_execute(script_path, wait=False):
    if wait:
        subprocess.Popen(['start', 'cmd', '/k', 'python', script_path], shell=True).wait()
    else:
        subprocess.Popen(['start', 'cmd', '/k', 'python', script_path], shell=True)

if __name__ == "__main__":
    input_script = 'input_data.py'
    path_rtp_script = 'dynamic_plot.py'
    processing_script = 'detection.py'

    a = subprocess.Popen(['start', 'cmd', '/k', 'python', input_script], shell=True)
    b = subprocess.Popen(['start', 'cmd', '/k', 'python', path_rtp_script], shell=True)

    b.wait()
    c = subprocess.Popen(['start', 'cmd', '/k', 'python', processing_script], shell=True).wait()

    # still c opens simultaneously
    # HELPPPPPP