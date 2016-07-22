class Opcode:
	def __init__ (self, code, operation, bytes):
		self.code = code	
		self.operation = operation
		self.bytes = bytes	

x = Opcode('60','PUSH1',1)
x2 = Opcode('61','PUSH2',2)
lst = [
Opcode('00','STOP',0),
Opcode('01','ADD',0),
Opcode('02','MUL',0),
Opcode('03','SUB',0),
Opcode('04','DIV',0),
Opcode('05','SDIV',0),
Opcode('06','MOD',0),
Opcode('07','SMOD',0),
Opcode('08','ADDMOD',0),
Opcode('09','MULMOD',0),
Opcode('0a','EXP',0),
Opcode('0b','SIGNEXTEND',0),
Opcode('10','LT',0),
Opcode('11','GT',0),
Opcode('12','SLT',0),
Opcode('13','SGT',0),
Opcode('14','EQ',0),
Opcode('15','ISZERO',0),
Opcode('16','AND',0),
Opcode('17','OR',0),
Opcode('18','XOR',0),
Opcode('19','NOT',0),
Opcode('1a','BYTE',0),
Opcode('20','SHA3',0),
Opcode('30','ADDRESS',0),
Opcode('31','BALANCE',0),
Opcode('32','ORIGIN',0),
Opcode('33','CALLER',0),
Opcode('34','CALLVALUE',0),
Opcode('35','CALLDATALOAD',0),
Opcode('36','CALLDATASIZE',0),
Opcode('37','CALLDATACOPY',0),
Opcode('38','CODESIZE',0),
Opcode('39','CODECOPY',0),
Opcode('3a','GASPRICE',0),
Opcode('3b','EXTCODESIZE',0),
Opcode('3c','EXTCODECOPY',0),
Opcode('40','BLOCKHASH',0),
Opcode('41','COINBASE',0),
Opcode('42','TIMESTAMP',0),
Opcode('43','NUMBER',0),
Opcode('44','DIFFICULTY',0),
Opcode('45','GASLIMIT',0),
Opcode('50','POP',0),
Opcode('51','MLOAD',0),
Opcode('52','MSTORE',0),
Opcode('53','MSTORE8',0),
Opcode('54','SLOAD',0),
Opcode('55','SSTORE',0),
Opcode('56','JUMP',0),
Opcode('57','JUMP1',0),
Opcode('58','PC',0),
Opcode('59','MSIZE',0),
Opcode('5a','GAS',0),
Opcode('5b','JUMPDEST',0),
Opcode('60','PUSH1',1),
Opcode('61','PUSH2',2),
Opcode('62','PUSH3',3),
Opcode('63','PUSH4',4),
Opcode('64','PUSH5',5),
Opcode('65','PUSH6',6),
Opcode('66','PUSH7',7),
Opcode('67','PUSH8',8),
Opcode('68','PUSH9',9),
Opcode('69','PUSH10',10),
Opcode('6a','PUSH11',11),
Opcode('6b','PUSH12',12),
Opcode('6c','PUSH13',13),
Opcode('6d','PUSH14',14),
Opcode('6e','PUSH15',15),
Opcode('6f','PUSH16',16),
Opcode('70','PUSH17',17),
Opcode('71','PUSH18',18),
Opcode('72','PUSH19',19),
Opcode('73','PUSH20',20),
Opcode('74','PUSH21',21),
Opcode('75','PUSH22',22),
Opcode('76','PUSH23',23),
Opcode('77','PUSH24',24),
Opcode('78','PUSH25',25),
Opcode('79','PUSH26',26),
Opcode('7a','PUSH27',27),
Opcode('7b','PUSH28',28),
Opcode('7c','PUSH29',29),
Opcode('7d','PUSH30',30),
Opcode('7e','PUSH31',31),
Opcode('7f','PUSH32',32),
Opcode('80','DUP1',0),
Opcode('81','DUP2',0),
Opcode('82','DUP3',0),
Opcode('83','DUP4',0),
Opcode('84','DUP5',0),
Opcode('85','DUP6',0),
Opcode('86','DUP7',0),
Opcode('87','DUP8',0),
Opcode('88','DUP9',0),
Opcode('89','DUP10',0),
Opcode('8a','DUP11',0),
Opcode('8b','DUP12',0),
Opcode('8c','DUP13',0),
Opcode('8d','DUP14',0),
Opcode('8e','DUP15',0),
Opcode('8f','DUP16',0),
Opcode('90','SWAP1',0),
Opcode('91','SWAP2',0),
Opcode('92','SWAP3',0),
Opcode('93','SWAP4',0),
Opcode('94','SWAP5',0),
Opcode('95','SWAP6',0),
Opcode('96','SWAP7',0),
Opcode('97','SWAP8',0),
Opcode('98','SWAP9',0),
Opcode('99','SWAP10',0),
Opcode('9a','SWAP11',0),
Opcode('9b','SWAP12',0),
Opcode('9c','SWAP13',0),
Opcode('9d','SWAP14',0),
Opcode('9e','SWAP15',0),
Opcode('9f','SWAP16',0),
Opcode('a0','LOG0',0),
Opcode('a1','LOG1',0),
Opcode('a2','LOG2',0),
Opcode('a3','LOG3',0),
Opcode('a4','LOG4',0),
Opcode('f0','CREATE',0),
Opcode('f1','CALL',0),
Opcode('f2','CALLCODE',0),
Opcode('f3','RETURN',0),
Opcode('f4','DELEGATECALL',0),
Opcode('ff','SUICIDE',0),
]

