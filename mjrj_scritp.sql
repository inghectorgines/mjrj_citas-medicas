CREATE DATABASE IF NOT EXISTS mjrj_scritp;
USE mjrj_scritp;

CREATE TABLE usuarios(
    id       int(25) auto_increment not null,
    nombre    varchar(100),
    apellidos varchar(255),
    noConsultorio int(25),
    email     varchar(255) not null,
    password  varchar(255) not null,
    fecha     date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;


CREATE TABLE citas(
    id         int(25) auto_increment not null,
    usuario_id int(25) not null,
    paciente      varchar(255) not null,
    descripcion MEDIUMTEXT,
    horaAtencion varchar(255),
    costo        float(10,2),
    fecha       date not null,
    CONSTRAINT pk_citas PRIMARY KEY(id),
    CONSTRAINT fk_cita_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;