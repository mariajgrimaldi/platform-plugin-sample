from openedx.core.djangoapps.course_groups.api import get_group, get_group_info_for_group
from xmodule.partitions.partitions import NoSuchUserPartitionGroupError


class GroupPartitionScheme:
    """
    This scheme uses lms cohorts (CourseUserGroups) and cohort-partition
    mappings (CourseUserGroupPartitionGroup) to map lms users into Partition
    Groups.
    """

    @classmethod
    def get_grouped_user_partition(cls, course):
        for user_partition in course.user_partitions:
            if user_partition.scheme == cls:
                return user_partition

        return None

    @classmethod
    def get_group_for_user(cls, course_key, user, user_partition):
        group = get_group(user, course_key)
        if group is None:
            return None

        group_id, partition_id = get_group_info_for_group(group)
        if partition_id is None:
            return None

        if partition_id != user_partition.id:
            return None

        try:
            return user_partition.get_group(group_id)
        except NoSuchUserPartitionGroupError:
            return None
