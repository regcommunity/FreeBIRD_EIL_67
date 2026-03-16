from pybirdai.models.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage, track_table_init

class F_15_00_a_REF_FINREP_3_0_UnionItem:
	base = None #F_15_00_a_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT"})
	def TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT(self) -> str:
		''' return string from RCGNTN_STTS enumeration '''
		return self.base.TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT()
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
	@lineage(dependencies={"base.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.base.ACCNTNG_CLSSFCTN()
	@lineage(dependencies={"base.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.base.HLD_SL_INDCTR()
	@lineage(dependencies={"base.MSRMNT_MTHD"})
	def MSRMNT_MTHD(self) -> str:
		''' return string from MSRMNT_MTHD enumeration '''
		return self.base.MSRMNT_MTHD()
	@lineage(dependencies={"base.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.base.SBJCT_IMPRMNT_INDCTR()
	@lineage(dependencies={"base.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self) -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		return self.base.NGTBL_SCRTY_INDCTR()
	@lineage(dependencies={"base.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.base.CRRYNG_AMNT()
	@lineage(dependencies={"base.AMNT_DRCGNSD_CPTL_PRPS"})
	def AMNT_DRCGNSD_CPTL_PRPS(self) -> int:
		return self.base.AMNT_DRCGNSD_CPTL_PRPS()

class F_15_00_a_REF_FINREP_3_0_Base:
	def TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT() -> str:
		''' return string from RCGNTN_STTS enumeration '''
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass
	def ACCNTNG_CLSSFCTN() -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		pass
	def HLD_SL_INDCTR() -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		pass
	def MSRMNT_MTHD() -> str:
		''' return string from MSRMNT_MTHD enumeration '''
		pass
	def SBJCT_IMPRMNT_INDCTR() -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		pass
	def NGTBL_SCRTY_INDCTR() -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		pass
	def CRRYNG_AMNT() -> int:
		pass
	def AMNT_DRCGNSD_CPTL_PRPS() -> int:
		pass

class F_15_00_a_REF_FINREP_3_0_UnionTable :
	F_15_00_a_REF_FINREP_3_0_UnionItems = [] # F_15_00_a_REF_FINREP_3_0_UnionItem []
	F_15_00_a_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None # Advances_that_are_not_loans
	F_15_00_a_REF_FINREP_3_0_Other_loans_Table = None # Other_loans
	F_15_00_a_REF_FINREP_3_0_Credit_card_debt_Table = None # Credit_card_debt
	F_15_00_a_REF_FINREP_3_0_Trade_receivables_Table = None # Trade_receivables
	F_15_00_a_REF_FINREP_3_0_Finance_leases_Table = None # Finance_leases
	F_15_00_a_REF_FINREP_3_0_On_demand_and_short_notice_Table = None # On_demand_and_short_notice
	F_15_00_a_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None # Reverse_repurchase_agreements
	F_15_00_a_REF_FINREP_3_0_Debt_securities_Table = None # Debt_securities
	F_15_00_a_REF_FINREP_3_0_Equity_instruments_security_Table = None # Equity_instruments_security
	F_15_00_a_REF_FINREP_3_0_Equity_instruments_instrument_Table = None # Equity_instruments_instrument
	def calc_F_15_00_a_REF_FINREP_3_0_UnionItems(self) -> list[F_15_00_a_REF_FINREP_3_0_UnionItem] :
		items = [] # F_15_00_a_REF_FINREP_3_0_UnionItem []
		for item in self.F_15_00_a_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss:
			newItem = F_15_00_a_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_15_00_a_REF_FINREP_3_0_Other_loans_Table.Other_loanss:
			newItem = F_15_00_a_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_15_00_a_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts:
			newItem = F_15_00_a_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_15_00_a_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless:
			newItem = F_15_00_a_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_15_00_a_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess:
			newItem = F_15_00_a_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_15_00_a_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices:
			newItem = F_15_00_a_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_15_00_a_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss:
			newItem = F_15_00_a_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_15_00_a_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess:
			newItem = F_15_00_a_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_15_00_a_REF_FINREP_3_0_Equity_instruments_security_Table.Equity_instruments_securitys:
			newItem = F_15_00_a_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_15_00_a_REF_FINREP_3_0_Equity_instruments_instrument_Table.Equity_instruments_instruments:
			newItem = F_15_00_a_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_15_00_a_REF_FINREP_3_0_UnionItems = []
		self.F_15_00_a_REF_FINREP_3_0_UnionItems.extend(self.calc_F_15_00_a_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Advances_that_are_not_loans(F_15_00_a_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT

class Other_loans(F_15_00_a_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT

class Credit_card_debt(F_15_00_a_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT

class Trade_receivables(F_15_00_a_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT

class Finance_leases(F_15_00_a_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT

class On_demand_and_short_notice(F_15_00_a_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT

class Reverse_repurchase_agreements(F_15_00_a_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT

class Debt_securities(F_15_00_a_REF_FINREP_3_0_Base):
	LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT = None # LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT
	@lineage(dependencies={"LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.CRRYNG_AMNT
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR
	EXCHNG_TRDBL_DRVTV_PSTN = None # EXCHNG_TRDBL_DRVTV_PSTN
	@lineage(dependencies={"EXCHNG_TRDBL_DRVTV_PSTN.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.EXCHNG_TRDBL_DRVTV_PSTN.HLD_SL_INDCTR

class Equity_instruments_security(F_15_00_a_REF_FINREP_3_0_Base):
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR

class Equity_instruments_instrument(F_15_00_a_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT

class F_15_00_a_REF_FINREP_3_0_Advances_that_are_not_loans_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	Advances_that_are_not_loanss = []# Advances_that_are_not_loans[]
	def calc_Advances_that_are_not_loanss(self) :
		items = [] # Advances_that_are_not_loans[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Advances_that_are_not_loanss = []
		self.Advances_that_are_not_loanss.extend(self.calc_Advances_that_are_not_loanss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_15_00_a_REF_FINREP_3_0_Other_loans_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	Other_loanss = []# Other_loans[]
	def calc_Other_loanss(self) :
		items = [] # Other_loans[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Other_loanss = []
		self.Other_loanss.extend(self.calc_Other_loanss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_15_00_a_REF_FINREP_3_0_Credit_card_debt_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	Credit_card_debts = []# Credit_card_debt[]
	def calc_Credit_card_debts(self) :
		items = [] # Credit_card_debt[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Credit_card_debts = []
		self.Credit_card_debts.extend(self.calc_Credit_card_debts())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_15_00_a_REF_FINREP_3_0_Trade_receivables_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	Trade_receivabless = []# Trade_receivables[]
	def calc_Trade_receivabless(self) :
		items = [] # Trade_receivables[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Trade_receivabless = []
		self.Trade_receivabless.extend(self.calc_Trade_receivabless())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_15_00_a_REF_FINREP_3_0_Finance_leases_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	Finance_leasess = []# Finance_leases[]
	def calc_Finance_leasess(self) :
		items = [] # Finance_leases[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Finance_leasess = []
		self.Finance_leasess.extend(self.calc_Finance_leasess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_15_00_a_REF_FINREP_3_0_On_demand_and_short_notice_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	On_demand_and_short_notices = []# On_demand_and_short_notice[]
	def calc_On_demand_and_short_notices(self) :
		items = [] # On_demand_and_short_notice[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.On_demand_and_short_notices = []
		self.On_demand_and_short_notices.extend(self.calc_On_demand_and_short_notices())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_15_00_a_REF_FINREP_3_0_Reverse_repurchase_agreements_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	Reverse_repurchase_agreementss = []# Reverse_repurchase_agreements[]
	def calc_Reverse_repurchase_agreementss(self) :
		items = [] # Reverse_repurchase_agreements[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Reverse_repurchase_agreementss = []
		self.Reverse_repurchase_agreementss.extend(self.calc_Reverse_repurchase_agreementss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_15_00_a_REF_FINREP_3_0_Debt_securities_Table:
	LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT_Table = None # LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	EXCHNG_TRDBL_DRVTV_PSTN_Table = None # EXCHNG_TRDBL_DRVTV_PSTN
	Debt_securitiess = []# Debt_securities[]
	def calc_Debt_securitiess(self) :
		items = [] # Debt_securities[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Debt_securitiess = []
		self.Debt_securitiess.extend(self.calc_Debt_securitiess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_15_00_a_REF_FINREP_3_0_Equity_instruments_security_Table:
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	Equity_instruments_securitys = []# Equity_instruments_security[]
	def calc_Equity_instruments_securitys(self) :
		items = [] # Equity_instruments_security[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Equity_instruments_securitys = []
		self.Equity_instruments_securitys.extend(self.calc_Equity_instruments_securitys())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_15_00_a_REF_FINREP_3_0_Equity_instruments_instrument_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	Equity_instruments_instruments = []# Equity_instruments_instrument[]
	def calc_Equity_instruments_instruments(self) :
		items = [] # Equity_instruments_instrument[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Equity_instruments_instruments = []
		self.Equity_instruments_instruments.extend(self.calc_Equity_instruments_instruments())
		CSVConverter.persist_object_as_csv(self,True)
		return None

