<?php
namespace Home\Controller;
use Think\Controller;
class SchoolController extends Controller {
    public function index($id){
		$condition['house_id']=$id;
		$School = M("school");
		$schools = $School->where($condition)->select();
		$this->ajaxReturn($schools,'JSON');
    }
}