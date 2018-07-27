<?php
namespace Home\Controller;
use Think\Controller;
class IndexController extends Controller {
    public function index(){
    	$District = M("district");
    	$districts = $District->where()->select();
    	$this->assign('districts',$districts);
        $this->display();
    }
    public function get_all($price,$area,$distance){
    	$House = M("ershou");
        $map["unit_price"]  = array("egt",((float)$price)*10000);
        $map['housearea'] = array("egt",(float)$area);
        $map['distance'] = array("egt",((float)$distance)*1000);
 		$houses = $House->where($map)->select();
		$this->ajaxReturn($houses,'JSON');
    }
}