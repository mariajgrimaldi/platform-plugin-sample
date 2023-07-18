from platform_plugin_sample.roles import CourseProfessorRole

from openedx_filters import PipelineStep

class CheckProfessorRole(PipelineStep):

    def run(self, user, roles, course_key):
        # If user belongs to cohort with professor type, then append professor role to be checked
        return {
            "user": user,
            "roles": roles.append(CourseProfessorRole(course_key)),
            "course_key": course_key,
        }
