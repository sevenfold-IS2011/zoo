<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">
	<html>
	<head>
		<link rel="stylesheet" type="text/css" href="../css/master.css" />
	</head>
		<body>
		<h3>Descrizione degli animali:</h3>
			<xsl:for-each select="zoo:area">
<!--			<xsl:if test="@id=01"> -->

  		<h4>Area <xsl:value-of select="./@nome"/>:</h4>
  		<xsl:for-each select="zoo:animale">
  			<table class="animal">
  				<tr>
						<td>Nome</td>
						<td><xsl:value-of select="zoo:nome"/></td>
					</tr>
					<tr>
						<td>Sesso</td>
						<td><xsl:value-of select="zoo:sesso"/></td>
					</tr>
					<tr>
						<td>Età</td>
						<td><xsl:value-of select="zoo:eta"/></td>
					</tr>
					<tr>
						<td></td>
						<td>
							<img>
      					<xsl:attribute name="src">
      						<xsl:value-of select="zoo:img" />
      					</xsl:attribute>
    					</img>
    				</td>
					</tr>
				</table>
				</xsl:for-each>
<!--			</xsl:if>  -->
			</xsl:for-each>
		</body>
	</html>
	</xsl:template>
</xsl:stylesheet>

