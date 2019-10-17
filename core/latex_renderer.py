import os
import subprocess
from tempfile import mkdtemp, mkstemp

from jinja2 import Environment, FileSystemLoader


class LatexDocument:
    template_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "core", "templates")

    def __init__(self, tasks):
        self.tasks = tasks

    def generate_latex(self):
        env = Environment(block_start_string="(%", block_end_string="%)",
                          variable_start_string="((", variable_end_string="))",
                          comment_start_string="((#", comment_end_string="#))",
                          loader=FileSystemLoader(searchpath=self.template_dir))

        template = env.get_template("latex/document_base.tex")
        return template.render({"tasks": self.tasks})

    def generate_pdf(self):
        latex = self.generate_latex()

        temp_dir = mkdtemp()
        os.chdir(temp_dir)
        texfile, texfilename = mkstemp(dir=temp_dir)
        os.write(texfile, latex.encode("utf-8"))
        os.close(texfile)

        process = subprocess.Popen(["pdflatex", "-jobname=task",
                                    "-halt-on-error", "-interaction=batchmode", texfilename])
        process.communicate(timeout=5)

        with open(os.path.join(temp_dir, "task.pdf"), "rb") as file:
            pdf = file.read()

        # TODO: Delete Temp files
        # shutil.rmtree(temp_dir)

        return pdf
