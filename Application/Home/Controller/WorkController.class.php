<?php
namespace Home\Controller;
use Think\Controller;
class WorkController extends Controller {
    public function index($id){
		$condition['house_id']=$id;
		$Work = M("work");
		$works = $Work->where($condition)->select();
		$this->ajaxReturn($works,'JSON');
    }
}