<?php
namespace Home\Controller;
use Think\Controller;
class HospitalController extends Controller {
    public function index($id){
		$condition['house_id']=$id;
		$Hospital = M("hospital");
		$hospitals = $Hospital->where($condition)->select();
		$this->ajaxReturn($hospitals,'JSON');
    }
}