--
-- PostgreSQL database dump
--

-- Dumped from database version 16.6 (Ubuntu 16.6-1.pgdg24.04+1)
-- Dumped by pg_dump version 16.6 (Ubuntu 16.6-1.pgdg24.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: companies; Type: TABLE; Schema: public; Owner: missfionajean
--

CREATE TABLE public.companies (
    id integer NOT NULL,
    name character varying(32)
);


ALTER TABLE public.companies OWNER TO missfionajean;

--
-- Name: companies_id_seq; Type: SEQUENCE; Schema: public; Owner: missfionajean
--

CREATE SEQUENCE public.companies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


-- ALTER SEQUENCE public.companies_id_seq OWNER TO missfionajean;
ALTER SEQUENCE public.companies_id_seq OWNER TO missfionajean;

--
-- Name: companies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: missfionajean
--

ALTER SEQUENCE public.companies_id_seq OWNED BY public.companies.id;


--
-- Name: employees; Type: TABLE; Schema: public; Owner: missfionajean
--

CREATE TABLE public.employees (
    id integer NOT NULL,
    name character varying(32),
    company_id integer
);


ALTER TABLE public.employees OWNER TO missfionajean;

--
-- Name: employees_id_seq; Type: SEQUENCE; Schema: public; Owner: missfionajean
--

CREATE SEQUENCE public.employees_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.employees_id_seq OWNER TO missfionajean;

--
-- Name: employees_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: missfionajean
--

ALTER SEQUENCE public.employees_id_seq OWNED BY public.employees.id;


--
-- Name: companies id; Type: DEFAULT; Schema: public; Owner: missfionajean
--

ALTER TABLE ONLY public.companies ALTER COLUMN id SET DEFAULT nextval('public.companies_id_seq'::regclass);


--
-- Name: employees id; Type: DEFAULT; Schema: public; Owner: missfionajean
--

ALTER TABLE ONLY public.employees ALTER COLUMN id SET DEFAULT nextval('public.employees_id_seq'::regclass);


--
-- Data for Name: companies; Type: TABLE DATA; Schema: public; Owner: missfionajean
--

COPY public.companies (id, name) FROM stdin;
3	Google
4	Netflix
1	Tesla
\.


--
-- Data for Name: employees; Type: TABLE DATA; Schema: public; Owner: missfionajean
--

COPY public.employees (id, name, company_id) FROM stdin;
1	Matt	1
2	Dave	2
3	Fiona	3
4	Jonas	1
\.


--
-- Name: companies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: missfionajean
--

SELECT pg_catalog.setval('public.companies_id_seq', 4, true);


--
-- Name: employees_id_seq; Type: SEQUENCE SET; Schema: public; Owner: missfionajean
--

SELECT pg_catalog.setval('public.employees_id_seq', 4, true);


--
-- Name: companies unique_name; Type: CONSTRAINT; Schema: public; Owner: missfionajean
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT unique_name UNIQUE (name);


--
-- PostgreSQL database dump complete
--

