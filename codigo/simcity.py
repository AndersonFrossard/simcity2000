
import os
import hashlib
import sys
#https://www.geeksforgeeks.org/python-seek-function/
def apply_cheat_on(filename):
	new_name = filename[:-4]+'-edited.sc2'
	found = 0
	max_found = 3
	file_size = os.path.getsize(filename)
	if file_size > 80000:
		max_found = 4
	count = 0
	hack = b'\x7F'
	d = open(new_name, "wb")
	print('Arquivo.... : ' + filename +' ' + str(file_size)+ ' bytes')
	with open(filename, 'rb+') as f:
		while True:
			data = f.read(1)
			count +=1

			data_next = f.read(1)
			data_old = data[:]
			f.seek(-1, 1)
			if ( (data.hex(sep=' ') == '00') and (data_next.hex(sep=' ') == '02')  ):
				found +=1
				if (found == max_found) :
						print('Pattern found... n = ', found, 'aplying cheat....')
						data = hack
						found +=1
			d.write(data)
			if is_end_of_file(count, file_size):
				print('***** Reached end of file *****')
				break
			
	d.close()
	return new_name

def is_end_of_file(count, file_size):
	return count >= file_size

def get_sha256_from_file(filename):
	with open(filename, "rb") as f:
		f_byte = f.read()
		result = hashlib.sha256(f_byte)
	return result.hexdigest()



def get_sha256_of_edited_file(original_filename):
	new_name = apply_cheat_on(original_filename)
	return get_sha256_from_file(new_name)

def get_sha(lixo):
	return lixo

def jogador(numero):
	return numero

def dinheiro(valor):
	d = int(valor)
	print(hex(d))
	bytes_val = d.to_bytes(2, 'big')
	print(bytes_val)
	search_number(decimal_number, filename)


def main():
	filenames = ['../belford.sc2', '../MANHAT.sc2','../NEWCITY.SC2', '../TESTE01.SC2']
	destinos = ['newT.sc2', 'teste.txt']
	try:
		print("Parameter....: ", sys.argv[1])
		print(get_sha256_of_edited_file(sys.argv[1]))
	except Exception as e:
		print("Try using this command line: python simcity.py name_of_file_to_be_hacked.sc2")
		print(e)



if __name__ == '__main__':
	print('Starting ...')
	main()
