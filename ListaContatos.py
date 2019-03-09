#!/usr/bin/python
# -*- coding: utf-8 -*-
import time, os


class Lista:

  def __init__(self):
      self.contatos = []

  def AddContato(self, contato):
      self.contatos.append(contato)

  def DellContato(self, contato):
      self.contatos.pop(contato)


  def SelfPrint(self):
     i = 0
     for p, v in self.contatos:
       print(str(i) + " - " + str(p) + " | tel: " + str(v) )
       i += 1



  def WaitClear(self, sleep_time):
      time.sleep(sleep_time)
      os.system("cls")


class Contato:

  def __init__(self, name, numero):
      self.name = name
      self.numero = numero



class Menu:


  def __init__(self):

      self.main = {'1': self.ListContato,
                   '2': self.AddContato,
                   '3': self.RemoveContato,
                   '4': self.Sair,
                    }

      self.Lista = Lista()

      self.Control()


  # MENU MAIN

  def Sair(self):
      self.Exit()

  def ListContato(self):
      self.Lista.SelfPrint()

  def AddContato(self):
      nome = input("Insira o nome do contato: ")
      telefone = input("Insira o número do contato: ")
      self.Lista.AddContato([nome,telefone])
      print("Contato adicionado com sucesso")


  def RemoveContato(self):
      self.Lista.SelfPrint()
      r = int(input("Digite o número a ser removido :"))
      self.Lista.DellContato(r)
      print("Contato removido com sucesso!!")



  def Exit(self):
      print("Encerrando o programa!\nTchau!")

  def Show(self):
      self.WaitClear(1.5)
      print("\n\n""Seja bem vindo à sua Lista de Contatos! \n" +
                     "Selecione o número da ação que deseja concluir. ")
      option = input("\n" +
                     "|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n" +
                     "|  1. Listar contatos          |\n" +
                     "|  2. Adicionar contato        |\n" +
                     "|  3. Remover contato          |\n" +
                     "|  4. Sair                     |\n" +
                     "|______________________________|\n\n")
      return option

  def Control(self):
      option = 0

      while option != "4":
          option = self.Show()
          try:
              function = self.main[option]
              function()
          except KeyError:
              print("Digite um número aceitável!")


  def WaitClear(self, sleep_time):
      time.sleep(sleep_time)
      os.system("cls")




if __name__ == '__main__':
  Menu()
