from django.db import models

# Create your models here.


class Project(models.Model):
    class Meta:
        db_table = 'OA_Project'
    pro_id = models.CharField(max_length=32, primary_key=True)

    code = models.CharField(max_length=12, null=True, blank=True)
    client = models.CharField(max_length=32, null=True, blank=True)
    engagement = models.CharField(max_length=255, null=True, blank=True)
    industry = models.CharField(max_length=255, null=True, blank=True)
    function = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    team = models.CharField(max_length=255, null=True, blank=True)
    duration = models.CharField(max_length=32, null=True, blank=True)
    start_date = models.DateField(max_length=64, null=True, blank=True)
    sub_industry = models.CharField(max_length=255, null=True, blank=True)
    sub_function = models.CharField(max_length=255, null=True, blank=True)
    ed = models.CharField(max_length=255, null=True, blank=True)
    ap = models.CharField(max_length=255, null=True, blank=True)
    asc_pro = models.CharField(max_length=255, null=True, blank=True)
    account = models.CharField(max_length=255, null=True, blank=True)
    end_date = models.DateField(max_length=64, null=True, blank=True)
    key_issue = models.CharField(max_length=255, null=True, blank=True)
    solutions_and_impacts = models.CharField(max_length=556, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    sector = models.CharField(max_length=255, null=True, blank=True)
    contacts = models.CharField(max_length=255, null=True, blank=True)
    fee = models.CharField(max_length=255, null=True, blank=True)
    target = models.CharField(max_length=255, null=True, blank=True)
    lop = models.CharField(max_length=255, null=True, blank=True)
    deck = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    data = models.CharField(max_length=255, null=True, blank=True)
    interview_guide = models.CharField(max_length=255, null=True, blank=True)
    focus_gp = models.CharField(max_length=255, null=True, blank=True)
    survey = models.CharField(max_length=255, null=True, blank=True)
    resources = models.CharField(max_length=255, null=True, blank=True)
    collected = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.team


class Employee(models.Model):
    class Meta:
        db_table = 'OA_Employee'

    emp_id = models.CharField('员工ID', max_length=32, primary_key=True)
    working_state = models.CharField('在职状态', max_length=12, choices=(('in', '在职'), ('leave', '离职')))
    name = models.CharField('英文名', max_length=32)
    gender = models.CharField('性别', max_length=6, choices=(('M', '男'), ('F', '女')))

    # default null
    mbti = models.CharField('职业性格测试', max_length=12, null=True, blank=True)
    birthday = models.CharField('出生日期', max_length=8, null=True, blank=True)
    mobile = models.CharField('电话电话', max_length=16, null=True, blank=True)
    hire_date = models.DateField('录入日期', null=True, blank=True)
    education = models.TextField('教育经历', null=True, blank=True)
    work_exp = models.TextField('工作经历', null=True, blank=True)
    tenure = models.CharField('在职日期', max_length=32, null=True, blank=True)
    recruited = models.CharField('招聘渠道', max_length=32, null=True, blank=True)
    promotion = models.TextField('晋升经历', null=True, blank=True)
    about = models.TextField('关于', null=True, blank=True)
    professional_aspirations = models.TextField('职业意向', null=True, blank=True)
    user_guide = models.CharField(max_length=255, null=True, blank=True)
    favorites = models.TextField('兴趣爱好', null=True, blank=True)
    training_sessions = models.TextField('培训课程', null=True, blank=True)
    name_cn = models.CharField('中文名', max_length=16, null=True, blank=True)
    id1 = models.CharField('身份证号', max_length=32, null=True, blank=True)
    id2 = models.CharField('护照号',  max_length=32, null=True, blank=True)
    join_date = models.DateField('入职日期', null=True, blank=True)
    level = models.CharField('级别', max_length=255, null=True, blank=True)
    loc = models.CharField('办公地点', max_length=255, null=True, blank=True)
    module = models.CharField(max_length=255, null=True, blank=True)
    ra_ten = models.CharField(max_length=255, null=True, blank=True)
    a_ten = models.CharField(max_length=255, null=True, blank=True)
    sa_ten = models.CharField(max_length=255, null=True, blank=True)
    asc_w_ten = models.CharField(max_length=255, null=True, blank=True)
    asc_ten = models.CharField(max_length=255, null=True, blank=True)
    login_mobile = models.CharField(max_length=255, null=True, blank=True)
    openid = models.CharField(max_length=32, null=True, blank=True)
    leave_date = models.CharField(max_length=32, null=True, blank=True)
    email = models.CharField('电子邮箱', max_length=255, null=True, blank=True)
    company = models.CharField('就职公司', max_length=255, null=True, blank=True)

    project = models.ManyToManyField(Project, through='EmployeeProject')

    def __str__(self):
        return self.name_cn


class EmployeeProject(models.Model):
    class Meta:
        db_table = 'OA_Employee_Project'

    id = models.CharField(max_length=32, primary_key=True)

    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pro = models.ForeignKey(Project, on_delete=models.CASCADE)

    emp_order = models.IntegerField(null=True, default=0)
    emp_name = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return self.emp