line = '6060604052361561007f576000357c0100000000000000000000000000000000000000000000000000000000900480632bc9ed02146100815780634e3b62ec146100a257806354fd4d50146100f45780638da5cb5b14610115578063b6549f751461014c578063c623674f14610159578063e322a468146101d25761007f565b005b61008c600450610288565b6040518082815260200191505060405180910390f35b6100f26004803590602001906004018035906020019191908080601f01602080910402602001604051908101604052809392919081815260200183838082843782019150505050505090506102a4565b005b6100ff60045061027f565b6040518082815260200191505060405180910390f35b6101206004506101f3565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b610157600450610399565b005b610164600450610219565b60405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f1680156101c45780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6101dd60045061029b565b6040518082815260200191505060405180910390f35b600060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6001600050805480601f0160208091040260200160405190810160405280929190818152602001826000508054801561027757820191906000526020600020905b81548152906001019060200180831161025a57829003601f168201915b505050505081565b60026000505481565b600360009054906101000a900460ff1681565b60046000505481565b600060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614801561030e5750600360009054906101000a900460ff16155b1561039557806001600050908051906020019082805482825590600052602060002090601f01602090048101928215610364579182015b82811115610363578251826000505591602001919060010190610345565b5b50905061038f9190610371565b8082111561038b5760008181506000905550600101610371565b5090565b50600050505b5b50565b600060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161480156104035750600360009054906101000a900460ff16155b1561042c576001600360006101000a81548160ff02191690830217905550426004600050819055505b5b56'

def ListSearch(lst, opcode):
	for i, val in enumerate(lst):
		if val.code == opcode :
			return val

def WriteToFile (name, line):
	f =  open(name, 'w')
	f.write(line)
	f.close();

def ReadByte(line, counter, length):
	result = ''
	for i in range (0, length*2):
		result = result + line[counter + i];
	return result

def OneOperation(line, counter, f):
	opcode = ReadByte(line, counter, 1)
	a = ListSearch(lst, opcode)
	counter = counter + 2
	f.write(a.operation +' ' + ReadByte(line, counter, a.bytes) + '\n') 
	print a.operation +' ' + ReadByte(line, counter, a.bytes) 
	counter = counter + 2 * a.bytes
	return counter

def Parse (line, address):
	f = open(address,'w')
	counter = 0
	while counter < len(line):
		counter = OneOperation(line, counter, f)
	f.close()
		

Parse(line, '/home/anilam/temp/temp')
