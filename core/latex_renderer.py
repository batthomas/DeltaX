import os
import shutil
import subprocess
from tempfile import mkdtemp, mkstemp

from jinja2 import Environment, FileSystemLoader


class LatexDocument:
    template_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "core", "templates")

    def __init__(self, tasks):
        self.temp_dir = mkdtemp()
        self.tasks = tasks
        self.latex = self.generate_latex()

    def generate_latex(self):
        env = Environment(block_start_string="(%", block_end_string="%)",
                          variable_start_string="((", variable_end_string="))",
                          comment_start_string="((#", comment_end_string="#))",
                          loader=FileSystemLoader(searchpath=self.template_dir))
        template = env.get_template("latex/document_base.tex")
        return template.render({"tasks": self.tasks})

    def generate_pdf(self):
        latex = self.latex

        cwd = os.getcwd()
        os.chdir(self.temp_dir)
        texfile, texfilename = mkstemp(dir=self.temp_dir)
        os.write(texfile, latex.encode("utf-8"))
        os.close(texfile)
        process = subprocess.Popen(["pdflatex",
                                    "-jobname=task",
                                    "-halt-on-error",
                                    "-interaction=batchmode", texfilename])
        process.communicate(timeout=5)
        os.chdir(cwd)

        with open(os.path.join(self.temp_dir, "task.pdf"), "rb") as file:
            pdf = file.read()

        with open(os.path.join(self.temp_dir, "task.log"), "rb") as file:
            log = file.read()

        return pdf, log

    def __del__(self):
        shutil.rmtree(self.temp_dir)
