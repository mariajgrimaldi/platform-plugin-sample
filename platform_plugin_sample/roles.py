from common.djangoapps.student.roles import CourseRole, register_access_role

@register_access_role
class CourseProfessorRole(CourseRole):
    """A course Professor"""
    ROLE = 'professor'

    def __init__(self, *args, **kwargs):
        super().__init__(self.ROLE, *args, **kwargs)
