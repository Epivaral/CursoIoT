
------------------- Paso 1---------------------------
--        crear la tabla
-----------------------------------------------------

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[DHT22](
	[registro] [bigint] IDENTITY(1,1) NOT NULL,
	[dispositivo] [nvarchar](50) NULL,
	[temperatura] [numeric](5,2) NULL,
	[humedad] [numeric](5,2) NULL,
	[capturadoen] [datetime2](7) NOT NULL,
 CONSTRAINT [PK_DHT22] PRIMARY KEY CLUSTERED 
(
	[registro] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

----------------

-- query de insercion para el Stream Analytics job

SELECT Dispositivo
    , Temperatura
    ,Humedad
    ,EventProcessedUtcTime as [capturadoen]
INTO SQLOut
FROM IoTHub


-------------------------------------------------------
-------------------------------------------------------
-------------------- Paso 3 ---------------------------
--  Query para la Azure Function 
-------------------------------------------------------

SELECT ltrim(str(count(*))) as registros
FROM DHT22
where DATEDIFF(MI,capturadoen, getdate())> 5
