#!/user/bin/python
# -*- coding: utf-8 -*-
# encoding=utf-8


def balance(message,data=0):
	win_dict, lose_dict, lose_fs_dict, invalid_dict = {}, {}, {}, {}
	message = json.loads(message)

	if not message:
		return

	ball, id_number, is_bet, bet_time = message[0], message[1], message[2], message[3]
	ball_number = []

	if isinstance(ball,list):
		for i in ball:
			ball_number.append(int(i))

	if is_bet == BET_SETTLE_END_MARK:
		qishu = message[1]
		commonOne_p.set_js_end(LOTTERY_TYPE, qishu, 0)
		return

	if is_bet == DEMO_BET_SETTLE_END_MARK:
		qishu = message[1]
		commonOne_p.set_js_end(LOTTERY_TYPE, qishu, 1)
		return

	if is_bet == BET_SETTLE_MARK:
		bet_tab = globalConfig.betTable
	elif is_bet == DEMO_BET_SETTLE_MARK:
		bet_tab = globalConfig.shiwan_betTable

	conn, cur = commonOne_p.mysql_pri_client(1)
	# bet_sql = "select * from %s where %s and js=0 and %s" %(bet_tab, id_number, bet_time)
	bet_sql = "select `id`,`uid`,`username`,`mingxi_1`,`mingxi_2`,`mingxi_3`,`win`,`fs`,`money`,`odds`,`did`,`agent_id`,`type`,`ptype`,`is_shiwan`,`site_id` from " + bet_tab + " where " + id_number + " and js=0  and " + bet_time

	cur.execute(bet_sql)
	rows = cur.fetchall()
	conn.commit()
	cur.close()
	conn.close()

	if len(rows) < 1:
		return


	for row in rows:
		win_dict[row['uid']], lose_dict[row['uid']], lose_fs_dict[row['uid']], invalid_dict[row['uid']] = [], [], [], []
	BALL = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	W, Q, B, S, G = [], [], [], [], []
	Wn, Qn, Bn, Sn, Gn = [], [], [], [], []
	Wdx, Qdx, Bdx, Sdx, Gdx = [], [], [], [], []
	Wds, Qds, Bds, Sds, Gds = [], [], [], [], []
	Wzh, Qzh, Bzh, Szh, Gzh = [], [], [], [], []
	WG_lh, Z_dx, Z_ds = [], [], []
	Q5_1Z, Q3_1Z, Z3_1Z, H3_1Z = [], [], [], []
	Q3_2Z, Z3_2Z, H3_2Z = [], [], []
	WQ, WB, WS, WG, QB, QS, QG, BS, BG, SG = [], [], [], [], [], [], [], [], [], []
	Q3_G3, Z3_G3, H3_G3 = [], [], []
	Q3_G6, Z3_G6, H3_G6 = [], [], []
	Q3_KD, Z3_KD, H3_KD = [], [], []
	for row in rows:
		try:

			# 万位
			if row['mingxi_1'] == unicode('万位', 'utf-8'):

				if str(row['mingxi_2']) in BALL:
					Wn.append(str(row['mingxi_2']))
				elif row['mingxi_2'] in [unicode('大', 'utf-8'), unicode('小', 'utf-8')]:
					Wdx.append(row['mingxi_2'])
				elif row['mingxi_2'] in [unicode('单', 'utf-8'), unicode('双', 'utf-8')]:
					Wds.append(row['mingxi_2'])
				elif row['mingxi_2'] in [unicode('质', 'utf-8'), unicode('合', 'utf-8')]:
					Wzh.append(row['mingxi_2'])
				
			# 千位
			if row['mingxi_1'] == unicode('千位', 'utf-8'):

				if str(row['mingxi_2']) in BALL:
					Qn.append(str(row['mingxi_2']))
				elif row['mingxi_2'] in [unicode('大', 'utf-8'), unicode('小', 'utf-8')]:
					Qdx.append(row['mingxi_2'])
				elif row['mingxi_2'] in [unicode('单', 'utf-8'), unicode('双', 'utf-8')]:
					Qds.append(row['mingxi_2'])
				elif row['mingxi_2'] in [unicode('质', 'utf-8'), unicode('合', 'utf-8')]:
					Qzh.append(row['mingxi_2'])

			# 百位
			if row['mingxi_1'] == unicode('百位', 'utf-8'):

				if str(row['mingxi_2']) in BALL:
					Bn.append(str(row['mingxi_2']))
				elif row['mingxi_2'] in [unicode('大', 'utf-8'), unicode('小', 'utf-8')]:
					Bdx.append(row['mingxi_2'])
				elif row['mingxi_2'] in [unicode('单', 'utf-8'), unicode('双', 'utf-8')]:
					Bds.append(row['mingxi_2'])
				elif row['mingxi_2'] in [unicode('质', 'utf-8'), unicode('合', 'utf-8')]:
					Bzh.append(row['mingxi_2'])

			# 十位
			if row['mingxi_1'] == unicode('十位', 'utf-8'):

				if str(row['mingxi_2']) in BALL:
					Sn.append(str(row['mingxi_2']))
				elif row['mingxi_2'] in [unicode('大', 'utf-8'), unicode('小', 'utf-8')]:
					Sdx.append(row['mingxi_2'])
				elif row['mingxi_2'] in [unicode('单', 'utf-8'), unicode('双', 'utf-8')]:
					Sds.append(row['mingxi_2'])
				elif row['mingxi_2'] in [unicode('质', 'utf-8'), unicode('合', 'utf-8')]:
					Szh.append(row['mingxi_2'])

			# 个位
			if row['mingxi_1'] == unicode('个位', 'utf-8'):

				if str(row['mingxi_2']) in BALL:
					Gn.append(str(row['mingxi_2']))
				elif row['mingxi_2'] in [unicode('大', 'utf-8'), unicode('小', 'utf-8')]:
					Gdx.append(row['mingxi_2'])
				elif row['mingxi_2'] in [unicode('单', 'utf-8'), unicode('双', 'utf-8')]:
					Gds.append(row['mingxi_2'])
				elif row['mingxi_2'] in [unicode('质', 'utf-8'), unicode('合', 'utf-8')]:
					Gzh.append(row['mingxi_2'])

			# 双面 总和大小单双 盘龍虎和
			if row['mingxi_1'] == unicode('總和,龍虎', 'utf-8'):

				if row['mingxi_2'] in [unicode('龙', 'utf-8'), unicode('虎', 'utf-8'), unicode('和', 'utf-8')]:
					WG_lh.append(row['mingxi_2'])
				elif row['mingxi_2'] in [unicode('总大', 'utf-8'), unicode('总小', 'utf-8')]:
					Z_dx.append(row['mingxi_2'])
				elif row['mingxi_2'] in [unicode('总单', 'utf-8'), unicode('总双', 'utf-8')]:
					Z_ds.append(row['mingxi_2'])

			num = row['mingxi_2'].strip(',').split(',')

			if row['mingxi_1'] == unicode('一字组合', 'utf-8'):
				# 	【一字组合玩法】
				# 	◎全五一字组合：0~9任选1个号进行投注，当开奖结果[万位、千位、百位、十位、个位]任一数与所选的号码相同时，即为中奖。
				#   同个号码出现多次时只计一次中奖
				# 	※举例：下注一字【5号】＄100，一字賠率2	.404五颗球开出9，5，8，3，5	派彩为＄240.4
				# 	◎前三：0~9	任选1个号进行投注，当开奖结果[万位、千位、百位]任一数与所选的号码相同时，即为中奖。
				# 	◎中三：0~9	任选1个号进行投注，当开奖结果[千位、百位、十位]任一数与所选的号码相同时，即为中奖。
				# 	◎后三：0~9	任选1个号进行投注，当开奖结果[百位、十位、个位]任一数与所选的号码相同时，即为中奖。
				if row['mingxi_3'][:2] == unicode('全五', 'utf-8'):
					Q5_1Z.append(str(row['mingxi_2']))
				elif row['mingxi_3'][:2] == unicode('前三', 'utf-8'):
					Q3_1Z.append(str(row['mingxi_2']))
				elif row['mingxi_3'][:2] == unicode('中三', 'utf-8'):
					Z3_1Z.append(str(row['mingxi_2']))
				elif row['mingxi_3'][:2] == unicode('后三', 'utf-8'):
					H3_1Z.append(str(row['mingxi_2']))

			if row['mingxi_1'] == unicode('二字组合', 'utf-8'):
				# 于前三、中三、后三0~9任选2个号进行投注，当开奖结果任二数与所选的号码相同时，即为中奖。
				# ※举例：投注者购买后三二字组合，选择2个相同号码如为11，
				# 当期开奖结果如为xx11x、xx1x1、xxx11、皆视为中奖。（x = 0~9 任一数）
				# ※举例：投注者购买后三二字组合，选择2个不同号码如为12，
				# 当期开奖结果如为xx12x、xx1x2、xx21x、xx2x1、xxx12、xxx21皆视为中奖。（x = 0~9任一数）

				if row['mingxi_3'][:2] == unicode('前三', 'utf-8'):
					Q3_2Z.append(str(row['mingxi_2']))
				elif row['mingxi_3'][:2] == unicode('中三', 'utf-8'):
					Z3_2Z.append(str(row['mingxi_2']))
				elif row['mingxi_3'][:2] == unicode('后三', 'utf-8'):
					H3_2Z.append(str(row['mingxi_2']))

			if row['mingxi_1'] == unicode('二字和数', 'utf-8'):
				# 开奖结果万千位、万百位、万十位、万个位、千百位、千十位、千个位、百十位、百个位、十个位
				# 数字总和的个位数为1、3、5、7、9时为“单”，若为0、2、4、6、8时为“双”，当投注和数单双与开奖结果的和数单双相符时，即为中奖。
				# ※举例：投注者购买百十和数单，当期开奖结果如为20290（百2+十9+个0=11为单），则视为中奖。

				# 二字和数	双	万十和数
				
				if row['mingxi_3'][0] == unicode('万', 'utf-8') and row['mingxi_3'][1] == unicode('千', 'utf-8'):
					WQ.append(str(row['mingxi_2']))
				elif row['mingxi_3'][0] == unicode('万', 'utf-8') and row['mingxi_3'][1] == unicode('百', 'utf-8'):
					WB.append(str(row['mingxi_2']))
				elif row['mingxi_3'][0] == unicode('万', 'utf-8') and row['mingxi_3'][1] == unicode('十', 'utf-8'):
					WS.append(str(row['mingxi_2']))
				elif row['mingxi_3'][0] == unicode('万', 'utf-8') and row['mingxi_3'][1] == unicode('个', 'utf-8'):
					WG.append(str(row['mingxi_2']))
				elif row['mingxi_3'][0] == unicode('千', 'utf-8') and row['mingxi_3'][1] == unicode('百', 'utf-8'):
					QB.append(str(row['mingxi_2']))
				elif row['mingxi_3'][0] == unicode('千', 'utf-8') and row['mingxi_3'][1] == unicode('十', 'utf-8'):
					QS.append(str(row['mingxi_2']))
				elif row['mingxi_3'][0] == unicode('千', 'utf-8') and row['mingxi_3'][1] == unicode('个', 'utf-8'):
					QG.append(str(row['mingxi_2']))
				elif row['mingxi_3'][0] == unicode('百', 'utf-8') and row['mingxi_3'][1] == unicode('十', 'utf-8'):
					BS.append(str(row['mingxi_2']))
				elif row['mingxi_3'][0] == unicode('百', 'utf-8') and row['mingxi_3'][1] == unicode('个', 'utf-8'):
					BG.append(str(row['mingxi_2']))
				elif row['mingxi_3'][0] == unicode('十', 'utf-8') and row['mingxi_3'][1] == unicode('个', 'utf-8'):
					SG.append(str(row['mingxi_2']))

			if row['mingxi_1'] == unicode('组选三', 'utf-8'):
				# 组选三
				if row['mingxi_3'][:2] == unicode('前三', 'utf-8'):
					# ◎前三：会员可以挑选5~10个号码，当开奖结果[万位、千位、百位]中有且只有两个号码重复，则视为中奖。
					# 挑选不同个数的号码有其相对应的赔率。
					# 如果是选择(1、2、3、4、5)，则只要开奖结果[万位、千位、百位]中，有出现1、2、3、4、5中的任何两个号码，且其中有一个号码重复则中奖。
					# ※例如：112、344，若是开出豹子则不算中奖。
					# ※备注："豹子"为三字同号，例如：111、222
					Q3_G3.append(str(row['mingxi_2']))
				elif row['mingxi_3'][:2] == unicode('中三', 'utf-8'):
					# ◎中三：会员可以挑选5~10个号码，当开奖结果[千位、百位、十位]中有且只有两个号码重复，则视为中奖。挑选不同个数的号码有其相对应的赔率
					# 如果是选择(1、2、3、4、5)，则只要开奖结果[千位、百位、十位]中，有出现1、2、3、4、5中的任何两个号码，且其中有一个号码重复则中奖。
					# ※例如：112、344，若是开出豹子则不算中奖。
					Z3_G3.append(str(row['mingxi_2']))
				elif row['mingxi_3'][:2] == unicode('后三', 'utf-8'):
					# ◎前三：会员可以挑选5~10个号码，当开奖结果[万位、千位、百位]中有且只有两个号码重复，则视为中奖。
					# 挑选不同个数的号码有其相对应的赔率。
					# 如果是选择(1、2、3、4、5)，则只要开奖结果[万位、千位、百位]中，有出现1、2、3、4、5中的任何两个号码，且其中有一个号码重复则中奖。
					# ※例如：112、344，若是开出豹子则不算中奖。
					# ※备注："豹子"为三字同号，例如：111、222
					H3_G3.append(str(row['mingxi_2']))
				else:
					pass

			if row['mingxi_1'] == unicode('组选六', 'utf-8'):
				if row['mingxi_3'][:2] == unicode('前三', 'utf-8'):
					"""
						◎前三：会员可以挑选4~8个号码，当开奖结果[万位、千位、百位]都出现在所下注的号码中且没有任何号码重复，则视为中奖。
						挑选不同个数的号码有其相对应的赔率，中奖赔率以所选号码中的最小赔率计算派彩。
						※例如：如果是选择(1、2、3、4)，则开奖结果[万位、千位、百位]为123、124、134、234都中奖，其他都是不中奖。
						例如：112、133、145、444等都是不中奖。
					"""
					Q3_G6.append(str(row['mingxi_2']))
				elif row['mingxi_3'][:2] == unicode('中三', 'utf-8'):
					Z3_G6.append(str(row['mingxi_2']))
				elif row['mingxi_3'][:2] == unicode('后三', 'utf-8'):
					H3_G6.append(str(row['mingxi_2']))

				else:
					pass

			# 【跨度玩法】
			if row['mingxi_1'] == unicode('跨度', 'utf-8'):
				if row['mingxi_3'][:2] == unicode('前三', 'utf-8'):
					Q3_KD.append(str(row['mingxi_2']))
				elif row['mingxi_3'][:2] == unicode('中三', 'utf-8'):
					Z3_KD.append(str(row['mingxi_2']))
				elif row['mingxi_3'][:2] == unicode('后三', 'utf-8'):
					H3_KD.append(str(row['mingxi_2']))
				else:
					pass

		except:
			# 如果结算期间有任何错误，注单、错误信息在此处打印并写入日志，不会卡住不结算
			print row
			exstr = traceback.format_exc()
			print exstr
			commonOne_p.write_blance_error_log(row, exstr)
	if data == 1:
		return win_dict,lose_dict,lose_fs_dict,invalid_dict
	commonOne_p.merge_win(win_dict, bet_time, bet_tab)
	commonOne_p.merge_lose(lose_dict, bet_time, bet_tab)
	commonOne_p.merge_lose_fs(lose_fs_dict, bet_time, bet_tab)
	commonOne_p.merge_invalid(invalid_dict, bet_time, bet_tab)
