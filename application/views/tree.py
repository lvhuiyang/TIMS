from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.messages import get_messages
from application.views import CheckUserAuthenticatedMixin


class TreeView(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="tree.html", context={'messages': get_messages(request)})

    def post(self, request, *args, **kwargs):
        type = request.POST['type']
        result = []

        class TreeNode:
            def __init__(self, value, left=None, right=None):
                self.value = value
                self.left = left
                self.right = right

        # 前序遍历：以“根左右”顺序递归遍历
        def pre_traverse(node):
            if node is None:
                return None
            result.append(node.value)
            pre_traverse(node=node.left)
            pre_traverse(node=node.right)

        # 中序遍历：以“左根右”顺序递归遍历
        def mid_traverse(node):
            if node is None:
                return None
            mid_traverse(node.left)
            result.append(node.value)
            mid_traverse(node.right)

        # 后序遍历：以“左右根”顺序递归遍历
        def post_traverse(node):
            if node is None:
                return None
            post_traverse(node.left)
            post_traverse(node.right)
            result.append(node.value)

        student_a = TreeNode("同学A")
        student_b = TreeNode("同学B")
        student_c = TreeNode("同学C")
        student_d = TreeNode("同学D")
        student_e = TreeNode("同学E")
        student_f = TreeNode("同学F")
        student_g = TreeNode("同学G")
        class_cs_1401 = TreeNode("计科1401", left=student_a, right=student_b)
        class_cs_1402 = TreeNode("计科1402", left=student_c, right=None)
        class_software_1401 = TreeNode("软件1401", left=student_d, right=student_e)
        class_software_1402 = TreeNode("软件1402", left=student_f, right=student_g)
        marjor_cs = TreeNode("计算机科学与技术", left=class_cs_1401, right=class_cs_1402)
        marjor_software = TreeNode("软件工程", left=class_software_1401, right=class_software_1402)
        root_institute = TreeNode("计算机科学与技术学院", left=marjor_cs, right=marjor_software)
        if type == "pre":
            pre_traverse(root_institute)
        elif type == "mid":
            mid_traverse(root_institute)
        elif type == "post":
            post_traverse(root_institute)
        else:
            result = ["参数错误"]
        return_result = "开始遍历 => "
        for i in result:
            return_result = return_result + i + "=> "
        return_result += "遍历结束"
        return HttpResponse(return_result)
