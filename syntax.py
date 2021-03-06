from dataclasses import dataclass
from typing import Any
from lark.tree import Meta


def Many(*x):
    return x


class AST:
    loc: Meta


@dataclass
class Lit(AST):
    value: str


class LStr(Lit):
    ...


class LChar(Lit):
    ...


class LNum(Lit):
    ...


class TypeSig(AST):
    annot: Any


@dataclass
class TsArr(TypeSig):
    contains: TypeSig


@dataclass
class TsCall(TypeSig):
    name: str
    args: list[TypeSig]


@dataclass
class TsVar(TypeSig):
    name: str


class Expr(AST):
    annot: Any


@dataclass
class EAssign(Expr):
    lvalue: Expr
    op: str
    value: Expr


@dataclass
class ECast(Expr):
    target: Expr
    sig: TypeSig


@dataclass
class EOp(Expr):
    lhs: Expr
    op: str
    rhs: Expr


@dataclass
class ECall(Expr):
    target: Expr
    args: list[Expr]


@dataclass
class EDot(Expr):
    target: Expr
    attr: str


@dataclass
class ELit(Expr):
    lit: Lit


@dataclass
class EVar(Expr):
    name: str


@dataclass
class VarDecl(AST):
    name: str
    sig: TypeSig | None
    value: Expr | None


class Stmt(AST):
    ...


@dataclass
class SDecl(Stmt):
    decl: VarDecl


@dataclass
class SBreak(Stmt):
    ...


@dataclass
class SContinue(Stmt):
    ...


@dataclass
class SReturn(Stmt):
    value: Expr | None


@dataclass
class SExpr(Stmt):
    expr: Expr


@dataclass
class SBlock(Stmt):
    stmts: list[Stmt]


@dataclass
class SIf(Stmt):
    cond: Expr
    body: Stmt
    orelse: Stmt | None


@dataclass
class SWhile(Stmt):
    cond: Expr
    step: Expr | None
    body: Stmt


class Decl(AST):
    ...


@dataclass
class DDecl(Decl):
    decl: VarDecl


@dataclass
class DFunc(Decl):
    modifiers: list[str]
    name: str
    args: list[tuple[str, TypeSig]]
    ret: TypeSig
    body: SBlock


@dataclass
class DClass(Decl):
    modifiers: list[str]
    name: str
    body: list[Decl]


@dataclass
class File(AST):
    decls: list[Decl]
