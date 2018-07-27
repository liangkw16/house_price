<?php
namespace Home\Controller;
use Think\Controller;
class BusController extends Controller {
    public function index($id){
		$condition['house_id']=$id;
		$Bus = M("bus");
		$buses = $Bus->where($condition)->select();
		$this->ajaxReturn($buses,'JSON');
    }
}