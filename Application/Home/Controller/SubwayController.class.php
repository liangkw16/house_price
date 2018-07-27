<?php
namespace Home\Controller;
use Think\Controller;
class SubwayController extends Controller {
    public function index($id){
		$condition['house_id']=$id;
		$Subway = M("subway");
		$subways = $Subway->where($condition)->select();
		$this->ajaxReturn($subways,'JSON');
    }
}